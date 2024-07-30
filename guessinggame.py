import random

def guessing_game():
    """
    A guessing game where the user tries to guess a random number between 1 and 100.
    """
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize the number of attempts
    attempts = 0

    # Loop until the user guesses the correct number
    while True:
        # Prompt the user to guess a number
        user_guess = int(input("Guess a number between 1 and 100: "))

        # Increment the number of attempts
        attempts += 1

        # Check if the user's guess is correct
        if user_guess == secret_number:
            print(f" Congratulations! You guessed the correct number in {attempts} attempts.")
            break

        # Provide a hint if the user's guess is too high or too low
        elif user_guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")

# Call the guessing game function
guessing_game()