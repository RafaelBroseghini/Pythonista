from hourlyEmployee import HourlyEmployee
from salaryEmployee import SalaryEmployee
from manager import Manager
from executive import Executive

class Company(object):
    def __init__(self, name, hierarchy = [HourlyEmployee, SalaryEmployee, Manager, Executive]):
        self.name = name
        self.hierarchy = hierarchy
    
    def raise_employee(self, emp):
        highest_pos = False
        raised = False
        e = 0
        while not raised and not highest_pos:
            try:
                if isinstance(emp, self.hierarchy[e]):
                    emp = self.hierarchy[e+1](emp.name,emp.department)
                    raised = True
            except:
                highest_pos = True
                return "No promotion. {} is a(n) {} at the highest spot in the company, only below the CEO.".format(emp.name,self.hierarchy[e].__name__)
            e += 1
        return emp