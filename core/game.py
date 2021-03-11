class AI:
    def __init__(self):
        pass

    def valid(self, columns, rows, matrix, index1, index2):
        element1 = matrix[index1]
        element2 = matrix[index2]

        if index1 == index2:
            return False
        if element1 == None or element2 == None:
            return False
        if element1 != element2 and element1 + element2 != 10:
            return False

        if index1 > index2:
            space = matrix[index2+1:index1]
            if space.count(None) == len(space):
                return True
            
            columnNumber = index1 % 9
            columnNumber2 = index2 % 9

            if columnNumber != columnNumber2:
                return False

            column = []
            for i in range(rows):
                column.append(matrix[columnNumber + i*columns])

            row1 = index1 // 9
            row2 = index2 // 9

            spaceRow = column[row2+1:row1]
            if spaceRow.count(None) == len(spaceRow):
                return True
        """
        elif index1 < index2:
            space = matrix[index1+1:index2]
            if space.count(None) == len(space):
                return True

            
            columnNumber = index1 % 9
            columnNumber2 = index2 % 9

            if columnNumber != columnNumber2:
                return False
            
            column = []
            for i in range(rows):
                column.append(matrix[columnNumber + i*columns])

            row1 = index1 // 9
            row2 = index2 // 9

            spaceRow = column[row2+1:row1]
            if spaceRow.count(None) == len(spaceRow):
                return True
        """
        return False
        

    def getAllMoves(self, columns, rows, matrix):
        lenMatrix = len(matrix)
        return [[i, i2] for i in range(lenMatrix) for i2 in range(lenMatrix) if self.valid(columns, rows, matrix, i, i2)]

class Game:
    """
    Game manager. Includes user actions
    """
    def __init__(self):
        # Number of moves 
        self.numMoves = 0

        self.columns = 3
        self.rows = 3   
        self.matrix = [1, 2, 4,
                        1, 2, 4, 
                        1, 2, 4]

    def isEmpty(self):
        for element in self.matrix:
            if element != None:
                return False
        return True

    def printGame(self):
        """
            Print the game board
        """
        print("Game Grid: ")
        for row in range(self.rows):
            for i in range(self.columns):
                element = self.matrix[row*self.columns + i]
                if element != None:
                    print(element, end=" | ")
                else:
                    print(" ", end=" | ")
            print("\n", end="")
    
    def removePair(self, coordsA, coordsB):
        self.matrix[coordsA] = None
        self.matrix[coordsB] = None

    def deal(self):
        # Create a matrix to append at the end filled with Null
        auxMatrix = [None for i in range(9) for i in range(self.rows)]

        # One dimension array of game matrix without Null elements 
        flattenMatrix = [element for element in self.matrix if element != None]

        for index, element in enumerate(flattenMatrix):
            auxMatrix[index] = element

        self.rows += 3
        self.matrix.extend(auxMatrix)

