class AI:
    def __init__(self):
        pass

    def valid(self, columns, rows, matrix, index1, index2):
        element1 = matrix[index1]
        element2 = matrix[index2]

        if element1 == None or element2 == None:
            return False
        if element1 != element2 and element1 + element2 != 10:
            return False

        space = matrix[index2+1:index1]
        if space == [None] * len(space):
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
        if spaceRow == [None] * len(spaceRow):
            return True

        return False
        

    def getAllMoves(self, rows, columns, matrix):
        lenMatrix = len(matrix)
        return [[i, i2] for i in range(lenMatrix) for i2 in range(i+1, lenMatrix) if self.valid(columns, rows, matrix, i2, i)]

class Game:
    """
    Game manager. Includes user actions
    """
    def __init__(self, columns, rows, matrix):
        # Number of moves 
        self.numMoves = 0
        self.columns = columns
        self.rows = rows
        self.matrix = matrix

    def isEmpty(self, matrix):
        if matrix == [None] * len(matrix):
            return True
        return False

    def printGame(self, rows, columns, matrix):
        print("Game Grid: ")
        for row in range(rows):
            for i in range(columns):
                element = matrix[row*columns + i]
                if element != None:
                    print(element, end=" | ")
                else:
                    print(" ", end=" | ")
            print("\n", end="")

    def removePair(self,  matrix, coordsA, coordsB):
        matrix[coordsA] = None
        matrix[coordsB] = None

        return matrix

    def deal(self, rows, columns, matrix):
        # Create a matrix to append at the end filled with Null
        auxMatrix = [None for i in range(columns) for i in range(rows)]

        # One dimension array of game matrix without Null elements 
        flattenMatrix = [element for element in matrix if element != None]

        for index, element in enumerate(flattenMatrix):
            auxMatrix[index] = element

        rows += rows
        matrix.extend(auxMatrix)

        return rows, columns, matrix

