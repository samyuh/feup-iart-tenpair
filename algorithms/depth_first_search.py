# -- Imports -- #
# -- External Libraries -- #
import time
import threading

from _collections import deque

# Personal Libraries
from core.game import Game
from core.logic import Logic

class DepthFirstSearch(threading.Thread):
    """
    A class used to run the Depth First Search algorithm 

    Attributes
    ----------
    game : Game
      - The initial Game State to run the algorithm
      
    callback : Callback
      - callback used to return the gamestate to the caller thread after if shutsdown

    """
    def __init__(self, game, callback=lambda: None):
        """
        Constructor method for initializing the Depth First Search algorithm

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
        Method called to run the Depth First Search Algorithm
        This algorithm traverses the possible moves of the game by starting at the root node and and exploring each branch of a game sequence as far as possible until no more moves are avaliable
        """

        # rows, columns, gameState = deal(rows, columns, gameState.copy())
        # Double Ended Queue to allow O(1) pop and append
        # Set to check if an element was already visited in O(1)
        game = self.game
        queue = deque([game])
        visited = set()

        start = time.time()
        while True:
            if (len(visited) % 10000 == 0):
                print("Visited: {} Remaining: {}".format(len(visited), len(queue)))
            
            try:
                # Next GameState
                game = queue.pop()
            except IndexError as e:
                print("DFS is only accepting boards that can be solved with one deal.")
                self.callback([])
                break

            # Found a solution [Empty Matrix]
            if game.isEmpty():
                print("Found a solution: ")
                print("Total Moves: {}".format(game.moves))
                print("Time elapsed: {}".format(time.time() - start))

                self.callback(game.getFullGame())
                break
            # Get available moves and add them to the queue
            else:
                append = queue.append

                operationList = Logic.getAllMoves(game)
                #removePair = game.removePair

                newGameMoves = game.moves + 1
                for operation in operationList:
                    newGame = Game(newGameMoves,game.dealValue, game.rows, game.columns, game.matrix.copy(),game)
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

        
        