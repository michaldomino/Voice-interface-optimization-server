from django.db import models

from apps.texts.models import Text, TextLanguage


class SttTest(models.Model):
    text = models.OneToOneField(Text, on_delete=models.RESTRICT)
    language = models.ForeignKey(TextLanguage, on_delete=models.RESTRICT)
    text2 = models.TextField()

    def __str__(self):
        return f'{self.text}'
