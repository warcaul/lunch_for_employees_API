from django.db import models
import datetime
from authentication.models import User
from django.conf import settings

class Restaurant(models.Model):
    """Модель ресторану"""
    name_of_rest = models.CharField(max_length=50, db_index=True)


class Menu(models.Model):
    """Модель меню"""
    name_of_menu = models.CharField(max_length=50, db_index=True)
    first_course = models.CharField(max_length=50, null=True, blank=True)
    second_course = models.CharField(max_length=50, null=True, blank=True)
    snack = models.CharField(max_length=50, null=True, blank=True)
    salad = models.CharField(max_length=50, null=True, blank=True)
    side = models.CharField(max_length=50, null=True, blank=True)
    dish = models.CharField(max_length=50, null=True, blank=True)
    beverage = models.CharField(max_length=50, null=True, blank=True)
    day = models.DateField()
    rest = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    users_votes = models.ManyToManyField( to='Menu', through='Vote', blank=True,)


    @property
    def votes(self):
        """розрахунок популярності меню"""
        return self.users_votes.count()

    class Meta:
        ordering = ['day']


class Vote(models.Model):
    """Модель голосування"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    menu_for_vote = models.ForeignKey(
        Menu, on_delete=models.CASCADE, db_index=True)