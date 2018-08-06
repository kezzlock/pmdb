from django.contrib.auth.models import User
from django.db import models
from django.test import TestCase
from django.utils import timezone

from pipeline.models import Project


class RobjectModelTestCase(TestCase):
    """Test for Project model.

    Help method (with 'help_' prefix) are not part of test. They allow to
    simplify tests and to reduce amount of code.

    Null: It is database-related. Defines if a given database column
        will accept null values or not.
    Blank: It is validation-related. It will be used during forms validation,
        when calling form.is_valid().

    Now, where most developers get it wrong:Defining null=True for string-based
    fields such as CharField and TextField. Avoid doing that. Otherwise, you
    will end up having two possible values for “no data”, that is: None and an
    empty string. Having two possible values for “no data” is redundant.
    The Django convention is to use the empty string, not NULL.
    """

    def help_create_object(self, name="Test object", strength="500mg",
                           username=None):
        """Create an instance of Project model.

        Since User is required by default TestUser is created as well.
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

    def help_check_field_type(self, field_name, field_type):
        """Check if database field has correct type."""
        checked_field = Project._meta.get_field(field_name)
        self.assertIsInstance(checked_field, field_type)

    def help_check_field_is_required(self, field_name):
        """Check if field value is required.

        Note from django:
        As currently implemented, setting auto_now or auto_now_add to True
        will cause the field to have editable=False and blank=True set.
        """
        checked_field = Project._meta.get_field(field_name)
        if isinstance(checked_field, models.DateTimeField) and \
                (checked_field.auto_now or checked_field.auto_now_add):
            self.assertFalse(checked_field.null)
        else:
            self.assertFalse(checked_field.null)
            self.assertFalse(checked_field.blank)

    def test_object_creation(self):
        proj1 = self.help_create_object()
        self.assertTrue(isinstance(proj1, Project))
        self.assertEqual(proj1.name, "Test object")

    def test_fields_classes(self):
        self.help_check_field_type("name", models.CharField)
        self.help_check_field_type("create_date", models.DateTimeField)
        self.help_check_field_type("modify_date", models.DateTimeField)
        self.help_check_field_type("created_by", models.ForeignKey)
        self.help_check_field_type("modified_by", models.ForeignKey)
        self.help_check_field_type("strength", models.CharField)
        self.help_check_field_type("brand_name", models.CharField)
        self.help_check_field_type("description", models.TextField)
        self.help_check_field_type("project_type", models.IntegerField)
        self.help_check_field_type("contract_type", models.IntegerField)
        self.help_check_field_type("manager", models.ForeignKey)
        self.help_check_field_type("status", models.IntegerField)
        self.help_check_field_type(
            "prescription_category", models.IntegerField)
        self.help_check_field_type("pack_size", models.CharField)
        self.help_check_field_type("shelf_life", models.IntegerField)

    def test_string_fields_are_not_null(self):
        """Django string fields shouldn't be null.

        Strings in django by default should be empty string '' even if field
        is required, so null is unallowable.

        If field is required set blank=False.
        """
        # get list of string fields
        string_fields = [f for f in Project._meta.get_fields() if isinstance(
            f, (models.CharField, models.TextField))]

        for string_field in string_fields:
            # if string_field.null:
            #     print(f"\nfield not null: {string_field}")
            self.assertFalse(string_field.null)

    def test_required_fields_are_not_null_or_blank(self):
        self.help_check_field_is_required("create_date")
        self.help_check_field_is_required("created_by")
        self.help_check_field_is_required("name")
        self.help_check_field_is_required("strength")
        self.help_check_field_is_required("project_type")
        self.help_check_field_is_required("manager")
        self.help_check_field_is_required("prescription_category")

    def test_str_method(self):
        proj1 = self.help_create_object()
        self.assertEqual(proj1.__str__(), proj1.name)

    def test_get_absolute_url(self):
        proj1 = self.help_create_object()
        self.assertEqual(f"/{proj1.id}/", proj1.get_absolute_url())

# TODO:
# 1. Test choices.
# 2. Test default values for options fields.
# 3. Test char lengths.
