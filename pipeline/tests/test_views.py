from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone

from pipeline.forms import ProjectCreateForm
from pipeline.models import Project


class BasicTestCase(TestCase):
    @classmethod
    def setUp(self):
        # define test client
        self.client = Client()
        # set url
        self.url = "/"

    def help_get_or_create_user(self, username="TestUser"):
        if not username:
            user, created = User.objects.get_or_create(username="TestUser")
        else:
            user, created = User.objects.get_or_create(username=username)
        return user

    def help_get_or_create_project(self, name="TestObject1", strength="500mg",
                                   user=None):
        if not user:
            user = self.help_get_or_create_user()
        project, created = Project.objects.get_or_create(
            name=name, strength=strength, manager=user, created_by=user)
        if not project.create_date:
            project.create_date = timezone.now()
        return project


class ProjectListViewTestCase(BasicTestCase):
    def setUp(self):
        super().setUp()
        # create user
        self.user = self.help_get_or_create_user()
        # create project
        self.project = self.help_get_or_create_project()
        # set url
        self.url = reverse('project-list')

    def test_url(self):
        self.assertEqual(self.url, "/")

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "pipeline/project_list.html")

    def test_view_response(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.project.name)

    def test_view_pass_project_list_to_context(self):
        proj1 = self.help_get_or_create_project()
        proj2 = self.help_get_or_create_project(name="TestObject2")
        response = self.client.get(self.url)
        self.assertIn(proj1, response.context["object_list"])
        self.assertIn(proj2, response.context["object_list"])


class ProjectDetailViewTestCase(BasicTestCase):
    def setUp(self):
        super().setUp()
        # create user
        self.user = self.help_get_or_create_user()
        # create project
        self.project = self.help_get_or_create_project()
        # set url
        self.url = reverse('project-detail', args=[self.project.pk])

    def test_url(self):
        self.assertEqual(self.url, f"/{self.project.pk}/")

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "pipeline/project_details.html")

    def test_view_response(self):
        response = self.client.get(self.url)
        self.assertContains(response, self.project.name)

    def test_view_pass_project_object_to_context(self):
        response = self.client.get(self.url)
        self.assertEqual(self.project, response.context["object"])


class ProjectCreateViewTestCase(BasicTestCase):
    def setUp(self):
        super().setUp()
        self.user = None
        self.project = None
        self.url = reverse('project-create')

    def test_url(self):
        self.assertEqual(self.url, f"/create/")

    def test_template_used(self):
        response = self.client.get(self.url)
        self.assertTemplateUsed(response, "pipeline/project_create.html")

    def test_form_instance_in_context(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)
        self.assertIsInstance(response.context["form"], ProjectCreateForm)

    def test_model_class_in_form(self):
        response = self.client.get(self.url)
        form = response.context["form"]
        self.assertEqual(form._meta.model, Project)

# TODO: 1. test required fields,
# TODO: 2. test for success url and succes save
# TODO: 3. test form_valid method
