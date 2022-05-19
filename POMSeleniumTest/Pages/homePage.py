import os
from selenium.webdriver.support.ui import Select
from POMSeleniumTest.Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains


class HomePage():
    """homepage class
    """

    def __init__(self, driver):
        self.driver = driver
        # welcome menu
        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linkText = Locators.logout_link_linkText
        self.about_link_id = Locators.about_link_id
        self.support_link_text = Locators.support_link_text
        self.notification_button_id = Locators.notification_button_id
        self.marketplace_link_id = Locators.marketplace_link_id

        # admin menu
        # user management menu
        self.admin_list_id = Locators.admin_list_id
        self.user_management_link_id = Locators.user_management_link_id
        self.user_list_id = Locators.users_list_id
        self.role_list_id = Locators.role_list_id

        # user edit
        self.add_user_button_id = Locators.add_user_button_id
        self.employee_name_id = Locators.employee_name_id
        self.employee_username_id = Locators.employee_username_id
        self.employee_status_id = Locators.employee_status_id
        self.employee_password_id = Locators.employee_password_id
        self.employee_confirm_id = Locators.employee_confirm_password_id
        self.save_button_id = Locators.save_button_id

        # search user
        self.search_username_id = Locators.search_username_id
        self.search_user_role_id = Locators.search_user_role_id
        self.search_employee_name_id = Locators.search_employee_name_id
        self.search_employee_status_id = Locators.search_employee_status_id
        self.search_button_id = Locators.search_button_id
        self.question_mark_xpath = Locators.question_mark_xpath

        # job menu
        self.menu_admin_job_id = Locators.menu_admin_job_id

        self.menu_job_title = Locators.menu_job_title

        self.menu_job_pay_grade = Locators.menu_job_pay_grade

        self.menu_job_employment_status = Locators.menu_job_employment_status

        self.menu_job_categories = Locators.menu_job_categories

        self.menu_job_departments = Locators.menu_job_departments

        # job add title

        self.menu_job_title_add_button_id = Locators.menu_job_title_add_button_id

        self.menu_job_title_edit_id = Locators.menu_job_title_edit_id

        self.menu_job_description_id = Locators.menu_job_description_id

        self.menu_job_specification_id = Locators.menu_job_specification_id

        self.menu_job_note_id = Locators.menu_job_note_id

        self.menu_job_title_add_save_button_id = Locators.menu_job_title_add_save_button_id

        # job edit

        self.menu_job_edit = Locators.menu_job_title_link_text

        self.menu_job_title_edit_button_id = Locators.menu_job_title_edit_save_button_id

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_about(self):
        self.driver.find_element_by_id(self.about_link_id).click()

    def click_support(self):
        self.driver.find_element_by_link_text(
            self.support_link_text).click()
        self.driver.back()

    def click_notification_button(self):
        element = self.driver.find_element_by_id(
            self.notification_button_id)

        elem = ActionChains(self.driver).move_to_element(element)
        elem.click().perform()

    def click_question_button(self):
        element = self.driver.find_element_by_xpath(
            self.question_mark_xpath)

        elem = ActionChains(self.driver).move_to_element(element)
        elem.click().perform()

    def hover_and_click_marketplace(self):
        element_to_hover_over = self.driver.find_element_by_id(
            self.marketplace_link_id)
        hover = ActionChains(self.driver).move_to_element(
            element_to_hover_over)
        hover.click().perform()

        self.driver.back()

    def hover_admin_list(self):
        admin = self.driver.find_element_by_id(
            self.admin_list_id)
        user_management = self.driver.find_element_by_id(
            self.user_management_link_id)
        hover1 = ActionChains(self.driver).move_to_element(
            admin)
        user = self.driver.find_element_by_id(
            self.user_list_id)
        hover1.perform()

        hover2 = ActionChains(self.driver).move_to_element(user_management)

        hover2.perform()

        hover3 = ActionChains(self.driver).move_to_element(user)

        hover3.perform()

        user.click()

    def add_new_user(self, employee_name, employee_user_name, employee_password, employee_confirm_password):
        self.driver.find_element_by_id(
            self.add_user_button_id).click()

        userRole = Select(self.driver.find_element_by_id(self.role_list_id))
        userRole.select_by_value("1")  # Admin
        # userRole.select_by_value("2")  # ESS

        self.driver.find_element_by_id(self.employee_name_id).clear()
        self.driver.find_element_by_id(
            self.employee_name_id).send_keys(employee_name)

        self.driver.find_element_by_id(self.employee_username_id).clear()
        self.driver.find_element_by_id(
            self.employee_username_id).send_keys(employee_user_name)

        status = Select(self.driver.find_element_by_id(
            self.employee_status_id))
        status.select_by_value("1")  # Enabled
        # status.select_by_value("0")  # Disabled

        self.driver.find_element_by_id(self.employee_password_id).clear()
        self.driver.find_element_by_id(
            self.employee_password_id).send_keys(employee_password)

        self.driver.find_element_by_id(self.employee_confirm_id).clear()
        self.driver.find_element_by_id(
            self.employee_confirm_id).send_keys(employee_confirm_password)

        self.driver.find_element_by_id(self.save_button_id).click()

    def search_user(self, user_name, employee_name):
        self.driver.find_element_by_id(self.search_username_id).clear()
        self.driver.find_element_by_id(
            self.search_username_id).send_keys(user_name)

        userRoleSearch = Select(
            self.driver.find_element_by_id(self.search_user_role_id))
        userRoleSearch.select_by_value("0")  # All
        # userRoleSearch.select_by_value("1")  # Admin
        # userRoleSearch.select_by_value("2")  # ESS

        self.driver.find_element_by_id(self.search_employee_name_id).clear()
        self.driver.find_element_by_id(
            self.search_employee_name_id).send_keys(employee_name)

        statusSearch = Select(self.driver.find_element_by_id(
            self.search_employee_status_id))

        statusSearch.select_by_value("1")  # Enabled
        # statusSearch.select_by_value("0")  # Diasabled

        self.driver.find_element_by_id(self.search_button_id).click()

    def click_admin_job(self):
        admin = self.driver.find_element_by_id(
            self.admin_list_id)
        job = self.driver.find_element_by_id(
            self.menu_admin_job_id)
        hover1 = ActionChains(self.driver).move_to_element(
            admin)
        job_titles = self.driver.find_element_by_id(
            self.menu_job_title)
        hover1.perform()

        hover2 = ActionChains(self.driver).move_to_element(job)

        hover2.perform()

        hover3 = ActionChains(self.driver).move_to_element(job_titles)

        hover3.perform()

        job_titles.click()

    def click_job_title_add(self, job_title, job_description, job_note):
        self.driver.find_element_by_id(
            self.menu_job_title_add_button_id).click()

        self.driver.find_element_by_id(self.menu_job_title_edit_id).clear()
        self.driver.find_element_by_id(
            self.menu_job_title_edit_id).send_keys(job_title)

        self.driver.find_element_by_id(self.menu_job_description_id).clear()
        self.driver.find_element_by_id(
            self.menu_job_description_id).send_keys(job_description)

        self.driver.find_element_by_id(
            self.menu_job_specification_id).send_keys(os.getcwd()+r"\Upload_images\Testing.jpg")

        self.driver.find_element_by_id(self.menu_job_note_id).clear()
        self.driver.find_element_by_id(
            self.menu_job_note_id).send_keys(job_note)

        self.driver.find_element_by_id(
            self.menu_job_title_add_save_button_id).click()

    def click_job_title_edit(self, job_title, job_description, job_note):
        self.driver.find_element_by_link_text(
            self.menu_job_edit).click()

        self.driver.find_element_by_id(
            self.menu_job_title_edit_button_id).click()

        self.driver.find_element_by_id(self.menu_job_title_edit_id).clear()
        self.driver.find_element_by_id(
            self.menu_job_title_edit_id).send_keys(job_title)

        self.driver.find_element_by_id(self.menu_job_description_id).clear()
        self.driver.find_element_by_id(
            self.menu_job_description_id).send_keys(job_description)

        self.driver.find_element_by_id(
            self.menu_job_specification_id).send_keys(os.getcwd()+r"\Upload_images\Testing.jpg")

        self.driver.find_element_by_id(self.menu_job_note_id).clear()
        self.driver.find_element_by_id(
            self.menu_job_note_id).send_keys(job_note)

        self.driver.find_element_by_id(
            self.menu_job_title_edit_button_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(
            self.logout_link_linkText).click()
