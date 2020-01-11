import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

from ..users.models import User


class Employee(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='employees')
    pretend_salary = models.DecimalField(max_digits=17, decimal_places=2, null=True)
    role = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = 'EMPLOYEE'
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
