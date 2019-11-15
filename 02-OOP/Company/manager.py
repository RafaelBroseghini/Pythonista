from employee import Employee


class Manager(Employee):
    def __init__(self, name, department, salary=100000):
        super().__init__(name, department)
        self.salary = salary

    def __str__(self):
        return "{} is a manager in the {} deparment earning ${}/yr.".format(
            self.name, self.department, self.salary
        )
