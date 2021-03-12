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
        # Create a matrix to append at the end filled with Null
        #auxMatrix = [None for i in range(columns) for i in range(rows)]

        # One dimension array of game matrix without Null elements 
        flattenMatrix = [element for element in matrix if element != None]

        #for index, element in enumerate(flattenMatrix):
            #auxMatrix[index] = element

        matrix.extend(flattenMatrix)
        rows = len(matrix) // 9                                             
                                                                        
        return rows, columns, matrix

