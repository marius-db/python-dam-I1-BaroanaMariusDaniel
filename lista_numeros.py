"""Simple script to read a list of numbers separated by commas and show
the numbers, their sum, average, maximum and whether there are duplicates.

This file uses only very basic Python constructs so it is suitable for
beginners and includes comments explaining each step.
"""


def main():
	# Ask the user for input. Use try/except to handle keyboard interrupt
	# (Ctrl+C) or EOF (Ctrl+Z on Windows, Ctrl+D on Unix-like systems).
	try:
		input_str = input("Enter a list of numbers separated by commas: ")
	except (KeyboardInterrupt, EOFError):
		# If the user cancels the input, print a message and exit cleanly.
		print('\nInput cancelled by the user.')
		return

	# Split the input string on commas. This gives parts that may include
	# extra spaces which we'll strip later.
	parts = input_str.split(',')
	numbers = []  # list that will hold the converted numeric values

	# Simple helper function to convert a string to a number.
	# It tries int first (to keep integers when possible) and then float.1,
	# If the conversion fails, it returns None.
	def convert_to_number(s):
		s = s.strip()  # remove surrounding whitespace
		if s == '':
			# Empty string (for example when the user types ,,) -> ignore
			return None
		# First, prefer integers when possible (so '3' becomes int 3).
		# If int() fails, try float() which also handles exponential forms
		# like '1e3' and special floats like 'nan'/'inf'.
		try:
			return int(s)
		except ValueError:
			#Float is checked here instead of outside the exception so that we make sure the float doesn't accidentally 
            #turn a 3 into a 3.0 for example and it only gets to turn numbers that int can't catch
			try:
				return float(s)
			except ValueError:
				# Not a valid number
				return None

	# Convert each part and collect valid numbers. If a part is not a number
	# we inform the user and continue with the rest.
	for p in parts:
		n = convert_to_number(p)
		if n is None:
			p_clean = p.strip()
			if p_clean != '':
				print(f"'{p_clean}' is not a valid number. It will be ignored.")
			# skip empty parts silently to avoid noisy messages
			continue
		numbers.append(n)

	# If there are no valid numbers, inform the user and stop.
	if len(numbers) == 0:
		print("No valid numbers were entered.")
		return

	# Show the list of numbers we parsed so the user can verify them.
	print("Numbers entered:", numbers)

	# Calculate the sum using the built-in sum(). This works with ints and
	# floats mixed together.
	try:
		total = sum(numbers)
	except TypeError:
		# Extra safety: if something non-numeric got into the list.
		print("Error computing the sum: non-numeric value in the list.")
		return

	# Calculate the average (mean). Division by zero won't happen because we
	# already checked that numbers is not empty, but we still protect it.
	try:
		average = total / len(numbers)
	except Exception as e:
		print("Error computing the average:", e)
		return

	# Find the maximum value using max().
	try:
		maximum = max(numbers)
	except ValueError:
		# This would only happen if numbers were empty.
		print("Could not determine the maximum: the list is empty.")
		return

	# Detect duplicates: converting to a set removes duplicates, so if the
	# set length is different we have repeated values.
	has_duplicates = len(set(numbers)) != len(numbers)

	# Print results on separate lines for clarity.
	print("Sum:", total)
	print("Average:", average)
	print("Maximum:", maximum)
	print("Duplicates:", "Yes" if has_duplicates else "No")


if __name__ == '__main__':
	main()

