from django.db import models

# Create your models here.

class blooddonation(models.Model):
  name = models.CharField(max_length=50)
  number = models.CharField(max_length=20)
  address = models.CharField(max_length=100)
  blood_group = models.CharField(max_length=15)
  donation_date = models.CharField(max_length=20)
  
  def __str__(self):
        return self.name

  
