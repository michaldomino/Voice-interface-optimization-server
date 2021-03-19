from django.db import models

from apps.voice_interface_optimization.models import Text


class TtsTest(models.Model):

    text = models.ForeignKey(Text, on_delete=models.RESTRICT)
    volume = models.FloatField()
    pitch = models.FloatField()
    rate = models.FloatField()

    class Meta:
        unique_together = (('text', 'volume', 'pitch', 'rate'))