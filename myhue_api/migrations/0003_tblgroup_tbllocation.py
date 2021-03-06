# Generated by Django 2.2 on 2022-01-15 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhue_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='tblLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tblGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhue_api.tblLocation')),
            ],
        ),
    ]
