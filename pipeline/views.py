from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.urls import reverse_lazy

from pipeline.models import Project
from pipeline.forms import ProjectCreateForm


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
