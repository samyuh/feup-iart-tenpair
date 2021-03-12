from core.game import Game, AI
import copy
from _collections import deque
import time

# Number of moves 
matrixStart = [1, 2, 3, 4, 5, 6, 7, 8, 9,
               1, 1, 1, 2, 1, 3, 1, 4, 1, 
               5, 1, 6, 1, 7, 1, 8, 1, 9]
def isEmpty(matrix):
    for element in matrix:
        if element != None:
            return False
    return True

def printGame(rows, columns, matrix):
    print("Game Grid: ")
    for row in range(rows):
        for i in range(columns):
            element = matrix[row*columns + i]
            if element != None:
                print(element, end=" | ")
            else:
                print(" ", end=" | ")
        print("\n", end="")

def removePair(matrix, coordsA, coordsB):
    matrix[coordsA] = None
    matrix[coordsB] = None

    return matrix

def deal(rows, columns, matrix):
    # Create a matrix to append at the end filled with Null
    auxMatrix = [None for i in range(columns) for i in range(rows)]

    # One dimension array of game matrix without Null elements 
    flattenMatrix = [element for element in matrix if element != None]

    for index, element in enumerate(flattenMatrix):
        auxMatrix[index] = element

    rows += rows
    matrix.extend(auxMatrix)

    return rows, columns, matrix

def breathFirstSearch():
    gameState = matrixStart
    columns = 9
    rows = 3   
    
    ai = AI()
    # rows, columns, gameState = deal(rows, columns, gameState.copy())
    # Double Ended Queue to allow O(1) pop and append
    # Set to check if an element was already visited in O(1)
    queue = deque([(rows, columns, gameState.copy())])
    visited = set()

    start = time.time()
    while True:
        if (len(visited) % 10000 == 0):
            print("Visited: {} Remaining: {}".format(len(visited), len(queue)))
            print(rows)
        
        # Next GameState
        rows, columns, gameState = queue.popleft()
        # Found a solution [Empty Matrix]
        if gameState == [None] * len(gameState):
            print("found")
            break
        # GameState Already Visited
        elif repr(gameState) in visited:
            pass
        # Get available moves and add them to the queue
        else:
            visited.add(repr(gameState))
            operationList = ai.getAllMoves(rows, columns, gameState)
            for operation in operationList:
                queue.append((rows, columns, removePair(gameState.copy(), operation[0], operation[1])))
            

            rows, columns, gameState = deal(rows, columns, gameState.copy())
            if rows < 7:
                queue.append((rows, columns, gameState))

    end = time.time()
    print("Visited: {}".format(len(gameState)))
    print("Time elapsed: {}".format(end - start))


if __name__ == "__main__":
    breathFirstSearch()

    
