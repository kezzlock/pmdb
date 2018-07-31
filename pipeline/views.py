from django.views.generic import DetailView
from django.shortcuts import render

from pipeline.models import Project



class ProjectDetailView(DetailView):
    model = Project
    template_name = 'pipeline/project_details.html'
