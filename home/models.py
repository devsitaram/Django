from django.db import models

# Create your models here.
class Student(models.Model):
    # id = models.BigAutoField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    image = models.ImageField()
    files = models.FileField()

class Product(models.Model):
    pass
