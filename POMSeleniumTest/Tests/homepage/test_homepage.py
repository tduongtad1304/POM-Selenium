"""import unittest"""
from locale import windows_locale
import HtmlTestRunner
from POMSeleniumTest.Pages.homePage import HomePage
from POMSeleniumTest.Pages.loginPage import LoginPage

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


"""import pages"""


class TestHomePage(unittest.TestCase):
    def setUp(self):
        """setUp method"""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')

    def test_welcome_menu(self):

        driver = self.driver
        webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()

        self.assertIn("OrangeHRM", driver.title)

        """handle login process"""
        login = LoginPage(driver)

        login.enter_username('Admin')

        login.enter_password('admin123')

        login.click_login()

        """handle homepage process"""
        homepage = HomePage(driver)

        homepage.click_welcome()

        homepage.click_about()

        homepage.click_support()

        homepage.click_notification_button()

        homepage.click_question_button()

        time.sleep(5)

        driver.switch_to.window(driver.window_handles[0])

        homepage.hover_and_click_marketplace()

    def test_admin_user_management(self):
        driver = self.driver

        login = LoginPage(driver)

        login.enter_username('Admin')

        login.enter_password('admin123')

        login.click_login()

        admin = HomePage(driver)

        admin.hover_admin_list()

        admin.add_new_user(
            "Jasmine Morgan", "abcdefgh", "abc.12345", "abc.12345")

        time.sleep(3)

    def test_search_user(self):
        driver = self.driver

        login = LoginPage(driver)

        login.enter_username('Admin')

        login.enter_password('admin123')

        login.click_login()

        admin = HomePage(driver)

        admin.hover_admin_list()

        admin.search_user("", "Jasmine Morgan")

        time.sleep(3)

    def test_admin_add_job(self):
        driver = self.driver

        login = LoginPage(driver)

        login.enter_username('Admin')

        login.enter_password('admin123')

        login.click_login()

        admin = HomePage(driver)

        admin.click_admin_job()

        admin.click_job_title_add(
            "Testing Software", "lorem ipsum dolor sit amet", "No note description"),

        # admin.click_job_title_edit(
        #     "Animation Design ", "lorem ipsum dolor sit amet", "For beginners")

        time.sleep(3)

    def tearDown(self):
        """tearDown method"""
        self.driver.close()

        self.driver.quit()

        print('Test completed')


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='D:/TAD/POMSelenium/POMSeleniumTest/Reports'))
