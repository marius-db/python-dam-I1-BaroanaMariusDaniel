# This program asks the user for their name and birth year,
# calculates their age, and classifies them as a minor, adult, or senior.
# It also handles errors if the user enters an invalid birth year.

from datetime import datetime  # Import the datetime module to get the current year

# Get the current year from the system
current_year = datetime.now().year

# Prompt the user to enter their name
name = input("Enter your name: ")

# Prompt the user to enter their birth year
birth_year = input("Enter your birth year: ")

try:
    # Try to convert the input birth year to an integer
    birth_year = int(birth_year)
    # Calculate the user's age
    age = current_year - birth_year
    # Check if the birth year is in the future
    if age < 0:
        print("You haven't been born yet!")
    # Classify as minor if under 18
    elif age < 18:
        print(f"{name}, you are {age} years old and classified as a minor.")
    # Classify as adult if between 18 and 65 (inclusive)
    elif age <= 65:
        print(f"{name}, you are {age} years old and classified as an adult.")
    # Classify as senior if over 65
    else:
        print(f"{name}, you are {age} years old and classified as a senior.")
except ValueError:
    # Handle the case where the input is not a valid integer
    print("Please enter a valid number for your birth year.")