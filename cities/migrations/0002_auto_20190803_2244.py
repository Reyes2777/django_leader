# Generated by Django 2.2.4 on 2019-08-03 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'ordering': ('name',)},
        ),
    ]
