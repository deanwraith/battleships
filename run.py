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


def generate_ship_position(board):
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


def message():
    """
    Welcome message to the game.
    """
    print("Ready to play Battleships! Good Luck")
    username = input("Choose a username and hit enter: \n")
    print(f'\nHi {username}! Your battleships will be placed randomly for you.'
          'You will have to find 10 ships on the hidden board to win.')
    print('\nO are unselected positions, * are misses and # hits'
          'The board is 8 x 8 so use intergers between 1 and 8.')


def generate_boards():
    """
    Creates boards for the game. A user board for attempts,
    a user board for following computers attempts and a
    hidden board for computers ships.
    """
    produce_board(user)
    produce_board(computer)
    produce_board(user_guess)
    generate_ship_position(user)
    generate_ship_position(computer)


def user_turn():
    """
    Get input from user, check if position is valid,
    check whether they hit a ship and show the the result.
    """
    print("Make your mark:")
    print_board(user_guess)
    repeat = True
    while repeat:
        # check whether data is valid
        while True:
            print("\nChoose a column")
            guess_col = input("Enter a number and press enter: \n")
            if validate_data(guess_col):
                break
        while True:
            print("\nChoose a row")
            guess_row = input("Enter a number and press enter: \n")
            if validate_data(guess_row):
                break

        # minus 1 as the users enter numbers between 1 and 8
        guess_col = int(guess_col)-1
        guess_row = int(guess_row)-1

        # check if we've already chosen that position
        if (user_guess[guess_row][guess_col] == " * " or
                user_guess[guess_row][guess_col] == " # "):
            print("You've already picked that position, try again!")
        else:
            repeat = False
    # Check whether that spot is a hit or not and display result
    if computer[guess_row][guess_col] == " o ":
        user_guess[guess_row][guess_col] = " # "
        print("\nHIT!")
    else:
        user_guess[guess_row][guess_col] = " * "
        print("\nMISS!")


def computer_guess():
    """
    Computer guess.
    """
    print("\n\nOpponents turn!")
    repeat = True
    # Generate first random numbers
    guess_col = random_number(computer)
    guess_row = random_number(computer)
    # Check if we've already chosen that spot
    while repeat:
        if (user[guess_row][guess_col] == " * " or
                user[guess_row][guess_col] == " # "):
            guess_col = random_number(computer)
            guess_row = random_number(computer)
        else:
            repeat = False
    # Display to the user what the computer chose and result
    print(f"Opponent chose {guess_col + 1}, {guess_row + 1}")
    if user[guess_row][guess_col] == " o ":
        user[guess_row][guess_col] = " # "
        print("HIT! :(")
    else:
        user[guess_row][guess_col] = " * "
        print("MISS!")


def game_play():
    """
    Main loop for playing the game. Boards are generated and display message.
    Whileloops will check for hit or miss and display appropriate message.
    """
    generate_boards()
    message()
    i = 0
    while i < 20:
        print(f"\nTurns used {i +1}/20 \n")
        user_turn()
        print_board(user_guess)
        input("\nPress Enter for next step...")
        computer_guess()
        print("\nUser board: ")
        print_board(user)
        input("\nPress Enter for next step...")
        i += 1
        if check_winner(user) == 10:
            i = 20
        elif check_winner(user_guess) == 10:
            i = 20
    check_winner_final()


def validate_data(value):
    """
    If value is not between 1 and 8, display error and request user to go again
    Argument: user input value
    """
    try:
        if int(value) > 8 or int(value) < 1:
            raise ValueError(
                "Your shot is off the board! Choose a number between 1 and 8"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        print("Please enter an integer between 1 and 8")
        return False
    return True


def check_winner(board):
    """
    Sums the number of times " # " (hit battleships) appear in the board.
    Argument: a list
    """
    total = 0
    for list in board:
        total += list.count(" # ")
    return total


def check_winner_final():
    """
    Check for a winner after 20 turns and report the result
    """
    user_result = check_winner(user_guess)
    comp_result = check_winner(user)
    if user_result > comp_result:
        print("Congratulations! You WIN!")
    elif user_result < comp_result:
        print("You lost!")
    else:
        print("It was a draw!")


# Call the main function
game_play()
