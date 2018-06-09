from employee import Employee
class Executive(Employee):
    def __init__(self, name, department, salary=200000):
        super().__init__(name, department)
        self.salary = salary
    
    def __str__(self):
            return "{} is an Executive in the {} deparment earning ${}/yr.".format(self.name, self.department, self.salary)