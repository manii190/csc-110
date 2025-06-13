import random
random.seed(123)
SYMBOLS =[" ◎ ", " △ ", " ▞ ", " ● ", " ▣ ", 
           " ▤ ", " ▲ ", " ▼ ", " * ", " < ",
           " > ", " = ", " ≡ ", " ☼ ", " ♦ ",
           " ◭ ", " ► ", " ◘ ", " ◓ ", " ▌ "]
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

def create_background(w, l, num_symbols):
    import random
    random.seed(123)
    pattern = []
    for _ in range(l):
        row = [random.choice(SYMBOLS[:num_symbols]) for _ in range(w)]
        pattern.append(row)
    return pattern

def add_h_stripe(pattern, start_row, h, symbol_index):
    import random
    random.seed(123)
    symbol = SYMBOLS[symbol_index]
    for row in range(start_row, min(start_row + h, len(pattern))):
        pattern[row] = [symbol] * len(pattern[row])
    return pattern

def add_v_stripe(pattern, column_start, stripe_width, symbol_index):
    import random
    random.seed(123)
    symbol = SYMBOLS[symbol_index]

    for row in pattern:
        end_col = min(column_start + stripe_width, len(row))
        for col in range(column_start, end_col):
            row[col] = symbol

    return pattern
def add_square(pattern, x_pos, y_pos, size, symbol_index):
    import random
    random.seed(123)
    symbol = SYMBOLS[symbol_index]
    for i in range(x_pos, min(x_pos + size, len(pattern))):
        for j in range(y_pos, min(y_pos + size, len(pattern[i]))):
            pattern[i][j] = symbol
    return pattern

def add_rectangle(pattern, x_pos, y_pos, rect_w, rect_h, symbol_index):
    import random
    random.seed(123)
    symbol = SYMBOLS[symbol_index]we124
    for i in range(x_pos, min(x_pos + rect_h, len(pattern))):
        for j in range(y_pos, min(y_pos + rect_w, len(pattern[i]))):
            pattern[i][j] = symbol
    return pattern
def add_triangle_a(pattern, x_pos, y_pos, s, symbol_index):
    import random
    random.seed(123)
    """Draws a right triangle pointing downward, starting from the top-left corner."""
    symbol = SYMBOLS[symbol_index]
    for i in range(s):
        for j in range(i + 1):
            if x_pos + i < len(pattern) and y_pos + j < len(pattern[0]):
                pattern[x_pos + i][y_pos + j] = symbol
    return pattern
def add_triangle_b(pattern, x_pos, y_pos, size, symbol_pos):
    for i in range(size):
        for j in range(i + 1):  # Correctly fill the row
            if x_pos + i < len(pattern) and y_pos + j < len(pattern[0]):
                pattern[x_pos + i][y_pos + j] = SYMBOLS[symbol_pos]
    return pattern
def add_triangle_c(pattern, x, y, size, index_symbol):
    for p1 in range(x, x + size):
        for p2 in range(size - (p1 - x) - 1):  # Adjust column count
            if p1 < len(pattern) and p2 + y < len(pattern[0]):
                pattern[p1][p2 + y] = SYMBOLS[index_symbol]
    return pattern
def add_triangle_d(pattern, x_pos, y_pos, size, symbol_pos):
    for i in range(size):
        for j in range(size - i):  # Correctly fill the triangle
            if x_pos + i < len(pattern) and y_pos + j < len(pattern[0]):
                pattern[x_pos + i][y_pos + j] = SYMBOLS[symbol_pos]
    return pattern