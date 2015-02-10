from django.contrib import messages

from django_browserid.views import JSONResponse
from django_browserid.views import Verify


class BrowserIDVerify(Verify):

    def login_failure(self, msg=''):
        if not msg:
            msg = ('Login failed. Please make sure that you are an accepted Mozillian.')
        messages.warning(self.request, msg)
        return JSONResponse({'redirect': self.failure_url})
