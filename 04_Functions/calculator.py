a = int(input("Enter a: "))
b = int(input("Enter b: "))

choice = int(input(
    "=== Calculator Menu ===\n"
    "1. Addition\n"
    "2. Subtraction\n"
    "3. Multiplication\n"
    "4. Division\n"
    "5. Exit\n"
    "Enter your choice: "
))
if choice == 1:
    print("Result:", a + b)

elif choice == 2:
    print("Result:", a - b)

elif choice == 3:
    print("Result:", a * b)

elif choice == 4:
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

elif choice == 5:
    print("Exiting Calculator...")

else:
    print("Invalid Choice")
