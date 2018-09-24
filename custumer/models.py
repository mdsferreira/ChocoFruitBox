from django.db import models
from order.models import Fruit, ChocolateType

class Subscription(models.Model):
    start_date = models.DateTimeField()    
    end_date = models.DateTimeField()    

class Address(models.Model):
    zipcode = models.CharField(max_length=20, null=True, blank=True, verbose_name='ZipCode')
    address = models.CharField(max_length=250, null=False, blank=False, verbose_name='Address')
    city = models.CharField(max_length=250, null=False, blank=False, verbose_name='City')
    state = models.CharField(max_length=250, null=False, blank=False, verbose_name='State')
    country = models.CharField(max_length=250, null=False, blank=False, verbose_name='Country')

class Custumer(models.Model):
    bulling_day = models.IntegerField(null=False, blank=False, verbose_name='Bulling Day')
    subscription = models.ForeignKey(Subscription, models.PROTECT, null=True, blank=True, verbose_name='Subscription')
    address = models.ForeignKey(Address, models.PROTECT, null=False, blank=False, verbose_name='Address')
    is_active = models.BooleanField(blank=False, verbose_name='Active')

class Friend(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=250, null=True, blank=True, verbose_name='Last Name')
    birthday = models.DateField(null=True, blank=True, verbose_name='Birthday')
    subscription = models.ForeignKey(Subscription, models.PROTECT, null=True, blank=True, verbose_name='Subscription')
    is_active = models.BooleanField(blank=False, verbose_name='Active')

class FruitPreference(models.Model):
    custumer = models.ForeignKey(Custumer, models.PROTECT, null=False, blank=False, verbose_name='Custumer')
    fruit = models.ForeignKey(Fruit, models.PROTECT, null=False, blank=False, verbose_name='Fruit')
    level = models.IntegerField(null=False, blank=False, verbose_name='Bulling Day', max_length=1)

class ChocolatePreference(models.Model):
    custumer = models.ForeignKey(Custumer, models.PROTECT, null=False, blank=False, verbose_name='Custumer')
    chocolate_type = models.ForeignKey(ChocolateType, models.PROTECT, null=False, blank=False, verbose_name='Chocolate Type')
    level = models.IntegerField(null=False, blank=False, verbose_name='Bulling Day', max_length=1)