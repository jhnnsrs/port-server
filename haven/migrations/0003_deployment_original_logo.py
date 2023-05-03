# Generated by Django 3.2.18 on 2023-05-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haven', '0002_deployment_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='deployment',
            name='original_logo',
            field=models.CharField(blank=True, help_text='The original logo url', max_length=1000, null=True),
        ),
    ]
