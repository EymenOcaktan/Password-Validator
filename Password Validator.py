letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = letters.upper()
numbers = "0123456789"
special_chars = "!@#€%&/*?\\$"

while True:
    pw = input("Please enter a password (at least 8 characters, includes upper, lower, number, special): ")

    if len(pw) < 8:
        print("❌ Password must be at least 8 characters long.")
        continue

    has_lower = any(char in letters for char in pw)
    has_upper = any(char in upper_letters for char in pw)
    has_number = any(char in numbers for char in pw)
    has_special = any(char in special_chars for char in pw)

    if not has_lower:
        print("❌ Password must contain at least one lowercase letter.")
    if not has_upper:
        print("❌ Password must contain at least one uppercase letter.")
    if not has_number:
        print("❌ Password must contain at least one number.")
    if not has_special:
        print("❌ Password must contain at least one special character.")

    if has_lower and has_upper and has_number and has_special:
        print("✅ Password accepted! Great Job :)")
        break