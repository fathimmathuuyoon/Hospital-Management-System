from django.contrib import admin

from newapp import models
from newapp.models import Department

# Register your models here.
admin.site.register(models.Doctor)
admin.site.register(models.Patient)
admin.site.register(Department)
admin.site.register(models.Booking)