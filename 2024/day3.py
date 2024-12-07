import re
from pathlib import Path

# Get all the lines from the file and make a big string
def recover_data(file):
    with open(file, 'r') as f:
        data = f.read()
    return data

# Find all the times that the expression with mul appears. Multiply the numbers. And make an addition with all the results.
def find_mul(data):
    # mul+(+1 to 3 digit number + , + 1 to 3 digit number + )
    # It seems that if I had parenthesis to the numbers I could get them to use them in the future
    # So this expression, finds the pattern exactly as I write it: r"mul\(\d{1,3},\d{1,3}\)"
    # and this other expression also finds the pattern as I write it, but it separates the numbers: r"mul\((\d{1,3}),(\d{1,3})\)"
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, data)
    return matches

def calculate_mul(numbers):
    total = 0
    for x, y in numbers:
        total += int(x) * int(y)
    return total

#  For part two, remove all parts that are between a don't() and a do()
def remove_disabled_sections(data):
    result = []
    enabled = True
    i = 0

    while i < len(data):
        if data[i:i+7] == "don't()":
            enabled = False
            i += 7
        elif data[i:i+4] == "do()":
            enabled = True
            i += 4
        elif enabled:
            result.append(data[i])
            i += 1
        else:
            i += 1

    return ''.join(result)

# Part one
script_dir = Path(__file__).parent
filename = script_dir / "day3input.txt"

text= recover_data(filename)
print(f"The result of the addition for all the multiplications that appear with mul  is {calculate_mul(find_mul(text))}")
# Part two
print(f"The result of the addition for all the multiplications that appear with mul and are enabled is {calculate_mul(find_mul(remove_disabled_sections(text)))}")
