# Generated by Django 4.0.3 on 2022-03-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Camera', '0002_tlproject_delete_camsettings'),
    ]

    operations = [
        migrations.AddField(
            model_name='tlproject',
            name='frames_shot',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tlproject',
            name='project_path',
            field=models.CharField(default='', max_length=255),
        ),
    ]
