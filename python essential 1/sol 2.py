try:
    # Take user inputs
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))

    # Check if age is negative
    if age < 0:
        print("Age cannot be negative")
    else:
        # String concatenation for full name
        full_name = first_name + " " + last_name
        print("Full Name: " + full_name)

        # Age next year
        print("You will be " + str(age + 1) + " next year")

except ValueError:
    print("Invalid age input")
