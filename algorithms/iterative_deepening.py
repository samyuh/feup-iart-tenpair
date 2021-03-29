# -- Imports -- #
# -- External Libraries -- #
import time
import threading

from _collections import deque

# Personal Libraries
from core.game import Game
from core.logic import Logic

class IterativeDeepening(threading.Thread):
    """
    A class used to run the Iterative Deepening Algorithm 
    """
    def __init__(self, callback=lambda: None):
        """
        Constructor method for initializing theIterative Deepening algorithm

        Attributes
        ----------
        callback : Callback
            callback used to return the gamestate to the caller thread after if shutsdown
                
        """
        threading.Thread.__init__(self)
        self.callback = callback

    def run(self):
        """
        Method called to run the Iterative Deepening Algorithm
        This algorithm runs a depth first search Algorithm with incremental depth increase until the solution is found
        """
        start = time.time()
        for i in range(1, 30):
            gameState = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    1, 1, 1, 2, 1, 3, 1, 4, 1, 
                    5, 1, 6, 1, 7, 1, 8, 1, 9]
            columns = 9
            rows = 3
            game = Game(0, 0, rows, columns, gameState)
            game.heuristic = self.heuristic(gameState)
            print("depth", i ,"attempt") 
            if (self.iterativeDeepeningAux(game, i)):
                end = time.time()
                print("Time elapsed: {}".format(end - start))

    def heuristic(self, matrix):
        """
        Calculates the game heuristic, based on the ammount of pairs avaliable on the board.

        Attributes
        ----------
        matrix : list of int 
            flattened list of the game State.
        Returns
        -------
        int
            returns the number of avaliable pairs of the board, which is a value that represents the heuristic of a Game.

        """
        return len([element for element in matrix if element !=  None]) / 2
        
    def iterativeDeepeningAux(self, game, depth):
        """ 
        Method used to run the algorithm iteratively by continously changing the depth if the solution is not found
        """
        # rows, columns, gameState = deal(rows, columns, gameState.copy())
        # Double Ended Queue to allow O(1) pop and append
        # Set to check if an element was already visited in O(1)
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
                
                if (newGameMoves) == depth:
                    continue 

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