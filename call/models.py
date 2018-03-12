from django.db import models


class Call(models.Model):
    TYPES_CALL = (
        ('start', 'Start'),
        ('end', 'End'),
    )
    type = models.CharField(
        max_length=10,
        choices=TYPES_CALL
    )
    start = models.DateTimeField()
    end = models.DateTimeField(blank=True, null=True)
    call_id_external = models.CharField(max_length=255)
    source = models.CharField(max_length=11)
    destination = models.CharField(max_length=11)

    def __str__(self):
        return "%s to %s" % (self.source, self.destination)
