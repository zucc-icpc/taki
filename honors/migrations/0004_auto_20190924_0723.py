# Generated by Django 2.2.5 on 2019-09-23 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('honors', '0003_auto_20190924_0711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='honor',
            options={'ordering': ('-time',)},
        ),
    ]
