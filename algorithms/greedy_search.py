# -- Imports -- #
# -- External Libraries -- #
import time
import threading

from queue import PriorityQueue

# Personal Libraries
from core.game import Game
from core.logic import Logic

class GreedySearch(threading.Thread):
    """
    A class used to run the Greedy Search Algorithm

    Attributes
    ----------
    game : Game
      - The initial Game State to run the algorithm
      
    callback : Callback
      - callback used to return the gamestate to the caller thread after if shutsdown

    heuristic : int
      - Integer containing the value for the game heuristic used in this algorithm

    """
    def __init__(self, game, callback=lambda: None):
        """
        Constructor method for initializing the Greedy Search Algorithm

        Parameters
        ----------

        game : Game
          - The initial Game State to run the algorithm
        callback : Callback
          - callback used to return the gamestate to the caller thread after if shutsdown
                
        """
        threading.Thread.__init__(self)
        self.callback = callback
        self.game = game

    def heuristic(self, matrix):
        """
        Calculates the game heuristic, based on the ammount of pairs avaliable on the board.

        Parameters
        ----------
        matrix : list of int 
          - flattened list of the game State.
        Returns
        -------
        int
          - returns the number of avaliable pairs of the board, which is a value that represents the heuristic of a Game.

        """
        return len([element for element in matrix if element !=  None]) / 2

    def run(self):
        """
        Method called to run the Greedy Search Algorithm.
        This algorithm uses an heuristic to suggest the following best move and calculate and aproximate optimal solution

        """
        game = self.game
        # Priority Queue to order by heuristic
        queue = PriorityQueue()
        queue.put(game)

        visited = set()
        visited.add(repr(game.matrix))
        
        start = time.time()
        while True:
            game = queue.get()
            if game.isEmpty():
                end = time.time()
                print("Time elapsed: {}".format(end - start))
                
                gameStates = game.getFullGame()
                self.callback(gameStates)
                print("Found a solution: ")
                print("Total Moves: {}".format(game.moves))
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
        
