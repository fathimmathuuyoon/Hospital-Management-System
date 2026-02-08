from django.contrib import admin

from newapp import models

# Register your models here.
admin.site.register(models.Doctor)
admin.site.register(models.Patient)
admin.site.register(models.Department)
admin.site.register(models.Booking)
admin.site.register(models.Prescription)