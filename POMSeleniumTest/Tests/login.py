"""import unittest"""
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class LoginTesting(unittest.TestCase):
    """login testing

    Args:
        unittest (_type_): test login
    """

    def setUp(self):
        """setUp method"""
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def test_login(self):
        """test_login method"""

        driver = self.driver

        driver.get('https://opensource-demo.orangehrmlive.com/')

        self.assertIn("OrangeHRM", driver.title)

        driver.find_element_by_id('txtUsername').send_keys('Admin')

        driver.find_element_by_id('txtPassword').send_keys('admin123')

        driver.find_element_by_id('btnLogin').click()

        driver.find_element_by_id('welcome').click()

        driver.find_element_by_link_text('Logout').click()

    def tearDown(self):
        """tearDown method"""
        self.driver.close()

        self.driver.quit()

        print('Test completed')


if __name__ == "__main__":
    unittest.main()
