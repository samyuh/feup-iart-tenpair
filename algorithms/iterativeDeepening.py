# Personal Libraries
from core.game import Game
from core.ai import Ai

import time
from _collections import deque

def greedyHeuristic(matrix):
    return len([element for element in matrix if element !=  None]) / 2
    
def iterativeDeepeningAux(game, depth):
    """
        Iterative Deepening Algorithm
    """
    ai = Ai()
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

        
        if (game.moves + 1) == depth:
            continue  

        # Found a solution [Empty Matrix]
        if game.isEmpty():
            print("Found a solution: ")
            print("Total Moves: {}".format(game.moves))
            return True
        # GameState Already Visited
        elif repr(game.matrix) in visited:
            pass
        # Get available moves and add them to the queue
        else:
            visited.add(repr(game.matrix))
            append = queue.append

            operationList = ai.getAllMoves(game.rows, game.columns, game.matrix)
            #removePair = game.removePair

            newGameMoves = game.moves + 1
            for operation in operationList:
                newGame = Game(newGameMoves,game.dealValue, game.rows, game.columns, game.matrix.copy())
                newGame.removePair(operation[0], operation[1])
                append(newGame)

            if game.dealValue < 1:
                rowsDeal, columnsDeal, gameStateDeal = game.deal(game.rows, game.columns, game.matrix.copy())
                gameDeal = Game(game.moves, game.dealValue + 1, rowsDeal, columnsDeal, gameStateDeal)
                append(gameDeal)

def iterativeDeepening(maxDepth):
    start = time.time()
    for i in range(1, 28):
        gameState = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                      1, 1, 1, 2, 1, 3, 1, 4, 1, 
                      5, 1, 6, 1, 7, 1, 8, 1, 9]
        columns = 9
        rows = 3
        game = Game(0, 0, rows, columns, gameState)
        game.heuristic = greedyHeuristic(gameState)
        print("depth", i ,"attempt") 
        if (iterativeDeepeningAux(game, i)):
            end = time.time()
            print("Time elapsed: {}".format(end - start))
            return True

