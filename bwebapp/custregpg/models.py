from django.db import models
from django.forms import ModelForm

# Create your models here.

class CustRegst(models.Model):
    first_name = models.CharField(max_length= 100, )
    middle_name = models.CharField(max_length=100,null=True)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=50, primary_key=True, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    mobile = models.IntegerField()

