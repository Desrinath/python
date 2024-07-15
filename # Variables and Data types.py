def calculator():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter your choice: ")

    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))

    if choice == "1":
        r = "ADDITION"
        operation = number1 + number2
    elif choice == "2":
        r = "SUBTRACTION"
        operation = number1 - number2
    elif choice == "3":
        r = "MULTIPLICATION"
        operation = number1 * number2
    elif choice == "4":
        r = "DIVISION"
        operation = number1 / number2
    else:
        print("Enter a choice between 1 to 4")
        return

    print(f"{r} answer: {operation}")

calculator()
