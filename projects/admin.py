from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('customer', )


class TimeEntryInline(admin.TabularInline):
    def unit(self, instance):
        return str(instance.timesheet.project.billing_rate)
    

    readonly_fields = ('unit',)
    model = models.TimeEntry
    extra = 0


@admin.register(models.Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('project', 'reference', 'consultant', 'start_date', 'end_date', )
    inlines = [TimeEntryInline]


