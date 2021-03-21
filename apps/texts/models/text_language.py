from django.db import models


class TextLanguage(models.Model):
    code = models.CharField(max_length=20)

    def __str__(self):
        return self.code
