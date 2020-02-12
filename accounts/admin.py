from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'vat_number', 'vat_applicable', 'address_line_1', 'postal_code', 'city',
                    'country_code')
    list_filter = ('vat_applicable',)
    search_fields = ('company_name', 'vat_number')

@admin.register(models.ConsultantProfile)
class ConsultantProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company')
    list_filter = ('user', 'company')
    search_fields = ('user', 'company')
    raw_id_fields = ('user',)

