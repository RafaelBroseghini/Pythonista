'''
CS 150 B LAB 02.

Purpose: Write a program that simulates a vending machine mode of operation.

Author: Rafael Broseghini.

Date: 

Filename: broseghini_Lab2Change.py
'''
money_inserted = float(input('Enter value of money inserted: ')) # Money has decimals therefore has to be a float statement.

item_price = float(input('Enter item price: '))

change = round(money_inserted - item_price, 2) # Before rounding the float(input) statement, python was giving different answers for the same amount of change. I would input 1.00 (money) and .40(item price) therefore change being .60 it would give me back 2 quarters and one dime (correct answer), but when I input 10.00 (money) and 9.40 (item price) therefore change being .60 python would give me back 2 quarters and one nickel (wrong answer).

change_print = ('Change: $') # Formulas are easier to insert in formatting later.

dollar_coins_print = ('Dollar coin(s):')

quarters_print = ('Quarter(s):')

dimes_print = ('Dime(s):')

nickels_print = ('Nickel(s):')

print('%-s %2.2f' %(change_print, change)) # Float statement with two decimals.

# Scribble calculations in a sheet of paper. 

dollar_coins = (change*100)//100 # Think in pennies. 

quarters = ((change*100)%100)//25 # Basically aplly a chain rule in which you turn the previous // into % and divide (//) by the assigned coin value.

dimes = (((change*100)%100)%25)//10 

nickels = ((((change*100)%100)%25)%10)//5 

# 'Old' formatting.

print('      %-18s %2d' %(dollar_coins_print, dollar_coins))

print('      %-18s %2d' %(quarters_print, quarters))

print('      %-18s %2d' %(dimes_print, dimes))

print('      %-18s %2d' %(nickels_print, nickels))

# Done!!
