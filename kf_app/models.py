from django.db import models

# Create your models here.
class User(models.Model):
	Uname = models.CharField(max_length=30)
	email = models.CharField(max_length = 100)
	pwd = models.CharField(max_length = 50)
	