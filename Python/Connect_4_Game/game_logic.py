from copy import deepcopy
import time
EMPTY = 0
RED = 1
BLACK = 2
BOARD_SIZE = (7,6)
# Board format: a 2D array that holds 0's that represent empty spaces, 1's that represent red pieces, and 2's that represent black pieces.
# The bottom layer is the FIRST array, the next highest the second, etc. This makes the code look nicer and makes the positive Y direction up.
ai_classes = []
def initialize_board():
    # Returns an empty board.
    this_board = []
    for i in range(0,BOARD_SIZE[1]):
        this_board.append([])
        for _ in range(0,BOARD_SIZE[0]):
            this_board[i].append(0)
    return this_board


# Don't change this variable.
EMPTY_BOARD = initialize_board()

def pieces_on_board(board):
    count=0
    for row in board:
        for value in row:
            if value != 0:
                count+=1
    return count


def get_y_of(board, move):
    # Returns the y location of a piece placed in location MOVE on board BOARD, so, where it will land when dropped. Bottom is 0, top is 6.
    # If the function returns -1, the column is full.
    for y in range(0, len(board)):
        if board[y][move]==EMPTY:
            return y
    return -1


def is_valid_move(board, move):
    return 0 <= move <= 6 and get_y_of(board, move) != -1


def make_move(board, move, team):
    # Board is the initial position of the board.
    # Move is a number 0 through 6 that represents where the piece will go (left to right)
    # Team is the piece that will be placed on the board, RED or BLACK
    # Function returns the board state after the move is made as well as a boolean representing whether the move was successful.
    new_board = deepcopy(board)
    place_y = get_y_of(board,move)
    if place_y==-1:
        return board, False
    new_board[place_y][move] = team
    return new_board, True


def print_board(board, empty_char="#", red_char="R", black_char="B"):
    # Prints the board in a human-readable way. By default, '#' is empty, 'R' is red, and 'B' is black. Can be changed.
    chars = [empty_char, red_char, black_char]
    for i in range(BOARD_SIZE[1]-1,-1,-1):
        this_str = ""
        for x in range(0, BOARD_SIZE[0]):
            this_str+=chars[board[i][x]] + " "
        print(this_str)


def in_row(board,team,max_val=4):
    # Returns maximum number of pieces in a row on board board by team team. It stops counting after max, which is 4 by default.
    max_num = 0
    for i in range(0,BOARD_SIZE[1]):
        for x in range(0, BOARD_SIZE[0]):
            if board[i][x]==team:
                this_num=1
                num_x = 1
                # Check to the right
                for num in range(x+1,BOARD_SIZE[0]):
                    if board[i][num]==team:
                        num_x+=1
                    else:
                        break
                num_y = 1
                for num in range(i+1,BOARD_SIZE[1]):
                    if board[num][x]==team:
                        num_y+=1
                    else:
                        break
                num_xy = 1
                x_plus,y_plus = 1,1
                while x+x_plus < BOARD_SIZE[0] and i+y_plus < BOARD_SIZE[1]:
                    if board[i+y_plus][x+x_plus]==team:
                        num_xy+=1
                    else:
                        break
                    x_plus+=1
                    y_plus+=1
                num_yx = 1
                x_minus,y_plus = 1,1
                while x-x_minus >= 0 and i+y_plus < BOARD_SIZE[1]:
                    if board[i+y_plus][x-x_minus]==team:
                        num_yx+=1
                    else:
                        break
                    x_minus+=1
                    y_plus+=1
                this_num=max([num_x,num_y,num_xy,num_yx])
                if max_num<this_num:
                    max_num = this_num
                    if max_num>=max_val:
                        return min(max_num,max_val)
    return min(max_num,max_val)


def win_conditions(board,team):
    winning_moves = []
    for i in range(0,BOARD_SIZE[0]):
        next_board, _ = make_move(board,i,team)
        if check_game_end(next_board) == team:
            winning_moves.append(i)
    return winning_moves


def check_game_end(board):
    # Returns the winner if there is one, 0 for a tie, -1 otherwise
    for i in range(1,3):
        if in_row(board,i)>=4:
            return i
    is_tie = True
    for i in range(0,BOARD_SIZE[1]):
        for x in range(0,BOARD_SIZE[0]):
            if board[i][x]==0:
                is_tie = False
                break
        if not is_tie:
            break
    return 0 if is_tie else -1

def next_boards(board,team):
    boards = []
    for i in range(0,7):
        boards.append(make_move(board,i,team)[0])
    return boards