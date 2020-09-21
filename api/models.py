from django.db import models


# Create your models here.
class TextKey(models.Model):
    id = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.id


class TextLanguage(models.Model):
    id = models.CharField(max_length=5, primary_key=True)

    def __str__(self):
        return self.id


class Text(models.Model):
    key = models.ForeignKey(TextKey, on_delete=models.RESTRICT)
    language = models.ForeignKey(TextLanguage, on_delete=models.RESTRICT)
    text = models.TextField(unique=True)

    def __str__(self):
        return self.text

    class Meta:
        unique_together = (('key', 'language'))


class TextResult(models.Model):
    text = models.ForeignKey(Text, on_delete=models.RESTRICT)
    volume = models.FloatField()
    pitch = models.FloatField()
    rate = models.FloatField()
