from django.utils.translation import ugettext_lazy
from django.db import models

COUNTRY_CHOICES = (
    ('BE', ugettext_lazy('Belgium')),
    ('CN', ugettext_lazy('China')),
    ('DE', ugettext_lazy('Germany')),
    ('FR', ugettext_lazy('France')),
    ('HK', ugettext_lazy('Hong Kong')),
    ('NL', ugettext_lazy('The Netherlands')),
    ('PL', ugettext_lazy('Poland')),
    ('US', ugettext_lazy('United States of America')),
)


class CompanyMixin(models.Model):
    company_name = models.CharField(max_length=255)
    vat_number = models.CharField(max_length=32)
    vat_applicable = models.BooleanField(default=True)

    iban = models.CharField(max_length=255, blank=True)
    bic = models.CharField(max_length=32, blank=True)

    phone = models.CharField(max_length=32, blank=True)
    email = models.EmailField(max_length=255, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.company_name


class AddressMixin(models.Model):
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    postal_code = models.CharField(max_length=32)
    city = models.CharField(max_length=255)
    country_code = models.CharField(max_length=2, default='BE', choices=COUNTRY_CHOICES)

    class Meta:
        abstract = True
