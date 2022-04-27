"""import unittest"""
import HtmlTestRunner
from POMSeleniumTest.Pages.homePage import HomePage
from POMSeleniumTest.Pages.loginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))


"""import pages"""


class LogoutTesting(unittest.TestCase):
    """logout testing

    Args:
        unittest (_type_): test logout
    """

    def setUp(self):
        """setUp method"""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_01_login_valid(self):
        """test_login method"""

        driver = self.driver

        driver.get('https://opensource-demo.orangehrmlive.com/')

        self.assertIn("OrangeHRM", driver.title)

        """handle login process"""
        login = LoginPage(driver)

        login.enter_username('Admin')

        login.enter_password('admin123')

        login.click_login()

        """handle homepage process"""
        homepage = HomePage(driver)

        homepage.click_welcome()

        homepage.click_logout()

    def tearDown(self):
        """tearDown method"""
        self.driver.close()

        self.driver.quit()

        print('Test completed')


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(
        output='D:/TAD/POMSelenium/POMSeleniumTest/Reports'))
