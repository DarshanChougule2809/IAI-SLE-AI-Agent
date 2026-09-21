import random
import timeit
import statistics


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


# ---------------------------------------------------------
# SLE-2 PROFILING
# ---------------------------------------------------------

def run_profiling():
    print("\n======================================")
    print("       SLE-2 PROFILING")
    print("======================================")

    # Same input data for both versions
    marks = (80, 75, 85, 70, 90)

    # -----------------------------------------------------
    # Version A: Original Method
    # Creates a new list and uses append()
    # -----------------------------------------------------
    def original_percentage():
        mark_list = []

        for mark in marks:
            mark_list.append(mark)

        total = sum(mark_list)
        percentage = total / 5

        return percentage

    # -----------------------------------------------------
    # Version B: Optimized Method
    # Directly uses sum() on the existing data
    # -----------------------------------------------------
    def optimized_percentage():
        total = sum(marks)
        percentage = total / 5

        return percentage

    # -----------------------------------------------------
    # Check that both versions give the same result
    # -----------------------------------------------------

    original_result = original_percentage()
    optimized_result = optimized_percentage()

    print("\nTest Data:", marks)

    print("Original Result:", original_result, "%")
    print("Optimized Result:", optimized_result, "%")

    if original_result == optimized_result:
        print("Result Check: Both versions give the same result.")
    else:
        print("Result Check: Results are different.")

    # -----------------------------------------------------
    # Profiling settings
    # -----------------------------------------------------

    runs = 5
    iterations = 1000000

    original_times = []
    optimized_times = []

    print("\n--------------------------------------")
    print("Running Profiling...")
    print("--------------------------------------")

    # -----------------------------------------------------
    # Run profiling multiple times
    # -----------------------------------------------------

    for i in range(runs):

        original_time = timeit.timeit(
            original_percentage,
            number=iterations
        )

        optimized_time = timeit.timeit(
            optimized_percentage,
            number=iterations
        )

        original_times.append(original_time)
        optimized_times.append(optimized_time)

        print(f"\nRun {i + 1}")
        print(f"Original Time  : {original_time:.6f} seconds")
        print(f"Optimized Time : {optimized_time:.6f} seconds")

    # -----------------------------------------------------
    # Calculate average execution time
    # -----------------------------------------------------

    avg_original = statistics.mean(original_times)
    avg_optimized = statistics.mean(optimized_times)

    # -----------------------------------------------------
    # Convert average time into milliseconds
    # -----------------------------------------------------

    original_ms = (avg_original / iterations) * 1000
    optimized_ms = (avg_optimized / iterations) * 1000

    # -----------------------------------------------------
    # Calculate performance improvement
    # -----------------------------------------------------

    if avg_original != 0:
        improvement = (
            (avg_original - avg_optimized)
            / avg_original
        ) * 100
    else:
        improvement = 0

    # -----------------------------------------------------
    # Display Final Results
    # -----------------------------------------------------

    print("\n======================================")
    print("          FINAL RESULTS")
    print("======================================")

    print(f"Average Original Time   : {avg_original:.6f} seconds")
    print(f"Average Optimized Time  : {avg_optimized:.6f} seconds")

    print(
        f"Original Time/Execution : "
        f"{original_ms:.9f} ms"
    )

    print(
        f"Optimized Time/Execution: "
        f"{optimized_ms:.9f} ms"
    )

    print(
        f"Performance Improvement : "
        f"{improvement:.2f}%"
    )

    # -----------------------------------------------------
    # Comparison
    # -----------------------------------------------------

    print("\n======================================")
    print("          COMPARISON")
    print("======================================")

    print("Version A: Original method")
    print("- Creates a new list")
    print("- Uses a for loop")
    print("- Uses append()")
    print("- Uses sum()")

    print("\nVersion B: Optimized method")
    print("- Uses the existing data directly")
    print("- Does not create another list")
    print("- Directly uses sum()")

    # -----------------------------------------------------
    # Conclusion
    # -----------------------------------------------------

    print("\n======================================")
    print("           CONCLUSION")
    print("======================================")

    if avg_optimized < avg_original:
        print("Optimized version is faster.")
        print("It avoids unnecessary list creation and append operations.")
    elif avg_optimized > avg_original:
        print("Original version is faster in this profiling run.")
    else:
        print("Both versions have nearly the same execution time.")

    print("\nSLE-2 profiling completed successfully.")


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main():

    print(greet_user())

    while True:

        print("\n======================================")
        print("          STUDY ASSISTANT")
        print("======================================")

        print("1. Calculate Percentage")
        print("2. Get Study Tip")
        print("3. Use Calculator")
        print("4. Run SLE-2 Profiling")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            calculate_percentage()

        elif choice == "2":
            print("\nStudy Tip:", get_study_tip())

        elif choice == "3":
            simple_calculator()

        elif choice == "4":
            run_profiling()

        elif choice == "5":
            print("\nGoodbye! Keep studying!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
