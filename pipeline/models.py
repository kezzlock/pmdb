from django.db import models
from django.contrib.auth.models import User

# main object model


class Project(models.Model):
    # type choices
    LIN, RD, RD_ex = (0, 1, 2)
    PTYPE_CHOICES = (
        (LIN, 'L-in'),
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
    # status
    PREPMB, PIPELINE, PORTFOLIO = (0, 1, 2)
    STATUS_CHOICES = (
        (PREPMB, 'pre-PMB'),
        (PIPELINE, 'pipeline'),
        (PORTFOLIO, 'portfolio'),
    )
    # prescription category
    OTC, RX, MD, DS = (0, 1, 2, 3)
    PRESCRIPTION_CHOICES = (
        (OTC, 'OTC'),
        (RX, 'Rx'),
        (MD, 'MD'),
        (DS, 'DS'),
    )
    # DATABASE SPECYFIC RECORDS
    create_date = models.DateTimeField('date created', auto_now_add=True)
    created_by = models.ForeignKey(
        'auth.User', null=True, related_name='created_by')
    modify_date = models.DateTimeField(
        'date modified', null=True, auto_now=True)
    modified_by = models.ForeignKey(
        'auth.User', null=True, related_name='modified_by')

    project_name = models.CharField(
        max_length=300, null=False, blank=False)  # required
    # molecule #required
    # form # required
    strength = models.CharField(
        max_length=200, null=False, blank=False)  # required
    brand_name = models.CharField(max_length=200, null=True, blank=True)
    # market # required
    description = models.TextField(blank=True, null=True)
    project_type = models.IntegerField(
        choices=PTYPE_CHOICES, default=LIN)  # required
    contract_type = models.IntegerField(choices=CTYPE_CHOICES, default=LSA)
    manager = models.ForeignKey(to=User, blank=False, null=False,  # required
                                on_delete=models.SET_NULL,
                                related_name="manager")
    status = models.IntegerField(choices=STATUS_CHOICES, default=PIPELINE)
    prescription_category = models.IntegerField(choices=PRESCRIPTION_CHOICES,
                                                default=RX)  # required
