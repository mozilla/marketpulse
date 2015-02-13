import json

from unittest import TestCase
from urlparse import parse_qs, urlparse

import responses

from nose.tools import eq_, raises

from marketpulse.base.mozillians import (BadStatusCode, MozilliansClient, ResourceDoesNotExist,
                                         MultipleResourcesReturned)


class TestMozilliansClientGet(TestCase):
    def setUp(self):
        API_URL = 'http://example.com/api/v2/'
        API_KEY = 'EXAMPLE_API_KEY'
        self.client = MozilliansClient(API_URL, API_KEY)

    @responses.activate
    def test_get_valid_status(self):
        """Test that valid response is returned for 200 status code."""
        url = 'http://example.com/api/v2/'
        body = '{"key1": "value1", "key2": "value2"}'
        responses.add(responses.GET, url=url, body=body, status=200,
                      content_type='application/json')

        response = self.client.get(url)
        eq_(len(responses.calls), 1)
        eq_(responses.calls[0].request.url, url)
        eq_(responses.calls[0].request.headers['X-API-KEY'], 'EXAMPLE_API_KEY')
        eq_(response, json.loads(body))

    @responses.activate
    @raises(BadStatusCode)
    def test_get_invalid_status(self):
        """Test that error is raised response for bad status code."""
        url = 'http://example.com/api/v2/'
        responses.add(responses.GET, url, status=404, content_type='application/json')
        self.client.get(url)

    @responses.activate
    def test_get_params(self):
        """Test that query parameters are appended in the URL."""
        url = 'http://example.com/api/v2/'
        params = {'param1': 'value1', 'param2': 'value2'}
        body = '{"key1": "value1", "key2": "value2"}'
        responses.add(responses.GET, url, body=body, status=200, content_type='application/json')
        response = self.client.get('http://example.com/api/v2/', params=params)

        eq_(len(responses.calls), 1)
        query = parse_qs(urlparse(responses.calls[0].request.url).query)
        eq_(query['param1'][0], 'value1')
        eq_(query['param2'][0], 'value2')
        eq_(responses.calls[0].request.headers['X-API-KEY'], 'EXAMPLE_API_KEY')
        eq_(response, json.loads(body))

    @responses.activate
    def test_get_users(self):
        url = 'http://example.com/api/v2/users'
        body = '{"key1": "value1", "key2": "value2"}'
        responses.add(responses.GET, url, body=body, status=200, content_type='application/json')
        response = self.client.get_users()
        eq_(len(responses.calls), 1)
        eq_(response, json.loads(body))

    @responses.activate
    def test_get_groups(self):
        url = 'http://example.com/api/v2/groups'
        body = '{"key1": "value1", "key2": "value2"}'
        responses.add(responses.GET, url, body=body, status=200, content_type='application/json')
        response = self.client.get_groups()
        eq_(len(responses.calls), 1)
        eq_(response, json.loads(body))

    @responses.activate
    def test_get_skills(self):
        url = 'http://example.com/api/v2/skills'
        body = '{"key1": "value1", "key2": "value2"}'
        responses.add(responses.GET, url, body=body, status=200, content_type='application/json')
        response = self.client.get_skills()
        eq_(len(responses.calls), 1)
        eq_(response, json.loads(body))


class TestMozilliansClientUserLookup(TestCase):
    def setUp(self):
        self.client = MozilliansClient('http://example.com/api/v2/', 'EXAMPLE_API_KEY')

    @raises(ResourceDoesNotExist)
    @responses.activate
    def test_does_not_exist(self):
        url = 'http://example.com/api/v2/users'
        body = '{"count": 0}'
        responses.add(responses.GET, url, body=body, status=200, content_type='application/json')

        self.client.lookup_user({'email': 'foo@example.com'})

    @raises(MultipleResourcesReturned)
    @responses.activate
    def test_multiple_resources_returned(self):
        url = 'http://example.com/api/v2/users'
        body = '{"count": 2}'
        responses.add(responses.GET, url, body=body, status=200, content_type='application/json')

        self.client.lookup_user({'email': 'foo@example.com'})

    @responses.activate
    def test_valid_response(self):
        resource_url = 'http://example.com/api/v2/users'
        profile_url = 'http://example.com/api/v2/users/1'
        body = '{"count": 1, "results": [{"_url": "http://example.com/api/v2/users/1"}]}'
        detailed_body = '{"key1": "value1", "key2": "value2"}'
        responses.add(responses.GET, resource_url, body=body, status=200,
                      content_type='application/json')
        responses.add(responses.GET, profile_url, body=detailed_body, status=200,
                      content_type='application/json')

        response = self.client.lookup_user({'email': 'foo@example.com'})
        eq_(len(responses.calls), 2)
        query = parse_qs(urlparse(responses.calls[0].request.url).query)
        eq_(query['email'][0], 'foo@example.com')
        eq_(response, json.loads(detailed_body))

    @responses.activate
    def test_vouched_status(self):
        url = 'http://example.com/api/v2/users'
        expected_result = '{"_url": "http://example.com/users/1", "is_vouched": true}'
        body = '{"count": 1, "results": [%s]}' % expected_result
        responses.add(responses.GET, url, body=body, status=200, content_type='application/json')

        user, status = self.client.is_vouched('foo@example.com')
        eq_(len(responses.calls), 1)
        query = parse_qs(urlparse(responses.calls[0].request.url).query)
        eq_(query['email'][0], 'foo@example.com')
        eq_(user, json.loads(expected_result))
        eq_(status, True)
