class Game:
    """
    Game Class that includes all necessary parameters to store a Game State and all the necessary methods that can be executed on that Game
    """
    def __init__(self, moves, dealValue, rows, columns, matrix, previousState = None):
        """
        Constructor for Game object, indicating the board, all its properties, and also storing the precious Game, if it exists

        Attributes
        ----------

        moves : list of moves
            list with all the possible game moves
        dealValue : int
            number of deals already made in the game
        rows : int
            ammount of rows of the game's current state
        columns : int
            ammount of columns of the game's current state
        matrix : list of int
            flattened matrix with the current game state
        previousState : Game
            Previous Game object of the previous Game State. It is used to store the game Sequence. Default value is None
        
        """
        self.moves = moves
        self.dealValue = dealValue
        self.columns = columns
        self.rows = rows
        self.matrix = matrix
        self.heuristic = 0
        self.previousState = previousState
        self.pair = None
       
    def __gt__(self, other):
        """
        Method for overloading Game object comparison

        Attributes
        ----------
        other : Game
            other game Object to compare the current Game with

        Returns
        -------
        boolean
            Returns True if the current object heuristic is greater than the other Object, False otherwise
        """
        return self.heuristic > other.heuristic
    
    def __eq__(self, other):
        """
        Method for overloading Game object equality comparison

        Attributes
        ----------
        other : Game
            other game Object to compare the current Game with

        Returns
        -------
        bool
            Returns True if the current object heuristic is equal to the other Object, False otherwise
        """
        return self.heuristic == other.heuristic

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self)

    def isEmpty(self):
        """
        Objective Function for calculating if the gameState is empty (has no more occupied elements)

        Returns
        -------
        bool : True if the Game matrix is empty, False otherwise
        """

        if self.matrix == [None] * len(self.matrix):
            return True
        return False

    def printGame(self):
        """
        Method for printing the Game matrix
        """
        print("Game Grid: ", end="")
        for index, i in enumerate(self.matrix):
            if index % self.columns == 0:
                print("\n", end="")   
            if i == None:
                print(" ", end=" | ")
            else:                
                print(i, end=" | ")
        for j in range(self.columns* self.rows - len(self.matrix)):
            print(" ", end=" | ")                                    

    def getFullGame(self):
        """
        Get Method for returning the full Game Sequence

        Returns
        -------
        list of Games
            returns a list with the game sequence of moves until this very move
        """

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
        """
        Method for printing the current gameSequence
        """
        gameSequence = self.getFullGame()
        print(len(gameSequence))
        
        for i in gameSequence:
            print()
            print(i.pair)
            i.printGame()
            print()
        print()

    def removePair(self, coordsA, coordsB):
        """
        Method for removing a specific given pair

        Attributes
        ----------
        coordsA : int
            value for the position of the first number to be removed
        coordsB : int
            value for the position of the second number to be removed
        
        """
        self.pair = [coordsA, coordsB]
        self.matrix[coordsA] = None
        self.matrix[coordsB] = None  