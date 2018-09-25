from django.contrib import admin
from order import models

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Bill)
class BillAdmin(admin.ModelAdmin):
    pass
