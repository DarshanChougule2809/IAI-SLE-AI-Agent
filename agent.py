import random

def greet_user():
    return "Hello! I am your Study Assistant. How can I help you?"

def calculate_percentage():
    marks = []

    print("\nEnter marks of 5 subjects:")
    for i in range(5):
        mark = float(input(f"Enter marks for subject {i + 1}: "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    print("Total Marks:", total)
    print("Percentage:", percentage, "%")

    if percentage >= 75:
        print("Result: Excellent performance!")
    elif percentage >= 60:
        print("Result: Very good performance!")
    elif percentage >= 40:
        print("Result: You passed. Keep improving!")
    else:
        print("Result: Need more practice.")


def get_study_tip():
    tips = [
        "Study for 25 minutes and take a 5-minute break.",
        "Make short notes while studying.",
        "Practice previous question papers.",
        "Revise difficult topics regularly.",
        "Keep your phone away while studying."
    ]

    return random.choice(tips)


def simple_calculator():
    print("\nSimple Calculator")
    
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero.")

    else:
        print("Invalid operator.")


def main():
    print(greet_user())

    while True:
        print("\nChoose an option:")
        print("1. Calculate Percentage")
        print("2. Get Study Tip")
        print("3. Use Calculator")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculate_percentage()

        elif choice == "2":
            print("Study Tip:", get_study_tip())

        elif choice == "3":
            simple_calculator()

        elif choice == "4":
            print("Goodbye! Keep studying!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
