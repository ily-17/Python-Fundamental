from calculator.operations import (
    add,
    subtract,
    multiply,
    divide
)

from calculator.utils import display_menu


def main():

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(a, b))

            elif choice == "2":
                print("Result:", subtract(a, b))

            elif choice == "3":
                print("Result:", multiply(a, b))

            elif choice == "4":
                print("Result:", divide(a, b))

        except ValueError:
            print("Please enter valid numbers.")


if __name__ == "__main__":
    main()
