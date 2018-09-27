from django.db import models
from customer.models import Customer

class Bill(models.Model):
    value = models.FloatField(null=False, blank=False, verbose_name='Total Value')
    payday = models.DateField(null=True, blank=True, verbose_name='Payday')    
    discount = models.FloatField(null=False, blank=False, verbose_name='Total Value')

    def __str__(self):
        return self.value

class Order(models.Model):    
    customer = models.ForeignKey(Customer, models.PROTECT, null=True, blank=True, verbose_name='Bill')
    bill = models.ForeignKey(Bill, models.PROTECT, null=True, blank=True, verbose_name='Bill')
    order_date = models.IntegerField(null=False, blank=False, verbose_name='Bulling Day')
    order_number = models.CharField(max_length=100, null=False, blank=False, verbose_name='Order Number')

    def __str__(self):
        return self.order_number + '/' + str(self.customer)



