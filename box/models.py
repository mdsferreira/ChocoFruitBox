from django.db import models

class ChocolateType(models.Model):
    description = models.CharField(max_length=250, null=False, blank=False, verbose_name='Description')
    is_active = models.BooleanField(default=True, verbose_name='Active')

    def __str__(self):
        return self.description

class Fruit(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name='Name')
    is_active = models.BooleanField(default=True, verbose_name='Active')

    def __str__(self):
        return self.name

class Chocolate(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name='Name')
    description = models.CharField(max_length=250, null=True, blank=True, verbose_name='Description')
    chocolate_type = models.ForeignKey(ChocolateType, models.PROTECT, null=False, blank=False, verbose_name='Chocolate type')
    fruit = models.ForeignKey(Fruit, models.PROTECT, null=False, blank=False, verbose_name='Fruit')
    is_active = models.BooleanField(default=True, verbose_name='Active')

    def __str__(self):
        return self.name

class Box(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False, verbose_name='Name')
    description = models.CharField(max_length=250, null=False, blank=False, verbose_name='Description')
    chocolate = models.ManyToManyField(Chocolate, blank=True)

    def __str__(self):
        return self.name

