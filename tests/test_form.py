import allure
from pages.form_page import FormPage


@allure.feature("Form Submission")
@allure.story("Positive scenario")
def test_form_submission(driver):
    """
    Позитивный тест: корректная отправка формы с валидными данными.
    Проверяет, что появляется алерт с текстом "Message received!".
    """
    page = FormPage(driver)
    with allure.step("Заполнение формы и отправка"):
        message_text = page.get_tools_message()
        page.enter_name("Ivan").enter_password("hello123").select_drinks(
            ["Milk", "Coffee"]
        ).select_color("Yellow").select_like_automation("Yes").enter_email(
            "i_goldmen@gmail.com"
        ).enter_message(
            message_text
        ).submit()
    with allure.step("Проверка алерта"):
        alert_text = page.get_alert_text()
        assert alert_text == "Message received!"
