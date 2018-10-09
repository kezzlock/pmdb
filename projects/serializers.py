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


class ProjectSerializer(serializers.ModelSerializer):
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
    modified_by = serializers.SerializerMethodField('get_modified_by_full_name')
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
