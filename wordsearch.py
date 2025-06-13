'''
mani abhiram reddy
csc 110
project -11

'''
def text_to_dictionary(file_name):
    """
    This function reads a file, processes each line as a word, and creates a dictionary 
    where the word is the key and its reverse is the value.

    Args:
        file_name (str): The name of the file containing words.

    Returns:
        dict: A dictionary with words as keys and their reversed versions as values.
    """
    words = {}
    file = open(file_name, 'r')
    for line in file:
        word = line.strip()
        words[word] = word[::-1]
    file.close()
    return words


def load_search_grid(file_name):
    """
    This function reads a grid from a file, where each line contains words separated by spaces.
    It returns a list of lists representing the grid.

    Args:
        file_name (str): The name of the file containing the word grid.

    Returns:
        list: A 2D list where each element is a list of words in a row.
    """
    list = []
    file = open(file_name, 'r')
    for line in file:
        words = line.strip().split()
        list.append(words)
    return list


def search(word_bank, grid):
    """
    This function searches for words from the word_bank in the grid both horizontally 
    (left-to-right) and vertically (top-to-bottom). It returns a dictionary containing
    the word positions.

    Args:
        word_bank (dict): A dictionary where the key is the word and the value is its reverse.
        grid (list): A 2D list representing the word grid.

    Returns:
        dict: A dictionary containing words and their positions in the grid.
    """

    result = {}

    # Horizontal search: check each row for the word and its reverse
    word_keys = list(word_bank.keys())
    for i in range(len(word_keys)):
        word = word_keys[i]
        for j in range(len(grid)):
            row_str = ""
            for k in range(len(grid[0])):
                row_str += grid[j][k].upper()
            word_position = row_str.find(word.upper())
            if word_position != -1:
                result[word] = [j + 1, word_position + 1]  # 1-based index
            reverse_word_position = row_str.find(word_bank[word].upper())
            if reverse_word_position != -1:
                result[word] = [j + 1, reverse_word_position + len(word_bank[word])]

    # Vertical search: check each column for the word and its reverse
    for i in range(len(word_keys)):
        word = word_keys[i]
        for j in range(len(grid[0])):
            col_str = ""
            for k in range(len(grid)):
                col_str += grid[k][j].upper()
            word_position = col_str.find(word.upper())
            if word_position != -1:
                result[word] = [word_position + 1, j + 1]  # 1-based index
            reverse_word_position = col_str.find(word_bank[word].upper())
            if reverse_word_position != -1:
                result[word]= [reverse_word_position + len(word_bank[word]), j + 1]

    return result












