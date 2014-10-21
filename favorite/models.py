from django.db import models
from django.contrib.auth.models import User
from catalog.models import Item


class Favorite(models.Model):
    user = models.ForeignKey(User)
    item = models.ForeignKey(Item)