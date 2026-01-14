# Calculator

def add(a, b):
    return a + b    
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
def power(a, b):
    return a ** b
def modulus(a, b):
    return a % b

def my_choices():
     print("Select operation:")
     print("1. Add")
     print("2. Subtract")
     print("3. Multiply")
     print("4. Divide")
     print("5. View Stored Values")
     print("Type 'End' to exit")

print("Welcome to the simple calculator")
name = input("Enter your name: ").title().strip()

stored_value = []
flag = True
while flag:
    print(f"Hello {name}! Please select an operation:")
    my_choices()
    choice = input("Enter choice (1/2/3/4 or 'End'): ")
    if choice == '1':
        first_number = input("Enter first number: ")
        second_number = input("Enter second number: ")
        print('result: ', add(int(first_number), int(second_number)))
        stored_value.append(add(int(first_number), int(second_number)))
    elif choice == '2':
        first_number = input("Enter first number: ")
        second_number = input("Enter second number: ")
        print('result: ', subtract(int(first_number), int(second_number)))
        stored_value.append(subtract(int(first_number), int(second_number)))
    elif choice == '3':
        first_number = input("Enter first number: ")
        second_number = input("Enter second number: ")
        print('result: ', multiply(int(first_number), int(second_number)))
        stored_value.append(multiply(int(first_number), int(second_number)))
    elif choice == '4':
        try:
            print('result: ', divide(int(first_number), int(second_number)))
            stored_value.append(divide(int(first_number), int(second_number)))
        except ValueError as e:
            print("Error:", e)
    elif choice == '5':
        stored_flag = True
        while stored_flag:
             print("Stored values:", stored_value)
             my_choices()
             stored_operations = input("Enter choice 1/2/3/4 or 'End' for stored operations: ")
             if stored_operations.lower() == 'end':
                print("So long, fairwell, Au revior!")
                stored_flag = False
             elif stored_operations == '1':
                result = sum(stored_value)
                print("Sum of stored values:", result)
             elif stored_operations == '2':
                result = subtract(int(stored_value[0]), int(stored_value[1]))
                print("Subtraction of stored values:", result)
             elif stored_operations == '3':
                result = multiply(int(stored_value[0]), int(stored_value[1]))
                print("Multiplication of stored values:", result)
             elif stored_operations == '4':
                try:
                    result = divide(int(stored_value[0]), int(stored_value[1]))
                    print("Division of stored values:", result)
                except ValueError as e:
                    print("Error:", e)
             else:
                print("Invalid input")
    elif choice.lower() == 'end':
        print("Goodbye and thanks for all the fish!")
        flag = False
    else:
        print("Invalid input")
