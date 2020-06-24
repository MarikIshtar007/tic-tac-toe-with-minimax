from math import inf
import time
from random import randint
from colored_io import *

recur_call = 0

human = +1
comp = -1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def show_board(board, player_key, comp_key):
    number = 1
    play_dico = {
        +1: player_key,
        -1: comp_key,
        0: ''
    }
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                print(str(number).center(6), end="")
            elif board[i][j] == +1:
                print(f"\033[91m {play_dico[board[i][j]]}\033[00m".center(16), end="")
            elif board[i][j] == -1:
                print(f"\033[96m {play_dico[board[i][j]]}\033[00m".center(16), end="")
            if j != 2:
                print("\033[93m {}\033[00m".format('|'), end="")
            number += 1
        print()
        if i != 2:
            prYellow("---------------------", endo="\n")
    print("")


def win(board, pl):
    winnin_pos = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    for posi in winnin_pos:
        temp = []
        for position in posi:
            x, y = position
            temp.append(board[x][y])
        if temp[0] == pl and (temp.count(temp[0]) == len(temp)):
            return True
    return False


# def is_empty(board):
#     empty_places = []
#
#     for i, row in enumerate(board):
#         for j, cell in enumerate(row):
#             if cell == 0:
#                 empty_places.append([i, j])
#     return empty_places

def get_depth(board):
    depth = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                depth += 1
    return depth

def evaluate(board):
    if win(board, comp):
        score = -1
    elif win(board, human):
        score = +1
    else:
        score = 0
    return score


def minimax(board, depth, player):
    global recur_call
    recur_call += 1
    if player == comp:
        best_x = -1
        best_y = -1
        best_score = +inf
    else:
        best_x = -1
        best_y = -1
        best_score = -inf

    if depth == 0 or win(board, human) or win(board, comp):
        return -1, -1, evaluate(board)

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = player
                _, _, c_score = minimax(board, depth - 1, -player)
                board[i][j] = 0
                c_i, c_j = i, j

                if player == comp:
                    if c_score < best_score:
                        best_score = c_score
                        best_x = c_i
                        best_y = c_j
                else:
                    if c_score > best_score:
                        best_score = c_score
                        best_x = c_i
                        best_y = c_j

    return best_x, best_y, best_score


def comp_turn(player_key, comp_key):
    global recur_call
    depth = get_depth(board)
    if depth == 0 or win(board, human) or win(board, comp):
        return
    print("It's the Computer's turn...\n")
    time.sleep(1.4)
    if depth == 9:
        i = randint(0, 2)
        j = randint(0, 2)
    else:
        i, j, _ = minimax(board, depth, comp)

    if board[i][j] == 0:
        board[i][j] = comp
    else:
        return
    time.sleep(1)
    print(f'The computer has searched {recur_call} possibilities and made a choice.')
    show_board(board, player_key, comp_key)
    recur_call = 0


def player_turn(player_key, comp_key):
    if get_depth(board) == 0:
        return
    if win(board, human):
        return

    loc = input("Its your turn now. Enter a value 1-9.\n")
    dico = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
            '4': (1, 0), '5': (1, 1), '6': (1, 2),
            '7': (2, 0), '8': (2, 1), '9': (2, 2)
            }
    while loc not in dico:
        loc = input("Enter proper cell number\n")
    x, y = dico[loc]
    if board[x][y]== 0:
        board[x][y] = human
    else:
        print("That's an illegal move. You lost your turn.")
        time.sleep(1)
    show_board(board, player_key, comp_key)


def main():
    print("Welcome to the Game of Tic Tac Toe.. played by a Machine!!")
    print("Can you Beat it?.. ")
    time.sleep(1.6)
    player_key = input("\n\n Would you like to be X or O ?\n\n").upper()
    while player_key.lower() != 'x' and player_key.lower() != 'o':
        player_key = input("Please enter a valid choice. Either X or O\n").upper()
    if player_key == 'X':
        comp_key = 'O'
        comp1 = False
    else:
        comp_key = 'X'
        comp1 = True
    print(f'You have chosen {player_key}.')
    time.sleep(2)
    print(f'The Computer gets the {comp_key}.')
    time.sleep(2)
    print("As a rule.... X always goes first..")

    # players = itertools.cycle(['X', 'O'])
    # if player == 'O':
    #     curr_player = next(players)
    #     curr_player = next(players)
    # else:
    #     curr_player = next(players)
    #     print("the current player is ", curr_player)
    # show_board(board)
    # print("The Grid locations are  1 - 9.")
    # print("Enter the grid location to place your", curr_player)

    # Actual game loop starts

    # Actual Game loop
    show_board(board, player_key, comp_key)
    while get_depth(board) != 0:
        if comp1:
            comp_turn(player_key=player_key, comp_key=comp_key)
            comp1 = False
        player_turn(player_key, comp_key)
        comp_turn(player_key, comp_key)
        if win(board, comp) or win(board, human):
            break

    if win(board, human):
        print("You Won")
    elif win(board, comp):
        print("You LOST!")
    else:
        print("It's a draw")
    exit()


if __name__ == "__main__":
    main()
