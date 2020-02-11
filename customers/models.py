from django.db import models
from contrib.model_mixins import AddressMixin, CompanyMixin
from accounts.models import ConsultantProfile
from django.utils.translation import ugettext_lazy

BILLING_RATE_CHOICES = [
    ('HR', ugettext_lazy('Hourly Rate')),
    ('FD', ugettext_lazy('Flat Daily Rate')),
    ('PR', ugettext_lazy('Per-Project Basis')),
]

CONTACT_TYPE_CHOICES = [
    ('TC', ugettext_lazy('Timesheet Contact')),
    ('IC', ugettext_lazy('Invoicing Contact')),
    ('BT', ugettext_lazy('Backup Timesheet Contact')),
    ('BI', ugettext_lazy('Backup Invoicing Contact')),
    ('TL', ugettext_lazy('Teamlead')),
    ('BT', ugettext_lazy('Backup Teamlead')),
    ('LM', ugettext_lazy('Line Manager')),
    ('BL', ugettext_lazy('Backup Line Manager')),
    ('EC', ugettext_lazy('Emergency Contact')),
]

class Customer(AddressMixin, CompanyMixin, models.Model):
    billing_rate = models.CharField(max_length=2, default='HR', choices=BILLING_RATE_CHOICES)

    def __str__(self):
        return self.company_name


class CustomerContact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=100, blank=True)
    contact_type = models.CharField(max_length=2, default='TC', choices=CONTACT_TYPE_CHOICES)
