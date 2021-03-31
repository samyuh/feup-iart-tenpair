# -- Imports -- #
# -- External Libraries -- #
import time
import threading

from _collections import deque

# Personal Libraries
from core.game import Game
from core.logic import Logic

class IterativeDeepening(threading.Thread):
    def __init__(self, game, callback=lambda: None):
        threading.Thread.__init__(self)
        self.game = game
        self.callback = callback

    def run(self):
        start = time.time()
        for i in range(1, 999):
            game = Game(0, 0, self.game.rows, self.game.columns, self.game.matrix)
            game.heuristic = self.greedyHeuristic(self.game.matrix)
            print("Depth", i ,"attempt") 
            if (self.iterativeDeepeningAux(game, i)):
                end = time.time()
                print("Time elapsed: {}".format(end - start))
                break

    def greedyHeuristic(self, matrix):
        return len([element for element in matrix if element !=  None]) / 2
        
    def iterativeDeepeningAux(self, game, depth):
        """
            Iterative Deepening Algorithm
        """
        queue = deque([game])
        visited = set()

        while True:
            if (len(visited) % 10000 == 0):
                print("Visited: {} Remaining: {}".format(len(visited), len(queue)))
                
            
            if len(queue) == 0:
                print("failed depth ", depth)
                return False
            # Next GameState
            game = queue.pop()
            #game.printGame()

            
            if (game.moves + 1) == depth:
                continue  

            # Found a solution [Empty Matrix]
            if game.isEmpty():
                gameStates = game.getFullGame()
                self.callback(gameStates)
                game.printGameSequence()
                print("Found a solution: ")
                print("Total Moves: {}".format(game.moves))
                return True
            # Get available moves and add them to the queue
            else:
                append = queue.append

                operationList = Logic.getAllMoves(game)
                #removePair = game.removePair

                newGameMoves = game.moves + 1
                for operation in operationList:
                    newGame = Game(newGameMoves,game.dealValue, game.rows, game.columns, game.matrix.copy(), game)
                    newGame.removePair(operation[0], operation[1])
                    if repr(newGame.matrix) not in visited:
                        visited.add(repr(newGame.matrix))
                        append(newGame)

                if game.dealValue < 1:
                    gameDeal = Game(game.moves, game.dealValue + 1, game.rows, game.columns,game.matrix.copy(), game)
                    Logic.deal(gameDeal)
                    if repr(gameDeal.matrix) not in visited:
                        visited.add(repr(gameDeal.matrix))
                        append(gameDeal)