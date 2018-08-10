from django.urls import path

from .views import (MoleculeCreateView, MoleculeDeleteView, MoleculeDetailView,
                    MoleculeListView, MoleculeUpdateView, PharmaFormCreateView,
                    PharmaFormDeleteView, PharmaFormDetailView,
                    PharmaFormListView, PharmaFormUpdateView,
                    TherapeuticAreaCreateView, TherapeuticAreaDeleteView,
                    TherapeuticAreaDetailView, TherapeuticAreaListView,
                    TherapeuticAreaUpdateView)

urlpatterns = [
    # molecule
    path('molecule/', MoleculeListView.as_view(), name='molecule-list'),
    path('molecule/<int:pk>/', MoleculeDetailView.as_view(),
         name='molecule-detail'),
    path('molecule/create/', MoleculeCreateView.as_view(),
         name='molecule-create'),
    path('molecule/<int:pk>/update/', MoleculeUpdateView.as_view(),
         name='molecule-update'),
    path('molecule/<int:pk>/delete/', MoleculeDeleteView.as_view(),
         name='molecule-delete'),
    # pharmaform
    path('pharmaform/', PharmaFormListView.as_view(), name='pharmaform-list'),
    path('pharmaform/<int:pk>/', PharmaFormDetailView.as_view(),
         name='pharmaform-detail'),
    path('pharmaform/create/', PharmaFormCreateView.as_view(),
         name='pharmaform-create'),
    path('pharmaform/<int:pk>/update/', PharmaFormUpdateView.as_view(),
         name='pharmaform-update'),
    path('pharmaform/<int:pk>/delete/', PharmaFormDeleteView.as_view(),
         name='pharmaform-delete'),
    # TherapeuticArea
    path('therapeuticarea/', TherapeuticAreaListView.as_view(), name='therapeuticarea-list'),
    path('therapeuticarea/<int:pk>/', TherapeuticAreaDetailView.as_view(),
         name='therapeuticarea-detail'),
    path('therapeuticarea/create/', TherapeuticAreaCreateView.as_view(),
         name='therapeuticarea-create'),
    path('therapeuticarea/<int:pk>/update/', TherapeuticAreaUpdateView.as_view(),
         name='therapeuticarea-update'),
    path('therapeuticarea/<int:pk>/delete/', TherapeuticAreaDeleteView.as_view(),
         name='therapeuticarea-delete'),
]
