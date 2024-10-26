import pytest
from Resources.resource_codes import *


@pytest.mark.test1
def test_scenario_1():
    print("Test Scenario1")
    scenario_method()
    assert True


@pytest.mark.test2
def test_scenario_2():
    print("Test Scenario 2")
    assert True    