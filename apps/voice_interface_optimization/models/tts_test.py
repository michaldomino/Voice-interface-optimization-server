from django.db import models

from .text import Text


class TtsTest(models.Model):

    text = models.ForeignKey(Text, on_delete=models.RESTRICT)
    volume = models.FloatField()
    pitch = models.FloatField()
    rate = models.FloatField()

    class Meta:
        unique_together = (('text', 'volume', 'pitch', 'rate'))