from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from custumer import models


@admin.register(models.ChocolatePreference)
class ChocolatePreferenceAdmin(admin.ModelAdmin):
    pass

@admin.register(models.FruitPreference)
class FruitPreferenceAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Friend)
class FriendAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    pass    

class ProfileInline(admin.StackedInline):
    model = models.Custumer
    can_delete = False
    verbose_name_plural = 'Custumer'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

@admin.register(models.Custumer)
class CustumerAdmin(admin.ModelAdmin):
    pass