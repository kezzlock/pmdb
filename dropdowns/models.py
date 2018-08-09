from django.db import models

import pycountry


class Molecule(models.Model):
    """Database model for API molecule."""

    name = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.name


class PharmaForm(models.Model):
    """Pharmaceutical form of Molecule."""

    type = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.type


class TherapeuticArea(models.Model):
    """List of all Therapeutic Areas."""

    type = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.type


class PackType(models.Model):
    """Django data model PackType"""

    type = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return self.type


class AtcClass(models.Model):
    """Django data model AtcClass"""

    code = models.CharField(max_length=6, null=False, blank=False)
    type = models.CharField(max_length=300, null=False, blank=False)

    def __str__(self):
        return str(f"{self.code} {self.type}")


class Market(models.Model):
    """Django data model Market"""

    name = models.CharField(max_length=300, null=False, blank=False)

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
