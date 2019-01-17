from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):
  superuser = None
  PASSWORD = 'badpassword'

  def rev(self, name):
    return self.live_server_url + reverse(name)

  def create_user(self, su=False):
    u = User(username='u1', is_superuser=su)
    u.save()
    u.set_password(self.PASSWORD)
    return u

  def login_to_site(self):
    self.browser.get(self.rev('accounts:login'))
    username = self.browser.find_element_by_name('username')
    username.send_keys(self.superuser.username)
    password = self.browser.find_element_by_name('password')
    password.send_keys(self.PASSWORD)
    submit_button = self.browser.find_element_by_xpath('//*[@id="main"]/section/form/div/div[3]/ul/li/input')
    submit_button.click()
    # self.assertEquals(self.browser.current_url, self.live_server_url)

  def setUp(self):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1200x600')
    self.browser = webdriver.Chrome(chrome_options=options)
    self.superuser = self.create_user(su=True)

  def tearDown(self):
    self.browser.quit()

  def test_open_home_page(self):

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
    self.assertEquals(dismiss_button.is_displayed(), False)

  def test_click_to_login(self):

    # user visits website
    self.browser.get(self.live_server_url)

    # user clicks on login
    login_button = self.browser.find_element_by_xpath('//*[@id="header"]/a')
    login_button.click()
    self.assertEquals(self.browser.current_url, self.rev('accounts:login'))

  def test_post_requests(self):

    # user logs in
    self.login_to_site()

    # user clicks to post requests page
    post_req_button = self.browser.find_element_by_xpath('//*[@id="navPanel"]/nav/ul[1]/li[3]/a')
    post_req_button.click()
    self.assertEquals(self.browser.current_url, self.rev('blog:post-requests'))
