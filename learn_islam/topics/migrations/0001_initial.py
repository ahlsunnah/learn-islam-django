# Generated by Django 2.0.10 on 2019-01-26 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(blank=True, max_length=20, verbose_name='Color')),
                ('level', models.PositiveIntegerField(blank=True, verbose_name='Level')),
                ('order', models.PositiveIntegerField(blank=True, verbose_name='Order')),
                ('slug', models.CharField(blank=True, max_length=255, verbose_name='Slug')),
            ],
        ),
        migrations.CreateModel(
            name='TopicTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='topics.Topic')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='topictranslation',
            unique_together={('locale', 'topic')},
        ),
    ]