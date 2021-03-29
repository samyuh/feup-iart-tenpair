class Logic:
    """
        Class for the Game Logic
    """
    @staticmethod
    def deal(game):
        """
        Static Method that allows executing the "Deal" Move of the "Ten Pair" Game

        Parameters
        ----------
        game : Game
            executes the Deal Move on this game 
        """
        
        # One dimension array of game matrix without Null elements 
        flattenMatrix = [element for element in game.matrix if element != None]

        game.matrix.extend(flattenMatrix)       
        game.rows = len(game.matrix)// game.columns + (1 if len(game.matrix) % game.columns != 0 else 0)

    @staticmethod
    def validMove(game, index1, index2):
        """
        Static Method that checks if a move is valid
        Parameters
        ----------
        game : Game
            game object with the game state matrix
        index1 : int
            value for the position of the first number to be removed
        index2 : int
            value for the position of the second number to be removed

        Returns
        -------
        bool
            Returns True if the move is valid, False otherwise
        """
        element1 = game.matrix[index1]
        element2 = game.matrix[index2]

        if element1 == None or element2 == None:
            return False
        if element1 != element2 and element1 + element2 != 10:
            return False

        space = game.matrix[index2+1:index1]
        if space == [None] * len(space):
            return True
        
        columnNumber = index1 % game.columns
        columnNumber2 = index2 % game.columns

        if columnNumber != columnNumber2:
            return False

        column = [game.matrix[columnNumber + i*game.columns] for i in range(game.rows) if columnNumber + i*game.columns < len(game.matrix)]

        row1 = index1 // game.columns
        row2 = index2 // game.columns

        spaceRow = column[row2+1:row1]
        if spaceRow == [None] * len(spaceRow):
            return True
        
        return False
    
    @staticmethod
    def getAllMoves(game):
        """
        Static Method for returning all the current possible moves of a Game object

        Parameters
        ----------
        game : Game
            game object with the game state matrix

        Returns
        -------
        list of lists of 2 ints
            Returns a list containing pairs of elements that represent valid moves 

        """
        lenMatrix = len(game.matrix)
        return [[i, i2] for i in range(lenMatrix) for i2 in range(i+1, lenMatrix) if Logic.validMove(game, i2, i)]