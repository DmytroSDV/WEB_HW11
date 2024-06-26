## Python web #11

Мета цього домашнього завдання — створити REST API для зберігання та управління контактами. API повинен бути побудований з використанням інфраструктури FastAPI та використовувати SQLAlchemy для управління базою даних.

Контакти повинні зберігатися в базі даних та містити в собі наступну інформацію:
  - Ім'я
  - Прізвище
  - Електронна адреса
  - Номер телефону
  - День народження
  - Додаткові дані (необов'язково)

API повинен мати можливість виконувати наступні дії:
  - Створити новий контакт
  - Отримати список всіх контактів
  - Отримати один контакт за ідентифікатором
  - Оновити існуючий контакт
  - Видалити контакт

На придачу до базового функціоналу CRUD API також повинен мати наступні функції:
  - Контакти повинні бути доступні для пошуку за іменем, прізвищем чи адресою електронної пошти (Query).
  - API повинен мати змогу отримати список контактів з днями народження на найближчі 7 днів.


### Загальні вимоги

  1. Використання фреймворку FastAPI для створення API
  2. Використання ORM SQLAlchemy для роботи з базою даних
  3. В якості бази даних слід використовувати PostgreSQL.
  4. Підтримка CRUD операцій для контактів
  5. Підтримка зберігання дати народження контакту
  6. Надання документів для API
  7. Використання модуля перевірки достовірності даних Pydantic
