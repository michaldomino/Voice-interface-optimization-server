from django.contrib import admin

from apps.tts_tests import models

# Register your models here.
admin.site.register(models.TtsTest)
admin.site.register(models.TtsTestResult)
