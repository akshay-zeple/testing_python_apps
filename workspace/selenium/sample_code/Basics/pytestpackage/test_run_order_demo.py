import pytest

@pytest.mark.run(order=2)
def test_run_order_methodA(oneTimeSetUp, setUp):
    print("Running method A")

@pytest.mark.run(order=1)
def test_run_order_methodC(oneTimeSetUp, setUp):
    print("Running method C")

@pytest.mark.run(order=3)
def test_run_order_methodB(oneTimeSetUp, setUp):
    print("Running method B")