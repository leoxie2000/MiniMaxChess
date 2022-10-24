# pip3 install python-chess


import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from IDSMiniMaxAI import IDSMiniMaxAI

import sys


player1 = HumanPlayer()
player2 = RandomAI()
player3 = MinimaxAI(1)
player4 = AlphaBetaAI(2)
player5 = IDSMiniMaxAI(2)
game = ChessGame(player2, player5)

while not game.is_game_over():
    print(game)
    game.make_move()

print(game.result())
#print(hash(str(game.board)))
