from django.conf import settings

from django_browserid.auth import BrowserIDBackend

from marketpulse.base.mozillians import MozilliansClient, MozilliansClientLegacy


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

    def create_user(self, email):
        user = super(MozilliansAuthBackend, self).create_user(email)

        try:
            mozillian = self.mozillians_client.lookup_user({'email': email})
        except:
            mozillian = None

        if user and mozillian:
            user.mozillians_url = mozillian['url']
            user.save()

        return user


class MozilliansAuthBackendLegacy(BrowserIDBackend):
    def __init__(self, *args, **kwargs):
        super(MozilliansAuthBackendLegacy, self).__init__(*args, **kwargs)

        self.api_url = settings.MOZILLIANS_API_URL
        self.api_key = settings.MOZILLIANS_API_KEY
        self.app_name = settings.MOZILLIANS_APP_NAME

        self.mozillians_client = MozilliansClientLegacy(self.api_url, self.api_key, self.app_name)

    def is_valid_email(self, email):
        try:
            user = self.mozillians_client.email_lookup(email)
        except:
            user = None

        authentication_policy = getattr(settings, 'MOZILLIANS_AUTHENTICATION_POLICY',
                                        lambda x: True)

        return user and authentication_policy(user)

    def create_user(self, email):
        user = super(MozilliansAuthBackendLegacy, self).create_user(email)

        try:
            mozillian = self.mozillians_client.email_lookup(email)
        except:
            mozillian = None

        if user and mozillian:
            user.mozillians_url = mozillian['url']
            user.save()

        return user
