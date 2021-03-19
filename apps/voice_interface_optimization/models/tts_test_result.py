from django.db import models

from Voice_interface_optimization_server import settings
from .tts_test import TtsTest


class TtsTestResult(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    tts_test = models.ForeignKey(TtsTest, on_delete=models.RESTRICT)
    result = models.BooleanField()