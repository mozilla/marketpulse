from urlparse import urljoin

from django.test import TestCase, override_settings

import responses

from nose.tools import eq_, ok_

from marketpulse.auth.backend import MozilliansAuthBackend


@override_settings(MOZILLIANS_API_URL='http://example.com/api/v2/')
@override_settings(MOZILLIANS_API_KEY='EXAMPLE_API_KEY')
class MozilliansAuthBackendTests(TestCase):

    def test_mozillians_client(self):
        backend = MozilliansAuthBackend()
        eq_(backend.mozillians_client.key, 'EXAMPLE_API_KEY')
        eq_(backend.mozillians_client.base_url, 'http://example.com/api/v2/')

    @responses.activate
    def test_valid_email(self):
        backend = MozilliansAuthBackend()
        body = '{"count": 1, "results": [{"_url": "http://example.com/api/v2/users/1"}]}'
        url = urljoin(backend.mozillians_client.base_url, 'users')
        responses.add(responses.GET, url=url, body=body, status=200,
                      content_type='application/json')
        ok_(backend.is_valid_email('foo@example.com'))

    @responses.activate
    def test_invalid_email(self):
        backend = MozilliansAuthBackend()
        body = '{"count": 0, "results": []}'
        url = urljoin(backend.mozillians_client.base_url, 'users')
        responses.add(responses.GET, url=url, body=body, status=200,
                      content_type='application/json')
        ok_(not backend.is_valid_email('foo@example.com'))

    @responses.activate
    @override_settings(MOZILLIANS_AUTHENTICATION_POLICY=lambda x: False)
    def test_custom_authentication_policy(self):
        backend = MozilliansAuthBackend()
        body = '{"count": 1, "results": [{"_url": "http://example.com/api/v2/users/1"}]}'
        url = urljoin(backend.mozillians_client.base_url, 'users')
        responses.add(responses.GET, url=url, body=body, status=200,
                      content_type='application/json')
        ok_(not backend.is_valid_email('foo@example.com'))

    def test_normalize_lower_case_email(self):
        email = 'foo@bar.com'
        backend = MozilliansAuthBackend()
        normalized_email = backend._normalize_email(email)
        eq_(normalized_email, 'foo@bar.com')

    def test_normalize_mixed_case_email(self):
        email = 'Foo@BaR.com'
        backend = MozilliansAuthBackend()
        normalized_email = backend._normalize_email(email)
        eq_(normalized_email, 'Foo@bar.com')
