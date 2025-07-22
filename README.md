# Password Validator

A collection of beginner-friendly Python scripts that help validate password strength. These scripts check passwords against key security criteria and provide real-time feedback to ensure strong password creation.

## Features

- Minimum Length: Requires at least 8 characters
- Character Diversity: Ensures passwords contain:
  - At least one lowercase letter (a-z)
  - At least one uppercase letter (A-Z)  
  - At least one number (0-9)
  - At least one special character (!@#€%&/*?\$.)
- Clear Feedback: Provides specific error messages for each unmet requirement
- User-Friendly: Continuous validation loop until a strong password is entered

## Project Versions

This repository contains two different implementations of the password validator:

### Version 1: Basic Password Validator (`Password Validator.py`)

A simple, straightforward implementation using basic Python constructs. This version is ideal for beginners learning Python fundamentals.

**Key Characteristics:**
- Single file with linear code structure
- Direct variable checks using `any()` function
- Immediate error message printing
- Simple boolean logic for validation

**How to Use:**
1. Run the script:
   ```
   python "Password Validator.py"
   ```
2. Enter a password when prompted
3. Follow the feedback messages to create a strong password

**Example Output:**
```
Please enter a password (at least 8 characters, includes upper, lower, number, special): pass
❌ Password must be at least 8 characters long.
❌ Password must contain at least one uppercase letter.
❌ Password must contain at least one number.
❌ Password must contain at least one special character.

Please enter a password (at least 8 characters, includes upper, lower, number, special): MyPass123!
✅ Password accepted! Great Job :)
```

### Version 2: Function-Based Password Validator (`Password_validator_functions.py`)

A modular implementation using functions and better error handling. This version demonstrates good programming practices and code organization.

**Key Characteristics:**
- Modular design with separate validation functions
- Centralized error collection and handling
- Return tuple with validation status and messages
- More detailed and organized error reporting
- Includes period (.) as additional special character

**Functions Included:**
- `check_length(password)` - Validates minimum length requirement
- `check_has_lower(password)` - Checks for lowercase letters
- `check_has_upper(password)` - Checks for uppercase letters
- `check_has_digits(password)` - Validates presence of numbers
- `check_has_special_chars(password)` - Checks for special characters
- `password_validator(password)` - Main validation function that coordinates all checks

**How to Use:**
1. Run the script:
   ```
   python Password_validator_functions.py
   ```
2. Enter a password when prompted
3. View detailed error messages for any unmet requirements

**Example Output:**
```
Create your password: hello

Password requirements not met:
❌ Your password must contain at least 8 characters!
❌ Your password must contain at least one uppercase letter!
❌ Your password must contain at least one number!
❌ Your password must contain at least one special character!

Please try again.

Create your password: SecurePass1!
✅️ Your password is valid!
```

## Requirements

- Python 3.x
- No additional libraries required (uses built-in Python functions)

## Getting Started

1. Clone or download the repository
2. Navigate to the project directory
3. Choose which version you want to run:
   - For basic implementation: `python "Password Validator.py"`
   - For function-based implementation: `python Password_validator_functions.py`
4. Start creating strong passwords!

## Which Version Should You Use?

**Choose Version 1 (Basic) if:**
- You're new to Python programming
- You want to understand basic validation logic
- You prefer simple, linear code structure
- You're learning fundamental Python concepts

**Choose Version 2 (Function-Based) if:**
- You want to see modular programming practices
- You prefer organized, reusable code
- You're learning about function design and error handling
- You want to extend or modify the validation logic
