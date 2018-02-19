'''
CS 150 B LAB 01
Purpose: Calculate Payroll.

Author: Rafael Broseghini.
Date: 02/12/2016

Filename: BroseghiniPayroll.py
'''

name = input("Enter employee's name: ")

hrsWorked = float(input('Enter number of hours worked in a week: '))

payRate = float(input('Enter hourly pay rate: '))

grossPay = hrsWorked*payRate


federalTaxRate = float(input('Enter federal tax withholding rate: '))/100


federalDeduction = grossPay*federalTaxRate


stateTaxRate = float(input('Enter state tax withholding rate: '))/100


stateDeduction = grossPay*stateTaxRate


medicareRate = 1.45/100


medicareDeduction = grossPay*medicareRate


socialSecurityRate = 6.2/100


socialSecurityDeduction = grossPay*socialSecurityRate


totalDeductions = (federalDeduction + stateDeduction + medicareDeduction + socialSecurityDeduction)


netPay = (grossPay - federalDeduction - stateDeduction - medicareDeduction - socialSecurityDeduction)


print()
print()
print()
print()


print('Employee Name:', name)

print('Hours Worked:', round(hrsWorked, 1))

print('Pay Rate: $', round(payRate, 2))

print('Gross Pay: $', round(grossPay, 2))

print('Deductions:')

print('     ''Federal: $', round(federalDeduction, 2))

print('     ''State: $', round(stateDeduction, 2))

print('     ''Medicare: $', round(medicareDeduction, 2))

print('     ''Social Security: $', round(socialSecurityDeduction, 2))

print('     ''Total Deductions: $', round(totalDeductions, 2))

print('Net Pay: $', round(netPay, 2))

#
# Done!
