import game_logic as game
from random import randint
import math
class AI:
    name = "Default"
    team = -1

    def __init__(self,team):
        self.name="Default"
        self.team=team

    def make_move(self,board):
        return 0
class InputPlayer(AI):
    name = "Player"

    def __init__(self, team):
        super().__init__(team)
        self.name="Player"

    def make_move(self,board):
        return int(input("Make Move (0-6):\n"))


class RandomPlayer(AI):
    name = "Random"

    def __init__(self,team):
        super().__init__(team)
        self.name="Random"

    def make_move(self,board):
        valid_moves = []
        for i in range(0,game.BOARD_SIZE[0]):
            if game.get_y_of(board,i)!=-1:
                valid_moves.append(i)
        return valid_moves[randint(0,len(valid_moves)-1)]


game.ai_classes.append(RandomPlayer)


class Minimax(AI):
    # Loss function is how many the opponent has in a row.
    name = "Minimax"

    def __init__(self,team,depth=2):
        super().__init__(team)
        self.depth = depth
        self.other_team = game.RED if self.team == game.BLACK else game.BLACK

    def value_of(self, board):
        if isinstance(board,int) or isinstance(board,float):
            return board
        win = game.check_game_end(board)
        if win == self.team:
            loss = -1000 + game.pieces_on_board(board)
        elif win == self.other_team:
            loss = 1000 - game.pieces_on_board(board)
        else:
            loss = game.in_row(board, self.other_team) - 0.2*game.in_row(board,self.team)
        return loss

    def choose_val(self,values,evaluator=max):
        max_indices = []
        max_val = evaluator(values)
        for i in range(0,len(values)):
            if values[i] == max_val:
                max_indices.append(i)
        return max_indices[randint(0,len(max_indices)-1)], max_val

    def get_boards(self, board,team):
        boards = []
        if isinstance(board,int) or isinstance(board,float):
            return [board]
        if game.check_game_end(board) != -1:
            return [self.value_of(board)]
        for i in range(0, 7):
            new_board, valid = game.make_move(board, i, team)
            if not valid:
                boards.append(1000000 if team == self.team else -1000000)
            else:
                boards.append(new_board)
        return boards

    def make_move(self,board):
        boards = self.get_boards(board,self.team)
        return self.choose_move(boards)[0]

    def choose_move(self,boards,layer=1):
        playing = self.team if layer % 2 == 0 else self.other_team
        if layer==self.depth:
            values = []
            for board in boards:
                value = self.value_of(board)
                values.append(value)
            val = self.choose_val(values,max if playing==self.team else min)
            return val
        else:
            values = []
            for i in range(0,len(boards)):
                new_boards = self.get_boards(boards[i],playing)
                val = self.choose_move(new_boards,layer+1)
                values.append(val[1])
            val = self.choose_val(values,max if playing==self.team else min)
            return val


game.ai_classes.append(Minimax)


class MinimaxD4(Minimax):
    # Loss function is how many the opponent has in a row.
    name = "MinimaxD4"

    def __init__(self,team,depth=4):
        super().__init__(team)
        self.depth = depth
        self.other_team = game.RED if self.team == game.BLACK else game.BLACK


game.ai_classes.append(MinimaxD4)

class Sweeper(AI):
    name = "Sweeper"

    def __init__(self,team):
        super().__init__(team)
        self.location = randint(-1,5)
        self.direction = 1

    def make_move(self,board):
        # This is where your logic will go. This default AI will always go in the leftmost column.
        if self.location == 0:
            self.direction=1
        elif self.location==6:
            self.direction=-1
        self.location+=self.direction
        if game.check_game_end(board) != -1:
            return 0
        while game.get_y_of(board,self.location) == -1:
            self.location+=self.direction
        return self.location


game.ai_classes.append(Sweeper)

class Hierarchy(AI):
    # Change "Template" to your AI's name
    name = "Hierarchy"

    def __init__(self,team):
        super().__init__(team)
        self.hierarchy = [self.win,self.block_win,self.make_trap,self.block_trap,self.threaten_win,self.stop_threaten,self.increase_row,self.stop_increase_row]
        self.other_team = 2 if self.team==1 else 1

    def win(self,board,team=-1):
        if team==-1:
            team=self.team
        wcons = game.win_conditions(board,team)
        if len(wcons)==0:
            return -1
        return wcons[randint(0,len(wcons)-1)]

    def block_win(self,board):
        return self.win(board,self.other_team)

    def make_trap(self,board,team=-1):
        if team==-1:
            team=self.team
        boards = game.next_boards(board,team)
        for i in range(0,len(boards)):
            if len(game.win_conditions(boards[i],team))>=2:
                return i
        return -1

    def block_trap(self,board):
        return self.make_trap(board,team=self.other_team)

    def threaten_win(self,board,team=-1):
        if team==-1:
            team=self.team
        other_team = 1 if team==2 else 2
        boards = game.next_boards(board,team)
        moves = []
        for i in range(0,len(boards)):
            if len(game.win_conditions(boards[i],other_team))>0:
                continue
            conditions = len(game.win_conditions(boards[i],team))
            if conditions>0:
                moves.append(i)
        if len(moves)==0:
            return -1
        return moves[randint(0,len(moves)-1)]

    def stop_threaten(self,board):
        return self.threaten_win(board,self.other_team)

    def increase_row(self,board,team=-1):
        if team==-1:
            team=self.team
        boards = game.next_boards(board,team)
        current_score = game.in_row(board,team)
        moves=[]
        for i in range(0,len(boards)):
            if game.in_row(boards[i],team)>current_score:
                moves.append(i)
        if len(moves)==0:
            return -1
        return moves[randint(0,len(moves)-1)]

    def stop_increase_row(self,board):
        return self.increase_row(board,self.other_team)

    def make_move(self,board):
        for move in self.hierarchy:
            do_move = move(board)
            if do_move != -1 and game.is_valid_move(board,do_move):
                return do_move
        # Choose random valid move if no choices apply
        valid_moves = []
        for i in range(0, game.BOARD_SIZE[0]):
            if game.get_y_of(board, i) != -1:
                valid_moves.append(i)
        return valid_moves[randint(0, len(valid_moves) - 1)]


# Change "Template" to your AI's name
game.ai_classes.append(Hierarchy)


# Here's what you edit
class Template(AI):
    # Change "Template" to your AI's name
    name = "Default"

    def __init__(self,team):
        super().__init__(team)

    def make_move(self,board):
        # This is where your logic will go. This default AI will always go in the leftmost column.
        return 0

# Change "Template" to your AI's name
game.ai_classes.append(Template)

class GUACAMOLE_MAN(AI):
    # Change "Template" to your AI's name
    name = "GUACAMOLE_MAN"

    def __init__(self,team,depth=5):
        super().__init__(team)
        self.GUACAMOLE_MAN = [self.win,self.block_win,self.strat,self.block_trap,self.choose_move,self.make_trap,self.threaten_win]
        self.depth = depth
        self.other_team = game.RED if self.team == game.BLACK else game.BLACK

    def win(self,board,team=-1):
        if team==-1:
            team=self.team
        wcons = game.win_conditions(board,team)
        if len(wcons)==0:
            return -1
        return wcons[randint(0,len(wcons)-1)]

    def block_win(self,board):
        return self.win(board,self.other_team)

    def make_trap(self,board,team=-1):
        if team==-1:
            team=self.team
        boards = game.next_boards(board,team)
        for i in range(0,len(boards)):
            if len(game.win_conditions(boards[i],team))>=2:
                return i
        return -1

    def block_trap(self,board):
        return self.make_trap(board,team=self.other_team)

    def threaten_win(self,board,team=-1):
        if team==-1:
            team=self.team
        other_team = 1 if team==2 else 2
        boards = game.next_boards(board,team)
        moves = []
        for i in range(0,len(boards)):
            if len(game.win_conditions(boards[i],other_team))>0:
                continue
            conditions = len(game.win_conditions(boards[i],team))
            if conditions>0:
                moves.append(i)
        if len(moves)==0:
            return -1
        return moves[randint(0,len(moves)-1)]

    def value_of(self, board):
        if isinstance(board,int) or isinstance(board,float):
            return board
        win = game.check_game_end(board)
        if win == self.team:
            loss = -1000 + game.pieces_on_board(board)
        elif win == self.other_team:
            loss = 1000 - game.pieces_on_board(board)
        else:
            loss = game.in_row(board, self.other_team) - 0.2*game.in_row(board,self.team)
        return loss

    def choose_val(self,values,evaluator=max):
        max_indices = []
        max_val = evaluator(values)
        for i in range(0,len(values)):
            if values[i] == max_val:
                max_indices.append(i)
        return max_indices[randint(0,len(max_indices)-1)], max_val

    def get_boards(self, board,team):
        boards = []
        if isinstance(board,int) or isinstance(board,float):
            return [board]
        if game.check_game_end(board) != -1:
            return [self.value_of(board)]
        for i in range(0, 7):
            new_board, valid = game.make_move(board, i, team)
            if not valid:
                boards.append(1000000 if team == self.team else -1000000)
            else:
                boards.append(new_board)
        return boards


    def value_of(self, board):
        if isinstance(board,int) or isinstance(board,float):
            return board
        win = game.check_game_end(board)
        if win == self.team:
            loss = -1000 + game.pieces_on_board(board)
        elif win == self.other_team:
            loss = 1000 - game.pieces_on_board(board)
        else:
            loss = game.in_row(board, self.other_team) - 0.2*game.in_row(board,self.team)
        return loss

    def choose_val(self,values,evaluator=max):
        max_indices = []
        max_val = evaluator(values)
        for i in range(0,len(values)):
            if values[i] == max_val:
                max_indices.append(i)
        return max_indices[randint(0,len(max_indices)-1)], max_val

    def get_boards(self, board,team):
        boards = []
        if isinstance(board,int) or isinstance(board,float):
            return [board]
        if game.check_game_end(board) != -1:
            return [self.value_of(board)]
        for i in range(0, 7):
            new_board, valid = game.make_move(board, i, team)
            if not valid:
                boards.append(1000000000 if team == self.team else -1000000000)
            else:
                boards.append(new_board)
        return boards

    def make_move(self,board):
        boards = self.get_boards(board,self.team)
        return self.choose_move(boards)[0]
    
    def strat(self,board):
        if team==-1:
            team=self.team
        other_team = 1 if team==2 else 2
        if board[0][3] != self.team and board[0][3] != other_team:
            return 3
        else:
            return -1

    def choose_move(self,boards,layer=1):
        playing = self.team if layer % 2 == 0 else self.other_team
        if layer==self.depth:
            values = []
            for board in boards:
                value = self.value_of(board)
                values.append(value)
            val = self.choose_val(values,max if playing==self.team else min)
            return val
        else:
            values = []
            for i in range(0,len(boards)):
                new_boards = self.get_boards(boards[i],playing)
                val = self.choose_move(new_boards,layer+1)
                values.append(val[1])
            val = self.choose_val(values,max if playing==self.team else min)
            return val

game.ai_classes.append(GUACAMOLE_MAN)

class BasicallyMinimax(AI):
    # Loss function is how many the opponent has in a row.
    name = "BasicallyMinimax"

    def __init__(self,team,depth=3):
        super().__init__(team)
        self.depth = depth
        self.other_team = game.RED if self.team == game.BLACK else game.BLACK
        print(team)

    def value_of(self, board):
        if isinstance(board,int) or isinstance(board,float):
            return board
        win = game.check_game_end(board)
        if win == self.team:
            loss = -1000 + game.pieces_on_board(board)
        elif win == self.other_team:
            loss = 1000 - game.pieces_on_board(board)
        else:
            loss = game.in_row(board, self.other_team) - 0.25*game.in_row(board,self.team)
        return loss

    def choose_val(self,values,evaluator=max):
        max_indices = []
        max_val = evaluator(values)
        for i in range(0,len(values)):
            if values[i] == max_val:
                max_indices.append(i)
        return max_indices[randint(0,len(max_indices)-1)], max_val

    def get_boards(self, board,team):
        boards = []
        if isinstance(board,int) or isinstance(board,float):
            return [board]
        if game.check_game_end(board) != -1:
            return [self.value_of(board)]
        for i in range(0, 7):
            new_board, valid = game.make_move(board, i, team)
            if not valid:
                boards.append(1000000 if team == self.team else -1000000)
            else:
                boards.append(new_board)
        return boards

    def make_move(self,board):
        boards = self.get_boards(board,self.team)
        return self.choose_move(boards)[0]

    def choose_move(self,boards,layer=1):
        playing = self.team if layer % 2 == 0 else self.other_team
        if layer==self.depth:
            values = []
            for board in boards:
                value = self.value_of(board)
                values.append(value)
            val = self.choose_val(values,max if playing==self.team else min)
            return val
        else:
            values = []
            for i in range(0,len(boards)):
                new_boards = self.get_boards(boards[i],playing)
                val = self.choose_move(new_boards,layer+1)
                values.append(val[1])
            val = self.choose_val(values,max if playing==self.team else min)
            return val


game.ai_classes.append(BasicallyMinimax)

class Jdestroyer(AI):
    # Loss function is how many the opponent has in a row.
    name = "Jdestroyer"

    def __init__(self,team,depth=5):
        super().__init__(team)
        self.depth = depth
        self.other_team = game.RED if self.team == game.BLACK else game.BLACK

    def value_of(self, board):
        if isinstance(board,int) or isinstance(board,float):
            return board
        win = game.check_game_end(board)
        if win == self.team:
            loss = -1000 + game.pieces_on_board(board)
        elif win == self.other_team:
            loss = 1000 - game.pieces_on_board(board)
        else:
            loss = game.in_row(board, self.other_team) - 0.2*game.in_row(board,self.team)
        return loss

    def choose_val(self,values,evaluator=max):
        max_indices = []
        max_val = evaluator(values)
        for i in range(0,len(values)):
            if values[i] == max_val:
                max_indices.append(i)
        return max_indices[randint(0,len(max_indices)-1)], max_val

    def get_boards(self, board,team):
        boards = []
        if isinstance(board,int) or isinstance(board,float):
            return [board]
        if game.check_game_end(board) != -1:
            return [self.value_of(board)]
        for i in range(0, 7):
            new_board, valid = game.make_move(board, i, team)
            if not valid:
                boards.append(1000000 if team == self.team else -1000000)
            else:
                boards.append(new_board)
        return boards

    def make_move(self,board):
        boards = self.get_boards(board,self.team)
        return self.choose_move(boards,True)[0]

    def choose_move(self,boards,maximizingPlayer,layer=1, alpha=-math.inf, beta=math.inf):
        playing = self.team if layer % 2 == 0 else self.other_team
        values = []
        if layer==self.depth:
            values = []
            for board in boards:
                value = self.value_of(board)
                values.append(value)
            val = self.choose_val(values,max if playing==self.team else min)
            return val
        if maximizingPlayer:
            best = -math.inf
            for i in range(0, len(boards)):
                new_boards = self.get_boards(boards[i],playing)
                val = self.choose_move(new_boards,False,layer+1, alpha, beta)
                values.append(val[1])
                best = min(best, val[0])
                alpha = min(alpha, best)
                if beta <= alpha:
                    break
            val = self.choose_val(values,max if playing==self.team else min)
            return val
        else:
            best = math.inf
            for i in range(0, len(boards)):
                new_boards = self.get_boards(boards[i], playing)
                val = self.choose_move(new_boards,True,layer+1, alpha, beta)
                values.append(val[1])
                best = max(val[0], best)
                beta = max(beta, best)
                if beta <= alpha:
                    break
            val = self.choose_val(values,max if playing==self.team else min)
            return val

game.ai_classes.append(Jdestroyer)