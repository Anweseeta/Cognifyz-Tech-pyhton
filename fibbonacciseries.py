def fibonacci_sequence(n):
    """
    Generates the Fibonacci sequence up to n terms.
    """
    # Initialize the Fibonacci sequence with the first two terms
    sequence = [0, 1]

    # Generate the Fibonacci sequence up to n terms
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)

    # Return the Fibonacci sequence
    return sequence

def main():
    # Get the number of terms from the user
    n = int(input("Enter the number of terms: "))

    # Generate the Fibonacci sequence
    sequence = fibonacci_sequence(n)

    # Print the Fibonacci sequence
    print("Fibonacci Sequence:")
    for i, term in enumerate(sequence):
        print(f"Term {i+1}: {term}")

if __name__ == "__main__":
    main()