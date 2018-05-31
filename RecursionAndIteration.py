'''
Name: Rafael Broseghini
Prof: Roman Yasinovskyy

Course: CS-160
Date: 03/18/2017
'''
def iterative_fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
        print(a)

def recursive_fibonacci(n):
   if n <= 1:
       return n
   else:
       return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))


try:
   
   numbers = 11

   if numbers <= 0:
      print("Plese enter a integer greater than 0.")
   else:
      print("Fibonacci sequence using recursive method:")
      for i in range(numbers):
         print(recursive_fibonacci(i))
         
except Exception as ie:
   print('Must be an integer.\n')

print('\nFibonacci sequence using iterative method')
iterative_fibonacci(10)



def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n-1)
n = 10
print('\n\nFactorial of every number from 1 to 10 using recursive method:\n')
for i in range(1, n+1):
    print('Recursive factorial of ' + str(i) + ':')  
    print(recursive_factorial(i))

print("\n")

def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product

for i in range(1, 11):
    print('Iterative factorial of ' + str(i) + ':')
    print(factorial(i))

print()
print()
def multiples3(n):
    if n == 1:
        return 3
    else:
        return multiples3(n-1) + 3
    
for i in range(1, 10+1):
    print('Number ' + str(i) + ' multiple of 3 is: ')
    print(multiples3(i))
