import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel


class User(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(_('first name'), max_length=32)
    last_name = models.CharField(_('last name'), max_length=64)
    date_of_birth = models.DateField(_('date of birth'), null=True)
    email = models.EmailField(_('email address'), blank=True, null=True)
    email_confirmed = models.BooleanField(_('email confirmed'), default=False)
    phone_number = models.CharField(_('phone number'), null=True, max_length=16)
    terms_accepted = models.BooleanField(_('terms accepted'), default=False)

    class Meta:
        db_table = 'USER'
        verbose_name = _('user')
        verbose_name_plural = _('users')
