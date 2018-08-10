from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from dropdowns.models import (AtcClass, Molecule, PackType, PharmaForm,
                              TherapeuticArea)

# main object model


class Project(models.Model):
    """Database model for project.

    Main aplication object.
    """
    # Project type choices
    LIN, RD, RD_ex = (0, 1, 2)
    PTYPE_CHOICES = (
        (LIN, 'License-in'),
        (RD, 'R&D'),
        (RD_ex, 'R&D external'),
    )
    # contract type
    LSA, LATT, DA = (0, 1, 2)
    CTYPE_CHOICES = (
        (LSA, 'LSA'),
        (LATT, 'LA+TT'),
        (DA, 'DA'),
    )
    # status choices
    TERMINATED, PREPMB, PIPELINE, PORTFOLIO = (0, 1, 2, 3)
    STATUS_CHOICES = (
        (PREPMB, 'pre-PMB'),
        (PIPELINE, 'pipeline'),
        (PORTFOLIO, 'portfolio'),
        (TERMINATED, 'terminated'),
    )
    # prescription category
    OTC, RX, MD, DS = (0, 1, 2, 3)
    PRESCRIPTION_CHOICES = (
        (OTC, 'OTC'),
        (RX, 'Rx'),
        (MD, 'MD'),
        (DS, 'DS'),
    )
    # shell life
    SHELL_CHOICES = [(i, i) for i in range(49)]
    # priority choices
    TBC = 0
    LOW = 1
    NORMAL = 2
    HIGH = 3
    PRIORITY_CHOICES = (
        (TBC, 'tbc'),
        (LOW, 'Low'),
        (NORMAL, 'Normal'),
        (HIGH, 'High'),
    )

    # DATABASE SPECYFIC RECORDS
    create_date = models.DateTimeField('date_created', auto_now_add=True)
    created_by = models.ForeignKey(
        'auth.User', null=False, blank=False, related_name='created_by',
        on_delete=models.CASCADE)
    modify_date = models.DateTimeField(
        'date modified', null=True, auto_now=True)
    modified_by = models.ForeignKey(
        'auth.User', null=True, related_name='modified_by',
        on_delete=models.CASCADE)
    name = models.CharField(
        max_length=300, null=False, blank=False)  # required
    molecule = models.ForeignKey(
        Molecule, on_delete=models.CASCADE)  # required
    form = models.ForeignKey(PharmaForm, on_delete=models.CASCADE)  # required
    strength = models.CharField(
        max_length=200, null=False, blank=False)  # required
    brand_name = models.CharField(max_length=200, blank=True)
    # market  # required for subproject
    description = models.TextField(blank=True)
    project_type = models.IntegerField(
        choices=PTYPE_CHOICES, default=LIN)  # required
    contract_type = models.IntegerField(choices=CTYPE_CHOICES, default=LSA)
    manager = models.ForeignKey(to=User, blank=False, null=False,  # required
                                on_delete=models.CASCADE,
                                related_name="manager")
    status = models.IntegerField(choices=STATUS_CHOICES, default=PIPELINE,
                                 null=True, blank=True)
    prescription_category = models.IntegerField(choices=PRESCRIPTION_CHOICES,
                                                default=RX, null=False,
                                                blank=False)  # required
    atc_class = models.ForeignKey(AtcClass, blank=True, null=True,
                                  on_delete=models.CASCADE)
    pack_size = models.TextField(blank=True)
    pact_type = models.ForeignKey(PackType, blank=True, null=True,
                                  on_delete=models.CASCADE)
    shelf_life = models.IntegerField(choices=SHELL_CHOICES, default=0,
                                     null=True, blank=True)
    therapeutic_area = models.ForeignKey(TherapeuticArea, blank=True, null=True,
                                         on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=TBC,
                                   null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])
