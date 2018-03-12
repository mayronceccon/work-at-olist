from django.db import models


class Price(models.Model):
    price_fixed = models.FloatField()
    price_fractioned = models.FloatField()
    start = models.TimeField()
    end = models.TimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return "%s at %s" % (self.start, self.end)
