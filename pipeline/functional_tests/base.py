import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import override_settings


@override_settings(DEBUG=False)
class FunctionalTest(StaticLiveServerTestCase):
    """Basic class for Functional tests."""
    # number of seconds to browser wait
    MAX_WAIT = 10

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.main_window = None
        while not self.main_window:
            self.main_window = self.browser.current_window_handle

    def tearDown(self):
        self.browser.quit()

    def wait_for(self, fn):
        start_time = time.time()
        while True:
            try:
                return fn()
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > self.MAX_WAIT:
                    raise e
                time.sleep(0.5)
