import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the full path to the input file
input_file_path = os.path.join(script_dir, 'input.txt')

# Open the file
with open(input_file_path, 'r') as file:
    # Read each line
    lines = file.readlines()

# Initialize the total sum
total_sum = 0

# For each line
for line in lines:
    # Remove newline characters
    line = line.strip()

    # Find the first digit
    first_digit = next(char for char in line if char.isdigit())

    # Find the last digit
    last_digit = next(char for char in reversed(line) if char.isdigit())

    # Combine the two digits to form a two-digit number
    two_digit_number = int(first_digit + last_digit)

    # Add this number to the total sum
    total_sum += two_digit_number

# Print the total sum
print(total_sum)
#part 2
# Create a dictionary to map spelled out digits to their numerical equivalents
digit_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

# Initialize the total sum
total_sum = 0

# For each line
for line in lines:
    # Remove newline characters
    line = line.strip()

    # Find the first "digit"
    first_digit = ''
    for i in range(len(line)):
        if line[i].isdigit():
            first_digit = line[i]
            break
        else:
            for word in digit_map:
                if line.startswith(word, i):
                    first_digit = digit_map[word]
                    break
        if first_digit:
            break

    # Find the last "digit"
    last_digit = ''
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            last_digit = line[i]
            break
        else:
            for word in digit_map:
                if line.endswith(word, 0, i + len(word)):
                    last_digit = digit_map[word]
                    break
        if last_digit:
            break

    # Combine the two "digits" to form a two-digit number
    two_digit_number = int(first_digit + last_digit)

    # Add this number to the total sum
    total_sum += two_digit_number

# Print the total sum
print(total_sum)