from django.db import models
from decimal import Decimal

import datetime
import time

from django.utils.timezone import now
from accounts.models import CompanyProfile, ConsultantProfile
from customers.models import Customer


# Create your models here.
class Project(models.Model):
    consultant = models.ForeignKey(ConsultantProfile, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    third_party_identifier = models.CharField(max_length=255, blank=True)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


