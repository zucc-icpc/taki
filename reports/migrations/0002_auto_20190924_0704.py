# Generated by Django 2.2.5 on 2019-09-23 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'ordering': ('-created',)},
        ),
    ]