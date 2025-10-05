from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormPage:
    URL = "https://practice-automation.com/form-fields/"

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(self.URL)

    # Локаторы
    NAME = (By.ID, "name-input")
    PASSWORD = (By.XPATH, "//label[contains(text(),'Password')]/input")
    EMAIL = (By.ID, "email")
    MESSAGE = (By.ID, "message")
    SUBMIT = (By.ID, "submit-btn")

    # Вспомогательный метод для сильного скролла и клика через JS
    def _scroll_and_click(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'auto'});", element)
        self.driver.execute_script("arguments[0].click();", element)

    # Методы
    def enter_name(self, name: str):
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.NAME)
        )
        elem.clear()
        elem.send_keys(name)
        return self

    def enter_password(self, password: str):
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        elem.clear()
        elem.send_keys(password)
        return self

    def select_drinks(self, drinks: list):
        for drink in drinks:
            checkbox = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//input[@name='fav_drink' and @value='{drink}']")
                )
            )
            self._scroll_and_click(checkbox)
        return self

    def select_color(self, color_name: str):
        radio = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//input[@type='radio' and @value='{color_name}']")
            )
        )
        self._scroll_and_click(radio)
        return self

    def select_like_automation(self, value: str):
        select_elem = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "automation"))
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'auto'});", select_elem)
        select = Select(select_elem)
        select.select_by_visible_text(value)
        return self

    def enter_email(self, email: str):
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.EMAIL)
        )
        elem.clear()
        elem.send_keys(email)
        return self

    def enter_message(self, message: str):
        elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.MESSAGE)
        )
        elem.clear()
        elem.send_keys(message)
        return self

    def submit(self):
        submit_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.SUBMIT)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'auto'});", submit_btn)
        self.driver.execute_script("arguments[0].click();", submit_btn)
        return self

    def get_alert_text(self):
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text
