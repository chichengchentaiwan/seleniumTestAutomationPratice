from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.email_alert_message = (By.ID, "email-message")
        self.password_alert_message = (By.ID, "password-message")
        self.github_site_hyperlink = (By.LINK_TEXT, "GitHub")

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    # For the alert message of email field
    def get_email_alert_message(self):
        return self.driver.find_element(*self.email_alert_message).text

    # For the alert message of password field
    def get_password_alert_message(self):
        return self.driver.find_element(*self.password_alert_message).text

    def click_github_hyperlink(self):
        self.driver.find_element(*self.github_site_hyperlink).click()
