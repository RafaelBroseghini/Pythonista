from allEmployees import *

def main():
    ubisoft = Company("Ubisoft")
    rafa = Manager("Rafa","Internet")
    rafa = ubisoft.raise_employee(rafa)
    print(ubisoft.raise_employee(rafa))

if __name__ == '__main__':
    main()