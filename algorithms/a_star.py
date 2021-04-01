# -- Imports -- #
# -- External Libraries -- #
import time
import threading



from queue import PriorityQueue

# Personal Libraries
from core.game import Game
from core.logic import Logic

class AStar(threading.Thread):
    def __init__(self, game, callback=lambda: None):
        threading.Thread.__init__(self)
        self.game = game
        self.callback = callback

    def heuristic(self, matrix):
        return len([element for element in matrix if element !=  None]) / 2

    def run(self):
        """
        A* Algorithm
        """
        print("Running A*")
        # Priority Queue to order by heuristic
        queue = PriorityQueue()
        # Visited List
        visited = set()

        # Starter State
        game = self.game
        game.heuristic = self.heuristic(game.matrix)

        queue.put(game)

        visited.add(repr(game.matrix))

        # Algorithm Start Time
        start = time.time()
        while True:
            game = queue.get()

            if game.isEmpty():
                end = time.time()
                print("Time elapsed: {}".format(end - start))
                print("Total Moves: {}".format(game.moves))

                gameStates = game.getFullGame()
                self.callback(gameStates)
                break  
            
            # Remove Pair
            operationList = Logic.getAllMoves(game)
            newGameMoves = game.moves + 1
            for operation in operationList:
                newGame = Game(newGameMoves, game.dealValue, game.rows, game.columns, game.matrix.copy(), game)
                newGame.removePair(operation[0], operation[1])
                newGame.heuristic = newGameMoves + self.heuristic(newGame.matrix)
                if repr(newGame.matrix) not in visited:
                    visited.add(repr(newGame.matrix))
                    queue.put(newGame)

            # Deal
            gameDeal = Game(game.moves, game.dealValue + 1, game.rows, game.columns,game.matrix.copy(), game)
            Logic.deal(gameDeal)
            gameDeal.heuristic = game.moves + self.heuristic(gameDeal.matrix)
            if repr(gameDeal.matrix) not in visited:
                visited.add(repr(gameDeal.matrix))
                queue.put(gameDeal)
            
        