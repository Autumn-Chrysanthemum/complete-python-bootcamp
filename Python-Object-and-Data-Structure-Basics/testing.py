import random


def display_board(board):
    print('\n'*100)
    print(board[7]+"|"+board[8]+"|"+ board[9])
    print("------")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print("------")
    print(board[1]+"|"+board[2]+"|"+board[3])


def player_input():
    while True:
        player1 = input("\n\n\n\n\nPlayer 1: Do you want to be 'X' or 'O'?\n\n\n")
        print('\n' * 5)
        if player1 == "X":
            # print("Player1 is 'X'")
            player2 = "O"
            break
        elif player1 == "O":
            # print("Player1 is 'O'")
            player2 = "X"
            break
        else:
            pass
    return player1, player2


def place_marker(board, marker, position):
    board[position] = marker
    return board


def win_check(board, marker):
    # return True if win combination is present
    return board[7] == board[8] == board[9] == marker or board[4] == board[5] == board[6] == marker or board[1] == board[2] == board[3] == marker or board[7] == board[5] == board[3] == marker or board[1] == board[5] == board[9] == marker or board[2] == board[5] == board[8] == marker or board[3] == board[6] == board[9] == marker or board[1] == board[4] == board[7] == marker


def choose_first():
    flip_coin = random.randint(1,2)
    print(f"\n\nI fliped a coin! Player {flip_coin} will go first")
    return flip_coin

# used
def space_check(board, position):
    # return True is position is freely available
    return board[position] == " "


def full_board_check(board):
    # return True is board is full
    for i in range(1,10):
        if space_check(board, i):
            return False
        else:
            continue
    print("\n\n\n@@@  Tie!!!  @@@")
    return True

# used
def replay():
    # return True if player wants to play
    return input("\n\nAre you ready to play again? Enter Yes or No.\n\n") == "Yes"


def play():
    # return True if player wants to play
    if input("Ready to play? Enter Yes or No.") == "Yes":
        return True
    if input("Ready to play? Enter Yes or No.") == "No":
        return False


def player_choice(board, current_turn, marker):
    position = int(input(f"\nPlayer {current_turn}, choose your next position for {marker}: (1-9)\n\n"))
    if space_check(board, position):
        return position
    else:
        print(f"\nPosition {position} is not empty, choose another one\n")
        return player_choice(board, current_turn, marker)

def your_turn(marker, board, current_turn):
    # print(f'marker is {marker}')
    place_marker(board, marker, player_choice(board,current_turn, marker))
    display_board(board)
    if win_check(board, marker):
        print(f"\n\n\nCongratulations Player {current_turn} you win!!!")
        global win_marker
        win_marker = 1
        return win_marker, current_turn
    else:
        s = {1,2}
        s.remove(current_turn)
        current_turn = s.pop()
        if current_turn == 1:
            marker = player1_marker
        else:
            marker = player2_marker

        return current_turn, marker


                      ###### GAME #######
print('\n'*10)
print("*** Welcome to Tic Tac Toe! ***")

while True:
    board = [' '] * 10
    win_marker = 0
    player1_marker, player2_marker = player_input()
    display_board(board)
    current_turn = choose_first()
    if current_turn == 1:
        marker = player1_marker
    else:
        marker = player2_marker

    while win_marker or not full_board_check(board):
        current_turn, marker = your_turn(marker, board, current_turn)
        # print(f"win_marker is {win_marker}")
        if win_marker == 1:
            break

    if not replay():
        print("\n\n\n&&&   End of the game!   &&&")
        break



