
Basic Python Math Operations

Default (GPT-3.5)

User
Simple python code for addition, substraction multiplication division

ChatGPT
Certainly! Here's a simple Python code snippet that performs addition, subtraction, multiplication, and division:

python
Copy code
# Addition
num1 = 5
num2 = 3
result_addition = num1 + num2
print("Addition result:", result_addition)

# Subtraction
result_subtraction = num1 - num2
print("Subtraction result:", result_subtraction)

# Multiplication
result_multiplication = num1 * num2
print("Multiplication result:", result_multiplication)

# Division
result_division = num1 / num2
print("Division result:", result_division)
Just replace the values of num1 and num2 with the numbers you want to perform these operations on, and the code will output the results for each operation.




User
Using while loop

ChatGPT
Certainly! Here's the same set of operations (addition, subtraction, multiplication, and division) using a while loop:

python
Copy code
# Initialize variables
num1 = 5
num2 = 3
operation = None

while operation != '5':
    print("Options:")
    print("Enter '1' for addition")
    print("Enter '2' for subtraction")
    print("Enter '3' for multiplication")
    print("Enter '4' for division")
    print("Enter '5' to exit")

    operation = input("Enter your choice: ")

    if operation == '1':
        result = num1 + num2
        print("Result:", result)
    elif operation == '2':
        result = num1 - num2
        print("Result:", result)
    elif operation == '3':
        result = num1 * num2
        print("Result:", result)
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Division by zero is not allowed.")
    elif operation == '5':
        print("Exiting the program")
    else:
        print("Invalid input. Please enter a valid option.")
