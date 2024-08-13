import random

def number_guesser(min_value, max_value):
    """
    Generate a random number between min_value and max_value (inclusive).
    Let the user guess the number, providing feedback if the guess is too high or too low.

    Args:
        min_value (int): Minimum value of the range (inclusive).
        max_value (int): Maximum value of the range (inclusive).
    """
    # Generate a random number within the specified range
    number_to_guess = random.randint(min_value, max_value)

    # Initialize the number of attempts
    attempts = 0

    while True:
        # Ask the user for their guess
        user_guess = input(f"Guess a number between {min_value} and {max_value}: ")

        # Check if the user wants to quit
        if user_guess.lower() == "quit":
            print("Thanks for playing!")
            break

        # Try to convert the user's guess to an integer
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        # Increment the number of attempts
        attempts += 1

        # Check if the user's guess is correct
        if user_guess == number_to_guess:
            print(f" Congratulations! You found the number in {attempts} attempts.")
            break
        elif user_guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Example usage
number_guesser(1, 100)