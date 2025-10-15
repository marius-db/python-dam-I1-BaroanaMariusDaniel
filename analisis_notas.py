#analisis_notas.py

#The program asks for grades separated by commas, validates them, and
#prints a summary: count, average, min, max, pass% (>=5), excellent% (>=9),
#most frequent grade(s), and a message based on the average.


def parse_grades(input_str):
    """Parse a comma-separated string of grades into a list of floats.

    This function strips whitespace, ignores empty items, and raises a
    ValueError if any item cannot be converted to float.
    """
    if not input_str or input_str.strip() == "":
        raise ValueError("No input provided")

    parts = input_str.split(',')
    grades = []
    for p in parts:
        s = p.strip()
        if s == "":
            # ignore empty pieces caused by consecutive commas or trailing comma
            continue
        try:
            # Convert to float to allow decimal grades like 7.5
            num = float(s)
        except ValueError:
            raise ValueError(f"Invalid number: '{s}'")
        grades.append(num)

    if not grades:
        raise ValueError("No valid grades found in input")

    return grades


def analyze_grades(grades):
    """Return a dictionary with summary statistics for a list of numeric grades.

    No external modules are used; calculations are implemented with basic
    Python constructs so beginners can follow easily.
    """
    total = len(grades)

    # Calculate average manually
    sum_grades = 0.0
    for g in grades:
        sum_grades += g
    average = sum_grades / total

    # Minimum and maximum using simple loops
    minimum = grades[0]
    maximum = grades[0]
    # 1: means that it starts from position 1 in the index
    for g in grades[1:]:
        if g < minimum:
            minimum = g
        if g > maximum:
            maximum = g

    # Percentages for pass (>=5) and excellent (>=9)
    pass_count = 0
    excellent_count = 0
    for g in grades:
        if g >= 5:
            pass_count += 1
        if g >= 9:
            excellent_count += 1

    percent_pass = (pass_count / total) * 100
    percent_excellent = (excellent_count / total) * 100

    # Most frequent grade(s) without imports. We'll build a simple frequency
    # dictionary using only basic operations.
    freqs = {}
    for g in grades:
        # Use the grade value itself as key (floats). For beginners, exact
        # float equality is fine if the user inputs consistently.
        if g in freqs:
            freqs[g] += 1
        else:
            freqs[g] = 1

    # Find the maximum frequency
    max_count = 0
    for count in freqs.values():
        if count > max_count:
            max_count = count

    # Collect all grades that have the maximum frequency (handle ties)
    most_frequent = []
    for grade, count in freqs.items():
        if count == max_count:
            most_frequent.append(grade)

    # Sort the most frequent list for nicer display
    most_frequent.sort()

    # Level message based on average
    if average >= 8:
        level_msg = "Excellent level"
    elif average >= 5:
        level_msg = "Average level"
    else:
        level_msg = "Needs improvement"

    return {
        'total': total,
        'average': average,
        'min': minimum,
        'max': maximum,
        'percent_pass': percent_pass,
        'percent_excellent': percent_excellent,
        'most_frequent': most_frequent,
        'level_message': level_msg,
    }


def format_summary(summary):
    """Format the summary dictionary into a multi-line string for display."""
    most_freq = summary['most_frequent']
    if most_freq:
        # Show all most frequent grades separated by comma
        most_freq_str = ', '.join(f"{g:.2f}" for g in most_freq)
    else:
        most_freq_str = 'N/A'

    text = (
        f"Total grades: {summary['total']}\n"
        f"Average: {summary['average']:.2f}\n"
        f"Minimum: {summary['min']:.2f}\n"
        f"Maximum: {summary['max']:.2f}\n"
        f"Pass percentage (>=5): {summary['percent_pass']:.2f}%\n"
        f"Excellent percentage (>=9): {summary['percent_excellent']:.2f}%\n"
        f"Most frequent grade(s): {most_freq_str}\n\n"
        f"{summary['level_message']}"
    )
    return text


def main():
    """Main entry: read input, parse, analyze, and print results with error handling."""
    print("Enter a list of grades separated by commas (e.g. 7.5, 9, 4, 6):")
    user_input = input('> ')

    try:
        grades = parse_grades(user_input)
    except ValueError as e:
        print(f"Error: {e}")
        return

    summary = analyze_grades(grades)
    output = format_summary(summary)
    print('\nSummary:')
    print(output)


if __name__ == '__main__':
    main()
