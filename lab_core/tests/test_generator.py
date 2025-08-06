import pytest
from types import GeneratorType
from lab_core.generator import generate_scientists
from lab_core.scientist import Scientist


class TestGenerateScientists:

    def test_return_generator(self):
        gen = generate_scientists()
        assert isinstance(gen, GeneratorType)

    def test_generated_object_type(self):
        gen = generate_scientists(number=1)
        obj = next(gen)
        assert isinstance(obj, Scientist)

    def test_generate_zero(self):
        gen = generate_scientists(number=0)
        assert list(gen) == []

    def test_generator_lazy(self):
        gen = generate_scientists(number=10)
        assert hasattr(gen, '__next__')

    def test_number_of_objects(self):
        num = 3
        gen = generate_scientists(number=num)
        length = len(list(gen))
        assert length == num
