from django.db import models

from apps.texts.models import Text


class SttTest(models.Model):
    text = models.OneToOneField(Text, on_delete=models.RESTRICT)
