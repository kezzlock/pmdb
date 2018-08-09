from django import forms

from .models import Molecule


class MoleculeCreateForm(forms.ModelForm):
    """Form class for Molecule.

    Class to create a Form class from a Django model.
    """

    class Meta:
        model = Molecule
        fields = '__all__'


# class ProjectCreateForm(forms.ModelForm):
#     """Form class for Project.
#
#     Class to create a Form class from a Django model.
#     """
#
#     class Meta:
#         model = Project
#         fields = '__all__'
