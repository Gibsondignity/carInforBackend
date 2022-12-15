from django.contrib import admin
from .models import CarInfo, reportedCar


# Register your models here.

class listCarInfo(admin.ModelAdmin):
    list_display = ('car_number', 'owner_name', 'owner_dob', 'car_model', 'car_type', 'color', 'date_of_reg', 'region_of_reg', 'date_created', 'date_updated')

class listReportedCar(admin.ModelAdmin):
    list_display = ('car_number', 'reported_issue', 'reported_by', 'reported_date', 'date_updated')

admin.site.register(CarInfo, listCarInfo)
admin.site.register(reportedCar, listReportedCar)