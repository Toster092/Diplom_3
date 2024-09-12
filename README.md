## Дипломный проект. Задание 3: UI-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы UI-тесты на страницы `Восстановление пароля`, `Личный кабинет`, `Проверка основного функционала`, 
`Лента заказов`


### Структура проекта

- `tests` - пакет, содержащий тесты, разделенные по страницам.

### Запуск автотестов

**Установка зависимостей**

> `$ pip install pytest`
> `$ pip install requests'
> 'pip install Faker'
> 'pip install selenium'  

**Запуск автотестов и создание allure отчета**

>  `pytest --alluredir=allure_results`
**Создание HTML отчета** 
> `allure serve allure_results'