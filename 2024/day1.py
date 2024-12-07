from pathlib import Path
# Read the file and return 2 lists
def read_file_lists(filename):
    list1 = []
    list2 = []
    try:
        with open(filename, "r") as file:
            for line in file:
                # Divide the line of the file into 2 numbers
                # Split divides if finds a space, map makes the division into integers
                num1, num2 = map(int, line.split())
                # Add the numbers to the lists
                list1.append(num1)
                list2.append(num2)
    except FileNotFoundError:
        print(f"{filename} does not exist.")
        exit()
    except Exception as e:
        print(f"Error reading the file: {e}")
        exit()
    return list1, list2

# Sort 2 lists
def sort_lists(list1, list2):
    list1.sort()
    list2.sort()
    return list1, list2

# Compare both lists and calculate the distance between the numbers
def calculate_distance(list1, list2):
    distances = []
    # In zip is used to get a number from each list and iterate over both lists
    for num1, num2 in zip(list1, list2):
        distances.append(abs(num1 - num2))
    return distances

# Calculate total distance
def find_total_distance(list):
    distance = 0
    for num in list:
        distance += num
        # I did it like I would do it in C, I didn't know that I could use sum, I will try to remember it for next time.
    return distance

def find_similarity_score(list1, list2):
    score = 0
    for num in list1:
        time=    list2.count(num)
        score += time*num
    return score

# Part one
script_dir = Path(__file__).parent
filename = script_dir / "day1input.txt"

# Read the lists
list1, list2 = read_file_lists(filename)

# Sort the lists
list1, list2 = sort_lists(list1, list2)
#  Calculate distances between numbers of the lists
distances = calculate_distance(list1, list2)
# Find total distance
print (f"The total distance between my lists is {find_total_distance(distances)}")

    #  Part two
print (f"The similarity score of my lists is {find_similarity_score(list1, list2)}")
    