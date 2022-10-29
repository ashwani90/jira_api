from django.db import models
from django.contrib.auth import get_user_model
from datetime import date
from django.db.models import Q
from .category import Category

User = get_user_model()

class File(models.Model):
    name=models.CharField(max_length=255)
    path=models.CharField(max_length=255)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    created_on=models.DateField()
    updated_on=models.DateField()
