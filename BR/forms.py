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
        ('Autumn 18', 'Autumn 18'),
        ('Spring 19', 'Spring 19'),
        ('Autumn 19', 'Autumn 19'),
        ('Spring 20', 'Spring 20'),
        ('Autumn 20', 'Autumn 20'),
        ('Spring 21', 'Spring 21'),
        ('Autumn 21', 'Autumn 21'),
        ('Spring 22', 'Spring 22'),
        ('Autumn 22', 'Autumn 22'),
        ('t_session', 't_session'),
        ('Autumn 23', 'Autumn 23'),
    ]
    session = forms.ChoiceField(choices=[(str(index), session) for index, session in enumerate(SESSION_CHOICES, start=1)], label='Choose a session')

class CategoryForm(forms.Form):
    CATEGORY_CHOICES = [
        ('Aerospace Engineering_related_roles', 'Aerospace Engineering related roles'),
        ('Artificial Intelligence_related_roles', 'Artificial Intelligence related roles'),
        ('Other_related_roles', 'Other related roles'),
        ('Humanities and Social Science_related_roles', 'Humanities and Social Science related roles'),
        ('Mathematics_related_roles', 'Mathematics related roles'),
        ('Industrial and Systems Engineering_related_roles', 'Industrial and Systems Engineering related roles'),
        ('Computer Science_related_roles', 'Computer Science related roles'),
        ('Mechanical Engineering_related_roles', 'Mechanical Engineering related roles'),
        ('Electrical Engineering_related_roles', 'Electrical Engineering related roles'),
        ('Agriculture Engineering_related_roles', 'Agriculture Engineering related roles'),
        ('Architecture and Planning_related_roles', 'Architecture and Planning related roles'),
        ('Biotechnology_related_roles', 'Biotechnology related roles'),
        ('Environmental Science_related_roles', 'Environmental Science related roles'),
        ('Civil Engineering_related_roles', 'Civil Engineering related roles'),
        ('Geology and Geophysics_related_roles', 'Geology and Geophysics related roles'),
        ('Chemical Engineering_related_roles', 'Chemical Engineering related roles'),
        ('Chemistry_related_roles', 'Chemistry related roles'),
        ('Physics_related_roles', 'Physics related roles'),
        ('Metallurgical and Materials Engineering_related_roles', 'Metallurgical and Materials Engineering related roles'),
        ('Mining Engineering_related_roles', 'Mining Engineering related roles'),
        ('Ocean Engineering and Naval Architecture_related_roles', 'Ocean Engineering and Naval Architecture related roles'),
    ]
    category = forms.ChoiceField(choices=[(str(index), name) for index, (value, name) in enumerate(CATEGORY_CHOICES, start=1)], label='Choose a category')


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['name', 'roll_no',]
    
# class RecommendForm(forms.ModelForm):
#     class Meta:
#         model = Recommend
#         fields=[]
