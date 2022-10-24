import chess
import math
class IDSMiniMaxAI():
    def __init__(self, depth):
        self.max_depth = depth
        self.player = False
        self.best_move = None

    def choose_move(self, board):
        self.player = board.turn
        moves = self.minimax(board,0)
        print("IDS Minimax moves are ", moves)
        #reset
        self.best_move = None
        return moves

    def minimax(self,board,depth):
        for i in range(depth+1):
            self.max_depth = i
            v,move = self.maxVal(board,0)
            if not self.best_move:
                self.best_move = (v,move)
            else:
                if v > self.best_move[0]:
                    self.best_move = (v,move)
        return self.best_move[1]

    def evaluation(self, board):
        if board.is_checkmate() and board.outcome().winner == self.player:
            return math.inf
        vals = {'p': 1, 'n': 3, 'b': 3, 'r': 5, 'q': 9, 'k': 0}
        total = 0
        for squarename in chess.SQUARE_NAMES:
            piece = board.piece_at(chess.parse_square(squarename))
            if piece:
                name = piece.symbol().lower()
                color = piece.color
                val = vals[name]
                if color == self.player:
                    total += val
                else:
                    total -= val
        return total


    def cutoff_test(self, board, depth):
        #depth exceeding
        if depth > self.max_depth or board.is_game_over():

            return True
        return False

    def maxVal(self, board, depth):
        if self.cutoff_test(board, depth):
            # if board.is_game_over() and board.outcome().winner == self.player:
            #     print("Minimax wins")
            return self.evaluation(board), None
        v = -math.inf
        children = list(board.legal_moves)
        move = None

        for child in children:
            board.push(child)
            nextv, nextmoves = self.minVal(board,depth+1)
            if nextv > v:
                v = nextv
                move = child
            board.pop()
        if move:
            return v, move
        else:
            return v, None

    def minVal(self, board, depth):
        if self.cutoff_test(board, depth):
            # if board.is_game_over() and board.outcome().winner == self.player:
            #     print("Minimax wins")
            return self.evaluation(board), None
        v = math.inf
        children = list(board.legal_moves)
        move = None
        for child in children:
            board.push(child)
            nextv, nextmoves = self.maxVal(board,depth+1)
            if nextv < v:
                v = nextv
                move = child
            board.pop()
        if move:
            return v, move
        else:
            return v, None
