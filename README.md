Sure — since your project is the **Personal Assistant Agent** with greeting, date/time, and motivational quotes, here is a README in the same format as your example.

# AI-SLE

# Personal Assistant AI Agent

## Course

**02UAML204 - Introduction to Artificial Intelligence**

## Objective

The objective of this project is to demonstrate an AI-augmented coding workflow using **GitHub Copilot**.

The project implements a simple Python-based Personal Assistant Agent that can interact with the user and perform basic tasks such as greeting the user, providing the current date and time, and displaying motivational quotes.

## AI Tool Used

**GitHub Copilot Chat**

## Technologies

* Python
* Visual Studio Code
* Git
* GitHub
* GitHub Copilot

## Features

* Greeting the user
* Displaying the current date and time
* Providing motivational quotes
* Randomly selecting motivational quotes
* Continuous interaction using a menu
* Invalid menu choice handling
* Exit option

## Agent Workflow

The agent displays a menu and receives the user's choice. Based on the selected option, it identifies the appropriate predefined task, performs the operation, and displays the result.

### Example 1 - Greeting

```text
Hello! I am your Personal Assistant. How can I help you?
```

### Example 2 - Date and Time

```text
User: 1

Agent: Current date and time: 2026-08-12 14:10:00
```

### Example 3 - Motivational Quote

```text
User: 2

Agent: Motivation: Believe in yourself!
```

The motivational quote is selected randomly from a predefined list, so the agent can display different quotes each time.

### Example 4 - Invalid Choice

```text
User: 5

Agent: Invalid choice. Please try again.
```

### Example 5 - Exit

```text
User: 3

Agent: Goodbye!
```

## Functions

### `greet_user()`

Returns a friendly greeting message to the user.

### `get_current_datetime()`

Uses the Python `datetime` module to provide the current date and time.

### `get_motivation()`

Stores multiple motivational quotes in a list and uses the Python `random` module to randomly select and return one quote.

### `main()`

Controls the main program, displays the menu, accepts user input, and calls the appropriate functions based on the user's choice.

## Python Modules Used

### `datetime`

The `datetime` module is used to obtain the current date and time.

```python
import datetime
```

### `random`

The `random` module is used to randomly select a motivational quote from the list.

```python
import random
```

## How to Run

Open the project folder in **Visual Studio Code** and run:

```bash
python agent.py
```

The program will display:

```text
Hello! I am your Personal Assistant. How can I help you?

Choose an option:
1. Get current date and time
2. Get a motivational quote
3. Exit

Enter your choice:
```

Choose an option and follow the instructions displayed by the agent.

## Error Handling

The program handles invalid menu choices and displays an appropriate error message:

```text
Invalid choice. Please try again.
```

The program continues running after an invalid choice and allows the user to select another option.

## Project Structure

```text
Personal-Assistant-AI-Agent/
│
├── agent.py
└── README.md
```

## AI Contribution

GitHub Copilot Chat was used during the development of this project to assist with:

* Creating the greeting function
* Creating the date and time function
* Creating the motivational quote function
* Adding the `random` module
* Creating the list of motivational quotes
* Creating the main menu
* Adding user input handling
* Adding the program exit condition
* Adding invalid choice handling
* Identifying syntax and indentation issues
* Suggesting corrections and improvements
* Assisting with testing and debugging

The AI-generated code was **reviewed, tested, corrected, and verified** to ensure that the final program worked correctly.

## My Contribution

My contribution to the project included:

* Providing requirements and prompts to GitHub Copilot
* Reviewing AI-generated code
* Integrating the generated functions
* Correcting syntax and indentation errors
* Testing all program features
* Testing the date and time functionality
* Testing motivational quote generation
* Testing random quote selection
* Testing invalid inputs
* Verifying the exit functionality
* Preparing and documenting the final project

## Learning Outcomes

Through this project, I learned and practiced:

* Python functions
* Conditional statements
* `while` loops
* User input and output
* Python modules
* `datetime` module
* `random` module
* Lists
* Random selection
* Menu-driven programming
* AI-assisted programming
* Code testing and debugging
* Reviewing and validating AI-generated code

## Conclusion

This project demonstrates the development of a simple **Personal Assistant AI Agent** using **Python and GitHub Copilot Chat** as an AI-assisted coding tool.

The agent can **greet the user, provide the current date and time, display randomly selected motivational quotes, handle invalid menu choices, and exit the program when requested**.

Through this project, I gained practical knowledge of **Python functions, conditional statements, loops, user input, output statements, lists, modules, the `datetime` module, and the `random` module**. I also learned how to use **GitHub Copilot Chat** to generate code, suggest solutions, identify errors, and assist with debugging.

The project followed an **AI-augmented coding workflow**, where AI-generated code was reviewed, tested, corrected, and verified by me. This helped demonstrate the importance of understanding and validating AI-generated code rather than depending on it completely.

Overall, the project successfully demonstrates how **Python and AI coding tools can be combined to develop a simple interactive Personal Assistant Agent that performs useful basic tasks**.
