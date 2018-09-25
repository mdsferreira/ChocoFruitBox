from django.contrib import admin
from box import models

@admin.register(models.Chocolate)
class ChocolateAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Box)
class BoxAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Fruit)
class FruitAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ChocolateType)
class ChocolateTypeAdmin(admin.ModelAdmin):
    pass
