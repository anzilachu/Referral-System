from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    referral_code = models.CharField(_('Referral Code'), max_length=10, blank=True, null=True)
    points = models.IntegerField(_('Points'), default=0)
