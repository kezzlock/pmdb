from os import path

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from dropdowns.models import (AtcClass, Licensor, Market, Molecule, PackType,
                              PharmaForm, TherapeuticArea)

### main object model ###


class Project(models.Model):
    """Database model for project.

    Main aplication object.
    """
    # contract type
    LSA, LATT, DA = (0, 1, 2)
    CTYPE_CHOICES = (
        (LSA, 'LSA'),
        (LATT, 'LA+TT'),
        (DA, 'DA'),
    )
    # prescription category
    OTC, RX, MD, DS = (0, 1, 2, 3)
    PRESCRIPTION_CHOICES = (
        (OTC, 'OTC'),
        (RX, 'Rx'),
        (MD, 'MD'),
        (DS, 'DS'),
    )
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
    # Project type choices
    LIN, RD, RD_ex = (0, 1, 2)
    PTYPE_CHOICES = (
        (LIN, 'License-in'),
        (RD, 'R&D'),
        (RD_ex, 'R&D external'),
    )
    # Risk
    UNACCEPTABLE, LOW, MEDIUM, HIGH = (0, 1, 2, 3)
    RISK_CHOICES = (
        (UNACCEPTABLE, 'Unacceptable'),
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )
    # status choices
    TERMINATED, PREPMB, PIPELINE, PORTFOLIO = (0, 1, 2, 3)
    STATUS_CHOICES = (
        (PREPMB, 'pre-PMB'),
        (PIPELINE, 'pipeline'),
        (PORTFOLIO, 'portfolio'),
        (TERMINATED, 'terminated'),
    )
    # shell life
    SHELL_CHOICES = [(i, i) for i in range(49)]

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
    market = models.ForeignKey(to=Market, blank=False, null=False,  # required
                               on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    project_type = models.IntegerField(
        choices=PTYPE_CHOICES, default=LIN)  # required
    manager = models.ForeignKey(to=User, blank=False, null=False,  # required
                                on_delete=models.CASCADE,
                                related_name="manager")
    contract_type = models.IntegerField(choices=CTYPE_CHOICES, default=LSA)
    status = models.IntegerField(choices=STATUS_CHOICES, default=PIPELINE,
                                 null=True, blank=True)
    prescription_category = models.IntegerField(choices=PRESCRIPTION_CHOICES,
                                                default=RX, null=False,
                                                blank=False)  # required
    therapeutic_area = models.ForeignKey(TherapeuticArea, blank=True, null=True,
                                         on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=TBC,
                                   null=True, blank=True)
    atc_class = models.ForeignKey(AtcClass, blank=True, null=True,
                                  on_delete=models.CASCADE)
    pack_size = models.TextField(blank=True)

    pact_type = models.ForeignKey(PackType, blank=True, null=True,
                                  on_delete=models.CASCADE)
    shelf_life = models.IntegerField(choices=SHELL_CHOICES, default=0,
                                     null=True, blank=True)
    # finanse
    moq = models.CharField(max_length=200, blank=True)
    sku = models.TextField(blank=True)
    cogs = models.TextField(blank=True)
    pmb_budget = models.FloatField(null=True, blank=True, default=None)
    licence_costs = models.FloatField(null=True, blank=True, default=None)
    licence_comment = models.TextField(blank=True)
    regulatory_costs = models.FloatField(null=True, blank=True, default=None)
    other_costs = models.FloatField(null=True, blank=True, default=None)
    total_costs = models.FloatField(null=True, blank=True, default=None)
    fiveyear_income = models.FloatField(null=True, blank=True, default=None)
    npv = models.FloatField(null=True, blank=True, default=None)
    ebidta = models.FloatField(null=True, blank=True, default=None)
    ebitda_percent = models.DecimalField(null=True, blank=True, max_digits=5,
                                         decimal_places=2)
    # timelines plan

    # risks
    risk_type = models.IntegerField(choices=RISK_CHOICES, default=1, null=True,
                                    blank=True)
    risk_comment = models.TextField(blank=True)
    # IP STATUS
    ip = models.DateField(null=True, blank=True)
    dex = models.DateField(null=True, blank=True)
    mex = models.DateField(null=True, blank=True)
    mfd = models.DateField(null=True, blank=True)
    ip_comment = models.TextField(blank=True)
    # Licensing agreement summary
    licensor = models.ForeignKey(to=Licensor, blank=True, null=True,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project-detail', args=[str(self.id)])

    def get_fields_dict(self, exclude_fields=None, sorted=False):
        """
        Return dictionary with object fields:
            {field.verbose_name: field value, ...}

        Attrs:

        Waring: Relation fields are excluded
        """
        if not exclude_fields:
            exclude_fields = []
        fields_dict = {}
        # get list of fields with excluded relation fields
        fields = set(f for f in self._meta.get_fields()
                     if not (f.is_relation or f.one_to_one or
                             (f.many_to_one and f.related_model)))
        for field in fields:
            if field.name not in exclude_fields:
                if hasattr(self, f"get_{field.name}_display"):
                    fields_dict[field.name] = getattr(
                        self, f"get_{field.name}_display")
                else:
                    fields_dict[field.name] = getattr(self, field.name)
        if sorted:
            return sorted(fields_dict.items())
        return fields_dict.items()

    @classmethod
    def get_fields(cls, exclude_fields=None, sort=False):
        """
        Return dictionary with fields names:
            {field.name:field.verbose_name, ...}

        Attrs:
        """
        if not exclude_fields:
            exclude_fields = []
        # get list of fields with excluded relation fields
        fields = set(f for f in cls._meta.get_fields())
        if sort:
            return sorted(list(fields), key=lambda x: x.name)
        return fields

    @classmethod
    def get_integer_choices_fields(cls):
        # "---------"
        fields = set(f for f in cls._meta.get_fields() if (f.get_internal_type() == 'IntegerField'))
        return fields
### FILES OBJECTS ###


# class FileGroup(models.Model):
#     # required
#     name = models.CharField(
#         max_length=300, null=False, blank=False, unique=True)
#     description = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# class File(models.Model):
#     file = models.FileField(upload_to='uploads/')
#
#     def default_group():
#         # get or create default group
#         return FileGroup.objects.get_or_create(name="General")[0]
#
#     group = models.ForeignKey(
#         'FileGroup', null=False, blank=False, related_name='created_by',
#         on_delete=models.CASCADE, default=default_group)
#     project = models.ForeignKey(
#         'Project', null=False, blank=False, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.file.name
#
#     def filename(self):
#         return path.basename(self.file.name)
