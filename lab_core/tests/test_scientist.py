import pytest
from lab_core.scientist import Scientist


@pytest.fixture()
def base_data():
    return {
            'name': 'Test Scientist',
            'field': 'test',
            'publications': 5,
            'experience_years': 3,
            'impact_level': 'low'
        }

@pytest.fixture()
def base_scientist(base_data):
    return Scientist(**base_data)

@pytest.fixture
def valid_promotion_data():
    return {
        'name': 'Test Scientist',
        'field': 'test',
        'publications': 7,
        'experience_years': 6,
        'impact_level': 'low'
    }

@pytest.fixture
def invalid_promotion_data():
    return {
        'name': 'Test Scientist',
        'field': 'test',
        'publications': 5,
        'experience_years': 3,
        'impact_level': 'low'
    }


class TestScientist:
    def test_create_scientist_valid(self, base_data):
        test_obj = Scientist(**base_data)
        for key, value in base_data.items():
            assert getattr(test_obj, key) == value

    @pytest.mark.parametrize("field", ["invalid", "123", ""])
    def test_create_scientist_invalid_field(self, field, base_data):
        base_data['field'] = field
        error_msg = f"Field '{base_data["field"]}' is not valid."
        with pytest.raises(ValueError, match=error_msg):
            Scientist(**base_data)

    @pytest.mark.parametrize("impact_level", ["invalid", "", "11"])
    def test_create_scientist_invalid_impact_level(self, impact_level, base_data):
        base_data['impact_level'] = impact_level
        error_msg = f"Impact level '{base_data["impact_level"]}' is not valid."
        with pytest.raises(ValueError, match=error_msg):
            Scientist(**base_data)

    def test_repr(self, base_scientist):
        expected = f"Scientist: {base_scientist.name} | field: {base_scientist.field} | publications: {base_scientist.publications}"
        assert expected == repr(base_scientist)

    def test_str(self, base_scientist):
        expected = (f"{base_scientist.name} is a scientist in the {base_scientist.field} field. "
                f"{base_scientist.name} has {base_scientist.publications} publications and {base_scientist.experience_years} years of experience. "
                    f"The impact level is {base_scientist.impact_level}.")

        assert expected == str(base_scientist)

    def test_eq(self, base_scientist, base_data):
        other_scientist = Scientist(**base_data)
        assert other_scientist == base_scientist

    def test_impact_level_getter(self, base_scientist, base_data):
        impact_lvl = base_scientist.impact_level
        assert impact_lvl == base_data['impact_level']

    def test_impact_level_setter_success(self, base_data, base_scientist):
        new_impact_level = "high"
        base_scientist.impact_level = new_impact_level
        real_impact_lvl = base_scientist.impact_level
        assert real_impact_lvl == new_impact_level

    def test_impact_level_setter_fail(self):
        test_data = {
            'name': 'Test Scientist',
            'field': 'test',
            'publications': 5,
            'experience_years': 3,
            'impact_level': 'low'
        }
        test_obj = Scientist(**test_data)

        new_impact_level = "invalid"
        error_msg = f"Invalid impact level: {new_impact_level}"

        with pytest.raises(ValueError, match=error_msg):
            test_obj.impact_level = new_impact_level

    def test_publish(self, base_data, base_scientist):
        base_scientist.publish()
        assert base_scientist.publications == base_data['publications'] + 1

    @pytest.mark.parametrize("pubs, years, expected", [
        (8, 10, "medium"), # success
        (5, 10, pytest.raises(ValueError, match="Scientist is required to have more expertise.")),
        (8, 3, pytest.raises(ValueError, match="Scientist is required to have more expertise."))
    ])
    def test_promote(self, base_data, pubs, years, expected):
        base_data['publications'] = pubs
        base_data['experience_years'] = years
        test_obj = Scientist(**base_data)

        if isinstance(expected, str):
            test_obj.promote()
            assert test_obj.impact_level == expected
        else:
            with expected:
                test_obj.promote()
