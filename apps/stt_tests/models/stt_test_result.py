from django.db import models

from Voice_interface_optimization_server import settings
from apps.stt_tests.models import SttTest


class SttTestResult(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)
    stt_test = models.ForeignKey(SttTest, on_delete=models.RESTRICT)
    result = models.TextField()

    def __str__(self):
        return f'test: {self.stt_test}, result: {self.result} ({self.user})'
