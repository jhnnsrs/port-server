# Generated by Django 3.2.19 on 2023-08-29 10:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('haven', '0006_auto_20230829_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deployment',
            name='build_id',
            field=models.CharField(default=uuid.uuid4, max_length=400),
        ),
    ]
