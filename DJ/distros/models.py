from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Distro(models.Model):
	name = models.CharField(max_length=100)
	description	= models.TextField(blank=True)

