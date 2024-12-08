from pathlib import Path
from itertools import product

def read_file(file):
    # Reads the file and splits each line into two parts:
    # line1: Results (numbers before the colon).
    # line2: Lists of numbers (numbers after the colon).
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()
        line1, line2 = [], []

        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                line1.append(int(parts[0].strip()))
                line2.append([int(x) for x in parts[1].strip().split()])

    return line1, line2

def evaluate_expression(nums, operators):
    # Constructs and evaluates a mathematical expression strictly left-to-right.
    # nums: List of numbers.
    # operators: List of operators ('+', '*', '||').
    # Start with the first number
    expression = nums[0]
    # Iterate over numbers and corresponding operators
    for num, op in zip(nums[1:], operators):
        if op == '+':
            expression += num
        elif op == '*':
            expression *= num
        elif op == '||':
            expression = int(str(expression) + str(num))
    return expression

def find_matching_expressions(results, all_numbers, allow_concat):
    # Finds equations that match the results
    valid_count = 0 
    operators = ['+', '*']
    if allow_concat:
        # Add '||' if concatenation is allowed
        operators.append('||')

    for res, numbers in zip(results, all_numbers):
        # Determine the number of operators needed
        n = len(numbers) - 1
        operators_combinations = product(operators, repeat=n)

        for operator_combination in operators_combinations: 
            try:
                # Check if the evaluated expression matches the target result
                if evaluate_expression(numbers, operator_combination) == res:
                    valid_count += res
                    # Stop testing once a valid combination is found
                    break
            except Exception:
                continue

    return valid_count

script_dir = Path(__file__).parent
filename = script_dir / "day7input.txt"
result, numbers = read_file(filename)

# Part one
allow_concat = False
print(f"The total calibration result is {find_matching_expressions(result, numbers, allow_concat)}")
# Part two
allow_concat = True
print(f"The total calibration result with the concanation operator is {find_matching_expressions(result, numbers, allow_concat)}")
