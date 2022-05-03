import django
from django.contrib import admin
from checkin.models import ParkedVehicles, Slot

# Register your models here.
admin.site.register(ParkedVehicles)
admin.site.register(Slot)