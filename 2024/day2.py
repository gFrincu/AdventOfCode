from pathlib import Path
# Read the file and generate a list of lists structure
def define_lines(file):
    #  Open the file and close it when we don't need it more.
    with open(file, 'r') as f:
        # Get the file lines as a string split them by space and convert them to integers
        lines = [list(map(int, line.split())) for line in f.readlines()]
    
    return lines

# Check if the numbers are increasing or decreasing
def increase_decrease(list):
    # all checks if the condition is true for the all elements in the for loop, if it is true it returns True
    # check if the list increases
    if all(list[i] < list[i+1] for i in range(len(list) - 1)):
        return True
    # Check if the list decreases
    elif all(list[i] > list[i+1] for i in range(len(list) - 1)):
        return True
    # It doesn't increase nor decrease
    else:
        return False

# Check if the difference between the numbers is 1, 2 or 3
def differ_levels(list):
    return all(1 <= abs(list[i] - list[i+1]) <= 3 for i in range(len(list) - 1))

# Check all the conditions
def is_valid(list, allow_removal):
    # For part 1
    if increase_decrease(list) and differ_levels(list):
        return True
    # For part 2
    if allow_removal:
        for i in range(len(list)):
            # Creating lists without the i element and checking the conditions, if they are met return True
            reduced_list = list[:i] + list[i+1:]
            if increase_decrease(reduced_list) and differ_levels(reduced_list):
                return True

    return False



script_dir = Path(__file__).parent
filename = script_dir / "day2input.txt"

lines = define_lines(filename)
report_without_removal = 0
report_with_removal = 0

for list in lines:
    # Part one
    if is_valid(list, allow_removal=False):
        report_without_removal += 1
        # Part two
    if is_valid(list, allow_removal=True):
        report_with_removal += 1

print(f"The number of reports that are safe is: {report_without_removal}")
print(f"The number of reports that are safe with the possibility of removing a number is: {report_with_removal}")
