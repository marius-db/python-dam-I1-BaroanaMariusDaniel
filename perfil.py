# Ask the user for their name
name = input("Please enter your name: ")

# Ask the user for their birth year and handle invalid input
while True:
	birth_year_input = input("Please enter your birth year: ")
	try:
		birth_year = int(birth_year_input)
		break  # Exit the loop if input is valid
	except ValueError:
		print("Invalid input. Please enter a valid year (numbers only).")

# Calculate the user's age based on the current year
from datetime import datetime
current_year = datetime.now().year
age = current_year - birth_year

# Classify the user based on their age
if age < 18:
	category = "under 18"
elif 18 <= age <= 65:
	category = "between 18 and 65"
else:
	category = "over 65"

# Output the result
print(f"Hello, {name}! You are {age} years old and classified as {category}.")
