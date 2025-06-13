"""
MANI ABHIRAM
CSC 110
PROJECT 6
"""

import random
random.seed(123)
#list of symbols to use in the pattern
SYMBOLS =[" ◎ ", " △ ", " ▞ ", " ● ", " ▣ ", 
           " ▤ ", " ▲ ", " ▼ ", " * ", " < ",
           " > ", " = ", " ≡ ", " ☼ ", " ♦ ",
           " ◭ ", " ► ", " ◘ ", " ◓ ", " ▌ "]
#Prints the 2D pattern with a grid-like format."""
def print_pattern(pattern):
    import random
    random.seed(123)
    width = len(pattern[0]) - 1
    top_line = "┌" + "───┬" * width + "───┐"
    print(top_line)
    for i in range(len(pattern)):
        new_row = "│"
        for j in range(len(pattern[i])):
            new_row += pattern[i][j] + "│"
        print(new_row)
        if i != len(pattern) - 1:
            print("├" + "───┼" * width + "───┤")
    bottom_line = "└" + "───┴" * width + "───┘"
    print(bottom_line)
#Creates a 2D pattern filled with random symbols.
def create_background(w, l, num_symbols):
    """
    Creates a 2D pattern filled with random symbols.

    Parameters:
    w (int): Width of the pattern.
    l (int): Length of the pattern.
    n (int): Number of different symbols to use.

    Returns:
    list: A 2D list representing the pattern.
    """
    import random
    random.seed(123)
    pattern = []
    for _ in range(l):
        row = [random.choice(SYMBOLS[:num_symbols]) for _ in range(w)]
        pattern.append(row)
    return pattern
#Adds a horizontal stripe of a specified symbol to the pattern.
def add_h_stripe(pattern, start_row, h, symbol_index):
    """
    Adds a horizontal stripe of a specified symbol to the pattern.

    Parameters:
    p (list): The 2D list representing the pattern.
    r (int): The starting row for the stripe.
    h (int): Height of the stripe.
    s (int): The index of the symbol to use from SYMBOLS.

    Returns:
    list: The updated pattern with the horizontal stripe added.
    """
    import random
    random.seed(123)
    symbol = SYMBOLS[symbol_index]
    for row in range(start_row, min(start_row + h, len(pattern))):
        pattern[row] = [symbol] * len(pattern[row])
    return pattern
#Adds a vertical stripe of a specified symbol to the pattern
def add_v_stripe(pattern, column_start, stripe_width, symbol_index):
    """
    Adds a vertical stripe of a specified symbol to the pattern.

    Parameters:
    p (list): The 2D list representing the pattern.
    cs (int): The starting column for the stripe.
    w (int): Width of the stripe.
    s (int): The index of the symbol to use from SYMBOLS.

    Returns:
    list: The updated pattern with the vertical stripe added.
    """

    import random
    random.seed(123)
    symbol = SYMBOLS[symbol_index]

    for row in pattern:
        end_col = min(column_start + stripe_width, len(row))
        for col in range(column_start, end_col):
            row[col] = symbol

    return pattern
#Adds a square of a specified size to the pattern at given coordinates.
def add_square(pattern, x_pos, y_pos, size, symbol_index):
    """
    Adds a square of a specified size to the pattern at given coordinates.

    Parameters:
    p (list): The 2D list representing the pattern.
    x (int): The row index where the square starts.
    y (int): The column index where the square starts.
    sz (int): The size of the square (number of rows and columns).
    s (int): The index of the symbol to use from SYMBOLS.

    Returns:
    list: The updated pattern with the square added.
    """
    import random
    random.seed(123)
    symbol = SYMBOLS[symbol_index]
    for i in range(x_pos, min(x_pos + size, len(pattern))):
        for j in range(y_pos, min(y_pos + size, len(pattern[i]))):
            pattern[i][j] = symbol
    return pattern
#Adds a rectangle of specified dimensions to the pattern.
def add_rectangle(pattern, x_pos, y_pos, rect_w, rect_h, symbol_index):
    """
    Adds a rectangle of specified dimensions to the pattern.

    Parameters:
    p (list): The 2D list representing the pattern.
    x (int): The row index where the rectangle starts.
    y (int): The column index where the rectangle starts.
    w (int): Width of the rectangle.
    h (int): Height of the rectangle.
    s (int): The index of the symbol to use from SYMBOLS.

    Returns:
    list: The updated pattern with the rectangle added.
    """

    import random
    random.seed(123)
    symbol = SYMBOLS[symbol_index]
    for i in range(x_pos, min(x_pos + rect_h, len(pattern))):
        for j in range(y_pos, min(y_pos + rect_w, len(pattern[i]))):
            pattern[i][j] = symbol
    return pattern
#Adds an upward-facing triangle to the pattern.

def add_triangle_a(pattern, x_pos, y_pos, s, symbol_index):
    """
    Adds an upward-facing triangle to the pattern.

    Parameters:
    p (list): The 2D list representing the pattern.
    x (int): The row index where the triangle starts.
    y (int): The column index where the triangle starts.
    sz (int): The size of the triangle (number of rows).
    s (int): The index of the symbol to use from SYMBOLS.

    Returns:
    list: The updated pattern with the triangle added.
    """
    import random
    random.seed(123)
    """Draws a right triangle pointing downward,
    starting from the top-left corner."""
    symbol = SYMBOLS[symbol_index]
    for i in range(s):
        for j in range(i + 1):
            if x_pos + i < len(pattern) and y_pos + j < len(pattern[0]):
                pattern[x_pos + i][y_pos + j] = symbol
    return pattern
# Adds a downward-facing triangle to the pattern.
def add_triangle_b(pattern, x_pos, y_pos, size, symbol_pos):
    """
    Adds a downward-facing triangle to the pattern.

    Parameters:
    p (list): The 2D list representing the pattern.
    x (int): The row index where the triangle starts.
    y (int): The column index where the triangle starts.
    sz (int): The size of the triangle (number of rows).
    s (int): The index of the symbol to use from SYMBOLS.

    Returns:
    list: The updated pattern with the triangle added.
    """
    for i in range(size):
        for j in range(i + 1):  # Correctly fill the row
            if x_pos + i < len(pattern) and y_pos + j < len(pattern[0]):
                pattern[x_pos + i][y_pos + j] = SYMBOLS[symbol_pos]
    return pattern
#Adds a left-facing triangle to the pattern.
def add_triangle_c(pattern, x, y, size, index_symbol):
    """
    Adds a left-facing triangle to the pattern.

    Parameters:
    p (list): The 2D list representing the pattern.
    x (int): The row index where the triangle starts.
    y (int): The column index where the triangle starts.
    sz (int): The size of the triangle (number of rows).
    s (int): The index of the symbol to use from SYMBOLS.

    Returns:
    list: The updated pattern with the triangle added.
    """
    for p1 in range(x, x + size):
        for p2 in range(size - (p1 - x) - 1):  # Adjust column count
            if p1 < len(pattern) and p2 + y < len(pattern[0]):
                pattern[p1][p2 + y] = SYMBOLS[index_symbol]
    return pattern
# Adds a downward-facing triangle to the pattern, aligned to the left.

def add_triangle_d(pattern, x_pos, y_pos, size, symbol_pos):
    """
    Adds a downward-facing triangle to the pattern, aligned to the left.

    Parameters:
    p (list): The 2D list representing the pattern.
    x (int): The row index where the triangle starts.
    y (int): The column index where the triangle starts.
    sz (int): The size of the triangle (number of rows).
    s (int): The index of the symbol to use from SYMBOLS.

    Returns:
    list: The updated pattern with the triangle added.
    """
    for i in range(size):
        for j in range(size - i):  # Correctly fill the triangle
            if x_pos + i < len(pattern) and y_pos + j < len(pattern[0]):
                pattern[x_pos + i][y_pos + j] = SYMBOLS[symbol_pos]
    return pattern