import json
import re

from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from pipeline.forms import ProjectCreateForm
from pipeline.models import Project


class ProjectListView(ListView):
    model = Project
    template_name = 'pipeline/project_list.html'
    # columns = ['id', 'name', 'molecule', 'form', 'strength', 'brand_name',
    #            'market', 'moq']

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Prepare list to create JSON
    #     columns_json = []
    #     for column in self.columns:
    #         temp = {}
    #         temp['data'] = column
    #         temp['title'] = ' '.join(word.title() for word in filter(
    #             None, re.split("[, \-!?:_]+", column)))
    #         columns_json.append(temp)
    #     json_dumps = json.dumps(columns_json)
    #     print(json_dumps.replace('{\"', '{').replace('\":', ':').replace('"t', 't').replace('"','\''))
    #     context['columns_json'] = json_dumps.replace('\"', '')
    #     return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'pipeline/project_details.html'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'pipeline/project_create.html'
    success_url = reverse_lazy('project-list')


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'pipeline/project_update.html'
    success_url = reverse_lazy('project-list')


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')
