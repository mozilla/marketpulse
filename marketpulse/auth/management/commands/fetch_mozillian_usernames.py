from django.core.management.base import BaseCommand
from django.conf import settings

from marketpulse.auth.models import User
from marketpulse.base.mozillians import MozilliansClient


class Command(BaseCommand):
    help = 'Fetch mozillians username for existing users'

    def handle(self, *args, **options):
        api_url = settings.MOZILLIANS_API_URL
        api_key = settings.MOZILLIANS_API_KEY
        mozillians_client = MozilliansClient(api_url, api_key)
        for user in User.objects.all():
            try:
                mozillian = mozillians_client.lookup_user({'email': user.email}, detailed=False)
                user.mozillians_username = mozillian['username']
                user.save()
                self.stdout.write('Fetching username for {0}'.format(user.email))
            except:
                self.stdout.write('Unable to fetch username for {0}'.format(user.email))
                continue
