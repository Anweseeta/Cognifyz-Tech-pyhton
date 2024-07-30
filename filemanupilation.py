import re
from collections import Counter

def count_words_in_file(filename):
    """
    Reads a text file and counts the occurrences of each word in the file.
    """
    try:
        with open(filename, 'r') as file:
            # Read the file content
            content = file.read()

            # Convert the content to lowercase and split it into words
            words = re.findall(r'\b\w+\b', content.lower())

            # Count the occurrences of each word
            word_counts = Counter(words)

            # Return the word counts
            return word_counts

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

def main():
    # Get the filename from the user
    filename = input("Enter the filename: ")

    # Count the words in the file
    word_counts = count_words_in_file(filename)

    if word_counts:
        # Print the word counts in alphabetical order
        print("Word Counts:")
        for word, count in sorted(word_counts.items()):
            print(f"{word}: {count}")

if __name__ == "__main__":
    main()