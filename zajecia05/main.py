from fleet.ambulance import Ambulance
from operations import *
from personnel import *
from fleet.station import Station
from log_config import setup_logging

def run_application():
    logger = setup_logging()
    logger.info("Logger active")

    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance(1, "Type A", "on mission", (64.095340, 90.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance(2, "Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])
    ambulance3 = Ambulance(3, "Type B", "available", (55.095440, 11.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 123, 12000.0)
    employee2 = Employee("Jane", "Smith", 124, 8000.0)

    driver1 = Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 126, 11500.0, "DL12346", ["ALS", "PHTLS"])

    station1 = Station(1, (71.095340, 18.920282), ambulance1, driver1, employee1)
    station2 = Station(1, (51.155347, 17.528583), ambulance2, driver2, employee2)

    # sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    # sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # sprawdzenie ile mamy pracowników
    print(Employee.get_instances_count())

    # sprawdzenie ile mamy kierowców
    print(Driver.get_instances_count())

    # sprawdzenie ile mamy stacji
    print(Station.get_instances_count())


    # stworzenie kolejki
    queue = IncidentQueue()

    # zaraportowanie 2 zgłoszeń
    incident1 = Incident(1, "Power outage in sector 4",1,"Anna Kowalska", '2024-04-09 18:35:13', ambulance1, (50.095340, 18.920282))
    incident2 = Incident(2, "Fire alarm in building 21",2,"Dagmara Nowak", '2024-04-09 18:37:18', ambulance2, (53.047340, 16.920902))
    queue += incident1
    queue += incident2

    # sprawdzenie ile mamy incydentów
    print(Incident.get_instances_count())


    # sprawdzenie ile jest kolejek incydentów
    print(IncidentQueue.get_instances_count())

    # wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(queue)

    # daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")


    #sprawdzenie czy karetka dojechała do stacji
    print(station1.check_location())
    print(station2.check_location())

    #sprawdzenie czasu od zgłoszenia incydentu nr 1
    print(incident1.check_time_passed())

    #sprawdzenie dostępności (stanu) karetki - gdy jest na misji to nie jest dostępna:
    print(ambulance1.check_availability())
    print(ambulance2.check_availability())
    print(ambulance3.check_availability())

    #sprawdzenie odległości karetki od wypadku:
    print(ambulance1.check_distance_from_incident())
    print(ambulance2.check_distance_from_incident())
    print(ambulance3.check_distance_from_incident())

if __name__ == "__main__":
    run_application()