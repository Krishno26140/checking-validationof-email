# Email Validator




## Overview

This project is a simple and structured Python application that validates email addresses using regular expressions. It is designed to demonstrate clean coding practices, modular design, and proper input handling while remaining easy to understand.

## Features

* Email validation using regular expressions
* Modular function-based design
* Input sanitization using `.strip()`
* Clear and readable code structure

## Technologies

* Python 3
* Standard library module: `re`

## How It Works

The program checks whether the input email matches the following pattern:

```text
[a-zA-Z0-9_.+]+@[a-zA-Z]+\.[a-z]{3}
```

### Pattern Explanation

* `[a-zA-Z0-9_.+]+` : Username (letters, numbers, dot, underscore, plus)
* `@` : Required separator
* `[a-zA-Z]+` : Domain name (letters only)
* `\.` : Literal dot
* `[a-z]{3}` : Domain extension (e.g., com, net)

## Getting Started

### Prerequisites

* Python 3 installed on your system

### Installation and Execution

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/email-validator.git
   ```

2. Navigate to the project directory:

   ```bash
   cd email-validator
   ```

3. Run the program:

   ```bash
   python email_validator.py
   ```

## Usage Example

**Input:**

```text
test@gmail.com
```

**Output:**

```text
Email is valid
```

## Project Structure

```text
email-validator/
│
├── email_validator.py
└── README.md
```

## Limitations

* Only supports three-letter domain extensions
* Does not cover all valid real-world email formats

## Future Enhancements

* Support for multiple domain extensions (e.g., `.in`, `.org`)
* Extended validation rules for real-world scenarios
* Integration with additional input validators (phone, password)
* Conversion to a web-based interface

## Author

Subhradeep Sardar
BCA Student

##
