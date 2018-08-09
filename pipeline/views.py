from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView

from pipeline.forms import ProjectCreateForm
from pipeline.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'pipeline/project_list.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'pipeline/project_details.html'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'pipeline/project_create.html'
    success_url = reverse_lazy('project-list')


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')
