from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

  def setUp(self):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    self.browser = webdriver.Chrome(chrome_options=options)

  def tearDown(self):
    self.browser.quit()

  def test_open_page(self):

    # user visits website
    self.browser.get(self.live_server_url)

    # user notices iamsitting in the title
    self.assertIn('iamsitting', self.browser.title)

    # user notices website alert
    alert_text = self.browser.find_element_by_class_name('alert-dismissible').text
    self.assertIn('To reduce costs', alert_text)

    # dismiss website alert
    dismiss_button = self.browser.find_element_by_xpath("//button[@data-dismiss='alert']")
    dismiss_button.click()

  def test_click_to_login(self):

    # user visits website
    self.browser.get('http://localhost:8000')

    # user clicks on login
    login_button = self.browser.find_element_by_xpath("/html/body/div[1]/header/a")
    login_button.click()
