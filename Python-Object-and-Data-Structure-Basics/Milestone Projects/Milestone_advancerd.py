board = [' ']*10
game_state = True
announce = ''

def reset_board():
    global board, game_state
    board = [' ']*10
    game_state = True

def display_board(board):
    print('\n'*100)
    print(board[7]+"|"+board[8]+"|"+ board[9])
    print("------")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("------")
    print(board[1]+"|"+board[2]+"|"+board[3])

def win_check(board, marker):
    # return True if win combination is present
    return board[7] == board[8] == board[9] == marker or\
           board[4] == board[5] == board[6] == marker or\
           board[1] == board[2] == board[3] == marker or\
           board[7] == board[5] == board[3] == marker or\
           board[1] == board[5] == board[9] == marker or\
           board[2] == board[5] == board[8] == marker or\
           board[3] == board[6] == board[9] == marker or\
           board[1] == board[4] == board[7] == marker

def full_board_check(board):
    if ' ' in board[1:]:
        return False
    else:
        return True

def ask_player(mark):
    global board
    req = 'Choose where to place your: ' + mark
    while True:
        try:
            choice = int(input(req))
        except ValueError:
            print("Sorry, please input a number between 1-9.")
            continue

        if board[choice] == " ":
            board[choice] = mark
            break
        else:
            print("That space isn't empty")
            continue

def player_choice(mark):
    global board, game_state,announce
    # Set game blank game announcement
    announce = ''
    # Get Player Input
    mark = str(mark)
    # Validate input
    ask_player(mark)

    #Check for playre win
    if win_check(board,mark):
        print('\n' * 100)
        display_board()
        announce = mark + " wins!"
        game_state = False

    # Show board
    print('\n' * 100)
    display_board()

    # Check for a tie
    if full_board_check(board):
        announce = "Tie"
        game_state = False

    return game_state, announce

def play_game():
    reset_board()
    global announce

    # Set marks
    X = 'X'
    O = 'O'
    while True:
        # Show board
        print('\n' * 100)
        display_board()

        # Player X turn
        game_state, announce = player_choice(X)
        print(announce)
        if game_state == False:
            break

        # Player O turn
        game_state, announce = player_choice(O)
        print(announce)
        if game_state == False:
            break

    # Ask player for a rematch
    rematch = input('Would you lika to play again? y/n')
    if rematch == 'y':
        play_game()
    else:
        print("Thanks for playing")

play_game()

# TODO: NEEDED DEBUGGING