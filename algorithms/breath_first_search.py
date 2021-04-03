# -- Imports -- #
# -- External Libraries -- #
import time
import threading

from _collections import deque

# Personal Libraries
from core.game import Game
from core.logic import Logic

MAX_DEALS = 1

class BreathFirstSearch(threading.Thread):
    """
    A class used to run the Breadth First Search algorithm 

    Attributes
    ----------
    game : Game
      - The initial Game State to run the algorithm
      
    callback : Callback
      - callback used to return the gamestate to the caller thread after if shutsdown

    """
    def __init__(self, game, callback=lambda: None):
        """
        Constructor method for initializing the Breadth First Search algorithm

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
        Method called to run the Breadth First Search Algorithm.
        This algorithm finds the solution by searching all possible moves before advancing to the next move, traversing all possibilities moves until a solution is found(if possible) 
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
                game = queue.popleft()
            except IndexError as e:
                print("BFS is only accepting boards that can be solved with one deal.")
                self.callback([])
                return

            # Found a solution [Empty Matrix]
            if game.isEmpty():
                print("Found a solution: ")
                print("Total Moves: {}".format(game.moves))
                print("Time elapsed: {}".format(time.time() - start))

                gameStates = game.getFullGame()
                self.callback(gameStates)
                break
            # Get available moves and add them to the queue
            else:
                append = queue.append

                operationList = Logic.getAllMoves(game)
                newGameMoves = game.moves + 1
                for operation in operationList:
                    newGame = Game(newGameMoves, game.dealValue, game.rows, game.columns, game.matrix.copy(), game)
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