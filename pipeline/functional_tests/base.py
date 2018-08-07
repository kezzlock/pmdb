import time

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings

from pipeline.models import Project
from selenium import webdriver


@override_settings(DEBUG=False)
class FunctionalTest(StaticLiveServerTestCase):
    """Basic class for Functional tests."""
    # number of seconds to browser wait
    MAX_WAIT = 10

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.main_window = None
        while not self.main_window:
            self.main_window = self.browser.current_window_handle

    def tearDown(self):
        self.browser.quit()

    def wait(fn):
        """Decorator of function for loop checking funtion up to MAX_WAIT.

        Decorator returns a new function which will keep calling
        the input function, catching usual exceptions, until a timeout occurs.
        Required for selenium.
        """
        def modified_fn():
            start_time = time.time()
            while True:
                try:
                    return fn()
                except (AssertionError, WebDriverException) as e:
                    if time.time() - start_time > MAX_WAIT:
                        raise e
                    time.sleep(0.5)
        return modified_fn

    @wait
    def wait_for(self, fn):
        return fn()

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
