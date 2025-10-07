from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    """
    Page Object для работы с формой на practice-automation.com/form-fields/.
    Инкапсулирует элементы и действия над формой.
    """

    URL = "https://practice-automation.com/form-fields/"

    def __init__(self, driver):
        """
        Initialize the FormPage with a Selenium WebDriver and open the form page.
        """
        self.driver = driver
        self.driver.get(self.URL)
        self._wait = WebDriverWait(self.driver, 10)

    @property
    def name_input(self):
        """
        Returns the name input element using ID selector.
        """
        return self._wait.until(EC.visibility_of_element_located((By.ID, "name-input")))

    @property
    def password_input(self):
        """
        Returns the password input element using XPath selector.
        """
        return self._wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//label[contains(text(),'Password')]/input")
            )
        )

    @property
    def email_input(self):
        """
        Returns the email input element using ID selector.
        """
        return self._wait.until(EC.visibility_of_element_located((By.ID, "email")))

    @property
    def message_input(self):
        """
        Returns the message input element using ID selector.
        """
        return self._wait.until(EC.visibility_of_element_located((By.ID, "message")))

    @property
    def submit_btn(self):
        """
        Returns the submit button element using CSS selector.
        """
        return self._wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#submit-btn"))
        )

    def enter_name(self, name: str):
        """
        Enter text into the name input field.
        """
        self.name_input.clear()
        self.name_input.send_keys(name)
        return self

    def enter_password(self, password: str):
        """
        Enter text into the password input field.
        """
        self.password_input.clear()
        self.password_input.send_keys(password)
        return self

    def select_drinks(self, drinks: list):
        """
        Select drink checkboxes by their values.
        """
        for drink in drinks:
            checkbox = self._wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, f"//input[@name='fav_drink' and @value='{drink}']")
                )
            )
            self.driver.execute_script("arguments[0].click();", checkbox)
        return self

    def select_color(self, color_name: str):
        """
        Select a color radio button by its value.
        """
        radio = self._wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//input[@type='radio' and @value='{color_name}']")
            )
        )
        self.driver.execute_script("arguments[0].click();", radio)
        return self

    def select_like_automation(self, value: str):
        """
        Select an option from the automation dropdown.
        """
        select_elem = self._wait.until(
            EC.element_to_be_clickable((By.ID, "automation"))
        )
        select = Select(select_elem)
        select.select_by_visible_text(value)
        return self

    def enter_email(self, email: str):
        """
        Enter text into the email input field.
        """
        self.email_input.clear()
        self.email_input.send_keys(email)
        return self

    def get_tools_message(self):
        """
        Получает количество инструментов и самый длинный инструмент из списка Automation tools.
        Формирует строку для поля Message.
        """
        # Находим <ul> после <label>Automation tools</label>
        tools_elements = self.driver.find_elements(
            By.XPATH,
            "//label[contains(text(),'Automation tools')]/following-sibling::ul/li",
        )
        tools = [el.text for el in tools_elements]
        print("Найденные инструменты:", tools)
        tools_count = len(tools)
        longest_tool = max(tools, key=len) if tools else ""
        return f"{tools_count} tools, {longest_tool}"

    def enter_message(self, message: str):
        """
        Enter text into the message input field.
        """
        self.message_input.clear()
        self.message_input.send_keys(message)
        return self

    def submit(self):
        """
        Click the submit button to send the form.
        """
        self.driver.execute_script("arguments[0].click();", self.submit_btn)
        return self

    def get_alert_text(self):
        """
        Wait for alert, get its text, accept it and return the text.
        """
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text
