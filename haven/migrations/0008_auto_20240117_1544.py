# Generated by Django 3.2.16 on 2024-01-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haven', '0007_alter_deployment_build_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='flavour',
            field=models.CharField(default='vanilla', max_length=400),
        ),
        migrations.AddField(
            model_name='deployment',
            name='selectors',
            field=models.JSONField(default=list),
        ),
    ]
