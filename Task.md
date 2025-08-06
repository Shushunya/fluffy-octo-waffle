# Завдання та прогрес проєкту

## Завдання v0.1

### Classes

- [x] Scientist
- [x] LeadScientist

##### Scientist

###### Attributes

- [x] name: str
- [x] field: str
- [x] publications: int
- [x] experience_years: float

###### Validations

- [x] `field` attribute should be from the pull
- [x] `impact_level` should be in {"high", "medium", "low"}
###### Properties
- [x] impact_level: str 

###### Magic methods
- [x] `__str__`
- [x] ` __repr__`
- [x] `__eq__`
- [x] `__lt__`
- [x] `__gt__`

##### LeadScientist

Inherits `Scientist`

###### Attributes

- [x] team_size: int
- [x] lab_name: str

### Decorators

- [x] `@log_calls`
- [x] `@requires_publications(min=10)` 

#### log_calls

- [ ] prints logs whenever a method is called
- [x] uses `FileLogger` to write logs into file

#### requires_publications(min=10)

- [x] check whether the Scientist is successful enough for the promotion
- [x] raises ValueError if requirement is not met
- [ ] raise PromotionError

### Context Manager

- [x] `FileLogger`: writes logs into a file

### Generator

- [x] `generate_scientists(n)` — generated a number of Scientist objects

## Завдання v0.2

### Classes

Scientist

changes: 
- [ ] publications int -> (список назв публікацій)

add:
- [ ] method `add_publication(title: str)`
- [ ] Property `is_senior`: True, якщо досвіду більше 10 років

#### Experiment

- [ ] title: str
- [ ] scientist: Scientist
- [ ] зв'язок: 1 Scientist може мати багато Experiment
- [ ] status: str ("ongoing", "completed", "failed")

- [ ] Класовий атрибут allowed_statuses

- [ ] Статичний метод `validate_status(status: str)` → перевіряє чи статус валідний

- [ ] Property `is_successful`: повертає True, якщо статус "completed" та вченому > 5 років досвіду
