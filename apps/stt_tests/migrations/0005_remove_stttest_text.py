# Generated by Django 3.1.7 on 2021-06-14 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stt_tests', '0004_stttest_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stttest',
            name='text',
        ),
    ]
