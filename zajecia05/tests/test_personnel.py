import pytest
from personnel import Employee, Driver

@pytest.fixture
def employee():
    return Employee("John", "Doe", 123, 12000.0)

@pytest.fixture
def driver():
    return Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])

def test_employee_initialization(employee):
    assert employee.first_name == "John"
    assert employee.last_name == "Doe"
    assert employee.employee_id == 123
    assert employee.salary == 12000.0

def test_employee_update_salary(employee):
    employee.update_salary(13000.0)
    assert employee.salary == 13000.0

def test_driver_initialization(driver):
    assert driver.first_name == "Mike"
    assert driver.last_name == "Johnson"
    assert driver.employee_id == 125
    assert driver.salary == 10000.0
    assert driver.license_number == "DL12345"
    assert driver.qualifications == ["BLS"]

def test_driver_update_salary(driver):
    driver.update_salary(12000.0)
    assert driver.salary == 12000.0
