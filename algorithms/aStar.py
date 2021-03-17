# Personal Libraries
from core.game import Game
from queue import PriorityQueue
import time

def greedyHeuristic(matrix):
    return len([element for element in matrix if element !=  None]) / 2

def aStar(game):
    """
    A* Algorithm
    """
    # Priority Queue to order by heuristic
    queue = PriorityQueue()
    queue.put(game)

    visited = set()
    visited.add(repr(game.matrix))


    start = time.time()
    while True:
        game = queue.get()
        if game.isEmpty():
            game.printGameSequence()
            print("Found a solution: ")
            print("Total Moves: {}".format(game.moves))
            break  

        operationList = game.getAllMoves()
        newGameMoves = game.moves + 1
        for operation in operationList:
            newGame = Game(newGameMoves, game.dealValue, game.rows, game.columns, game.matrix.copy(), game)
            newGame.removePair(operation[0], operation[1])
            newGame.heuristic = newGameMoves + greedyHeuristic(game.matrix.copy())
            if repr(newGame.matrix) not in visited:
                visited.add(repr(newGame.matrix))
                queue.put(newGame)

        #rowsDeal, columnsDeal, gameStateDeal = game.deal(game.rows, game.columns, game.matrix.copy())
        gameDeal = Game(game.moves, game.dealValue + 1, game.rows, game.columns,game.matrix.copy(), game)
        gameDeal.deal()
        gameDeal.heuristic = game.moves + greedyHeuristic(gameDeal.matrix.copy())
        if repr(gameDeal.matrix) not in visited:
            visited.add(repr(gameDeal.matrix))
            queue.put(gameDeal)
        

        #print("Paths Chosen: {} Heuristic {}".format(queue.qsize, game.heuristic))
    end = time.time()
    print("Time elapsed: {}".format(end - start))
    

def aStarThread():
    gameState = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                1, 1, 1, 2, 1, 3, 1, 4, 1, 
                5, 1, 6, 1, 7, 1, 8, 1, 9]
    columns = 9
    rows = 3
    game = Game(0, 0, rows, columns, gameState)
    game.heuristic = greedyHeuristic(gameState)

    print("Starting AStar")
    aStar(game)