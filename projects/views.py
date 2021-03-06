from crispy_forms.utils import render_crispy_form
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from projects.forms import ProjectCreateForm, ProjectCreateFormJson
from projects.models import Project
from projects.serializers import ProjectSerializer


class ProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
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

    def get_context_data(self, **kwargs):
        details_dict = Project.get_detail_tabs()
        context = super().get_context_data(**kwargs)
        # add model fields to context
        exclude_fields = ["modified_by", "modify_date", "id", "name"]
        context['fields'] = Project.get_fields(
            sort=True, exclude=exclude_fields)
        context['informations'] = details_dict['informations']
        context['agreements'] = details_dict['agreements']
        context['schedule'] = details_dict['schedule']
        context['other'] = details_dict['other']
        # add serializer to context
        form = ProjectCreateFormJson
        context['form'] = form
        columns = ['id', 'name', 'molecule', 'manager', 'pharmaceutical_form',
                   'product_category', 'strength', 'market', 'moq']
        context['columns'] = columns[1:]
        return context


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'projects/project_details.html'


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateFormJson
    template_name = 'projects/project_create.html'
    success_url = reverse_lazy('project-list')


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = 'projects/project_update.html'
    success_url = reverse_lazy('project-list')


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')
