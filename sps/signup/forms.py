from django import forms
from login.models import Account

class SignUpForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'age', 'mobile_number', 'vehicle_number', 'pwd']