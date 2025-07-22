letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = letters.upper()
numbers = "0123456789"
special_chars = "!@#€%&/*?\\$."

def check_length(password):
    return len(password) >=8

def check_has_lower(password):
    return any(x in letters for x in password)
def check_has_upper(password):
    return any(x in upper_letters for x in password)
def check_has_digits(password):
    return any(x in numbers for x in password)
def check_has_special_chars(password):
    return any(x in special_chars for x in password)
def password_validator(password):
    errors= []
    if not check_length(password):
        errors.append("❌ Your password must contain at least 8 characters!")
    if not check_has_lower(password):
        errors.append("❌ Your password must contain at least one lowercase letter!")
    if not check_has_upper(password):
        errors.append("❌ Your password must contain at least one uppercase letter!")
    if not check_has_digits(password):
        errors.append("❌ Your password must contain at least one number!")
    if not check_has_special_chars(password):
        errors.append("❌ Your password must contain at least one special character!")

    if not errors:
        return True, "✅️ Your password is valid!"
    else:
        return False, errors

while True:
    pw = input("Create your password: ")
    is_valid, message = password_validator(pw)

    if is_valid:
        print(message)
        break
    else:
        print("\nPassword requirements not met:")
        for error in message:
            print(error)
        print("\nPlease try again.\n")


