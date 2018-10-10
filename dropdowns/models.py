import pycountry
from django.db import models


class Agreement(models.Model):
    """Django data model Agreement"""

    name = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Agreement'
        verbose_name_plural = 'Agreements'

    def __str__(self):
        return str(self.id)


class AtcClass(models.Model):
    """Django data model AtcClass"""

    code = models.CharField(max_length=6, null=False, blank=False)
    type = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'ATC-3 Class'
        verbose_name_plural = 'ATC-3 Classes'

    def __str__(self):
        return str(f"{self.code} {self.type}")


class DeliveryTerm(models.Model):
    """Django data model DeliveryTerms"""

    name = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Delivery Terms'
        verbose_name_plural = 'Delivery Terms'

    def __str__(self):
        return str(self.id)


class FormNFC12(models.Model):
    """Django data model Form NFC12"""

    name = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Form NFC12'
        verbose_name_plural = 'Forms NFC12'

    def __str__(self):
        return str(self.name)


class Licensor(models.Model):
    """Django data model Licensors"""

    name = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Licensor'
        verbose_name_plural = 'Licensors'

    def __str__(self):
        return str(self.name)


class Market(models.Model):
    """Django data model Market"""

    name = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Market'
        verbose_name_plural = 'Markets'

    def __str__(self):
        return str(self.name)

    # use https://pypi.org/project/pycountry/ for auto code generation
    @property
    def code(self):
        try:
            country = pycountry.countries.get(name=self.name)
            return country.alpha2
        except Exception:
            country = ''
        return country


class Molecule(models.Model):
    """Database model for API molecule."""

    name = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Molecule'
        verbose_name_plural = 'Molecules'

    def __str__(self):
        return self.name


class OtcAtc2Class(models.Model):
    """Django data model OtcAtc2Class"""

    code = models.CharField(max_length=6, null=False, blank=False)
    type = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'OTC ATC-2 Class'
        verbose_name_plural = 'OTC ATC-2 Classes'

    def __str__(self):
        return str(f"{self.code} {self.type}")


class PackType(models.Model):
    """Django data model PackType"""

    type = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Pack type'
        verbose_name_plural = 'Pack types'

    def __str__(self):
        return self.type


class PharmaForm(models.Model):
    """Pharmaceutical form of Molecule."""

    type = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Pharmaceutical form'
        verbose_name_plural = 'Pharmaceutical forms'

    def __str__(self):
        return self.type


class ProductCategory(models.Model):
    """Django data model ProductCategory"""

    type = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categorys'

    def __str__(self):
        return str(self.id)


class RegistrationStrategy(models.Model):
    """Django data model RegistrationStrategy"""

    name = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'RegistrationStrategy'
        verbose_name_plural = 'RegistrationStrategys'

    def __str__(self):
        return str(self.id)


class TherapeuticArea(models.Model):
    """List of all Therapeutic Areas."""

    type = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Therapeutic area'
        verbose_name_plural = 'Therapeutic areas'

    def __str__(self):
        return self.type
