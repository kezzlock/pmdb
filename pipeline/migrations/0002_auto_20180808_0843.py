# Generated by Django 2.0.7 on 2018-08-08 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pipeline', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.IntegerField(choices=[(0, 'License-in'), (1, 'R&D'), (2, 'R&D external')], default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'pre-PMB'), (2, 'pipeline'), (3, 'portfolio'), (0, 'terminated')], default=2, null=True),
        ),
    ]
