# Generated by Django 2.2.6 on 2019-11-10 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afro_app', '0003_auto_20191021_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='geolocation',
            field=models.TextField(max_length=1000),
        ),
    ]
