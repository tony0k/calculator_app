# factorial.py

# Function to calculate the factorial of a number
def factorial(x):
    if x < 0:
        return "Error! Factorial of a negative doesn't exist! Idiot!"
    elif x == 0:
        return 1
    else:
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
    