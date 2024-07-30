def is_palindrome(s):
    """
    Check whether a given string is a palindrome.

    Args:
        s (str): The string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()

    # Compare the string with its reverse
    return s == s[::-1]

# Example usage:
string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")