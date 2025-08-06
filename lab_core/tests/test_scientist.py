import pytest
from copy import deepcopy
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



class TestScientist:
    def test_create_scientist_valid(self, base_data):
        test_obj = Scientist(**base_data)
        for key, value in base_data.items():
            assert getattr(test_obj, key) == value

    @pytest.mark.parametrize("field", ["invalid", "123", ""])
    def test_create_scientist_invalid_field(self, field, base_data):
        data = deepcopy(base_data)
        data['field'] = field
        error_msg = f"Field '{field}' is not valid."
        with pytest.raises(ValueError, match=error_msg):
            Scientist(**data)

    @pytest.mark.parametrize("impact_level", ["invalid", "", "11"])
    def test_create_scientist_invalid_impact_level(self, impact_level, base_data):
        data = deepcopy(base_data)
        data['impact_level'] = impact_level
        error_msg = f"Impact level '{impact_level}' is not valid."
        with pytest.raises(ValueError, match=error_msg):
            Scientist(**data)

    def test_repr(self, base_scientist):
        expected = f"Scientist: {base_scientist.name} | field: {base_scientist.field} | publications: {base_scientist.publications}"
        assert expected == repr(base_scientist)

    def test_str(self, base_scientist):
        expected = (
            f"{base_scientist.name} is a scientist in the {base_scientist.field} field. "
            f"{base_scientist.name} has {base_scientist.publications} publications and "
            f"{base_scientist.experience_years} years of experience. "
            f"The impact level is {base_scientist.impact_level}."
        )
        assert str(base_scientist) == expected

    def test_eq(self, base_scientist, base_data):
        other_scientist = Scientist(**base_data)
        assert other_scientist == base_scientist

    def test_lt(self, base_scientist):
        scientist1 = deepcopy(base_scientist)
        scientist2 = deepcopy(base_scientist)
        scientist2.publications = scientist1.publications + 1
        assert scientist1 < scientist2
        assert not scientist2 < scientist1

    def test_lt_fail_non_scientist(self, base_scientist):
        other = "aa"
        assert not base_scientist < other
        assert not base_scientist < 1

    def test_gt(self, base_scientist):
        scientist1 = deepcopy(base_scientist)
        scientist2 = deepcopy(base_scientist)
        scientist2.publications = scientist1.publications + 1
        assert scientist2 > scientist1
        assert not scientist1 > scientist2

    def test_gt_fail_non_scientist(self, base_scientist):
        other = "aa"
        assert not base_scientist > other
        assert not base_scientist > 1

    def test_impact_level_getter(self, base_scientist, base_data):
        impact_lvl = base_scientist.impact_level
        assert impact_lvl == base_data['impact_level']

    def test_impact_level_setter_success(self, base_scientist):
        new_impact_level = "high"
        test_obj = deepcopy(base_scientist)
        test_obj.impact_level = new_impact_level
        real_impact_lvl = test_obj.impact_level
        assert real_impact_lvl == new_impact_level

    @pytest.mark.parametrize("lvl", ['invalid', '11'])
    def test_impact_level_setter_fail(self, base_scientist, lvl):
        error_msg = f"Invalid impact level: {lvl}"
        with pytest.raises(ValueError, match=error_msg):
            base_scientist.impact_level = lvl

    def test_publish(self, base_data, base_scientist):
        test_obj = deepcopy(base_scientist)
        test_obj.publish()
        assert test_obj.publications == base_scientist.publications + 1

    @pytest.mark.parametrize("pubs, years", [(5, 10), (8, 3)])
    def test_promote_fail(self, base_data, pubs, years, ):
        data = deepcopy(base_data)
        data['publications'] = pubs
        data['experience_years'] = years
        error_msg = "Scientist is required to have more expertise."
        test_obj = Scientist(**data)

        with pytest.raises(ValueError, match=error_msg):
            test_obj.promote()

    @pytest.mark.parametrize("pubs, years, expected", [(8, 10, "medium")])
    def test_promote_success(self, base_data, pubs, years, expected):
        data = deepcopy(base_data)
        data['publications'] = pubs
        data['experience_years'] = years
        test_obj = Scientist(**data)
        test_obj.promote()
        assert test_obj.impact_level == expected
