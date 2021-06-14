from django.db import models

from apps.texts.models import Text, TextLanguage


class TtsTest(models.Model):
    text = models.ForeignKey(Text, on_delete=models.RESTRICT)
    language = models.ForeignKey(TextLanguage, on_delete=models.RESTRICT)
    text2 = models.TextField()
    volume = models.FloatField()
    pitch = models.FloatField()
    rate = models.FloatField()

    def __str__(self):
        return f'{self.text} (volume:{self.volume}, pitch:{self.pitch}, rate:{self.rate})'

    class Meta:
        unique_together = (('text', 'volume', 'pitch', 'rate'))
