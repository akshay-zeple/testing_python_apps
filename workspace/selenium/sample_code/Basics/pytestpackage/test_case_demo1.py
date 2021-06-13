import pytest

@pytest.fixture()
def setUp():
    print("demo 1 set up")

def test_methodA(setUp):
    print("Running demo 1 method A")

def test_methodB(setUp):
    print("Running demo 1 method B")