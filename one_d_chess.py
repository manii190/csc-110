'''
mani abhi ram reddy
CSC 110
Project 5
This code has multiple functions to create a One D Chess
'''

def create_board():
    '''
    This function is to create characters in a One D chess board
    Returns:
        Characters of 1D chess
    '''
    # returns a list
    return ["WKi", "WKn", "WKn", "EMPTY", "EMPTY","EMPTY", "BKn", "BKn", "BKi"]

def printable_board(board):
    '''
    This function is to create a graphical representation of the board
    Args:
        board  :  board characters in create board function
    Returns:
        Graphical Representation of a One D chess Board
    '''
    board_seperate = "+-----------------------------------------------------+"
    board_new = board_seperate + "\n"
    row = "| "
    for i in range(len(board)):
        if board[i]== " EMPTY":
            if i == len(board) - 1:
                row += "    |"
            else:
                row += "    | "
        else:
            if i == len(board) - 1:
                row += f'{board[i]} |'
            else:
                row += f'{board[i]} | '
    return board_new + row + "\n" + board_seperate




def is_valid_move(board, position, player):
    '''
    This function checks whether the desired move by player is valid
    Args:
        board     :   one d board that is created
        position  :   position of move that user is considering
        player    :   current player who's making the move
    Returns:
        Returns the boolean value ( True or False)
    '''
    #checks if the position is a valid index
    if position < 0 or position >= len(board):
        return False
    #checks whether the position's index is white piece's player's
    if player == "WHITE":
        return board[position] == "WKi" or board[position] == "WKn"
    #checks whether the position's index is black piece's player's
    if player == "BLACK":
        return board[position] == "BKi" or board[position] == "BKn"
    return False

def move_king(board, position, direction):
    '''
    This function is to change position of king
    Args:
        board      :   one d board that is created
        position   :   position of move that user is considering
        direction  :   direction of the move
    Returns:
        New Board with king's new position
    '''
    #checks whether the direction is left
    if direction == "LEFT":
        # iterating over the pieces
        for i in range(position - 1, -1, -1):
            if board[i] != "EMPTY":
                board[i] = board[position]
                board[position] = "EMPTY"
                return
    #checks whether direction is right
    elif direction == "RIGHT":
        # iterating over the pieces
        for i in range(position + 1, len(board)):
            if board[i] != "EMPTY":
                board[i] = board[position]
                board[position] = "EMPTY"
                return
            
def move_knight(board, position, direction):
    '''
    This function is to change the position of knight
    Args:
        board      :   one d board that is created
        position   :   position of move that user is considering
        direction  :   direction of the move
    Returns:
        New Board with knight's new position
    '''
    #checks whether direction is left
    if direction == "LEFT":
        if position >= 2:
            if board[position - 2] == "EMPTY":
                board[position - 2] = board[position]
                board[position] = "EMPTY"
            else:
                board[position - 2] = board[position]
                board[position] = "EMPTY"
                return
    #checks whether direction is right
    elif direction == "RIGHT":
        if position <= len(board) - 3:
            if board[position + 2] == "EMPTY":
                board[position + 2] = board[position]
                board[position] = "EMPTY"
            else:
                board[position + 2] = board[position]
                board[position] = "EMPTY"
                return
# checks whether the desired move
def move(board, position, direction):
    '''
    This function checks whether the desired move by player is valid
    Args:
        board      :   one d board that is created
        position   :   position of move that user is considering
        direction  :   direction of the move
    '''
    piece = board[position]
    #checks if the piece in position white
    if piece[0]=="W":
        if "Ki" in piece:
            move_king(board, position, direction)
        else:
            move_knight(board, position, direction)
    #checks if the peace in position is black
    elif piece[0]=="B":
        if "Ki" in piece:
            move_king(board, position, direction)
        else:
            move_knight(board, position, direction)

def is_game_over(board):
    '''
    This function checks whether the game is over by 
    checking if there any pieces left on board
    Args:
        board     :   board characters in create board function
    Returns:
        Returns the boolean value ( True or False)
    '''
    #checks for white or black pieces in board and returns boolean
    return "WKi" not in board or "BKi" not in board

def whos_the_winner(board):
    '''
    This function checks who's the winner
    Args:
        board     :   one d board created
    Returns:
        Returns the winner
    '''
    # checks if there are any white pieces left on board
    if "WKi" not in board:
        return "Black"
    # checks if there are any black pieces left on board
    elif "BKi" not in board:
        return "White"
    #if both peices are left, it returns None
    else:
        return None
