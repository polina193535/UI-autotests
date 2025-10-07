from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    URL = "https://practice-automation.com/form-fields/"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.URL)
        # Page Factory: элементы инициализируются через свойства
        self._wait = WebDriverWait(self.driver, 10)

    @property
    def name_input(self):
        return self._wait.until(EC.visibility_of_element_located((By.ID, "name-input")))

    @property
    def password_input(self):
        return self._wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//label[contains(text(),'Password')]/input")
            )
        )

    @property
    def email_input(self):
        return self._wait.until(EC.visibility_of_element_located((By.ID, "email")))

    @property
    def message_input(self):
        return self._wait.until(EC.visibility_of_element_located((By.ID, "message")))

    @property
    def submit_btn(self):
        return self._wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))

    def enter_name(self, name: str):
        self.name_input.clear()
        self.name_input.send_keys(name)
        return self

    def enter_password(self, password: str):
        self.password_input.clear()
        self.password_input.send_keys(password)
        return self

    def select_drinks(self, drinks: list):
        for drink in drinks:
            checkbox = self._wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//input[@name='fav_drink' and @value='{drink}']")
                )
            )
            self.driver.execute_script("arguments[0].click();", checkbox)
        return self

    def select_color(self, color_name: str):
        radio = self._wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//input[@type='radio' and @value='{color_name}']")
            )
        )
        self.driver.execute_script("arguments[0].click();", radio)
        return self

    def select_like_automation(self, value: str):
        select_elem = self._wait.until(
            EC.element_to_be_clickable((By.ID, "automation"))
        )
        select = Select(select_elem)
        select.select_by_visible_text(value)
        return self

    def enter_email(self, email: str):
        self.email_input.clear()
        self.email_input.send_keys(email)
        return self

    def enter_message(self, message: str):
        self.message_input.clear()
        self.message_input.send_keys(message)
        return self

    def submit(self):
        self.driver.execute_script("arguments[0].click();", self.submit_btn)
        return self

    def get_alert_text(self):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text
