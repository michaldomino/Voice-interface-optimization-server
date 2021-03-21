# Generated by Django 3.1.1 on 2021-03-21 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TtsTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.FloatField()),
                ('pitch', models.FloatField()),
                ('rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TtsTestResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.BooleanField()),
                ('tts_test', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tts_tests.ttstest')),
            ],
        ),
    ]
