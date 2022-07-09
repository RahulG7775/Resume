from django.db import models

# Create your models here.
class Edudetails(models.Model):
    Education=models.CharField(max_length=70)
    College=models.CharField(max_length=150)
    Year_of_Passing=models.IntegerField()
    University =models.CharField(max_length=200)
    Marks=models.FloatField(max_length=2)