# Generated by Django 2.1.2 on 2018-10-05 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20181005_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='form',
            new_name='pharmaceutical_form',
        ),
    ]
