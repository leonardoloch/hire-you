import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from ..users.models import User


class Employer(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='employers')

    class Meta:
        db_table = 'EMPLOYER'
        verbose_name = _('employer')
        verbose_name_plural = _('employers')

