from employee import Employee


class SalaryEmployee(Employee):
    def __init__(self, name, department, salary=50000):
        super().__init__(name, department)
        self.salary = salary

    def __str__(self):
        return "{} is a salary employee in the {} earning ${}/yr.".format(
            self.name, self.department, self.salary
        )
