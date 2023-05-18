import string

def strength_check(password):
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special_char = any(char in string.punctuation for char in password)
    is_long_enough = len(password) >= 8
    has_no_whitespace = not any(char.isspace() for char in password)

    if (
        has_uppercase and has_lowercase and has_digit and has_special_char
        and is_long_enough and has_no_whitespace
    ):
        return "strong"
    else:
        feedback = ""
        if not is_long_enough:
            feedback += "- Password must be at least 8 characters long.\n"
        if not has_uppercase or not has_lowercase:
            feedback += "- Password must contain a combination of uppercase and lowercase letters.\n"
        if not has_digit:
            feedback += "- Password must contain at least one digit.\n"
        if not has_special_char:
            feedback += "- Password must contain at least one special character.\n"
        if not has_no_whitespace:
            feedback += "- Password must not contain whitespace characters.\n"
        return feedback

password = input("Enter your password: ")
result = strength_check(password)
print(f"Password strength:\n \t {result}")
