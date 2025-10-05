import pytest
from pages.form_page import FormPage

def test_form_submission(driver):
    page = FormPage(driver)

    # Шаги теста
    page.enter_name("John Doe")\
        .enter_password("password123")\
        .select_drinks(["Milk", "Coffee"])\
        .select_color("Yellow")\
        .select_like_automation("Yes")\
        .enter_email("john.doe@example.com")\
        .enter_message("3 tools, Selenium")\
        .submit()

    # Проверка алерта
    alert_text = page.get_alert_text()
    assert alert_text == "Message received!"
