# Generated by Django 2.0.10 on 2019-01-26 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20190126_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetranslation',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
    ]