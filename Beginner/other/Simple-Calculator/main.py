def add(one, two):
    return one + two

def subtract(one, two):
    return one - two

def multiply(one, two):
    return one * two

def divide(one, two):
    if two == 0:
        return "Error: Division by zero is not allowed."
    return one / two

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calculator():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

    one = get_number("Enter the first number: ")
    two = get_number("Enter the second number: ")

    while True:
        user_input = input("Enter an operation (+, -, *, /) or 'q' to quit: ").strip()
        if user_input.lower() == 'q':
            print("Exiting the calculator. Goodbye!")
            break
        if user_input in operations:
            result = operations[user_input](one, two)
            print(f"Result: {result}")
        else:
            print("Invalid operation. Please enter one of (+, -, *, /).")

if __name__ == "__main__":
    calculator()
