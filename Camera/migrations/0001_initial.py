# Generated by Django 4.0.3 on 2022-03-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CamSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cam_status', models.BooleanField(default=True)),
                ('tl_interval', models.IntegerField(default=0)),
            ],
        ),
    ]
