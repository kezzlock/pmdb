# Generated by Django 2.1.2 on 2018-10-09 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropdowns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Delivery Terms',
                'verbose_name_plural': 'Delivery Terms',
            },
        ),
    ]