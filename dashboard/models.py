from django.db import models
from django.conf import settings
from decimal import Decimal

# Create your models here.
class Dashboard(models.Model):
    user= models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='Dashboard')
    pending = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    credits = models.DecimalField(max_digits=20,decimal_places=1,default=Decimal('0.0'))
