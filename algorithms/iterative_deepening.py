# -- Imports -- #
# -- External Libraries -- #
import time
import threading

from _collections import deque
from queue import PriorityQueue

# Personal Libraries
from core.game import Game
from core.logic import Logic

class IterativeDeepening(threading.Thread):
    def __init__(self, game, callback=lambda: None):
        threading.Thread.__init__(self)

        self.game = game
        self.callback = callback

    def heuristic(self, game, matrix):
        return len([element for element in matrix if element !=  None]) / 2

    def run(self):
        start = time.time()

        estimatedCost = self.heuristic(self.game,self.game.matrix)
        # Priority Queue to order by heuristic

        while True:
            distance = self.search([self.game,], 0, estimatedCost)
            if distance == 0:
                print("Found Solution")
                return 
            if distance == float("inf"):
                print("Can't Found")
                return
            estimatedCost = distance

        
    def search(self, path, distance, estimatedCost):
        game = path.pop(0)
        if game.isEmpty():
            return 0

        estimate = distance + self.heuristic(game,game.matrix)
        if estimate > estimatedCost:
             return estimate

        minValue = float("inf")

        operationList = Logic.getAllMoves(game)
        newGameMoves = game.moves + 1
        test = []
        for operation in operationList:
            newGame = Game(newGameMoves, game.dealValue, game.rows, game.columns, game.matrix.copy(), game)
            newGame.removePair(operation[0], operation[1])
            test.append([newGame, 1])

        if game.dealValue < 1:
            gameDeal = Game(game.moves, game.dealValue + 1, game.rows, game.columns,game.matrix.copy(), game)
            Logic.deal(gameDeal)
            test.append([gameDeal, 0])

        for i in test:
            t = self.search([i[0],], distance + i[1], estimatedCost)
            if t == 0:
                print(distance)
                return 0
            if t < minValue:
                print(t)
                i[0].printGame()
                minValue = t
            minValue = t

        return minValue