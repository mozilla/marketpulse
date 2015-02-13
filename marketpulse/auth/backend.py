from django.conf import settings

from marketpulse.base.mozillians import MozilliansClient

from django_browserid.auth import BrowserIDBackend


class MozilliansAuthBackend(BrowserIDBackend):
    def __init__(self, *args, **kwargs):
        super(MozilliansAuthBackend, self).__init__(*args, **kwargs)

        api_url = settings.MOZILLIANS_API_URL
        api_key = settings.MOZILLIANS_API_KEY
        self.mozillians_client = MozilliansClient(api_url, api_key)

    def is_valid_email(self, email):
        try:
            user = self.mozillians_client.lookup_user({'email': email}, detailed=False)
        except:
            user = None

        authentication_policy = getattr(settings, 'MOZILLIANS_AUTHENTICATION_POLICY',
                                        lambda x: True)

        return user and authentication_policy(user)
