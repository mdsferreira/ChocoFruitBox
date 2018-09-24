from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    Order,
    Fruit,
    ChocolateType,
    Chocolate, 
    Bill)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    pass

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    pass

@admin.register(ChocolateType)
class ChocolateTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Chocolate)
class ChocolateAdmin(admin.ModelAdmin):
    pass
