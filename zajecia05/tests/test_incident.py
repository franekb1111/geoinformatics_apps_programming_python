import pytest
from operations.incident import Incident
from fleet.ambulance import Ambulance
from datetime import datetime

@pytest.fixture
def ambulance():
    return Ambulance(1, "Type A", "available", (64.095340, 90.920282), ["Defibrillator", "Oxygen tank"])

@pytest.fixture
def incident(ambulance):
    return Incident(1, "Power outage in sector 4", 1, "Anna Kowalska", '2024-04-09 18:35:13', ambulance, (50.095340, 18.920282))

def test_initialization(incident):
    assert incident.id == 1
    assert incident.description == "Power outage in sector 4"
    assert incident.priority == 1
    assert incident.reporter == "Anna Kowalska"
    assert incident.time == '2024-04-09 18:35:13'
    assert incident.location == (50.095340, 18.920282)

def test_check_time_passed(incident):
    current_time = datetime.strptime('2024-04-09 19:35:13', "%Y-%m-%d %H:%M:%S")
    incident_time = datetime.strptime(incident.time, "%Y-%m-%d %H:%M:%S")
    time_passed = current_time - incident_time
    assert str(time_passed) == "1:00:00"