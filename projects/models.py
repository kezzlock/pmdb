from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from dropdowns.models import (Agreement, AtcClass, DeliveryTerm, FormNFC12,
                              Licensor, Market, Molecule, OtcAtc2Class,
                              PackType, PharmaForm, ProductCategory,
                              RegistrationStrategy, TherapeuticArea)

# ### main object model ###


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
    DRAFT, PREPMB, PIPELINE, PORTFOLIO, TERMINATED = (0, 1, 2, 3, 4)
    STATUS_CHOICES = (
        (DRAFT, 'draft'),
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
    pharmaceutical_form = models.ForeignKey(
        PharmaForm, on_delete=models.CASCADE)  # required
    form = models.ForeignKey(
        FormNFC12, blank=True, null=True, on_delete=models.CASCADE)  # NFC12
    product_category = models.ForeignKey( # required
        ProductCategory, blank=False, null=False, on_delete=models.CASCADE)
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
    status = models.IntegerField(choices=STATUS_CHOICES, default=DRAFT,
                                 null=True, blank=True)
    therapeutic_area = models.ForeignKey(TherapeuticArea, blank=True, null=True,
                                         on_delete=models.CASCADE)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=TBC,
                                   null=True, blank=True)
    atc3_class = models.ForeignKey(AtcClass, blank=True, null=True,
                                   on_delete=models.CASCADE)
    otc_atc2_class = models.ForeignKey(OtcAtc2Class, blank=True, null=True,
                                       on_delete=models.CASCADE)
    pack_size = models.TextField(blank=True)
    pack_type = models.ForeignKey(PackType, blank=True, null=True,
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
    pmb_approval = models.DateField(null=True, blank=True)
    agreement = models.DateField(null=True, blank=True)
    project_start = models.DateField(null=True, blank=True)
    prototype_approved = models.DateField(null=True, blank=True)
    registration_batches_ready = models.DateField(null=True, blank=True)
    dossier_availability = models.DateField(null=True, blank=True)
    dossier_submission = models.DateField(null=True, blank=True)
    ma_granted = models.DateField(null=True, blank=True)
    artwork_approval = models.DateField(null=True, blank=True)
    product_in_dsv = models.DateField(null=True, blank=True)
    launch_date = models.DateField(null=True, blank=True)
    status_comment = models.TextField(blank=True)
    # timelines current status
    pmb_approval_current = models.DateField(null=True, blank=True)
    agreement_current = models.DateField(null=True, blank=True)
    project_start_current = models.DateField(null=True, blank=True)
    prototype_approved_current = models.DateField(null=True, blank=True)
    registration_batches_ready_current = models.DateField(null=True,
                                                          blank=True)
    dossier_availability_current = models.DateField(null=True, blank=True)
    dossier_submission_current = models.DateField(null=True, blank=True)
    ma_granted_current = models.DateField(null=True, blank=True)
    artwork_approval_current = models.DateField(null=True, blank=True)
    product_in_dsv_current = models.DateField(null=True, blank=True)
    launch_date_current = models.DateField(null=True, blank=True)
    status_comment_current = models.TextField(blank=True)
    # risks
    risk_type = models.IntegerField(choices=RISK_CHOICES, default=1, null=True,
                                    blank=True)
    risk_comment = models.TextField(blank=True)
    # IP STATUS
    ip = models.DateField(null=True, blank=True)
    dex = models.DateField(null=True, blank=True)
    mex = models.DateField(null=True, blank=True)
    mfd = models.DateField(null=True, blank=True) # market formation date
    ip_comment = models.TextField(blank=True)
    # Licensing agreement summary
    licensor = models.ForeignKey(to=Licensor, blank=True, null=True,
                                 on_delete=models.CASCADE)
    maq = models.CharField(max_length=300, blank=True)
    supply_price = models.TextField(blank=True)
    floor_price = models.FloatField(null=True, blank=True, default=None)
    # TODO: pole wyboru dla waluty:
    floor_price_currency = models.CharField(max_length=300, blank=True)
    reconciliation = models.NullBooleanField(blank=True)
    reconciliation_comment = models.TextField(blank=True)
    lead_time_launch = models.TextField(blank=True)
    lead_time_commercial = models.TextField(blank=True)
    supply_period = models.FloatField(null=True, blank=True, default=None)
    automatic_prolongation = models.NullBooleanField(blank=True)
    prolongation_period = models.FloatField(
        null=True, blank=True, default=None)
    agreement_expiry = models.TextField(blank=True)
    agreement_expiry_date = models.DateField(null=True, blank=True)
    notice_period = models.FloatField(null=True, blank=True, default=None)
    delivery_terms = models.ForeignKey(
        DeliveryTerm, blank=True, null=True, on_delete=models.CASCADE)
    manufacturing_site = models.TextField(blank=True)
    batch_release_site = models.TextField(blank=True)
    rolling_forecast = models.TextField(blank=True)
    inventory_level = models.TextField(blank=True)
    payment_terms = models.FloatField(null=True, blank=True, default=None)
    exclusive_suplies = models.NullBooleanField(blank=True)
    exclusivity_period = models.FloatField(null=True, blank=True, default=None)
    agreement_type = models.ForeignKey(
        Agreement, blank=True, null=True, on_delete=models.CASCADE)
    agreement_number_eou = models.CharField(max_length=300, blank=True)
    registration_strategy = models.ForeignKey(
        RegistrationStrategy, blank=True, null=True, on_delete=models.CASCADE)
    variation_cost = models.TextField(blank=True)
    additional_costs = models.TextField(blank=True)

    def __str__(self):
        """Return model string representation."""
        return self.name

    def get_absolute_url(self):
        """Return abolute url for model."""
        return reverse('project-detail', args=[str(self.id)])

    def get_fields_dict(self, exclude_fields=None, sorted=False):
        """Return dictionary containing model fields.

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
    def get_detail_tabs(cls):
        """
        Method return dict with keys matching details tabs,
        and a list of fields as a value of key.
        """
        details_tabs = {}
        fields = set(f for f in cls._meta.get_fields())
        informations = ["name", "molecule", "pharmaceutical_form", "form",
                        "product_category", "strength","brand_name",
                        "market","description", "project_type", "manager",
                        "status", "therapeutic_area", "priority",
                        "atc3_class", "otc_atc2_class", "ip", "ip_comment",
                        "dex", "mex", "mfd", "licensor"]
        schedule = ["project_start", "pmb_approval", "agreement",
                    "prototype_approved", "registration_batches_ready",
                    "dossier_availability", "dossier_submission",
                    "ma_granted", "artwork_approval", "product_in_dsv",
                    "launch_date", "status_comment", "pmb_approval_current",
                    "agreement_current", "project_start_current",
                    "prototype_approved_current",
                    "registration_batches_ready_current",
                    "dossier_availability_current",
                    "dossier_submission_current","ma_granted_current",
                    "artwork_approval_current", "product_in_dsv_current",
                    "launch_date_current", "status_comment_current"]
        agreements = ["contract_type", "pack_size", "pack_type", "moq",
                      "maq", "sku", "cogs", "pmb_budget", "licence_costs",
                      "licence_comment", "regulatory_costs", "other_costs",
                      "total_costs", "fiveyear_income", "npv", "ebidta",
                      "ebitda_percent", "supply_price", "floor_price",
                      "floor_price_currency", "reconciliation",
                      "reconciliation_comment", "lead_time_launch",
                      "lead_time_commercial", "supply_period",
                      "automatic_prolongation", "prolongation_period",
                      "agreement_expiry", "agreement_expiry_date",
                      "notice_period", "delivery_terms",
                      "manufacturing_site", "batch_release_site",
                      "rolling_forecast", "inventory_level","payment_terms",
                      "exclusive_suplies", "exclusivity_period",
                      "agreement_type", "agreement_number_eou",
                      "registration_strategy", "variation_cost",
                      "additional_costs"]
        other = ["shelf_life", "risk_type", "risk_comment"]
        for field in fields:
            if field.name in informations:
                details_tabs.setdefault("informations", []).append(field)
            elif field.name in schedule:
                details_tabs.setdefault("schedule", []).append(field)
            elif field.name in agreements:
                details_tabs.setdefault("agreements", []).append(field)
            elif field.name in other:
                details_tabs.setdefault("other", []).append(field)
        return details_tabs




    # CLASSMETHODS
    @classmethod
    def get_fields(cls, exclude=None, sort=False):
        """Return sorted list of fields.

        Return dictionary with fields names:
            {field.name:field.verbose_name, ...}

        Attrs:
        """
        if not exclude:
            exclude = []
        # get list of fields with excluded relation fields
        fields = set(f for f in cls._meta.get_fields()
                     if f.name not in exclude)
        if sort:
            return sorted(list(fields), key=lambda x: x.name)
        return fields

    @classmethod
    def get_integer_choices_fields(cls):
        """Return model integer fields."""
        fields = set(f for f in cls._meta.get_fields() if (
            f.get_internal_type() == 'IntegerField'))
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
