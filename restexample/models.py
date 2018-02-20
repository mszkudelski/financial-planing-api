from django.db import models
from rest_framework.authtoken.models import Token

class Category (models.Model):
    TYPE_CHOICES= (
        ( 'r', 'revenue'),
        ( 'e', 'expense')
    )
    name = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

class Revenue(models.Model):
    value = models.IntegerField()
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, related_name='revenues', on_delete=models.CASCADE)
    description = models.TextField(max_length=100)

class Expense(models.Model):
    value = models.IntegerField()
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, related_name='expenses', on_delete=models.CASCADE)
    description = models.TextField(max_length=100)

class Plan(models.Model):
    value = models.IntegerField()
    category = models.ForeignKey(Category, related_name='plans', on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)