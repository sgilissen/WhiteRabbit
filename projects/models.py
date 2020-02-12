from django.db import models
from django.utils.translation import ugettext_lazy

import datetime

from accounts.models import CompanyProfile, ConsultantProfile
from customers.models import Customer


BILLING_RATE_CHOICES = [
    ('HR', ugettext_lazy('Hourly Rate')),
    ('FD', ugettext_lazy('Flat Daily Rate')),
    ('PR', ugettext_lazy('Per-Project Basis')),
]


# Create your models here.
class Project(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    third_party_identifier = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)
    billing_rate = models.CharField(max_length=2, default='HR', choices=BILLING_RATE_CHOICES)

    def __str__(self):
        return self.name


class Timesheet(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reference = models.CharField(max_length=100, blank=True)
    consultant = models.ForeignKey(ConsultantProfile, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.project.name


class TimeEntry(models.Model):
    timesheet = models.ForeignKey(Timesheet, on_delete=models.CASCADE)
    date = models.DateField()
    units = models.DecimalField(max_digits=10, decimal_places=2)
