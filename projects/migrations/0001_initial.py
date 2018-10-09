# Generated by Django 2.1.2 on 2018-10-09 11:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dropdowns', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='date_created')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='date modified')),
                ('name', models.CharField(max_length=300)),
                ('strength', models.CharField(max_length=200)),
                ('brand_name', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('project_type', models.IntegerField(choices=[(0, 'License-in'), (1, 'R&D'), (2, 'R&D external')], default=0)),
                ('contract_type', models.IntegerField(choices=[(0, 'LSA'), (1, 'LA+TT'), (2, 'DA')], default=0)),
                ('status', models.IntegerField(blank=True, choices=[(1, 'pre-PMB'), (2, 'pipeline'), (3, 'portfolio'), (0, 'terminated')], default=2, null=True)),
                ('prescription_category', models.IntegerField(choices=[(0, 'OTC'), (1, 'Rx'), (2, 'MD'), (3, 'DS')], default=1)),
                ('priority', models.IntegerField(blank=True, choices=[(0, 'tbc'), (1, 'Low'), (2, 'Normal'), (3, 'High')], default=0, null=True)),
                ('pack_size', models.TextField(blank=True)),
                ('shelf_life', models.IntegerField(blank=True, choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48)], default=0, null=True)),
                ('moq', models.CharField(blank=True, max_length=200)),
                ('sku', models.TextField(blank=True)),
                ('cogs', models.TextField(blank=True)),
                ('pmb_budget', models.FloatField(blank=True, default=None, null=True)),
                ('licence_costs', models.FloatField(blank=True, default=None, null=True)),
                ('licence_comment', models.TextField(blank=True)),
                ('regulatory_costs', models.FloatField(blank=True, default=None, null=True)),
                ('other_costs', models.FloatField(blank=True, default=None, null=True)),
                ('total_costs', models.FloatField(blank=True, default=None, null=True)),
                ('fiveyear_income', models.FloatField(blank=True, default=None, null=True)),
                ('npv', models.FloatField(blank=True, default=None, null=True)),
                ('ebidta', models.FloatField(blank=True, default=None, null=True)),
                ('ebitda_percent', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('pmb_approval', models.DateField(blank=True, null=True)),
                ('agreement', models.DateField(blank=True, null=True)),
                ('project_start', models.DateField(blank=True, null=True)),
                ('prototype_approved', models.DateField(blank=True, null=True)),
                ('registration_batches_ready', models.DateField(blank=True, null=True)),
                ('dossier_availability', models.DateField(blank=True, null=True)),
                ('dossier_submission', models.DateField(blank=True, null=True)),
                ('ma_granted', models.DateField(blank=True, null=True)),
                ('artwork_approval', models.DateField(blank=True, null=True)),
                ('product_in_dsv', models.DateField(blank=True, null=True)),
                ('launch_date', models.DateField(blank=True, null=True)),
                ('status_comment', models.TextField(blank=True)),
                ('pmb_approval_current', models.DateField(blank=True, null=True)),
                ('agreement_current', models.DateField(blank=True, null=True)),
                ('project_start_current', models.DateField(blank=True, null=True)),
                ('prototype_approved_current', models.DateField(blank=True, null=True)),
                ('registration_batches_ready_current', models.DateField(blank=True, null=True)),
                ('dossier_availability_current', models.DateField(blank=True, null=True)),
                ('dossier_submission_current', models.DateField(blank=True, null=True)),
                ('ma_granted_current', models.DateField(blank=True, null=True)),
                ('artwork_approval_current', models.DateField(blank=True, null=True)),
                ('product_in_dsv_current', models.DateField(blank=True, null=True)),
                ('launch_date_current', models.DateField(blank=True, null=True)),
                ('status_comment_current', models.TextField(blank=True)),
                ('risk_type', models.IntegerField(blank=True, choices=[(0, 'Unacceptable'), (1, 'Low'), (2, 'Medium'), (3, 'High')], default=1, null=True)),
                ('risk_comment', models.TextField(blank=True)),
                ('ip', models.DateField(blank=True, null=True)),
                ('dex', models.DateField(blank=True, null=True)),
                ('mex', models.DateField(blank=True, null=True)),
                ('mfd', models.DateField(blank=True, null=True)),
                ('ip_comment', models.TextField(blank=True)),
                ('maq', models.CharField(blank=True, max_length=300)),
                ('supply_price', models.TextField(blank=True)),
                ('floor_price', models.FloatField(blank=True, default=None, null=True)),
                ('floor_price_currency', models.CharField(blank=True, max_length=300)),
                ('reconciliation', models.NullBooleanField()),
                ('reconciliation_comment', models.TextField(blank=True)),
                ('lead_time_launch', models.TextField(blank=True)),
                ('lead_time_commercial', models.TextField(blank=True)),
                ('supply_period', models.FloatField(blank=True, default=None, null=True)),
                ('automatic_prolongation', models.NullBooleanField()),
                ('prolongation_period', models.FloatField(blank=True, default=None, null=True)),
                ('agreement_expiry', models.TextField(blank=True)),
                ('agreement_expiry_date', models.DateField(blank=True, null=True)),
                ('notice_period', models.FloatField(blank=True, default=None, null=True)),
                ('manufacturing_site', models.TextField(blank=True)),
                ('batch_release_site', models.TextField(blank=True)),
                ('rolling_forecast', models.TextField(blank=True)),
                ('inventory_level', models.TextField(blank=True)),
                ('payment_terms', models.FloatField(blank=True, default=None, null=True)),
                ('exclusive_suplies', models.NullBooleanField()),
                ('exclusivity_period', models.FloatField(blank=True, default=None, null=True)),
                ('agreement_number_eou', models.CharField(blank=True, max_length=300)),
                ('variation_cost', models.TextField(blank=True)),
                ('additional_costs', models.TextField(blank=True)),
                ('atc3_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dropdowns.AtcClass')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to=settings.AUTH_USER_MODEL)),
                ('form', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dropdowns.FormNFC12')),
                ('licensor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dropdowns.Licensor')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowns.Market')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_by', to=settings.AUTH_USER_MODEL)),
                ('molecule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowns.Molecule')),
                ('otc_atc2_class', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dropdowns.OtcAtc2Class')),
                ('pact_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dropdowns.PackType')),
                ('pharmaceutical_form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowns.PharmaForm')),
                ('product_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dropdowns.ProductCategory')),
                ('therapeutic_area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dropdowns.TherapeuticArea')),
            ],
        ),
    ]
