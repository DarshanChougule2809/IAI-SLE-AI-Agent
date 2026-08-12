import datetime
import random

def greet_user():
    return "Hello! I am your Personal Assistant. How can I help you?"

def get_current_datetime():
    return datetime.datetime.now()

def get_motivation():
    quotes = [
        "Believe in yourself!",
        "Every day is a new opportunity.",
        "Keep learning and keep growing!",
        "Small steps lead to big achievements."
    ]
    return random.choice(quotes)

def main():
    print(greet_user())

    while True:
        print("\nChoose an option:")
        print("1. Get current date and time")
        print("2. Get a motivational quote")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current date and time:", get_current_datetime())

        elif choice == "2":
            print("Motivation:", get_motivation())

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
