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

