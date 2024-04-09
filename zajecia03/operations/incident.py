import importlib
import datetime
from fleet.ambulance import Ambulance

class Incident:
    __max_id = 0

    def __init__(self, id, description, priority, reporter, time, ambulance, location):
        self.id = id
        self.description = description
        self.priority = priority
        self.reporter = reporter
        self.time = time
        self.ambulance = ambulance
        self.ambulance.is_assigned = True
        self.ambulance.incident_location = location
        self.location = location
        Incident.__max_id += 1

    @classmethod
    def get_instances_count(cls):
        return f"Number of active incidents: {cls.__max_id}"

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r}, priority={self.priority!r}, reporter={self.reporter!r}, time={self.time!r}, ambulance={self.ambulance.id!r}, location={self.location!r})"

    def __str__(self):
        return f"Incident {self.id}: {self.description}. Priorty: {self.priority}, reporter: {self.reporter}, time of report: {self.time}, id of sent ambulance: {self.ambulance.id }, location: {self.location}"
    
    def check_time_passed(self):
        importlib.reload(datetime)
        time_passed = datetime.datetime.now() - datetime.datetime.strptime(self.time, "%Y-%m-%d %H:%M:%S") 
        return f"{time_passed} passed from incident {self.id} report (HH-MM-SS format)"