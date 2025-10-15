# cadena.py
# This program asks the user to enter a word or phrase,
# then counts and displays the number of vowels (a, e, i, o, u) in the input.
# The code includes comments to help beginners understand each step.

def count_vowels(text):
    """
    Count the number of vowels in the given text.
    Vowels are: a, e, i, o, u (both uppercase and lowercase).
    """
    # Check if the input is actually a string
    if not isinstance(text, str):
        # Raise a TypeError if the input is not a string
        raise TypeError("Input must be a string.")

    vowels = "aeiouAEIOU"  # String containing all vowels
    count = 0  # Variable to keep track of the number of vowels

    # Loop through each character in the text
    for char in text:
        if char in vowels:
            count += 1  # If the character is a vowel, increase the count by 1

    return count  # Return the total number of vowels found

def main():
    print("Vowel Counter")
    print("This program counts the number of vowels in a word or phrase you enter.")

    try:
        # Ask the user to enter a word or phrase
        user_input = input("Please enter a word or phrase: ")
    except KeyboardInterrupt:
        # Handle the case where the user presses Ctrl+C to interrupt the program
        print("\nProgram interrupted by user (KeyboardInterrupt). Exiting gracefully.")
        return
    except EOFError:
        # Handle the case where the user sends an EOF (Ctrl+D/Ctrl+Z)
        print("\nNo input received (EOFError). Exiting gracefully.")
        return
    except Exception as e:
        # Handle any other unexpected exceptions during input
        print(f"\nAn unexpected error occurred while reading input: {e}")
        return

    # Check if the input is empty (user pressed Enter without typing anything)
    if not user_input.strip():
        print("You did not enter anything. Please run the program again and enter a word or phrase.")
        return  # Exit the program

    try:
        # Call the function to count vowels
        num_vowels = count_vowels(user_input)
    except TypeError as te:
        # Handle the case where the input is not a string
        print(f"Error: {te}")
        return
    except Exception as e:
        # Handle any other unexpected exceptions during vowel counting
        print(f"An unexpected error occurred while counting vowels: {e}")
        return

    # Show the result to the user
    print(f"The number of vowels in your input is: {num_vowels}")

# This checks if the script is being run directly (not imported)
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # Catch any unexpected errors in the main function
        print(f"Fatal error: {e}")
