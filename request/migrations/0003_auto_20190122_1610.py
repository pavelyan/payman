# Generated by Django 2.1.4 on 2019-01-22 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0002_auto_20190122_1449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='company',
            new_name='costcenter',
        ),
    ]
