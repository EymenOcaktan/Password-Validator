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
- Two Implementations: Basic version and modular function-based version

## Files Included

- `Password Validator.py` - Simple, straightforward implementation
- `Password_validator_functions.py` - Modular version with separate validation functions

## How to Use

### Method 1: Basic Version
1. Run `Password Validator.py` using Python:
   ```
   python "Password Validator.py"
   ```
2. Enter a password when prompted
3. Follow the feedback messages to create a strong password
4. Receive confirmation when password meets all criteria

### Method 2: Function-Based Version
1. Run `Password_validator_functions.py` using Python:
   ```
   python Password_validator_functions.py
   ```
2. Enter a password when prompted
3. View detailed error messages for any unmet requirements
4. Continue until password passes all validations

## Example Output

### Weak Password Example
```
Please enter a password (at least 8 characters, includes upper, lower, number, special): pass
❌ Password must be at least 8 characters long.
❌ Password must contain at least one uppercase letter.
❌ Password must contain at least one number.
❌ Password must contain at least one special character.
```

### Function-Based Version Example
```
Create your password: hello

Password requirements not met:
❌ Your password must contain at least 8 characters!
❌ Your password must contain at least one uppercase letter!
❌ Your password must contain at least one number!
❌ Your password must contain at least one special character!

Please try again.
```

### Strong Password Success
```
Please enter a password (at least 8 characters, includes upper, lower, number, special): MyPass123!
✅ Password accepted! Great Job :)
```

```
Create your password: SecurePass1!
✅️ Your password is valid!
