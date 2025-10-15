# temperaturas.py
# This program converts temperatures between Celsius, Kelvin, and Fahrenheit.
# It is designed for beginners, with detailed comments explaining each step.

def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return c * 9 / 5 + 32

def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin."""
    return c + 273.15

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9

def kelvin_to_celsius(k):
    """Convert Kelvin to Celsius."""
    return k - 273.15

def main():
    print("Temperature Converter")
    print("You can convert between Celsius, Fahrenheit, and Kelvin.")
    print("Choose the input scale:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")

    # Ask the user to choose the input scale
    try:
        choice = input("Enter the number of your choice (1/2/3): ")
    except (KeyboardInterrupt, EOFError):
        # This handles the case where the user presses Ctrl+C (KeyboardInterrupt)
        # or Ctrl+D/Ctrl+Z (EOFError) to cancel the input.
        print("\nInput cancelled by the user.")
        return

    # Validate the choice input
    if choice not in ("1", "2", "3"):
        print("Invalid choice. Please run the program again and select 1, 2, or 3.")
        return

    # Ask the user to enter the temperature value
    try:
        temp_str = input("Enter the temperature value: ")
    except (KeyboardInterrupt, EOFError):
        # This handles the case where the user cancels the input for temperature value.
        print("\nInput cancelled by the user.")
        return

    # Try to convert the input to a float (number)
    try:
        temp = float(temp_str)
    except ValueError:
        # This handles the case where the user enters something that is not a number,
        # like letters or symbols.
        print("Invalid temperature value. Please enter a number.")
        return

    # Physically impossible temperature checks
    if choice == "1":
        # Celsius: below -273.15 is not possible
        if temp < -273.15:
            # This checks for temperatures below absolute zero in Celsius,
            # which are not physically possible.
            print("Temperature below absolute zero (-273.15°C) is not possible.")
            return
        c = temp
        f = celsius_to_fahrenheit(c)
        k = celsius_to_kelvin(c)
        print(f"{c}°C is {f}°F and {k}K.")
    elif choice == "2":
        # Fahrenheit: below -459.67 is not possible
        if temp < -459.67:
            # This checks for temperatures below absolute zero in Fahrenheit,
            # which are not physically possible.
            print("Temperature below absolute zero (-459.67°F) is not possible.")
            return
        f = temp
        c = fahrenheit_to_celsius(f)
        k = celsius_to_kelvin(c)
        print(f"{f}°F is {c}°C and {k}K.")
    elif choice == "3":
        # Kelvin: below 0 is not possible
        if temp < 0:
            # This checks for temperatures below absolute zero in Kelvin,
            # which are not physically possible.
            print("Temperature below absolute zero (0K) is not possible.")
            return
        k = temp
        c = kelvin_to_celsius(k)
        f = celsius_to_fahrenheit(c)
        print(f"{k}K is {c}°C and {f}°F.")

# This checks if the script is being run directly (not imported)
if __name__ == "__main__":
    main()