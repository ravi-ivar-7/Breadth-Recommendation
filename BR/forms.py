from django import forms
from .models import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    email = forms.CharField(max_length=65,label="Email",help_text="Enter Your E-mail Id")
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    erp_reg_email = forms.EmailField(label=" Institute  Email", required=True, help_text="Enter your Institute Email-id")
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

class SessionForm(forms.Form):
    SESSION_CHOICES = [
       
    ]
    session = forms.ChoiceField(choices=SESSION_CHOICES, widget=forms.RadioSelect)
    

class CategoryForm(forms.Form):
    CATEGORY_CHOICES = [
       
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.RadioSelect)





class CombinedForm(forms.Form):
    SESSION_CHOICES = [
        (1, 'Autumn 18'),
        (2, 'Spring 19'),
        (3, 'Autumn 19'),
        (4, 'Spring 20'),
        (5, 'Autumn 20'),
        (6, 'Spring 21'),
        (7, 'Autumn 21'),
        (8, 'Spring 22'),
        (9, 'Autumn 22'),
        (10, 't_session'),
        (11, 'Autumn 23'),
    ]
    session = forms.ChoiceField(choices=SESSION_CHOICES, widget=forms.RadioSelect)

    CATEGORY_CHOICES = [
         (1, 'Aerospace Engineering related roles'),
        (2, 'Artificial Intelligence related roles'),
        (3, 'Other related roles'),
        (4, 'Humanities and Social Science related roles'),
        (5, 'Mathematics related roles'),
        (6, 'Industrial and Systems Engineering related roles'),
        (7, 'Computer Science related roles'),
        (8, 'Mechanical Engineering related roles'),
        (9, 'Electrical Engineering related roles'),
        (10, 'Agriculture Engineering related roles'),
        (11, 'Architecture and Planning related roles'),
        (12, 'Biotechnology related roles'),
        (13, 'Environmental Science related roles'),
        (14, 'Civil Engineering related roles'),
        (15, 'Geology and Geophysics related roles'),
        (16, 'Chemical Engineering related roles'),
        (17, 'Chemistry related roles'),
        (18, 'Physics related roles'),
        (19, 'Metallurgical and Materials Engineering related roles'),
        (20, 'Mining Engineering related roles'),
        (21, 'Ocean Engineering and Naval Architecture related roles'),
    ]
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, widget=forms.RadioSelect)

    INTEREST_CHOICES = [
        (2, 'Specialized Topics'),
        (3, 'Competitive Programming for IT'),
        (4, 'Computer Architecture and Operating Systems'),
        (6, 'Programming and Software Engineering'),
        (7, 'Networking and Databases'),
        (8, 'Programming and Software Engineering; Networking and Databases'),
    ]
    personal_interests = forms.MultipleChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['name', 'roll_no',]
    
# class RecommendForm(forms.ModelForm):
#     class Meta:
#         model = Recommend
#         fields=[]
