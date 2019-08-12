import random

def display_board(board):
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(board[1]+"|"+board[2]+"|"+board[3])


def player_input():
    '''
    :return: (Player 1 marker, Player 2 marker)
    '''
    marker = ""
    while not (marker == "X" or marker == 'O'):
        marker = input("Player 1: Choose X or O").upper()
    if marker == "X":
        return 'X', 'O'
    else:
        return "O","X"

def place_marker(board, marker, position):
    board[position]=marker
    return position

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

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position] == " "

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    # board is full
    return True

def player_choise(board):
    position = 0
    while position not in range(1,10) or not space_check(board, position): # in [1,2,3,4,5,6,7,8,9]
        position = int(input("Choose a position: (1-9)"))
    return position


def replay():
    choice = input("Play again? Enter Yes or No")
    return choice


# MAIN PART OF THE CODE:

# WHILE LOOP TO KEEP RUNNING THE GAME
print("Welcome to game")

while True:
    # PLAY THE GAME

    ## SET EVERYTHING UP (BOARD, WHOS FIRST, CHOOSE MARKERS X,O)
    the_board = [' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')
    play_game = input("Ready to play? y or n")
    if play_game == "y":
        game_on = True
    else:
        game_on = False

    ## GAME PLAY
    while game_on:
        ### PLAYER ONE TURN
        if turn == "Player 1":
            #show the board
            display_board(the_board)
            # choose a position
            position = player_choise(the_board)
            # place the marker on the position
            place_marker(the_board, player1_marker, position)

            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!!')
                game_on = False
            else:
                # or check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    # No tie and no win? Then next player's turn
                    turn = "Player 2"



        else:
            ### PLAYER TWO TURN
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choise(the_board)
            # place the marker on the position
            place_marker(the_board, player2_marker, position)

            # check if they won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!!')
                game_on = False
            else:
                # or check if there is a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    # No tie and no win? Then next player's turn
                    turn = "Player 1"
                    
    # BREAK OUT OF THE WHILE LOOP ON replay()
    if not replay():
        break
