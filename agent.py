import random

# ============================================================
# SLE-1: STUDY ASSISTANT AI AGENT
# ============================================================

def greet_user():
    return "Hello! I am your Study Assistant. How can I help you?"


# ============================================================
# CALCULATE PERCENTAGE
# ============================================================

def calculate_percentage():

    marks = []

    print("\nEnter marks of 5 subjects (0-100):")

    for i in range(5):

        while True:

            try:
                mark = float(
                    input(f"Enter marks for subject {i + 1}: ")
                )

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                else:
                    print(
                        "Please enter marks between 0 and 100."
                    )

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / 5

    print("\nTotal Marks:", total)
    print("Percentage:", f"{percentage:.2f}%")

    if percentage >= 75:
        print("Result: Excellent performance!")

    elif percentage >= 60:
        print("Result: Very good performance!")

    elif percentage >= 40:
        print("Result: You passed. Keep improving!")

    else:
        print("Result: Need more practice.")


# ============================================================
# STUDY TIP
# ============================================================

def get_study_tip():

    tips = [
        "Study for 25 minutes and take a 5-minute break.",
        "Make short notes while studying.",
        "Practice previous question papers.",
        "Revise difficult topics regularly.",
        "Keep your phone away while studying."
    ]

    return random.choice(tips)


# ============================================================
# SIMPLE CALCULATOR
# ============================================================

def simple_calculator():

    print("\nSimple Calculator")

    try:

        num1 = float(
            input("Enter first number: ")
        )

        operator = input(
            "Enter operator (+, -, *, /): "
        )

        num2 = float(
            input("Enter second number: ")
        )

        if operator == "+":

            result = num1 + num2

        elif operator == "-":

            result = num1 - num2

        elif operator == "*":

            result = num1 * num2

        elif operator == "/":

            if num2 == 0:
                print("Cannot divide by zero.")
                return

            result = num1 / num2

        else:

            print("Invalid operator.")
            return

        print("Result:", result)

    except ValueError:

        print("Please enter valid numbers.")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    print(greet_user())

    while True:

        print("\n" + "=" * 45)
        print("             STUDY ASSISTANT")
        print("=" * 45)

        print("1. Calculate Percentage")
        print("2. Get Study Tip")
        print("3. Use Calculator")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            calculate_percentage()

        elif choice == "2":

            print("\nStudy Tip:", get_study_tip())

        elif choice == "3":

            simple_calculator()

        elif choice == "4":

            print("\nGoodbye! Keep studying!")
            break

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()
