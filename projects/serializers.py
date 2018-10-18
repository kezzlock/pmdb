from rest_framework import serializers

from projects.models import Project


def get_user_full_name(user):
    """Return full neme of a userself.

    if first and last name are provided return get_full_name()
    else return username

    return '-' if user not defined.
    """
    if user:
        if user.first_name and user.last_name:
            name = user.get_full_name()
        else:
            name = user.username
    else:
        name = "-"
    return name


class ProjectDetailSerializer(serializers.ModelSerializer):
    # TODO: create autointerator for integer choice fields
    # DateTimeField
    create_date = serializers.DateTimeField()
    modify_date = serializers.DateTimeField()
    # Ingeget choice
    project_type = serializers.CharField(source='get_project_type_display')
    contract_type = serializers.CharField(source='get_contract_type_display')
    status = serializers.CharField(source='get_status_display')
    prescription_category = serializers.CharField(
        source='get_prescription_category_display')
    priority = serializers.CharField(source='get_priority_display')
    shelf_life = serializers.CharField(source='get_shelf_life_display')
    risk_type = serializers.CharField(source='get_risk_type_display')
    # ForeignKey fields TODO: Create autointerator
    created_by = serializers.SerializerMethodField('get_creted_by_full_name')
    modified_by = serializers.SerializerMethodField(
        'get_modified_by_full_name')
    molecule = serializers.StringRelatedField()
    pharmaceutical_form = serializers.StringRelatedField()
    market = serializers.StringRelatedField()
    manager = serializers.SerializerMethodField('get_manager_full_name')
    therapeutic_area = serializers.StringRelatedField()
    atc_class = serializers.StringRelatedField()
    pact_type = serializers.StringRelatedField()
    licensor = serializers.StringRelatedField()
    product_category = serializers.StringRelatedField()
    otc_atc2_class = serializers.StringRelatedField()
    form = serializers.StringRelatedField()

    def get_creted_by_full_name(self, obj):
        user = obj.created_by
        return get_user_full_name(user)

    def get_modified_by_full_name(self, obj):
        user = obj.modified_by
        return get_user_full_name(user)

    def get_manager_full_name(self, obj):
        user = obj.manager
        return get_user_full_name(user)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('name', 'brand_name', 'molecule', 'description',
                  'product_category',
                  'strength',
                  'market',
                  'manager',
                  'project_type',
                  'pharmaceutical_form',
                  'form',
                  'contract_type',
                  'status',
                  'prescription_category',
                  'therapeutic_area',
                  'priority',
                  'atc3_class',
                  'otc_atc2_class',
                  'pack_size',
                  'pact_type',
                  'shelf_life',
                  'moq',
                  'sku',
                  'cogs',
                  'pmb_budget',
                  'licence_costs',
                  'licence_comment',
                  'regulatory_costs',
                  'other_costs',
                  'total_costs',
                  'fiveyear_income',
                  'npv',
                  'ebidta',
                  'ebitda_percent',
                  'pmb_approval',
                  'agreement',
                  'project_start',
                  'prototype_approved',
                  'registration_batches_ready',
                  'dossier_availability',
                  'dossier_submission',
                  'ma_granted',
                  'artwork_approval',
                  'product_in_dsv',
                  'launch_date',
                  'status_comment',
                  'pmb_approval_current',
                  'agreement_current',
                  'project_start_current',
                  'prototype_approved_current',
                  'registration_batches_ready_current',
                  'dossier_availability_current',
                  'dossier_submission_current',
                  'ma_granted_current',
                  'artwork_approval_current',
                  'product_in_dsv_current',
                  'launch_date_current',
                  'status_comment_current',
                  'risk_type',
                  'risk_comment',
                  'ip',
                  'dex',
                  'mex',
                  'mfd',
                  'ip_comment',
                  'licensor',
                  'maq',
                  'supply_price',
                  'floor_price',
                  'floor_price_currency',
                  'reconciliation',
                  'reconciliation_comment',
                  'lead_time_launch',
                  'lead_time_commercial',
                  'supply_period',
                  'automatic_prolongation',
                  'prolongation_period',
                  'agreement_expiry',
                  'agreement_expiry_date',
                  'notice_period',
                  'delivery_terms',
                  'manufacturing_site',
                  'batch_release_site',
                  'rolling_forecast',
                  'inventory_level',
                  'payment_terms',
                  'exclusive_suplies',
                  'exclusivity_period',
                  'agreement_type',
                  'agreement_number_eou',
                  'registration_strategy',
                  'variation_cost',
                  'additional_costs')
