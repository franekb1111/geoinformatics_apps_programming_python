# V1 - slajd 8: python -m personnel.driver
from .employee import Employee


class Driver(Employee):
    __max_id = 0

    def __init__(self, first_name, last_name, employee_id, salary, license_number, qualifications):
        # alternatywa: super().__init__(self, ...)
        Employee.__init__(self, first_name, last_name, employee_id, salary)
        self.license_number = license_number
        self.qualifications = qualifications
        Driver.__max_id += 1

    @classmethod
    def get_instances_count(cls):
        return f"Number of working drivers: {cls.__max_id}"

    def display_info(self):
        return f"Driver ID: {self.employee_id}, Name: {self.first_name} {self.last_name}, Salary: {self.salary}, License Number: {self.license_number}, Qualifications: {', '.join(self.qualifications)}"

if __name__ == "__main__":
    driver1 = Driver("Jane", "Smith", 1, 12000.00, "LIC1001", ["BLS"])
    print(driver1.display_info())
