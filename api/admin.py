from django.contrib import admin

# Register your models here.
from api import models

admin.site.register(models.TextKey)
admin.site.register(models.TextLanguage)
admin.site.register(models.Text)
admin.site.register(models.TextResult)
