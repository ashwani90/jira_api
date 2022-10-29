from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from django.db.models import Q

User = get_user_model()

class Category(models.Model):
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
