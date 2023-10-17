# Generated by Django 4.2.6 on 2023-10-17 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=150)),
                ('jins', models.CharField(max_length=6)),
                ('shahar', models.CharField(max_length=150)),
                ('davlat', models.CharField(max_length=150)),
                ('sms_kod', models.CharField(max_length=150)),
                ('tasdiqlangan', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
