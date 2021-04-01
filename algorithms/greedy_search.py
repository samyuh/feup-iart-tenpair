# -- Imports -- #
# -- External Libraries -- #
import time
import threading

from queue import PriorityQueue

# Personal Libraries
from core.game import Game
from core.logic import Logic

class GreedySearch(threading.Thread):
    def __init__(self, game, callback=lambda: None):
        threading.Thread.__init__(self)
        self.game = game
        self.callback = callback

    def heuristic(self, matrix):
        return len([element for element in matrix if element !=  None]) / 2

    def run(self):
        """
        Running Greedy Algorithm
        """
        # Priority Queue to order by heuristic
        queue = PriorityQueue()
        game = self.game
        
        queue.put(game)

        visited = set()
        visited.add(repr(game.matrix))
        
        start = time.time()
        while True:
            game = queue.get()
            if game.isEmpty():
                end = time.time()
                print("Time elapsed: {}".format(end - start))
                print("Found a solution: ")
                print("Total Moves: {}".format(game.moves))
            
                self.callback(game.getFullGame())
                break  

            operationList = Logic.getAllMoves(game)
            newGameMoves = game.moves + 1
            
            for operation in operationList:
                newGame = Game(newGameMoves, game.dealValue, game.rows, game.columns, game.matrix.copy(),game)
                newGame.removePair(operation[0], operation[1])
                newGame.heuristic = self.heuristic(game.matrix.copy())
                if repr(newGame.matrix) not in visited:
                    visited.add(repr(newGame.matrix))
                    queue.put(newGame)

            gameDeal = Game(game.moves, game.dealValue + 1, game.rows, game.columns,game.matrix.copy(), game)
            Logic.deal(gameDeal)
            gameDeal.heuristic = self.heuristic(gameDeal.matrix.copy())
            if repr(gameDeal.matrix) not in visited:
                visited.add(repr(gameDeal.matrix))
                queue.put(gameDeal)
        
