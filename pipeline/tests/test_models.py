from django.contrib.auth.models import User
from django.db import models
from django.test import TestCase
from django.utils import timezone

from pipeline.models import Project


class RobjectModelTestCase(TestCase):
    """Test for Project model."""

    def create_object(self, name="Test object", strength="500mg", username=None):
        """Method for fast object creation.

        Since User is required by default TestUser is created.
        """
        if not username:
            user, created = User.objects.get_or_create(username="TestUser")
        else:
            user, created = User.objects.get_or_create(username=username)
        project, created = Project.objects.get_or_create(
            name=name, strength=strength, manager=user, created_by=user)
        if not project.create_date:
            project.create_date = timezone.now()
        return project

    def test_object_creation(self):
        proj1 = self.create_object()
        self.assertTrue(isinstance(proj1, Project))
        self.assertEqual(proj1.__str__(), proj1.name)

    def test_fields_classes(self):
        name_field = Project._meta.get_field("name")
        self.assertIsInstance(name_field, models.CharField)
