from django.urls import path

from .views import (MoleculeCreateView, MoleculeDeleteView, MoleculeDetailView,
                    MoleculeListView)

urlpatterns = [
    # molecule
    path('molecule/', MoleculeListView.as_view(), name='molecule-list'),
    path('molecule/<int:pk>/', MoleculeDetailView.as_view(),
         name='molecule-detail'),
    path('molecule/create/', MoleculeCreateView.as_view(),
         name='molecule-create'),
    path('molecule/<int:pk>/delete/', MoleculeDeleteView.as_view(),
         name='molecule-delete'),
]
