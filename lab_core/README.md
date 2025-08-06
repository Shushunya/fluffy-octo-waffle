1. Створи клас Scientist:

```
class Scientist:
    def __init__(self, name: str, field: str, publications: int, experience_years: float): ...
```
2. Додай:

- `@property` → impact_level: high / medium / low

- `__str__`,` __repr__`, `__eq__`

- Валідація у `__init__` (наприклад, поле field має бути з переліку)

3. Зроби успадкування:

`class LeadScientist(Scientist)` з новим полем `team_size` або `lab_name`

4. Декоратори:

- `@log_calls` — виводить лог, коли викликається метод

- `@requires_publications(min=10)` — валідатор для успішних вчених

5. Контекстний менеджер:

- `class FileLogger`: пише дані про вченого в лог-файл у `__enter__` / `__exit__`

6. Генератор:

- `generate_scientists(n)` — генерує випадкових вчених з faker або руками

7. Покриття юніт-тестами (pytest):

- `test_scientist.py` — тести для логіки та property

1. Scientist
name (рядок)

field (рядок, галузь науки)

experience_years (int)

publications (список назв публікацій)

Метод add_publication(title: str)

Property is_senior: True, якщо досвіду більше 10 років

2. Experiment
title (рядок)

scientist (об’єкт Scientist)

status ("ongoing", "completed", "failed")

Класовий атрибут allowed_statuses

Статичний метод validate_status(status: str) → перевіряє чи статус валідний

Property is_successful: повертає True, якщо статус "completed" та вченому > 5 років досвіду

🔹 Особливі вимоги:
Використати @property і @classmethod/@staticmethod де потрібно

Продумати правильну інкапсуляцію: не всі атрибути мають бути доступні напряму

Класи повинні бути читабельними: реалізуй __str__ або __repr__ у Scientist

Реалізуй зв'язок: 1 Scientist може мати багато Experiment

🔸 Не обов’язково, але бажано:
Покрий код простими тестами (навіть вручну)

Напиши приклад створення об’єктів і взаємодії між ними
