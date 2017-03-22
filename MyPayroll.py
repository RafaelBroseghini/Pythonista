'''
CS 150 B LAB 01
Purpose: Calculate Payroll.

Author: Rafael Broseghini.
Date: 02/12/2016

Filename: BroseghiniPayroll.py
'''
# Specify all the input.

name = input("Enter employee's name: ")

hrsWorked = float(input('Enter number of hours worked in a week: '))

payRate = float(input('Enter hourly pay rate: '))

#Formula for Gross Pay.

grossPay = hrsWorked*payRate

# Individual's input has to be divided by 100. Remember it is in percentage notation.

federalTaxRate = float(input('Enter federal tax withholding rate: '))/100

#Formula for Federal Deduction.

federalDeduction = grossPay*federalTaxRate

# Individual's input has to be divided by 100. Remember it is in percentage notation.

stateTaxRate = float(input('Enter state tax withholding rate: '))/100

#Formula for State Deduction.

stateDeduction = grossPay*stateTaxRate

#Look up on the Word document what is the medicare rate provided by Dr. Hardy.

medicareRate = 1.45/100

#Formula for medicare Deduction

medicareDeduction = grossPay*medicareRate

#Look up on the Word Document what is the social Security rate provided by Dr. Hardy.

socialSecurityRate = 6.2/100

#Formula for social Security deduction.

socialSecurityDeduction = grossPay*socialSecurityRate

#Formula for Total Deductions.

totalDeductions = (federalDeduction + stateDeduction + medicareDeduction + socialSecurityDeduction)

#Formula for Net Pay.

netPay = (grossPay - federalDeduction - stateDeduction - medicareDeduction - socialSecurityDeduction)

# Stethic spacing below for better visualizing.

print()
print()
print()
print()

# Look up the WordDocument and check the data order.

print('Employee Name:', name)

# REMEMBER TO ROUND HOURS WORKED TO ONE DECIMAL AND MONETARY VALUES TO TWO DECIMALS.

print('Hours Worked:', round(hrsWorked, 1))

print('Pay Rate: $', round(payRate, 2))

print('Gross Pay: $', round(grossPay, 2))

print('Deductions:')

# Figure out a way to add margin!!!

print('     ''Federal: $', round(federalDeduction, 2))

print('     ''State: $', round(stateDeduction, 2))

print('     ''Medicare: $', round(medicareDeduction, 2))

print('     ''Social Security: $', round(socialSecurityDeduction, 2))

print('     ''Total Deductions: $', round(totalDeductions, 2))

print('Net Pay: $', round(netPay, 2))

#
# Done!
