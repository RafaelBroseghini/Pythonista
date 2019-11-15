from employee import Employee


class HourlyEmployee(Employee):
    def __init__(self, name, department, salary=25000):
        super().__init__(name, department)
        self.salary = salary

    def __str__(self):
        return "{} is a hourly employee in the {} deparment earning ${}/yr.".format(
            self.name, self.department, self.salary
        )
