import re

def password_strength_checker(password):
    """
    Evaluates the strength of a password based on length, presence of uppercase and lowercase letters, digits, and special characters.
    """
    # Initialize a dictionary to store the password strength metrics
    strength_metrics = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "digits": False,
        "special_chars": False
    }

    # Check password length
    if len(password) >= 8:
        strength_metrics["length"] = True

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength_metrics["uppercase"] = True

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength_metrics["lowercase"] = True

    # Check for digits
    if re.search(r"\d", password):
        strength_metrics["digits"] = True

    # Check for special characters
    if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", password):
        strength_metrics["special_chars"] = True

    # Calculate the password strength score
    strength_score = sum(1 for metric in strength_metrics.values() if metric)

    # Return the password strength metrics and score
    return strength_metrics, strength_score

def main():
    # Get the password from the user
    password = input("Enter a password: ")

    # Evaluate the password strength
    strength_metrics, strength_score = password_strength_checker(password)

    # Print the password strength metrics
    print("Password Strength Metrics:")
    for metric, value in strength_metrics.items():
        print(f"{metric.capitalize()}: {'Pass' if value else 'Fail'}")

    # Print the password strength score
    print(f"Password Strength Score: {strength_score}/5")

    # Provide a password strength recommendation
    if strength_score >= 4:
        print("Password strength: Strong")
    elif strength_score >= 2:
        print("Password strength: Medium")
    else:
        print("Password strength: Weak")

if __name__ == "__main__":
    main()