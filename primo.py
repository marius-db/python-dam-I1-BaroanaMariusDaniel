# primo.py
# This program asks the user to enter a number and tells if it is prime or not.
# A prime number is a number greater than 1 that has no divisors other than 1 and itself.

# Get input from the user
user_input = input("Enter a number: ")

# Try to convert the input to an integer
try:
    num = int(user_input)
except ValueError:
    # If the input is not a valid integer, print an error message and exit
    print("That is not a valid integer.")
    exit()

# Prime numbers are greater than 1
if num <= 1:
    print(num, "is not a prime number.")
else:
    # Assume the number is prime until we find a divisor
    is_prime = True

    # Check for divisors from 2 up to num - 1
    for i in range(2, num):
        if num % i == 0:
            # If num is divisible by i, it is not prime
            is_prime = False
            break  # No need to check further

    # Print the result
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
