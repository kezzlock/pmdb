from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, DetailView, ListView


class MoleculeListView(ListView):
    model = Molecule
    template_name = 'pipeline/molecule_list.html'


class MoleculeDetailView(DetailView):
    model = Molecule
    template_name = 'pipeline/molecule_details.html'


class MoleculeCreateView(CreateView):
    model = Molecule
    form_class = MoleculeCreateForm
    template_name = 'pipeline/molecule_create.html'
    success_url = reverse_lazy('molecule-list')


class MoleculeDeleteView(DeleteView):
    model = Molecule
    success_url = reverse_lazy('molecule-list')
