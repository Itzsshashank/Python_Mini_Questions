num1 = float(input("First Number: "))
num2 = float(input("Second Numer: "))
operation = input("Select operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
    print("The Addition of two numbers is:", result)
elif operation == '-':
    result = num1 - num2
    print("The Subtraction of two numbers is:", result)
elif operation == '*':
    result = num1 * num2
    print("The Product of two numbers is:", result)
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("The Division of two numbers is:", result)
else:
    print("Invalid operation. Please select a valid operation: +, -, *, /")

try:
    pass
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
