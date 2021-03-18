# -- Imports -- #
# -- External Libraries -- #
import time
import threading

from _collections import deque

# Personal Libraries
from core.game import Game

class BreathFirstSearch(threading.Thread):
    def __init__(self, callback=lambda: None):
        threading.Thread.__init__(self)
        self.callback = callback

        gameState = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    1, 1, 1, 2, 1, 3, 1, 4, 1, 
                    5, 1, 6, 1, 7, 1, 8, 1, 9]
        columns = 9
        rows = 3
        self.game = Game(0, 0, rows, columns, gameState)

    def run(self):
        """
            Breath First Search Algorithm
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
            
            # Next GameState
            game = queue.popleft()

            # Found a solution [Empty Matrix]
            if game.isEmpty():
                game.printGameSequence()
                print("Found a solution: ")
                print("Total Moves: {}".format(game.moves))
                break
            # Get available moves and add them to the queue
            else:
                append = queue.append

                operationList = game.getAllMoves()
                newGameMoves = game.moves + 1
                for operation in operationList:
                    newGame = Game(newGameMoves, game.dealValue, game.rows, game.columns, game.matrix.copy(), game)
                    newGame.removePair(operation[0], operation[1])
                    if repr(newGame.matrix) not in visited:
                        visited.add(repr(newGame.matrix))
                        append(newGame)
                
                if game.dealValue < 1:
                    gameDeal = Game(game.moves, game.dealValue + 1, game.rows, game.columns,game.matrix.copy(), game)
                    gameDeal.deal()
                    if repr(gameDeal.matrix) not in visited:
                        visited.add(repr(gameDeal.matrix))
                        append(gameDeal)

        end = time.time()
        self.callback()
        print("Time elapsed: {}".format(end - start))

