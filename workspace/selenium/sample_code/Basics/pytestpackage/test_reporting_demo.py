import pytest
from pytestpackage.some_class_to_test import SomeClassToTest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class TestClassDemo():

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumbers(2,8)
        assert result == 20
        print("Running method A")

    def test_methodB(self):
        result = self.abc.sumNumbers(2, 8)
        assert result > 20
        print("Running method B")