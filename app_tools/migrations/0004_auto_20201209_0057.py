# Generated by Django 3.1.2 on 2020-12-08 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_tools', '0003_auto_20201209_0019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weaponline',
            old_name='rar',
            new_name='rarity',
        ),
    ]