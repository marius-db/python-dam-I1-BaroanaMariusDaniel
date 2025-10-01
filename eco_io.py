# Ask the user for 3 numbers and store them in a list
numbers = []
for i in range(1, 4):
    while True:
        num_input = input(f"Enter number {i}: ")
        try:
            num = float(num_input)  # Accepts integers and decimals
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

try:
    # Calculate the sum of the numbers
    sum_numbers = sum(numbers)

    # Find the biggest number
    max_number = max(numbers)

    # Calculate the average
    average = sum_numbers / len(numbers)

    # Display the results to the user
    print(f"The sum of the numbers is: {sum_numbers}")
    print(f"The biggest number is: {max_number}")
    print(f"The average of the numbers is: {average}")
except Exception as e:
    print(f"An error occurred during calculation: {e}")
