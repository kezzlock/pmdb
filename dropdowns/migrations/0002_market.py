# Generated by Django 2.0.7 on 2018-08-09 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropdowns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]
