# UI Autotests: Проверка формы

## Цель
Проверка функциональности формы на странице: https://practice-automation.com/form-fields/

## Тест-кейсы

### Позитивный тест-кейс
- **ID**: ТС_001
- **Название**: Корректная отправка формы с валидными данными.
- **Описание**: Проверка корректной отправки формы при правильном заполнении всех обязательных полей верными данными.
- **Предусловия**: Пользователь открыл старинцу формы.
- **Шаги**:
1. Ввести в поле **Name**: `Ivan`.  
  2. Ввести в поле **Password**: `hello123`.  
  3. Выбрать **What is your favorite drink?**: `Milk`, `Coffee`.  
  4. Выбрать **What is your favorite color?**:`Yellow`.  
  5. Выбрать **Do you like automation?**: `Yes`.  
  6. Ввести в поле **Email**:  `i_goldmen@gmail.com`.  
  7. Ввести в поле **Message**: `4 tools, webdriver-manager`.  
  8. Нажать кнопку **Submit**. 
- **Ожидаемый результат**: Появляется alert с текстом: `Message received!`
- **Фактический результат**: Появляется alert с текстом: `Message received!`
- **Статус**: Пройден
- **Приоритет**: Высокий



### Негативный тест
- **ID**: ТС_002
- **Название**: Отправка формы без имени.
- **Описание**: Проверка поведения формы, если не заполнить поле `Name`
- **Предусловия**: Пользователь открыл старинцу формы.
- **Шаги**:
1. Не зполнять поле `Name`.  
  2. Ввести в поле **Password**: `hello123`. 
  3. Выбрать **What is your favorite drink?**: `Milk`, `Coffee`.  
  4. Выбрать **What is your favorite color?**: `Yellow`.  
  5. Выбрать **Do you like automation?**: `Yes`.  
  6. Ввести в поле **Email**: `i_goldmen@gmail.com`.   
  7. Ввести в поле **Message**: `4 tools, webdriver-manager`.  
  8. Нажать кнопку **Submit**. 
- **Ожидаемый результат**: 
- Форма не отправляется. 
- Фокус возвращается на поле `Name`
- **Фактический результат**: -
- **Статус**: -
- **Приоритет**: Средний

## Запуск тестов и отчет Allure

1. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```
2. Запустите тесты с генерацией Allure-отчета:
   ```
   pytest --alluredir=allure-results
   allure serve allure-results
   ```
3. Скриншот успешного отчета Allure:
   ![allure-report-example](allure-report/example.png)