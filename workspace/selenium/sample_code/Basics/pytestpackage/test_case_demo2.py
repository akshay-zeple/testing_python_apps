import pytest

@pytest.yield_fixture()
def setUp():
    print("demo 2 set up set up")
    yield
    print("demo 2 set up tear down")

def test_methodA(setUp):
    print("Running demo 2 method A")

def test_methodB(setUp):
    print("Running demo 2 method B")