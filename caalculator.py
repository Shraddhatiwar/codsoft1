def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    return a % b

def exponentiation(a, b):
    return a ** b

def calculator():
    while True:
        print("\nCalculator Menu:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Exponentiation (^)")
        print("7. Exit")

        # Get user choice
        choice = input("\nEnter the number of the operation you want to perform (1-7): ")

        # Exit condition
        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        # Validate choice
        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid choice! Please select a valid option.")
            continue

        # Input numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform operation
        if choice == '1':
            print(f"The result of addition: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of subtraction: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of multiplication: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"The result of division: {divide(num1, num2)}")
        elif choice == '5':
            print(f"The result of modulus: {modulus(num1, num2)}")
        elif choice == '6':
            print(f"The result of exponentiation: {exponentiation(num1, num2)}")

# Run the calculator project
if __name__ == "__main__":
    calculator()
