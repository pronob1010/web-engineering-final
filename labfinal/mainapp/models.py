from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE=(
        ('Type A','Type A'),
        ('Type B','Type B'),
        ('Type C','Type C'),
        ('Type D','Type D'),
        )
class categories(models.Model):
    tittle = models.CharField(max_length=100)

class product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.ManyToManyField(categories)
    Available_Unit = models.IntegerField()

class UserProfile(models.Model):
    TYPE=(
        ('Male','Male'),
        ('Female','Female'),
        ('Transgender','Transgender')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    gender = models.CharField(max_length=100, choices=TYPE,default=None)
    contact = models.CharField(max_length=15)
    image = models.ImageField(upload_to='media/images')
    