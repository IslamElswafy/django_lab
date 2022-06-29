from django.db import models

# Create your models here.

class MyUser(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20,null=True)
    password=models.CharField(max_length=20,null=True)
    email=models.EmailField(max_length=50,null=True)