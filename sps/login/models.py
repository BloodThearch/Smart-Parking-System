from django.db import models

# Create your models here.
class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)
    mobile_number = models.IntegerField(max_length=10, primary_key=True)
    vehicle_number = models.CharField(max_length=50)
    pwd = models.CharField(max_length=50)

    def __str__(self):
        return str(self.mobile_number)