from django.db import models

from apps.voice_interface_optimization.models import TextLanguage


class Text(models.Model):

    language = models.ForeignKey(TextLanguage, on_delete=models.RESTRICT)
    text = models.TextField()

    def __str__(self):
        return self.text

    class Meta:
        unique_together = (('language', 'text'))