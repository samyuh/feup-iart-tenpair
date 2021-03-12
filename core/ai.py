class Ai:
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

        column = [matrix[columnNumber + i*columns] for i in range(rows) if columnNumber + i*columns < len(matrix)]

        row1 = index1 // 9
        row2 = index2 // 9

        spaceRow = column[row2+1:row1]
        if spaceRow == [None] * len(spaceRow):
            return True

        return False
        

    def getAllMoves(self, rows, columns, matrix):
        lenMatrix = len(matrix)
        return [[i, i2] for i in range(lenMatrix) for i2 in range(i+1, lenMatrix) if self.valid(columns, rows, matrix, i2, i)]    