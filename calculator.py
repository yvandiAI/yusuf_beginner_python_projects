def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def power(a, b):
    return a ** b


def calculator():
    print("----- SIMPLE PYTHON CALCULATOR -----")
    print("Options: add | subtract | multiply | divide | power | quit")

    while True:
        choice = input("\nEnter operation: ").lower()

        if choice == "quit":
            print("Exiting Calculator")
            break

        if choice not in ["add", "subtract", "multiply", "divide", "power"]:
            print("Invalid Choice. Try again.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        try:
            if choice == "add":
                result = add(num1, num2)
            elif choice == "subtract":
                result = subtract(num1, num2)
            elif choice == "multiply":
                result = multiply(num1, num2)
            elif choice == "divide":
                result = divide(num1, num2)
            elif choice == "power":
                result = power(num1, num2)

            print(f"Result: {result}")

        except ZeroDivisionError as e:
            print(e)


if __name__ == "__main__":
    calculator()
