from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name



class Recommend(models.Model):
    gpa = models.CharField(max_length = 10)
    