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
        self.game = game
        self.callback = callback

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
        # Priority Queue to order by heuristic
        queue = PriorityQueue()
        game = self.game
        game.heuristic = self.heuristic(game.matrix)
        
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
                newGame.heuristic = self.heuristic(newGame.matrix)
                if repr(newGame.matrix) not in visited:
                    visited.add(repr(newGame.matrix))
                    queue.put(newGame)

            gameDeal = Game(game.moves, game.dealValue + 1, game.rows, game.columns,game.matrix.copy(), game)
            Logic.deal(gameDeal)
            gameDeal.heuristic = self.heuristic(gameDeal.matrix)
            if repr(gameDeal.matrix) not in visited:
                visited.add(repr(gameDeal.matrix))
                queue.put(gameDeal)
        
