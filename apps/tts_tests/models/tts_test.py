from django.db import models

from apps.texts.models import TextLanguage


class TtsTest(models.Model):
    language = models.ForeignKey(TextLanguage, on_delete=models.RESTRICT)
    text = models.TextField()
    volume = models.FloatField()
    pitch = models.FloatField()
    rate = models.FloatField()

    def __str__(self):
        return f'{self.text} (volume:{self.volume}, pitch:{self.pitch}, rate:{self.rate})'

    class Meta:
        unique_together = (('language', 'text', 'volume', 'pitch', 'rate'))
