from django.db import models


class TextLanguage(models.Model):
    id = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.id
