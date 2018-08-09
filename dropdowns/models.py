import pycountry
from django.db import models


class Molecule(models.Model):
    """Database model for API molecule."""

    name = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Molecule'
        verbose_name_plural = 'Molecules'

    def __str__(self):
        return self.name


class PharmaForm(models.Model):
    """Pharmaceutical form of Molecule."""

    type = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Pharmaceutical form'
        verbose_name_plural = 'Pharmaceutical forms'

    def __str__(self):
        return self.type


class TherapeuticArea(models.Model):
    """List of all Therapeutic Areas."""

    type = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Therapeutic area'
        verbose_name_plural = 'Therapeutic areas'

    def __str__(self):
        return self.type


class PackType(models.Model):
    """Django data model PackType"""

    type = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'Pack type'
        verbose_name_plural = 'Pack types'

    def __str__(self):
        return self.type


class AtcClass(models.Model):
    """Django data model AtcClass"""

    code = models.CharField(max_length=6, null=False, blank=False)
    type = models.CharField(max_length=300, null=False, blank=False)

    class Meta:
        verbose_name = 'ATC-3 Class'
        verbose_name_plural = 'ATC-3 Classes'

    def __str__(self):
        return str(f"{self.code} {self.type}")


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
