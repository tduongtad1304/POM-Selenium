class Locators():

    # Login Page Objects

    username_textbox_id = "txtUsername"

    password_textbox_id = "txtPassword"

    login_button_id = "btnLogin"

    invalid_credentials_error_message_xpath = '//*[@id = "spanMessage"]'

    # Home Page Locators

    # Welcome Menu Locators

    welcome_link_id = "welcome"

    logout_link_linkText = "Logout"

    about_link_id = "aboutDisplayLink"

    support_link_text = "Support"

    notification_button_id = "notification"

    # Marketing Locators

    marketplace_link_id = "MP_link"

    # Guide Page Locators

    question_mark_xpath = '//*[@id="branding"]/a[3]'

    # Navbar Locators

    # Admin Menu Locators
    admin_list_id = "menu_admin_viewAdminModule"

    # User Management Locators
    user_management_link_id = "menu_admin_UserManagement"

    users_list_id = "menu_admin_viewSystemUsers"

    # Edit user

    add_user_button_id = "btnAdd"

    role_list_id = "systemUser_userType"

    employee_name_id = "systemUser_employeeName_empName"

    employee_username_id = "systemUser_userName"

    employee_status_id = "systemUser_status"

    employee_password_id = "systemUser_password"

    employee_confirm_password_id = "systemUser_confirmPassword"

    save_button_id = "btnSave"

    search_username_id = "searchSystemUser_userName"

    search_user_role_id = "searchSystemUser_userType"

    search_employee_name_id = "searchSystemUser_employeeName_empName"

    search_employee_status_id = "searchSystemUser_status"

    search_button_id = "searchBtn"

    # Job Title Locators

    menu_admin_job_id = 'menu_admin_Job'

    menu_job_title = 'menu_admin_viewJobTitleList'

    menu_job_pay_grade = 'menu_admin_viewPayGrades'

    menu_job_employment_status = 'menu_admin_employmentStatus'

    menu_job_categories = 'menu_admin_jobCategory'

    menu_job_departments = 'menu_admin_workShift'

    # Edit Job Title

    menu_job_title_add_button_id = 'btnAdd'

    menu_job_title_add_save_button_id = "btnSave"

    menu_job_title_edit_id = 'jobTitle_jobTitle'

    menu_job_description_id = 'jobTitle_jobDescription'

    menu_job_specification_id = 'jobTitle_jobSpec'

    menu_job_note_id = 'jobTitle_note'

    menu_job_title_link_text = 'Automation Tester'

    menu_job_title_edit_save_button_id = "btnSave"
