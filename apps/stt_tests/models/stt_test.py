from django.db import models

from apps.texts.models import TextLanguage


class SttTest(models.Model):
    language = models.ForeignKey(TextLanguage, on_delete=models.RESTRICT)
    text = models.TextField()

    def __str__(self):
        return f'{self.text}'

    class Meta:
        unique_together = (('language', 'text'))
