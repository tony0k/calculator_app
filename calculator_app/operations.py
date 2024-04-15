# operations.py

# Function to add 2 numbers
def add(x,y):
    return x + y

# Function to subtract 2 numbers
def subtract(x, y):
    return x - y

# Function to multiply 2 numbers
def multiply(x, y):
    return x * y

# Function to divide 2 numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

# Function to power x to the exponent y
def power(x, y):
    return x ** y


if __name__ == "__main__":
    print("I prefer to be a module!")