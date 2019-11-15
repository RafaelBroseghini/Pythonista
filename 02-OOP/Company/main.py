from allEmployees import *


def main():
    ubisoft = Company("Ubisoft")
    rafa = SalaryEmployee("Rafa", "Internet")
    rafa = ubisoft.raise_employee(rafa)
    print(rafa)


if __name__ == "__main__":
    main()
