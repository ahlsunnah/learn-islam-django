# Generated by Django 2.0.10 on 2019-01-26 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_auto_20190126_1306'),
        ('topics', '0001_initial'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Description')),
                ('locale', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=20, verbose_name='Title')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='topic',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='topics.Topic'),
        ),
        migrations.AddField(
            model_name='course',
            name='track',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tracks.Track'),
        ),
        migrations.AddField(
            model_name='coursetranslation',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='courses.Course'),
        ),
        migrations.AlterUniqueTogether(
            name='coursetranslation',
            unique_together={('locale', 'course')},
        ),
    ]
