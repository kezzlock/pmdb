from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Submit
from django import forms
from django.urls import reverse_lazy

from .models import Project


class ProjectCreateForm(forms.ModelForm):
    """Form class for Project.

    Class to create a Form class from a Django model.
    """

    class Meta:
        """Define form Project and fields."""

        model = Project
        fields = ('name', 'brand_name', 'molecule', 'description',
                  'product_category',
                  'strength',
                  'market',
                  'manager',
                  'project_type',
                  'pharmaceutical_form',
                  'form',
                  'status',
                  'prescription_category',
                  'therapeutic_area',
                  'priority',
                  'atc3_class',
                  'otc_atc2_class')


class ProjectCreateFormJson(forms.ModelForm):
    """Form class for Project.

    Class to create a Form class from a Django model.
    """

    def __init__(self, *args, **kwargs):
        """Add Crispy helper to init."""
        super(ProjectCreateFormJson, self).__init__(*args, **kwargs)
        helper = FormHelper(self)
        helper.form_class = 'manipulate-form'
        helper.form_id = 'create_form'
        helper.form_action = reverse_lazy('project_create_json')
        helper.layout.append(
            Div(Div(
                Submit('create_project', 'Create project',
                       css_class="btn btn-block manipulate-form__submit-btn"),
                css_class='col-6 offset-6'),
                css_class='row')
        )
        self.helper = helper

    class Meta:
        """Define form Project and fields."""

        model = Project
        fields = ('name', 'brand_name', 'molecule', 'description',
                  'product_category',
                  'strength',
                  'market',
                  'manager',
                  'project_type',
                  'pharmaceutical_form',
                  'form',
                  'status',
                  'prescription_category',
                  'therapeutic_area',
                  'priority',
                  'atc3_class',
                  'otc_atc2_class')
