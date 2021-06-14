# Generated by Django 3.1.7 on 2021-06-14 21:09

from django.db import migrations, models
import django.db.models.deletion


def set_defaults(apps, schema_editor):
    TtsTest = apps.get_model('tts_tests', 'TtsTest')
    for tts_test in TtsTest.objects.all().iterator():
        tts_test.text2 = tts_test.text.text
        tts_test.language = tts_test.text.language
        tts_test.save()


class Migration(migrations.Migration):
    dependencies = [
        ('texts', '0001_initial'),
        ('tts_tests', '0002_auto_20210321_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='ttstest',
            name='language',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='texts.textlanguage',
                                    null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ttstest',
            name='text2',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.RunPython(set_defaults, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='ttstest',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='texts.textlanguage'),
            preserve_default=False,
        )
    ]
