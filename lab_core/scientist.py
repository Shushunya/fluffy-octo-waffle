from decorators import log_calls, requires_publications


# TODO: add to_dict
# TODO: make LEVELS and FIELDS enums
# TODO: add __hash__
class Scientist:
    LEVELS = ("low", "medium", "high")
    FIELDS = ("biology", "physics", "chemistry", "mathematics", "ai", 'test')

    def __init__(self, name: str, publications: int,
                 experience_years: float, impact_level: str,
                 field: str = "unknown"):
        self.name = name
        self.publications = publications
        self.experience_years = experience_years

        if field.lower() in Scientist.FIELDS:
            self.field = field.lower()
        else:
            raise ValueError(f"Field '{field}' is not valid.")

        if impact_level.lower() in Scientist.LEVELS:
            self._impact_level = impact_level
        else:
            raise ValueError(f"Impact level '{impact_level}' is not valid.")

    @property
    def impact_level(self):
        """The impact level property"""
        return self._impact_level

    @impact_level.setter
    def impact_level(self, value: str):
        if value.lower() in Scientist.LEVELS:
            self._impact_level = value.lower()
        else:
            raise ValueError(f"Invalid impact level: {value}")

    def __repr__(self):
        return (
            f"<Scientist name='{self.name}', field='{self.field}', "
            f"pubs={self.publications}, exp={self.experience_years}, "
            f"impact='{self.impact_level}'>"
        )

    def __str__(self):
        text = (f"{self.name} is a scientist in the {self.field} field. "
                f"{self.name} has {self.publications} publications and {self.experience_years} years of experience. ")
        impact_lvl = f"The impact level is {self.impact_level}."
        return text + impact_lvl

    def __eq__(self, other):
        if isinstance(other, Scientist):
            return (self.name.lower() == other.name.lower()
                    and self.field.lower() == other.field.lower()
                    and self.publications == other.publications
                    and self.experience_years == other.experience_years)
        return False

    def __lt__(self, other):
        if isinstance(other, Scientist):
            return self.publications < other.publications
        return False

    def __gt__(self, other):
        if isinstance(other, Scientist):
            return self.publications > other.publications
        return False

    @log_calls
    def publish(self):
        self.publications += 1

    @log_calls
    @requires_publications(minimum=7)
    def promote(self):
        maximum = len(Scientist.LEVELS)
        level_index = Scientist.LEVELS.index(self.impact_level)
        if level_index != maximum - 1:
            self._impact_level = Scientist.LEVELS[level_index+1]


class LeadScientist(Scientist):
    def __init__(self, name: str, publications: int,
                 experience_years: float, impact_level: str,
                 field: str, team_size: int, lab_name: str):
        super().__init__(name, publications, experience_years, impact_level, field)
        self.team_size = team_size
        self.lab_name = lab_name
