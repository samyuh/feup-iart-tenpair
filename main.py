import copy
import time
from _collections import deque
from queue import PriorityQueue

 # Personal Libraries
from core.game import Game
from core.ai import Ai

from queue import PriorityQueue

def greedyHeuristic(matrix):
    return len([element for element in matrix if element !=  None]) / 2

def greedy(game):
    """
    Greedy Algorithm
    """
    ai = Ai()

    # Priority Queue to order by heuristic
    queue = PriorityQueue()
    queue.put(game)

    visited = set()
    visited.add(repr(game.matrix))
    
    start = time.time()
    while True:
        game = queue.get()
        if game.isEmpty():
            print("Found a solution: ")
            print("Total Moves: {}".format(game.moves))
            break  

        operationList = ai.getAllMoves(game.rows, game.columns, game.matrix)
        newGameMoves = game.moves + 1
        for operation in operationList:
            newGame = Game(newGameMoves, game.dealValue, game.rows, game.columns, game.matrix.copy(), greedyHeuristic(game.matrix.copy()))
            newGame.removePair(operation[0], operation[1])
            if repr(newGame.matrix) not in visited:
                visited.add(repr(newGame.matrix))
                queue.put(newGame)

        rowsDeal, columnsDeal, gameStateDeal = game.deal(game.rows, game.columns, game.matrix.copy())
        gameDeal = Game(game.moves, game.dealValue + 1, rowsDeal, columnsDeal, gameStateDeal, greedyHeuristic(gameStateDeal.copy()))
        if repr(gameDeal.matrix) not in visited:
            visited.add(repr(gameDeal.matrix))
            queue.put(gameDeal)

        #print("Paths Chosen: {} Heuristic {}".format(queue.qsize, game.heuristic))

        
    
    end = time.time()
    print("Time elapsed: {}".format(end - start))

def aStar(game):
    """
    A* Algorithm
    """
    ai = Ai()

    # Priority Queue to order by heuristic
    queue = PriorityQueue()
    queue.put(game)

    visited = set()
    visited.add(repr(game.matrix))
    
    start = time.time()
    while True:
        game = queue.get()
        if game.isEmpty():
            print("Found a solution: ")
            print("Total Moves: {}".format(game.moves))
            break  

        operationList = ai.getAllMoves(game.rows, game.columns, game.matrix)
        newGameMoves = game.moves + 1
        for operation in operationList:
            newGame = Game(newGameMoves, game.dealValue, game.rows, game.columns, game.matrix.copy(), greedyHeuristic(game.matrix.copy()))
            newGame.removePair(operation[0], operation[1])
            newGame.heuristic = greedyHeuristic(game.matrix.copy())
            if repr(newGame.matrix) not in visited:
                visited.add(repr(newGame.matrix))
                queue.put(newGame)

        rowsDeal, columnsDeal, gameStateDeal = game.deal(game.rows, game.columns, game.matrix.copy())
        gameDeal = Game(game.moves, game.dealValue + 1, rowsDeal, columnsDeal, gameStateDeal, greedyHeuristic(gameStateDeal.copy()))
        if repr(gameDeal.matrix) not in visited:
            visited.add(repr(gameDeal.matrix))
            queue.put(gameDeal)

        #print("Paths Chosen: {} Heuristic {}".format(queue.qsize, game.heuristic))

        
    
    end = time.time()
    print("Time elapsed: {}".format(end - start))

def breathFirstSearch(game):
    """
        Breath First Search Algorithm
    """
    ai = Ai()
    # rows, columns, gameState = deal(rows, columns, gameState.copy())
    # Double Ended Queue to allow O(1) pop and append
    # Set to check if an element was already visited in O(1)
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
            print("Found a solution: ")
            print("Total Moves: {}".format(game.moves))
            break
        # Get available moves and add them to the queue
        else:
            append = queue.append

            operationList = ai.getAllMoves(game.rows, game.columns, game.matrix)
            newGameMoves = game.moves + 1
            for operation in operationList:
                newGame = Game(newGameMoves, game.dealValue, game.rows, game.columns, game.matrix.copy())
                newGame.removePair(operation[0], operation[1])
                if repr(newGame.matrix) not in visited:
                    visited.add(repr(newGame.matrix))
                    append(newGame)
            
            if game.dealValue < 1:
                rowsDeal, columnsDeal, gameStateDeal = game.deal(game.rows, game.columns, game.matrix.copy())
                gameDeal = Game(game.moves, game.dealValue + 1, rowsDeal, columnsDeal, gameStateDeal)

                if repr(gameDeal.matrix) not in visited:
                    visited.add(repr(gameDeal.matrix))
                    append(gameDeal)

    end = time.time()
    print("Time elapsed: {}".format(end - start))


def depthFirstSearch(game):
    """
        Depth First Search Algorithm
    """

    ai = Ai()
    # rows, columns, gameState = deal(rows, columns, gameState.copy())
    # Double Ended Queue to allow O(1) pop and append
    # Set to check if an element was already visited in O(1)
    queue = deque([game])
    visited = set()

    start = time.time()
    while True:
        if (len(visited) % 10000 == 0):
            print("Visited: {} Remaining: {}".format(len(visited), len(queue)))
        
        # Next GameState
        game = queue.pop()
        #game.printGame()

        # Found a solution [Empty Matrix]
        if game.isEmpty():
            print("Found a solution: ")
            print("Total Moves: {}".format(game.moves))
            break
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

    end = time.time()
    print("Time elapsed: {}".format(end - start))

if __name__ == "__main__":
    gameState = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                1, 1, 1, 2, 1, 3, 1, 4, 1, 
                5, 1, 6, 1, 7, 1, 8, 1, 9]
    columns = 9
    rows = 3
    game = Game(0, 0, rows, columns, gameState, greedyHeuristic(gameState))

    greedy(game)

    
