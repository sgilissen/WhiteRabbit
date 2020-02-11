from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'vat_number', 'vat_applicable', 'address_line_1', 'postal_code', 'city',
                    'country_code')
    list_filter = ('vat_applicable',)
    search_fields = ('company_name', 'vat_number')