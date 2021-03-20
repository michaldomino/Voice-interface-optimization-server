from django.db import models

from apps.texts.models import Text


class SttTest(models.Model):
    text = models.ForeignKey(Text, on_delete=models.RESTRICT)
