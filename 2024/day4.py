# For part one I've used this stack overflow question. Thanks to willredington. https://stackoverflow.com/questions/6313308/get-all-the-diagonals-in-a-matrix-list-of-lists-in-python
# Read the file and generate a list of lists structure
def define_lines(file):
    try:
    #  Open the file and close it when we don't need it more.
        with open(file, 'r') as f:
            matrix = [list(line.strip()) for line in f]
        return matrix
    except FileNotFoundError:
        print(f"Error: the file '{file}' doesn't exist.")
        return []
    except Exception as e:
        print(f"Can't read the file: {e}")
        return []

# Part one
#  Find words looking at a matrix vertically
def find_vertically(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    word_length = len(word)
    vertical = 0;
        # A loop to go through the columns
    for j in range(cols):
        # a loop to go through the rows
        for i in range(rows - word_length + 1):
            # Check if the word is in the matrix
            match = True
            for k in range(word_length):
                if matrix[i + k][j] != word[k]:
                    match = False
                    break
            if match:
                vertical += 1

    return vertical

# Find words in a matrix horizontally. From left to right and from right to left.
def find_horizontally(matrix, word):
    rows = len(matrix)
    horizontal_count = 0

    # a loop to go through the rows
    for i in range(rows):
        # Convert the row into a string
        row_string = ''.join(matrix[i])
        # Search the word from left to right
        index = row_string.find(word)
        while index != -1:
            horizontal_count += 1
            index = row_string.find(word, index + 1)
        # Search the word from right to left
        reversed_word = word[::-1]
        index = row_string.find(reversed_word)
        while index != -1:
            horizontal_count += 1
            index = row_string.find(reversed_word, index + 1)

    return horizontal_count

# Find all the diagonals of a matrix
def generate_diagonals(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    diagonals_1 = []  # lower-left-to-upper-right diagonals
    diagonals_2 = []  # upper-left-to-lower-right diagonals

    for p in range(rows + cols - 1):
        diagonals_1.append([matrix[r][p - r] for r in range(max(0, p - cols + 1), min(p + 1, rows)) if 0 <= p - r < cols])
        diagonals_2.append([matrix[r][cols - 1 - (p - r)] for r in range(max(0, p - cols + 1), min(p + 1, rows)) if 0 <= cols - 1 - (p - r) < cols])

    return diagonals_1, diagonals_2
    
def search_word_in_diagonals(diagonals, word):
    count = 0
    # Loop through all the diagonals
    for diagonal in diagonals:
        # Convert the diagonal into a string
        diagonal_str = ''.join(map(str, diagonal))
        # Search the word from left to right
        index = diagonal_str.find(word)
        while index != -1:
            count += 1
            index = diagonal_str.find(word, index + 1)
        # Search the word from right to left
        reversed_word = word[::-1]
        index = diagonal_str.find(reversed_word)
        while index != -1:
            count += 1
            index = diagonal_str.find(reversed_word, index + 1)

    return count

def find_words_in_matrix(matrix, word):
    # Generate the diagonals
    diagonals_1, diagonals_2 = generate_diagonals(matrix)
    # Search the word in all the Matrix
    count = search_word_in_diagonals(diagonals_1, word)
    count += search_word_in_diagonals(diagonals_2, word)
    count += find_horizontally(matrix, word)
    count += find_vertically(matrix, word)+find_vertically(matrix,word[::-1])
    return count

# Part two 
def find_x_mas(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    # We know that in the middle of the x, we will need to find an "A". So we will try to find those middles of the x. We are not checking borders.
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if matrix[i][j] == 'A':
                if is_x_mas(matrix, i, j):
                    count += 1

    return count

# Check diagonals to find the X-MAS pattern
def is_x_mas(matrix, i, j):
    rows = len(matrix)
    cols = len(matrix[0])

    if (i - 1 >= 0 and i + 1 < rows and j - 1 >= 0 and j + 1 < cols):
        top_left = matrix[i - 1][j - 1]
        bottom_right = matrix[i + 1][j + 1]
        top_right = matrix[i - 1][j + 1]
        bottom_left = matrix[i + 1][j - 1]

        # Check combinations of the diagonals
        diagonal_1 = (top_left == 'M' and bottom_right == 'S') or (top_left == 'S' and bottom_right == 'M')
        diagonal_2 = (top_right == 'M' and bottom_left == 'S') or (top_right == 'S' and bottom_left == 'M')

        return diagonal_1 and diagonal_2

    return False



filename = "day4input.txt"
matrix = define_lines(filename)
result=find_words_in_matrix(matrix, "XMAS")
print(f"The word appears {result} times in the matrix")
result = find_x_mas(matrix)
print(f"The X-MAS pattern appears {result} times in the matrix.")