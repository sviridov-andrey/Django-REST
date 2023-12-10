# Generated by Django 4.1.13 on 2023-12-10 00:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leson',
            name='video',
            field=models.URLField(blank=True, null=True, verbose_name='ссылка на видео'),
        ),
        migrations.AlterField(
            model_name='leson',
            name='сourse',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='education.course'),
        ),
    ]
