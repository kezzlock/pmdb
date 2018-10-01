from django.urls import reverse

from .base import FunctionalTest


class ProjectListTestCase(FunctionalTest):
    def setUp(self):
        super().setUp()
        # set url
        self.url = self.live_server_url + reverse("project-list")

    def help_create_projects_list(self, projects_num=10):
        projects_list = []
        for i in range(projects_num):
            project = self.help_get_or_create_project(name=f"TestProject{i}")
            projects_list.append(project)
        return projects_list

    def test_user_visit_empty_project_page(self):
        # Logged user visit projects page.
        # There are no objects
        self.browser.get(self.url)
        # ul_tag = self.browser.find_elements_by_tag_name("th")
        li_elements = self.browser.find_elements_by_tag_name("li")
        self.assertEqual(len(li_elements), 1)
        self.assertEqual(li_elements[0].text, "No projects yet.")

    def test_user_visit_not_empty_project_page(self):
        # create 10 defaults project
        projects = self.help_create_projects_list()
        # Logged user visit projects page.
        # There are 10 objects
        self.browser.get(self.url)
        li_elements = self.browser.find_elements_by_tag_name("li")
        self.assertEqual(len(li_elements), 10)
