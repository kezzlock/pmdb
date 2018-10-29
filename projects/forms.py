from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.urls import reverse_lazy

from .models import Project


class ProjectCreateForm(forms.ModelForm):
    """Form class for Project.

    Class to create a Form class from a Django model.
    """

    class Meta:
        model = Project
        # fields = '__all__'
        # exclude = ['created_by', 'create_date', 'modified_by', 'modify_date']
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
        super(ProjectCreateFormJson, self).__init__(*args, **kwargs)
        helper = FormHelper(self)
        helper.form_class = 'manipulate-form'
        helper.form_action = reverse_lazy('project_create_json')
        helper.layout.append(
            Submit('save_changes', 'Save changes',
                   css_class="btn btn-block manipulate-form__submit-btn",  onclick="showmms();"))
        # helper.disable_csrf = True
        self.helper = helper

    class Meta:
        model = Project
        fields = ('name', )
        # fields = ('name', 'brand_name', 'molecule', 'description',
        #           'product_category',
        #           'strength',
        #           'market',
        #           'manager',
        #           'project_type',
        #           'pharmaceutical_form',
        #           'form',
        #           'status',
        #           'prescription_category',
        #           'therapeutic_area',
        #           'priority',
        #           'atc3_class',
        #           'otc_atc2_class')
