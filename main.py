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

def deal(columns, rows, matrix):
    # Create a matrix to append at the end filled with Null
    auxMatrix = [None for i in range(9) for i in range(rows)]

    # One dimension array of game matrix without Null elements 
    flattenMatrix = [element for element in matrix if element != None]

    for index, element in enumerate(flattenMatrix):
        auxMatrix[index] = element

    rows += 3
    matrix.extend(auxMatrix)

def main():
    gameState = matrixStart
    columns = 9
    rows = 3   

    deal(columns, rows, gameState)
    #printGame(rows, columns, gameState)
    rows += rows
    
    ai = AI()
    queue = deque([gameState.copy()])
    visited = {"a", "b"}

    start = time.time()
    while True:
        if (len(visited) % 10000 == 0):
            print("Visited: {} Remaining: {}".format(len(visited), len(queue)))
        #printGame(rows, columns, gameState)
        gameState = queue.popleft()

        if gameState.count(None) == len(gameState):
            print("found")
            break
        if repr(gameState) in visited:
            pass
        else:
            visited.add(repr(gameState))
            operationList = ai.getAllMoves(columns, rows, gameState)
            for operation in operationList:
                gameCopy = gameState.copy()
                removePair(gameCopy, operation[0], operation[1])     
                
                queue.append(gameCopy)
            #queue.append((gameState.copy(), 'deal'))
    print(len(visited))
    end = time.time()
    print(end - start)


if __name__ == "__main__":
    main()

    
