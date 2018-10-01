from django import forms

from .models import Project


class ProjectCreateForm(forms.ModelForm):
    """Form class for Project.

    Class to create a Form class from a Django model.
    """

    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['created_by', 'create_date', 'modified_by', 'modify_date']
