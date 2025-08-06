from lab_core.scientist import Scientist


def generate_scientists(number=5):
    count = 0
    while count != number:
        name = f"John Doe {count}"
        sc_field = "AI"
        publications = 5 + count
        years = 3 + count
        impact_lvl = "low"
        yield Scientist(name=name, field=sc_field, publications=publications,
                        experience_years=years, impact_level=impact_lvl)
        count += 1
