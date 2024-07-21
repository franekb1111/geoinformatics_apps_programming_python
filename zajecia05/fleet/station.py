from log_config import setup_logging

class Station:
    __max_id = 0

    def __init__(self, id, location, ambulance, driver, employee):
        self.id = id
        self.location = location
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        Station.__max_id += 1

        logger = setup_logging()
        if(location[0] > 90 or location[0] < -90):
            logger.error("Dlugosc geograficzna musi byc w przedziale (-90, 90) dla stacji")
        if(location[1] > 180 or location[1] < -180):
            logger.error("Szerokosc geograficzna musi byc w przedziale (-180, 180) dla stacji")

    @classmethod
    def get_instances_count(cls):
        return f"Number of stations: {cls.__max_id}"
    
    def check_location(self):
        if(self.location == self.ambulance.location):
            return f"Karetka nr {self.ambulance.id} jest na stacji"
        else:
            return f"Karetka nr {self.ambulance.id} jeszcze nie dojechała na stację"

    
        
