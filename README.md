# Study Assistant AI Agent

## 1. Project Title

**Study Assistant AI Agent**

## 2. Project Description

The **Study Assistant AI Agent** is a simple Python-based interactive assistant designed to help students with basic academic tasks.

The program provides a menu-driven interface where the user can select different options. It can calculate the percentage of marks, provide random study tips, and perform basic mathematical calculations.

This project demonstrates the use of **Python functions, loops, conditional statements, lists, user input, and the random module**.

## 3. Features

The Study Assistant provides the following features:

1. **Calculate Percentage**

   * Accepts marks for five subjects.
   * Calculates total marks.
   * Calculates the percentage.
   * Displays a performance message based on the percentage.

2. **Get Study Tip**

   * Provides a random study tip.
   * Helps students develop better study habits.

3. **Simple Calculator**

   * Performs basic mathematical operations.
   * Supports:

     * Addition (`+`)
     * Subtraction (`-`)
     * Multiplication (`*`)
     * Division (`/`)
   * Prevents division by zero.

4. **Exit**

   * Allows the user to safely exit the program.

## 4. Technologies Used

* **Programming Language:** Python
* **Module Used:** `random`
* **Interface:** Command Line / Terminal

## 5. Requirements

To run this project, you need:

* Python 3.x
* A text editor or Python IDE
* Terminal or Command Prompt

No external libraries are required.

## 6. How to Run

### Step 1: Save the Program

Save the Python program with a `.py` extension.

Example:

```text
study_assistant.py
```

### Step 2: Open Terminal

Open Terminal or Command Prompt and navigate to the folder containing the Python file.

### Step 3: Run the Program

Use the following command:

```bash
python study_assistant.py
```

If your system uses `python3`, use:

```bash
python3 study_assistant.py
```

## 7. How the Program Works

When the program starts, it displays a greeting:

```text
Hello! I am your Study Assistant. How can I help you?
```

A menu is then displayed:

```text
1. Calculate Percentage
2. Get Study Tip
3. Use Calculator
4. Exit
```

The user enters a choice.

### Option 1: Calculate Percentage

The program asks for marks in five subjects.

For example:

```text
Subject 1: 80
Subject 2: 75
Subject 3: 85
Subject 4: 70
Subject 5: 90
```

It calculates:

```text
Total Marks: 400
Percentage: 80.0 %
Result: Excellent performance!
```

### Option 2: Get Study Tip

The program randomly selects a study tip from a predefined list.

Example:

```text
Study Tip: Practice previous question papers.
```

### Option 3: Calculator

The user enters two numbers and an operator.

Example:

```text
Enter first number: 20
Enter operator: *
Enter second number: 5

Result: 100
```

### Option 4: Exit

The program displays:

```text
Goodbye! Keep studying!
```

and terminates.

## 8. Functions Used

The project is divided into separate functions to make the program simple and organized.

### `greet_user()`

Displays the welcome message.

### `calculate_percentage()`

Accepts marks and calculates the total and percentage.

### `get_study_tip()`

Selects and returns a random study tip.

### `simple_calculator()`

Performs basic arithmetic operations.

### `main()`

Controls the main menu and connects all the functions.

## 9. Concepts Demonstrated

This project demonstrates the following Python concepts:

* Variables
* Functions
* Lists
* `if-elif-else` statements
* `while` loop
* `for` loop
* User input
* Arithmetic operators
* Random selection
* Error handling using conditions
* Modular programming

## 10. Example Output

```text
Hello! I am your Study Assistant. How can I help you?

Choose an option:
1. Calculate Percentage
2. Get Study Tip
3. Use Calculator
4. Exit

Enter your choice: 2

Study Tip: Make short notes while studying.
```

## 11. Advantages

* Simple and easy to use.
* Beginner-friendly Python project.
* Provides multiple useful functions.
* Uses a menu-driven interface.
* Does not require external packages.
* Demonstrates basic concepts of an AI-agent-style assistant.

## 12. Future Improvements

The Study Assistant can be improved by adding:

* Student timetable management.
* To-do list functionality.
* Subject-wise study planning.
* Quiz and question-answer features.
* Reminder functionality.
* Grade prediction.
* Voice input and output.
* Integration with an actual AI model.
* Database support for storing student information.

## 13. Conclusion

The **Study Assistant AI Agent** is a simple Python project that demonstrates how an interactive assistant can perform different tasks based on user input. It combines functions, loops, conditions, lists, and the random module to provide useful student-oriented features.

The project can also be expanded in the future by adding more advanced AI features, making it a more powerful personal learning assistant.
