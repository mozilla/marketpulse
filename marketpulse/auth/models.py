from django.contrib.auth.models import AbstractUser
from django.db.models import fields


class User(AbstractUser):
    mozillians_url = fields.URLField()
