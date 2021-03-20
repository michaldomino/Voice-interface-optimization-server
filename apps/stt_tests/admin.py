from django.contrib import admin

from apps.stt_tests import models

# Register your models here.
admin.site.register(models.SttTest)
admin.site.register(models.SttTestResult)
