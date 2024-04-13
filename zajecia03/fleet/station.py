class Station:
    __max_id = 0

    def __init__(self, id, location, ambulance, driver, employee):
        self.id = id
        self.location = location
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        Station.__max_id += 1 

    @classmethod
    def get_instances_count(cls):
        return f"Number of stations: {cls.__max_id}"
    
    def check_location(self):
        if(self.location == self.ambulance.location):
            return f"Karetka nr {self.ambulance.id} jest na stacji"
        else:
            return f"Karetka nr {self.ambulance.id} jeszcze nie dojechała na stację"

    
        
