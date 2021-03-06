from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import (AtcClass, Licensor, Market, Molecule, PackType,
                     PharmaForm, TherapeuticArea)

# Universal Generic View for dropdowns


class UniversalListView(ListView):
    template_name = 'dropdowns/universal_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add a model data for context
        context['model'] = self.model
        return context


class UniversalDetailView(DetailView):
    template_name = 'dropdowns/universal_details.html'


class UniversalCreateView(CreateView):
    fields = '__all__'
    template_name = 'dropdowns/universal_create.html'

    def __init__(self):
        self.success_url = reverse_lazy(
            f"{self.model._meta.verbose_name.lower().replace(' ','')}-list")


class UniversalUpdateView(UpdateView):
    fields = '__all__'
    template_name = 'dropdowns/universal_update.html'

    def __init__(self):
        self.success_url = reverse_lazy(
            f"{self.model._meta.verbose_name.lower().replace(' ','')}-list")


class UniversalDeleteView(DeleteView):
    template_name = 'dropdowns/universal_confirm_delete.html'

    def __init__(self):
        self.success_url = reverse_lazy(
            f"{self.model._meta.verbose_name.lower().replace(' ','')}-list")


# AtcClass

class AtcClassListView(UniversalListView):
    model = AtcClass


class AtcClassDetailView(UniversalDetailView):
    model = AtcClass


class AtcClassCreateView(UniversalCreateView):
    model = AtcClass


class AtcClassUpdateView(UniversalUpdateView):
    model = AtcClass


class AtcClassDeleteView(UniversalDeleteView):
    model = AtcClass


# Licensors

class LicensorListView(UniversalListView):
    model = Licensor


class LicensorDetailView(UniversalDetailView):
    model = Licensor


class LicensorCreateView(UniversalCreateView):
    model = Licensor


class LicensorUpdateView(UniversalUpdateView):
    model = Licensor


class LicensorDeleteView(UniversalDeleteView):
    model = Licensor

# Markets


class MarketListView(UniversalListView):
    model = Market


class MarketDetailView(UniversalDetailView):
    model = Market


class MarketCreateView(UniversalCreateView):
    model = Market


class MarketUpdateView(UniversalUpdateView):
    model = Market


class MarketDeleteView(UniversalDeleteView):
    model = Market

# Molecule


class MoleculeListView(UniversalListView):
    model = Molecule


class MoleculeDetailView(UniversalDetailView):
    model = Molecule


class MoleculeCreateView(UniversalCreateView):
    model = Molecule


class MoleculeUpdateView(UniversalUpdateView):
    model = Molecule


class MoleculeDeleteView(UniversalDeleteView):
    model = Molecule

# pack type


class PackTypeListView(UniversalListView):
    model = PackType


class PackTypeDetailView(UniversalDetailView):
    model = PackType


class PackTypeCreateView(UniversalCreateView):
    model = PackType


class PackTypeUpdateView(UniversalUpdateView):
    model = PackType


class PackTypeDeleteView(UniversalDeleteView):
    model = PackType

# PharmaForm


class PharmaFormListView(UniversalListView):
    model = PharmaForm


class PharmaFormDetailView(UniversalDetailView):
    model = PharmaForm


class PharmaFormCreateView(UniversalCreateView):
    model = PharmaForm


class PharmaFormUpdateView(UniversalUpdateView):
    model = PharmaForm


class PharmaFormDeleteView(UniversalDeleteView):
    model = PharmaForm

# therapeutic area


class TherapeuticAreaListView(UniversalListView):
    model = TherapeuticArea


class TherapeuticAreaDetailView(UniversalDetailView):
    model = TherapeuticArea


class TherapeuticAreaCreateView(UniversalCreateView):
    model = TherapeuticArea


class TherapeuticAreaUpdateView(UniversalUpdateView):
    model = TherapeuticArea


class TherapeuticAreaDeleteView(UniversalDeleteView):
    model = TherapeuticArea
