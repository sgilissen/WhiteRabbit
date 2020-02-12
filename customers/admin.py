from django.contrib import admin
from . import models


# Register your models here.
class CustomerContactAdmin(admin.TabularInline):
    model = models.CustomerContact
    extra = 0
    min_num = 0


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'vat_number', 'vat_applicable', 'address_line_1', 'postal_code', 'city',
                    'country_code')
    list_filter = ('vat_applicable',)
    search_fields = ('company_name', 'vat_number')
    inlines = [CustomerContactAdmin, ]
