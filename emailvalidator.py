import re

def validate_email(email):
    """
    Validate whether a given string is a valid email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email is valid, False otherwise.
    """
    # Regular expression pattern for a valid email address
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage:
email = input("Enter an email address: ")
if validate_email(email):
    print("Valid email address!")
else:
    print("Invalid email address.")