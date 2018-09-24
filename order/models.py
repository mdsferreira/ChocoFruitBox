from django.db import models

class Bill(models.Model):
    value = models.FloatField(null=False, blank=False, verbose_name='Total Value')
    payday = models.DateField(null=True, blank=True, verbose_name='Payday')    

class Order(models.Model):
    bulling_day = models.IntegerField(null=False, blank=False, verbose_name='Bulling Day')
    is_subscriber = models.BooleanField(blank=False, verbose_name='Subscriber')
    bill = models.ForeignKey(Bill, models.PROTECT, null=True, blank=True, verbose_name='Bill')

class Fruit(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name='Name')
    is_active = models.BooleanField(blank=False, verbose_name='Active')

class ChocolateType(models.Model):
    description = models.CharField(max_length=250, null=False, blank=False, verbose_name='Description')
    is_active = models.BooleanField(blank=False, verbose_name='Active')

class Chocolate(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name='Name')
    description = models.CharField(max_length=250, null=True, blank=True, verbose_name='Description')
    chocolate_type = models.ForeignKey(ChocolateType, models.PROTECT, null=False, blank=False, verbose_name='Chocolate type')
    fruit = models.ForeignKey(ChocolateType, models.PROTECT, null=False, blank=False, verbose_name='Fruit')
    is_active = models.BooleanField(blank=False, verbose_name='Active')

