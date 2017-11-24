from django.db import models


# Create your models here.
class DogFeed(models.Model):
    feed = models.CharField(primary_key=True, max_length=100)
    eat = models.BooleanField()