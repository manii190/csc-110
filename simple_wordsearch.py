def text_to_dictionary(filename):
    """
    Reads words from a file and returns a dictionary where each word maps to its reverse.
    """
    words = {}
    with open(filename, 'r') as file:
        for line in file:
            word = line.strip().lower()
            words[word] = word[::-1]  # Reverse the word
    return words


def load_search_grid(filename):
    """
    Reads a word search puzzle from a file and returns a 2D list (grid).
    """
    grid = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                grid.append(line.strip().split())
    return grid


def search_within_line(line, word):
    """
    Search for a word within a single line of the grid.
    Returns the starting index of the word if found, otherwise -1.
    """
    word_len = len(word)
    line_str = ''.join(line).lower()

    # Iterate through possible starting positions in the line
    for i in range(len(line_str) - word_len + 1):
        if line_str[i:i + word_len] == word:
            return i  # Return the starting index if the word is found
    return -1  # Return -1 if the word is not found


def transpose_grid(grid):
    """
    Transposes the grid (turn rows into columns) without using zip.
    """
    transposed = []
    num_cols = len(grid[0])  # Assuming all rows are the same length
    num_rows = len(grid)

    for col_idx in range(num_cols):
        transposed_row = []
        for row_idx in range(num_rows):
            transposed_row.append(grid[row_idx][col_idx])
        transposed.append(transposed_row)

    return transposed


def search(word_bank, puzzle):
    """
    Search for words in the grid (both horizontally and vertically).
    Returns a dictionary with the word and its starting position in the format [row, col].
    """
    results = {}
    
    # Search horizontally
    for row_idx in range(len(puzzle)):
        row = puzzle[row_idx]
        for word in word_bank:
            # Check for forward word in the row
            col_idx = search_within_line(row, word)
            if col_idx != -1:
                results[word] = [row_idx + 1, col_idx + 1]  # 1-based index
                break
            # Check for backward word in the row
            col_idx = search_within_line(row, word_bank[word])
            if col_idx != -1:
                results[word] = [row_idx + 1, col_idx + 1]  # 1-based index
                break
    
    # Transpose the grid for vertical search
    transposed_puzzle = transpose_grid(puzzle)

    # Search vertically (using the transposed grid)
    for col_idx in range(len(transposed_puzzle)):
        column = transposed_puzzle[col_idx]
        for word in word_bank:
            # Check for forward word in the column
            row_idx = search_within_line(column, word)
            if row_idx != -1:
                results[word] = [row_idx + 1, col_idx + 1]  # 1-based index
                break
            # Check for backward word in the column
            row_idx = search_within_line(column, word_bank[word])
            if row_idx != -1:
                results[word] = [row_idx + 1, col_idx + 1]  # 1-based index
                break

    return results











