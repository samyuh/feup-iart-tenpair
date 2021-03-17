class Game:
    """
    Game manager. Includes user actions
    """
    def __init__(self, moves, dealValue, rows, columns, matrix, previousState = None): 
        self.moves = moves
        self.dealValue = dealValue
        self.columns = columns
        self.rows = rows
        self.matrix = matrix
        self.heuristic = 0
        self.previousState = previousState
       

    def __gt__(self, other):
        return self.heuristic > other.heuristic
    
    def __eq__(self, other):
        return self.heuristic == other.heuristic

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self)

    def isEmpty(self):
        """
        Objective Function
        """
        if self.matrix == [None] * len(self.matrix):
            return True
        return False

    def printGame(self):
        print("Game Grid: ", end="")
        for index, i in enumerate(self.matrix):
            if index % self.columns == 0:
                print("\n", end="")                   
            print(i, end=" | ")
        for j in range(self.columns* self.rows - len(self.matrix)):
            print(" ", end=" | ")

    def removePair(self, coordsA, coordsB):
        self.matrix[coordsA] = None
        self.matrix[coordsB] = None

    def deal(self, rows, columns, matrix):
        # One dimension array of game matrix without Null elements 
        flattenMatrix = [element for element in matrix if element != None]

        matrix.extend(flattenMatrix)
        rows = len(matrix) // 9                                             
                                                                        
        return rows, columns, matrix

    def getFullGame(self):

        gameSequence = [self]
        currentGame = self
        previousGame = self.previousState

       
        while isinstance(previousGame,Game):
            currentGame = previousGame
            gameSequence.append(currentGame)
            previousGame = currentGame.previousState
        
        gameSequence.reverse()
        return gameSequence


    def printGameSequence(self):
        gameSequence = self.getFullGame()
        print(len(gameSequence))
        
        for i in gameSequence:
            print()
            i.printGame()
            print()
        print()

