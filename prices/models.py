from django.db import models


class Prices(models.Model):
    id = models.IntegerField(primary_key=True)
    price_fixed = models.FloatField()
    price_fractioned = models.FloatField()
    start = models.TimeField()
    end = models.TimeField()
    active = models.BooleanField(default=True)
