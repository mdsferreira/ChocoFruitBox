from django.db import models
from box.models import Fruit, ChocolateType
from django.contrib.auth.models import User


class Subscription(models.Model):
    start_date = models.DateTimeField(null=False, blank=False)    
    end_date = models.DateTimeField(null=True, blank=True)   

    def __str__(self):
        return str(self.start_date) +' - '+str(self.end_date)

class Address(models.Model):
    zipcode = models.CharField(max_length=20, null=True, blank=True, verbose_name='ZipCode')
    address = models.CharField(max_length=250, null=False, blank=False, verbose_name='Address')
    city = models.CharField(max_length=250, null=False, blank=False, verbose_name='City')
    state = models.CharField(max_length=250, null=False, blank=False, verbose_name='State')
    country = models.CharField(max_length=250, null=False, blank=False, verbose_name='Country')

    def __str__(self):
        return str(self.address) +', '+str(self.city)+', '+str(self.state)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='User')
    bulling_day = models.IntegerField(null=False, blank=False, verbose_name='Bulling Day')
    subscription = models.ForeignKey(Subscription, models.PROTECT, null=True, blank=True, verbose_name='Subscription')
    address = models.OneToOneField(Address, on_delete=models.CASCADE, verbose_name='Address')
    is_active = models.BooleanField(default=True, verbose_name='Active')

    def __str__(self):
        return str(self.user)

class Friend(models.Model):
    first_name = models.CharField(max_length=250, null=True, blank=True, verbose_name='First Name')
    last_name = models.CharField(max_length=250, null=True, blank=True, verbose_name='Last Name')
    birthday = models.DateField(null=True, blank=True, verbose_name='Birthday')
    address = models.ForeignKey(Address, models.PROTECT, null=False, blank=False, verbose_name='Address')
    subscription = models.ForeignKey(Subscription, models.PROTECT, null=True, blank=True, verbose_name='Subscription')
    is_active = models.BooleanField(default=True, verbose_name='Active')

    def __str__(self):
        return str(self.first_name)+ ' '+ str(self.last_name)

class FruitPreference(models.Model):
    custumer = models.ForeignKey(Customer, models.PROTECT, null=False, blank=False, verbose_name='Customer')
    fruit = models.ForeignKey(Fruit, models.PROTECT, null=False, blank=False, verbose_name='Fruit')
    level = models.SmallIntegerField(null=False, blank=False, verbose_name='Preference level')

    def __str__(self):
        return str(self.fruit)+ ' pref.: '+ str(self.level)

class ChocolatePreference(models.Model):
    custumer = models.ForeignKey(Customer, models.PROTECT, null=False, blank=False, verbose_name='Customer')
    chocolate_type = models.ForeignKey(ChocolateType, models.PROTECT, null=False, blank=False, verbose_name='Chocolate Type')
    level = models.SmallIntegerField(null=False, blank=False, verbose_name='Preference level')

    def __str__(self):
        return str(self.chocolate_type)+ ' pref.: '+ str(self.level)

