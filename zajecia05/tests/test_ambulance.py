import pytest
from fleet.ambulance import Ambulance

@pytest.fixture
def ambulance():
    return Ambulance(1, "Type A", "available", (64.095340, 90.920282), ["Defibrillator", "Oxygen tank"])

def test_initialization(ambulance):
    assert ambulance.id == 1
    assert ambulance.vehicle_type == "Type A"
    assert ambulance.status == "available"
    assert ambulance.location == (64.095340, 90.920282)
    assert ambulance.medical_equipment == ["Defibrillator", "Oxygen tank"]

def test_check_availability(ambulance):
    assert ambulance.check_availability() == 'Karetka nr 1 dostępna'
    ambulance.is_assigned = True
    assert ambulance.check_availability() == 'Karetka nr 1 niedostępna'

