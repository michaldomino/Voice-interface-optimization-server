from django.contrib import admin
import models

# Register your models here.
admin.site.register(models.TextLanguage)
admin.site.register(models.Text)
admin.site.register(models.TtsTest)
admin.site.register(models.TtsTestResult)

