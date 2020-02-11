from django.db import models
from contrib.model_mixins import AddressMixin, CompanyMixin
from accounts.models import ConsultantProfile


# Create your models here.
class Customer(AddressMixin, CompanyMixin, models.Model):
    def __str__(self):
        return self.company_name
