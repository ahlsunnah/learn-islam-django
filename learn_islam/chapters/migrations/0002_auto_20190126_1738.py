# Generated by Django 2.0.10 on 2019-01-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chaptertranslation',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='chaptertranslation',
            name='video',
            field=models.CharField(max_length=200, verbose_name='Video'),
        ),
    ]
