def calculator():
    """
    A basic calculator program that takes two numbers and an operator as input
    and displays the result of the operation.
    """
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Prompt the user to enter an operator
    operator = input("Enter an operator (+, -, *, /, %): ")

    # Perform the operation based on the operator
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    elif operator == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            print("Error: Modulus by zero is not allowed.")
            return
    else:
        print("Error: Invalid operator. Please enter +, -, *, /, or %.")
        return

    # Display the result
    print(f"The result of the operation is: {result}")

# Call the calculator function
calculator()