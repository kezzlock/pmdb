from rest_framework import serializers

from projects.models import Project


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
    created_by = serializers.StringRelatedField()
    modified_by = serializers.StringRelatedField()
    molecule = serializers.StringRelatedField()
    form = serializers.StringRelatedField()
    market = serializers.StringRelatedField()
    manager = serializers.StringRelatedField()
    therapeutic_area = serializers.StringRelatedField()
    atc_class = serializers.StringRelatedField()
    pact_type = serializers.StringRelatedField()
    licensor = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = '__all__'
