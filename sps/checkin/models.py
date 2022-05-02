from django.db import models
from login.models import Account

# Create your models here.

class ParkedVehicles(models.Model):
    mobile_number = models.ForeignKey(Account, on_delete=models.CASCADE)
    time_in = models.DateTimeField(primary_key=True, auto_now_add=True)
    time_out = models.DateField(auto_now_add=True)
    bill = models.FloatField(default=0.00)

    def __str__(self):
        return str(self.time_in)