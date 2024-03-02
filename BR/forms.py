from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.CharField(max_length=65,label="Email",help_text="Enter Your E-mail Id")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    erp_reg_email = forms.EmailField(label="ERP Registered personal Email", required=True, help_text="Enter your Institute Email-id")
    email = forms.EmailField(label="Email confirmation", required=True, help_text="Confirm Email")

    class Meta:
        model = User
        fields = ['erp_reg_email', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        erp_reg_email = cleaned_data.get("erp_reg_email")
        email = cleaned_data.get("email")

        if erp_reg_email and email and erp_reg_email != email:
            raise forms.ValidationError("The two email fields didn't match.")

        return cleaned_data





# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['name', 'roll_no',]
    
# class RecommendForm(forms.ModelForm):
#     class Meta:
#         model = Recommend
#         fields=[]
