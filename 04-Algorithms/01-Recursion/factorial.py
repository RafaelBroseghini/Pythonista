# Recursive function to compute the factorial of a given n

def factorial(n):
    # Base case
    if n == 0:
        return 1
    #Recursive call, moving towards the base case (n-1).
    return factorial(n-1) * n

print("Factorial of 1 is:", factorial(1))
print("Factorial of 2 is:", factorial(2))
print("Factorial of 3 is:", factorial(3))
print("Factorial of 10 is:", factorial(10))
print("Factorial of 30 is:", factorial(30))
print("Factorial of 50 is:", factorial(50))