try:
    # Take user input
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Check negative age
    if age < 0:
        print("Age cannot be negative")
    else:
        print("Hello " + name)

        # Age category
        if age < 13:
            print("You are a Child")
        elif 13 <= age <= 17:
            print("You are a Teenager")
        elif 18 <= age <= 59:
            print("You are an Adult")
        else:
            print("You are a Senior Citizen")

        # Voting eligibility
        if age >= 18:
            print("You are eligible to vote")
        else:
            print("You are not eligible to vote")

except ValueError:
    print("Invalid age input")
