from django.db import models
from django.conf import settings

from contrib.model_mixins import AddressMixin, CompanyMixin


# Create your models here.
class CompanyProfile(CompanyMixin, AddressMixin, models.Model):
    def __str__(self):
        return self.company_name


class ConsultantProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
