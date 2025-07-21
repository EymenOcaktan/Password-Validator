# Password-Validator
This is a beginner-friendly Python script that helps validate the strength of a password. It checks for key security criteria and provides real-time feedback.

## ✅ Features

- Requires a minimum length of 8 characters
- Ensures at least:
  - One lowercase letter
  - One uppercase letter
  - One number
  - One special character (`!@#€%&/*?\$`)
- Gives clear error messages until the password meets all requirements

## 💻 How to Use

1. Run the script using any Python interpreter.
2. Enter a password when prompted.
3. Follow the instructions if the password doesn't meet the rules.
4. Once a strong password is entered, you'll see a success message.

## 🛠️ Example

```bash
Please enter a password (at least 8 characters, includes upper, lower, number, special): pass
❌ Password must be at least 8 characters long.
❌ Password must contain at least one uppercase letter.
❌ Password must contain at least one number.
❌ Password must contain at least one special character.
...
✅ Password accepted! Great Job :)

