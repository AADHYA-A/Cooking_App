# recipes/models.py
from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    ingredients = models.TextField()
    preparation_time = models.IntegerField(help_text="in minutes")

    def __str__(self):
        return self.title