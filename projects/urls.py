"""projects URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.urls import path

from .api import (ProjectCreateJson, ProjectDetailJson, ProjectListJson,
                  ProjectUpdateJson)
from .views import (ProjectCreateView, ProjectDeleteView, ProjectDetailView,
                    ProjectListView, ProjectUpdateView)

urlpatterns = [
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(),
         name='project-update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(),
         name='project-delete'),
    # API
    path('api/project/datatable/', ProjectListJson.as_view(),
         name='project_list_json'),
    path('api/project/<int:pk>/', ProjectDetailJson.as_view(),
         name="project_detail_json"),
    path('api/project/create/', ProjectCreateJson.as_view(),
         name="project_create_json"),
    path('api/project/<int:pk>/update/', ProjectUpdateJson.as_view(),
         name="project_update_json"),

]
