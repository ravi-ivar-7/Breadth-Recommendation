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

    return render(request,'home.html',)

def home(request):
    user_profile = None
   
    return render(request,'home.html')

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
    if request.user.is_authenticated:
        try:
            user_profile = request.user
          
            context = {
               'email':user_profile.email,
            }
            print(user_profile.email)
        except UserProfile.DoesNotExist:
            print('does not exit')

            context = {}
    else:
        print('login')
        context = {}
    
    return render(request, 'account.html', context)
