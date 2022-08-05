from django.contrib import admin
from .models import Menu, Restaurant, Vote

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    pass


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    pass

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass