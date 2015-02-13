from django.test import TestCase

import mock

from marketpulse.auth.views import BrowserIDVerify


class BrowserIDVerifyTest(TestCase):
    @mock.patch('marketpulse.auth.views.messages.warning')
    def test_login_failure(self, msg_mock):
        verify = BrowserIDVerify()
        request_mock = mock.Mock()
        verify.request = request_mock
        verify.login_failure()
        msg = 'Login failed. Please make sure that you are an accepted Mozillian.'
        msg_mock.assert_called_with(mock.ANY, msg)

    @mock.patch('marketpulse.auth.views.messages.warning')
    def test_login_failure_msg(self, msg_mock):
        verify = BrowserIDVerify()
        request_mock = mock.Mock()
        verify.request = request_mock
        msg = 'Login failure msg.'
        verify.login_failure(msg)
        msg_mock.assert_called_with(mock.ANY, msg)
