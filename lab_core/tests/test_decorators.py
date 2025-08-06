import pytest
from datetime import datetime
from lab_core.decorators import log_calls, requires_publications

class Dummy:
    def __init__(self, publications=5, experience_years=3, field="test", log_path=None):
        self.publications = publications
        self.experience_years = experience_years
        self.field = field
        self._log_path = str(log_path)

    def __repr__(self):
        return f"<Dummy pubs={self.publications}, years={self.experience_years}, field={self.field}>"

    @log_calls
    def sample_publish(self):
        return "published"

    @log_calls
    @requires_publications(minimum=10)
    def sample_promote(self):
        return "promoted"

# -------------------------------
# Test @log_calls
# -------------------------------

def test_log_calls_creates_log_entry(tmp_path):
    log_path = tmp_path / "test_logs.txt"

    obj = Dummy(log_path=log_path)
    result = obj.sample_publish()

    func_name = Dummy.sample_publish.__name__
    date = datetime.now()

    expected_log_text = (
        f"[{date.strftime('%Y-%m-%d %H:%M:%S')}] "
        f"CALL: {func_name} | "
        f"OBJECT: {repr(obj)}"
        "\n"
    )

    assert result == "published"
    assert log_path.read_text() == expected_log_text

class TestRequiresPublications:

    def test_requires_publications_success(self):
        obj = Dummy(publications=10, experience_years=6, field='ai')
        result = obj.sample_promote()
        assert result == "promoted"

    def test_requires_publications_fail_publications(self):
        obj = Dummy(publications=3, experience_years=6, field='ai')
        with pytest.raises(ValueError, match="Scientist is required to have more expertise."):
            obj.sample_promote()

    def test_requires_publications_fail_experience(self):
        obj = Dummy(publications=10, experience_years=2, field='ai')
        with pytest.raises(ValueError, match="Scientist is required to have more expertise."):
            obj.sample_promote()

    def test_requires_publications_fail_field(self):
        obj = Dummy(publications=10, experience_years=6, field='unknown')
        with pytest.raises(ValueError, match="Scientist is required to have more expertise."):
            obj.sample_promote()
