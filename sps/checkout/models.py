from django.db import models
from login.models import Account

# Create your models here.

class LeftVehicles(models.Model):
    mobile_number = models.ForeignKey(Account, on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now_add=False)
    time_out = models.DateField(auto_now_add=True)
    bill = models.FloatField(default=0.00)
    transaction_id = models.CharField(max_length=200, default=(str(mobile_number)+"_"+str(time_in)+"_"+str(time_out)), primary_key=True)

    def __str__(self):
        return str(self.transaction_id)