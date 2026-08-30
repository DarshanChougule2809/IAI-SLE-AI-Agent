# Contribution Log

## Project Name

**Study Assistant AI Agent**

## Project Description

The Study Assistant AI Agent is a Python-based interactive assistant designed to help students with basic academic activities such as calculating percentage, providing study tips, and performing simple calculations.

---

## Step-by-Step Contribution Log

### Step 1 – Project Planning

**Work Done:**

* Decided to create a simple AI-agent-style project.
* Selected the **Study Assistant** as the project topic.
* Identified the basic functions required.

**Features Planned:**

* Welcome message
* Percentage calculation
* Random study tips
* Simple calculator
* Exit option

---

### Step 2 – Created the Python File

**Work Done:**

* Created the main Python source file.
* Named the file:

```text
study_assistant.py
```

* Prepared the basic program structure.

---

### Step 3 – Imported Required Module

**Work Done:**

* Imported the `random` module.
* The module is used to select a random study tip.

```python
import random
```

---

### Step 4 – Created Greeting Function

**Work Done:**

* Created the `greet_user()` function.
* Added a welcome message for the user.

```python
def greet_user():
    return "Hello! I am your Study Assistant. How can I help you?"
```

---

### Step 5 – Created Percentage Calculation

**Work Done:**

* Created the `calculate_percentage()` function.
* Added input for five subjects.
* Stored marks using a list.
* Calculated total marks.
* Calculated percentage.
* Added performance messages.

**Performance Levels:**

```text
75% and above  → Excellent performance
60%–74%        → Very good performance
40%–59%        → Passed
Below 40%      → Need more practice
```

---

### Step 6 – Created Study Tip Function

**Work Done:**

* Created a list containing different study tips.
* Used `random.choice()` to select one tip.
* Created the `get_study_tip()` function.

Example tips include:

```text
Study for 25 minutes and take a 5-minute break.
Make short notes while studying.
Practice previous question papers.
Revise difficult topics regularly.
Keep your phone away while studying.
```

---

### Step 7 – Created Calculator Function

**Work Done:**

* Created the `simple_calculator()` function.
* Added two number inputs.
* Added operator input.
* Implemented basic arithmetic operations.

**Supported Operators:**

```text
+  Addition
-  Subtraction
*  Multiplication
/  Division
```

* Added a condition to prevent division by zero.

---

### Step 8 – Created Main Menu

**Work Done:**

* Created the `main()` function.
* Added a continuous `while` loop.
* Created a menu for selecting different operations.

```text
1. Calculate Percentage
2. Get Study Tip
3. Use Calculator
4. Exit
```

---

### Step 9 – Added User Choice Handling

**Work Done:**

* Used `if-elif-else` statements to process the user's choice.
* Connected each menu option to its corresponding function.
* Added an invalid-choice message.

---

### Step 10 – Added Exit Functionality

**Work Done:**

* Added option 4 to exit the program.
* Used the `break` statement to terminate the loop.
* Added a goodbye message.

```text
Goodbye! Keep studying!
```

---

### Step 11 – Added Main Program Check

**Work Done:**

* Added the standard Python entry-point condition.

```python
if __name__ == "__main__":
    main()
```

* This ensures that the `main()` function runs when the file is executed directly.

---

### Step 12 – Tested Percentage Feature

**Testing Done:**

* Entered different marks for five subjects.
* Checked the total marks.
* Checked the percentage calculation.
* Tested different performance categories.

**Result:**

* Percentage was calculated correctly.
* Performance message was displayed correctly.

---

### Step 13 – Tested Study Tip Feature

**Testing Done:**

* Selected the Study Tip option multiple times.
* Verified that tips were selected randomly.

**Result:**

* Different study tips were displayed successfully.

---

### Step 14 – Tested Calculator

**Testing Done:**

* Tested addition.
* Tested subtraction.
* Tested multiplication.
* Tested division.
* Tested division by zero.

**Result:**

* Arithmetic operations worked correctly.
* Division by zero was handled safely.

---

### Step 15 – Tested Invalid Input Choice

**Testing Done:**

* Entered an invalid menu option.

Example:

```text
Enter your choice: 8
```

**Result:**

```text
Invalid choice. Please try again.
```

---

### Step 16 – Final Testing

**Work Done:**

* Tested all menu options together.
* Checked that the program returns to the main menu after completing an operation.
* Verified that the Exit option terminates the program.

**Result:**

* All implemented features worked successfully.

---

## Conclusion

The Study Assistant AI Agent was developed step by step by first planning the required features, creating individual functions, integrating them through a menu-driven system, and finally testing each feature. The final program provides a simple and interactive student assistant using Python.
