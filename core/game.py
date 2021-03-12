class Game:
    """
    Game manager. Includes user actions
    """
    def __init__(self, moves, rows, columns, matrix):
        # Number of moves 
        self.moves = moves
        self.columns = columns
        self.rows = rows
        self.matrix = matrix

    def isEmpty(self):
        if self.matrix == [None] * len(self.matrix):
            return True
        return False

    def printGame(self):
        print("Game Grid: ")
        for row in range(self.rows):
            for i in range(self.columns):
                element = self.matrix[self.rows*self.columns + i]
                if element != None:
                    print(element, end=" | ")
                else:
                    print(" ", end=" | ")
            print("\n", end="")

    def removePair(self, coordsA, coordsB):
        self.matrix[coordsA] = None
        self.matrix[coordsB] = None

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

