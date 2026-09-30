def main():
    while True:
        print("\nPython Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("Q. Quit")

        choice = input("Choose an option: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid option. Choose 1, 2, 3, 4, or Q.")
            continue

        try:
            first_number = float(input("Enter the first number: "))
            second_number = float(input("Enter the second number: "))
        except ValueError:
            print("Please enter valid numbers.")
            continue

        if choice == "1":
            result = first_number + second_number
        elif choice == "2":
            result = first_number - second_number
        elif choice == "3":
            result = first_number * second_number
        else:  # choice == "4"
            if second_number == 0:
                print("Cannot divide by zero.")
                continue
            result = first_number / second_number

        print(f"Result: {result}")


if __name__ == "__main__":
    main()