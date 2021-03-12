import copy
import time
from _collections import deque

 # Personal Libraries
from core.game import Game, AI

def breathFirstSearch():
    """
        Breath First Search Algorithm
    """

    gameState = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                1, 1, 1, 2, 1, 3, 1, 4, 1, 
                5, 1, 6, 1, 7, 1, 8, 1, 9]
    columns = 9
    rows = 3   
    
    game = Game(columns, rows, gameState)
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
        #printGame(rows, columns, gameState)
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
            removePair = game.removePair
            for operation in operationList:
                queue.append((rows, columns, removePair(gameState.copy(), operation[0], operation[1])))
            
            rowsDeal, columnsDeal, gameStateDeal = game.deal(rows, columns, gameState.copy())
            if rowsDeal < 11:
                queue.append((rowsDeal, columnsDeal, gameStateDeal))

    end = time.time()
    print("Visited: {}".format(len(gameState)))
    print("Time elapsed: {}".format(end - start))


def depthFirstSearch():
    """
        Depth First Search Algorithm
    """
    gameState = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                1, 1, 1, 2, 1, 3, 1, 4, 1, 
                5, 1, 6, 1, 7, 1, 8, 1, 9]
    columns = 9
    rows = 3   
    
    game = Game(columns, rows, gameState)
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
        rows, columns, gameState = queue.pop()
        #printGame(rows, columns, gameState)
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

            removePair = game.removePair 
            for operation in operationList:
                queue.append((rows, columns, removePair(gameState.copy(), operation[0], operation[1])))
            
            rowsDeal, columnsDeal, gameStateDeal = game.deal(rows, columns, gameState.copy())
            if rowsDeal < 11:
                queue.appendleft((rowsDeal, columnsDeal, gameStateDeal))

    end = time.time()
    print("Visited: {}".format(len(gameState)))
    print("Time elapsed: {}".format(end - start))

if __name__ == "__main__":
    breathFirstSearch()

    
