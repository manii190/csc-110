def read_file(file_name):
    '''
    This function reads a file and returns a 2D list.
    Args:
         file_name(str): The name of the file to read.
    Returns(list):
         It returns a 2D list representing the grid with 'X' for mines
         '0' for empty cells.
    '''
    file = open(file_name, 'r')
    lists = []
    i = int(file.readline().strip())  # Read the number of rows
    j = int(file.readline().strip())  # Read the number of columns

    row_index = 0
    while row_index < i:  # Use while loop to iterate through rows
        current_row = []
        elements = file.readline().strip().split(',')
        for col_index in range(len(elements)):  # Use for loop for columns
            if elements[col_index].strip() == "1":
                current_row.append('X')
            else:
                current_row.append('0')
        lists.append(current_row)  # Add the row to the grid
        row_index += 1  # Increment the row index

    file.close()  # Close the file
    return lists


def make_empty_grid(grid):
    '''
    This function creates an empty grid of the same size as the input grid.
    Args:
         grid(list): Input grid.
    Returns(list):
         It returns a new empty grid of the same size.
    '''
    new_grid = []
    row_index = 0
    while row_index < len(grid):  # Use while loop for rows
        sub_list = []
        col_index = 0
        while col_index < len(grid[row_index]):  # Use while loop for columns
            sub_list.append(" ")  # Add an empty space for each cell
            col_index += 1  # Increment the column index
        new_grid.append(sub_list)  # Append the empty row
        row_index += 1  # Increment the row index
    return new_grid  # Return the empty grid


def conditions(row, column, grid):
    row_offset = -1
    while row_offset <= 1:  # Use while loop for row offsets
        col_offset = -1
        while col_offset <= 1:  # Use while loop for column offsets
            x, y = row + row_offset, column + col_offset
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 'X':
                grid[x][y] = 'X'
            elif 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                grid[x][y] = str(int(grid[x][y]) + 1)
            col_offset += 1  # Increment column offset
        row_offset += 1  # Increment row offset


def update_grid(grid):
    rows = len(grid)
    columns = len(grid[0])
    row_index = 0
    while row_index < rows:  # Use while loop for rows
        col_index = 0
        while col_index < columns:  # Use while loop for columns
            if grid[row_index][col_index] == 'X':
                row_offset = -1
                while row_offset <= 1:  # Use while loop for row offsets
                    col_offset = -1
                    while col_offset <= 1:  # Use while loop for column offsets
                        x, y = row_index + row_offset, col_index + col_offset
                        if 0 <= x < rows and 0 <= y < columns:
                            if grid[x][y] != 'X':
                                grid[x][y] = str(int(grid[x][y]) + 1)
                        col_offset += 1  # Increment column offset
                    row_offset += 1  # Increment row offset
            col_index += 1  # Increment column index
        row_index += 1  # Increment row index

def print_grid(grid):
    '''
    This function prints the grid in readmode.
    
    Args:
        grid (list): The grid to be printed. A 2D list where each element 
                     represents a cell in the grid.
    
    Returns:
        None: This function does not return anything; it simply prints the grid.
    '''
    num_rows = len(grid)
    num_columns = len(grid[0])
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    for i in range(num_rows):
        print(f"{num_rows - 1 - i:2} ", end="")  # Print row number
        for j in range(num_columns):
            print(f"[{grid[i][j]}]", end="")  # Print each cell value
        print()  # Move to the next line after each row
    
    print("   ", end="")
    for j in range(num_columns):
        print(f"{alphabet[j]}  ", end="")  # Print column letters
    print()  # End the column letters line

def dig(grid, move, user_view):
    '''
    This function simulates the player's dig action
    Args:
        grid(list): The original grid with mine locations and numbers.
        move(str): The move to make.
        user_view(list): The player's view.

    Returns:
        None
    '''
    dictionary = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5,
                   "g": 6, "h": 7, "i": 8, "j": 9, "k": 10}
    letter = move[0].lower()
    row = int(move[1:])
    column = dictionary.get(letter, -1)
    row = len(grid) - row - 1
    if grid[row][column] == 'X':
        user_view[row][column] = 'X'
    else:
        row_offset = -1
        while row_offset <= 1:  # Use while loop for row offsets
            col_offset = -1
            while col_offset <= 1:  # Use while loop for column offsets
                x, y = row + row_offset, column + col_offset
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X':
                    user_view[x][y] = grid[x][y]
                col_offset += 1  # Increment column offset
            row_offset += 1  # Increment row offset
    print_grid(user_view)  # Print the updated user view


def determine_game_status(grid, user_view):
    '''
    This function determines if the game is over.
    Args:
         grid(list): The original grid (with mines and numbers).
         user_view(list): The player's current view (with uncovered cells).

    Returns(bool):
        It returns True if the game is still ongoing,
        False if it's over.
    '''
    row_index = 0
    while row_index < len(user_view):  # Using while loop for rows
        for col_index in range(len(user_view[row_index])):  # Using for loop for columns
            if user_view[row_index][col_index] == 'X':  # Check if a mine is uncovered
                return False  # Game is over if any mine is uncovered
        row_index += 1  # Move to the next row
    return True  # Game is still ongoing if no mine is uncovered

