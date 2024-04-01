from django.shortcuts import render,redirect,HttpResponse
from BR.models import *
from django.contrib import messages
from .forms import *
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
import csv
# import pandas as pd

from django.contrib.auth import login, authenticate,logout
from django.db.models import Q





def vs_home(request):

    return redirect('register')

def home(request):
    user_profile = None
   
    return redirect('register')

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'login_register.html', {'register_form': form})

    if request.method == 'POST':
     
            form = RegisterForm(request.POST)
            if form.is_valid():
                erp_reg_email = form.cleaned_data.get('erp_reg_email')

                if User.objects.filter(username=erp_reg_email).exists():
                    messages.error(request, 'A user with this Email already exists.')
                    return redirect('register')
                
                try:
                    user = form.save(commit=False)
                    user.username = erp_reg_email 
                    user.save()
                    return redirect('/account')

                except Exception as e:
                    messages.error(request, f'An error occurred while trying to create your account.[{e}]')
                    return redirect('register')
                
             
            
            else:
  
                for field, errors in form.errors.items():
                    for error in errors:
                        messages.error(request, f"{error}")
                return render(request, 'login_register.html', {'register_form': form})
    
        
def sign_in(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,'login_register.html', {'login_form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data['email'] 
            password = form.cleaned_data['password']
            user = authenticate(request,username=email,password=password)
            if user:
                messages.info(request, "successful login.")
                login(request, user)
                return redirect('account')

        messages.error(request,f'Invalid username or password')
        return render(request,'login_register.html',{'login_form': form})
    
def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login')        

@login_required(login_url='/login')
def account(request):
    if request.method == 'POST':
        # If the form is submitted
        combined_form = CombinedForm(request.POST)
        if combined_form.is_valid():
            # Process the combined form data
            session = combined_form.cleaned_data['session']
            category = combined_form.cleaned_data['category']
            personal_interests = combined_form.cleaned_data['personal_interests']
            # Do something with the collected data

            # Redirect or return response after processing the form data
            return HttpResponse("Form submitted successfully!")
    else:
        # If it's a GET request, render the form page
        combined_form = CombinedForm()
        return render(request, 'account.html', {'combined_form': combined_form})