from random import randint

user = []
user_guess = []
computer = []


def produce_board(board):
    """
    Produce the playing board of 8 "O" in 8 lists
    Arguments: an empty list
    Returns: a single list containing 8 lists of O
    """
    for i in range(8):
        board.append([" O "]*8)
    return board


def print_board(board):
    """
    Prints the lists containing the O, removes formatting and adds spaces
    Argument: a list
    """
    for ind in board:
        print(" ".join(ind))


def random_number(board):
    """
    Generates a random number between 1 and 8 minus 1.
    Subtract 1 as lists start at 0.
    Argument: a list
    """
    return randint(0, len(board)-1)


def generate_ship_postition(board):
    """
    Generates 10 ships and places them in random locations.
    It will place letter X for the ship and the loop will run
    and check ships are not placed in the same position.
    Argument: a list
    """
    ship_number = 0
    while ship_number < 10:
        ship_number = 0
        ship_col = random_number(board)
        ship_row = random_number(board)
        board[ship_row][ship_col] = " X "
        for row in board:
            ship_number += row.count(" X ")



