# Generated by Django 3.1.7 on 2021-03-04 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PortTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arkitekt_id', models.CharField(help_text='The corresponding Template on the Arkitekt Instance', max_length=1000)),
                ('namespace', models.CharField(help_text='Corresponds to docker hub user', max_length=100)),
                ('repo', models.CharField(help_text='Corresponds to docker repo name', max_length=100)),
                ('tag', models.CharField(help_text='Corresponds to docker hub user', max_length=100)),
            ],
        ),
    ]
