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

    def deal(self):
        # One dimension array of game matrix without Null elements 
        flattenMatrix = [element for element in self.matrix if element != None]

        self.matrix.extend(flattenMatrix)
        self.rows = len(self.matrix) // 9                                             

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

    def valid(self, index1, index2):
        element1 = self.matrix[index1]
        element2 = self.matrix[index2]

        if element1 == None or element2 == None:
            return False
        if element1 != element2 and element1 + element2 != 10:
            return False

        space = self.matrix[index2+1:index1]
        if space == [None] * len(space):
            return True
        
        columnNumber = index1 % 9
        columnNumber2 = index2 % 9

        if columnNumber != columnNumber2:
            return False

        column = [self.matrix[columnNumber + i*self.columns] for i in range(self.rows) if columnNumber + i*self.columns < len(self.matrix)]

        row1 = index1 // 9
        row2 = index2 // 9

        spaceRow = column[row2+1:row1]
        if spaceRow == [None] * len(spaceRow):
            return True

        return False
        
    def getAllMoves(self):
        lenMatrix = len(self.matrix)
        return [[i, i2] for i in range(lenMatrix) for i2 in range(i+1, lenMatrix) if self.valid(i2, i)]    