from django.db import models

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    profession = models.CharField(max_length=30)
    interests = models.TextField(max_length=200)
    pros = models.TextField(max_length=200)
    cons = models.TextField(max_length=200)
    
