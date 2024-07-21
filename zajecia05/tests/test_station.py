import pytest
from fleet.ambulance import Ambulance
from personnel import Employee, Driver
from fleet.station import Station

@pytest.fixture
def station():
    ambulance = Ambulance(1, "Type A", "available", (64.095340, 90.920282), ["Defibrillator", "Oxygen tank"])
    employee = Employee("John", "Doe", 123, 12000.0)
    driver = Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    return Station(1, (71.095340, 18.920282), ambulance, driver, employee)

def test_station_initialization(station):
    assert station.id == 1
    assert station.location == (71.095340, 18.920282)
    assert station.ambulance.id == 1
    assert station.driver.employee_id == 125
    assert station.employee.employee_id == 123

def test_check_location(station):
    assert station.check_location() == "Karetka nr 1 jeszcze nie dojechała na stację"
    station.ambulance.location = (71.095340, 18.920282)
    assert station.check_location() == "Karetka nr 1 jest na stacji"
