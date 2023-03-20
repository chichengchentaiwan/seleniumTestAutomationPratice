from selenium import webdriver
from pages.login_page import LoginPage


class TestLoginClass:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://hotel.testplanisphere.dev/ja/login.html")
        self.login_page = LoginPage(self.driver)

    # It's important that we make sure the test be executed within a pure new environment
    def teardown_method(self):
        self.driver.quit()

    # We assume the user data here is valid
    def test_login_with_valid_credentials(self):
        self.login_page.enter_email("testusertestplanisphere@gmail.com")
        self.login_page.enter_password("testpass")
        self.login_page.click_login_button()
        # If user is redirected to mypage, then it means login successfully
        assert "mypage" in self.driver.current_url

    def test_login_with_invalid_email(self):
        self.login_page.enter_email("invalidemail")
        self.login_page.enter_password("testpass")
        self.login_page.click_login_button()
        assert "メールアドレスを入力してください。" in self.login_page.get_email_alert_message()

    # We assume we have this user existing in our DB
    def test_login_with_invalid_password(self):
        self.login_page.enter_email("testusertestplanisphere@gmail.com")
        self.login_page.enter_password("testinvalidpass")
        self.login_page.click_login_button()
        assert "このフィールドを入力してください。" in self.login_page.get_password_alert_message()

    def test_login_with_blank_username(self):
        self.login_page.enter_password("testpass")
        self.login_page.click_login_button()
        assert "このフィールドを入力してください。" in self.login_page.get_email_alert_message()

    # We assume we have this user existing in our DB
    def test_login_with_blank_password(self):
        self.login_page.enter_email("testuser")
        self.login_page.click_login_button()
        assert "このフィールドを入力してください。" in self.login_page.get_password_alert_message()

    # Test purpose: make sure the GitHub hyperlink is clickable
    def test_github_hyperlink_clickable(self):
        self.login_page.click_github_hyperlink()
        assert "hotel-example-site" in self.driver.current_url
