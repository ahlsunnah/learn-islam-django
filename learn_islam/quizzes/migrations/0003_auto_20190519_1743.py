# Generated by Django 2.0.10 on 2019-05-19 17:43

import learn_islam.core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_auto_20190519_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiztranslation',
            name='locale',
            field=learn_islam.core.models.LocaleField(choices=[('ar', 'العربية'), ('fr', 'Français')], max_length=10, verbose_name='Language'),
        ),
    ]
