from django.urls import path
from BR import views

urlpatterns = [
    path('', views.vs_home, name='vs_home'),
    path('home', views.home, name='home'),
    
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),

    path('account', views.account, name='account'),
]