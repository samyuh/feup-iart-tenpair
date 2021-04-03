# -- Imports -- #
# -- External Libraries -- #
import time
import threading

from _collections import deque

# Personal Libraries
from core.game import Game
from core.logic import Logic

MAX_DEALS = 1

class IterativeDeepening(threading.Thread):
    """
    A class used to run the Iterative Deepening Algorithm 

    Attributes
    ----------
    game : Game
      - The initial Game State to run the algorithm
      
    callback : Callback
      - callback used to return the gamestate to the caller thread after if shutsdown

    """
    def __init__(self, game, callback=lambda: None):
        """
        Constructor method for initializing theIterative Deepening algorithm

        Parameters
        ----------
        game : Game
          - The initial Game State to run the algorithm
          
        callback : Callback
          - callback used to return the gamestate to the caller thread after if shutsdown
                
        """
        threading.Thread.__init__(self)
        self.game = game
        self.callback = callback

    def run(self):
        """
        Method called to run the Iterative Deepening Algorithm
        This algorithm runs a depth first search Algorithm with incremental depth increase until the solution is found
        """
        start = time.time()
        for i in range(1, 999):
            game = Game(0, 0, self.game.rows, self.game.columns, self.game.matrix)
            print("Depth", i ,"attempt") 
            if (self.iterativeDeepeningAux(game, i)):
                end = time.time()
                print("Time elapsed: {}".format(end - start))
                break
        
    def iterativeDeepeningAux(self, game, depth):
        """ 
        Method used to run the algorithm iteratively by continously changing the depth if the solution is not found
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
  
            if game.moves == depth:
                continue  

            # Found a solution [Empty Matrix]
            if game.isEmpty():
                print("Found a solution: ")
                print("Total Moves: {}".format(game.moves))

                gameStates = game.getFullGame()
                self.callback(gameStates)
                return True
            # Get available moves and add them to the queue
            else:
                append = queue.append

                operationList = Logic.getAllMoves(game)
                #removePair = game.removePair

                newGameMoves = game.moves + 1
                
                if (newGameMoves) == depth:
                    continue 

                for operation in operationList:
                    newGame = Game(newGameMoves,game.dealValue, game.rows, game.columns, game.matrix.copy(), game)
                    newGame.removePair(operation[0], operation[1])
                    if repr(newGame.matrix) not in visited:
                        visited.add(repr(newGame.matrix))
                        append(newGame)

                if game.dealValue < MAX_DEALS:
                    gameDeal = Game(game.moves, game.dealValue + 1, game.rows, game.columns,game.matrix.copy(), game)
                    Logic.deal(gameDeal)
                    if repr(gameDeal.matrix) not in visited:
                        visited.add(repr(gameDeal.matrix))
                        append(gameDeal)