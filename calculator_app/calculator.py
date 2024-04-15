# calculator.py
import sys

sys.path.append('C:\\Users\\tonyp\\repos\calculator_app')

from operations import add, subtract, multiply, divide, power
from factorial import factorial

# Main function to run the calculator
def main():
    print("Welcome to the calculator app!")

    while True:
        print("\nOperations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exponentiation")
        print("6. Factorial")
        print("7. Quit")

        choice = input("Enter operation number (1 - 7):")

        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
            if choice == '1':
                print(f'Result: {add(num1,num2)}')
            elif choice == '2':
                print(f'Result: {subtract(num1, num2)}')
            elif choice == '3':
                print(f'Result: {multiply(num1, num2)}')
            elif choice == '4':
                print(f'Result: {divide(num1, num2)}')
            elif choice == '5':
                print(f'Result: {power(num1, num2)}')
        elif choice == '6':
            num = int(input("Enter a number: "))
            print(f'Result: {factorial(num)}')
        elif choice == '7':
            print('Thank you for using the calculator, goodbye!')
            break
        else:
            print('Invalid input. Please enter a number between 1 and 7.')

# Run the calculator
if __name__ == '__main__':
    main()