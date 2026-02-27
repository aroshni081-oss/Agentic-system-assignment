try:
    
    # Take input from user
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Print sum
    print("Sum:", num1 + num2)

    # Check division
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        print("Division:", num1 / num2)

except ValueError:
    print("Invalid input")
