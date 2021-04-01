# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk
import time

# -- Costum Libraries -- #
import algorithms
from core import Game, Logic
from .frame import BaseFrame

class FrameGame(BaseFrame):
    """
    Class for an object containing all Game properties and methods
    
    Attributes
    ----------
    currentHint : pair of integers in a list
      - hint for the position of both elements that should be removed using the hint heuristic

    selected : list of lists of int
      - contains the numbers from the board currently being selected by the player

    runningHint : bool
      - Attribute used to verify if the hint for the next move has already been calculated

    cells : list of lists of cells
      - Contains the frame and the number of all the gameboard cells

    loading : bool
      - Attribute used to verify if the Game if the gmae is still being processed

    game : Game
      - Current Game object containing the game state

    move_count : int
      - Number of moves made in the current game

    main_grid : tk.Frame
      - Frame with the game grid

    quitBtn : tk.Button
      - GUI button to exit the current Game menu

    hintBtn : tk.Button
      - GUI button to show the hint for the next move of the player using an heuristic

    dealBtn : tk.Button
      - GUI button to execute the deal move
    
    moves_label : tk.label
      - Label of the moves to be displayed

    """

    def initGame(self, game):
        self.game = game

    def start_game(self):
        """
        Method for initializing a game
        """

        self.currentHint = [0, 2]
        self.selected = None
        self.runningHint = False
        self.loading = False
        self.clearFrame()
        self.move_count = 0

        # todo: adjust frame size as desired
        self.main_grid = tk.Frame(self, bg="#c7c7c7", bd="3")
        self.main_grid.pack(pady=(100,0))

        # Create Gui and represent first state
        self.make_GUI(self.game)
        self.update_GUI()

        # Quit Button
        self.quitBtn = tk.Button(self, text="Quit", command = lambda self=self: self.controller.routeBoardSelect() , font='Roboto 11 bold', fg='#ffffff', bg='#1D8EA0')
        self.quitBtn.place(relx=0.6, y=45)
        self.quitBtn.config(highlightbackground='#1D8EA0')

        # Next Move Button
        self.hintBtn = tk.Button(self, text="Hint", command = self.computerHint, font='Roboto 11 bold', fg='#ffffff', bg='#1D8EA0')
        self.hintBtn.place(relx=0.7, y=45)
        self.hintBtn.config(highlightbackground='#1D8EA0')

        # Deal Button
        self.dealBtn = tk.Button(self, text="Deal", command = self.playerDeal, font='Roboto 11 bold', fg='#ffffff', bg='#1D8EA0')
        self.dealBtn.place(relx=0.8, y=45)
        self.dealBtn.config(highlightbackground='#1D8EA0')

    def create_widgets(self):
        """
            Create the base widgets for the frame.
        """
        pass

    def getNextMove(self, states):
        self.runningHint = False
        index0_i = states[1].pair[0] // self.game.columns
        index0_j = states[1].pair[0] % self.game.columns

        index1_i = states[1].pair[1] // self.game.columns
        index1_j = states[1].pair[1] % self.game.columns

        print(states[1].pair)

        self.cells[index0_i][index0_j]["frame"].configure(bg="#FFFF00")
        self.cells[index0_i][index0_j]["number"].configure(bg="#FFFF00")

        self.cells[index1_i][index1_j]["frame"].configure(bg="#FFFF00")
        self.cells[index1_i][index1_j]["number"].configure(bg="#FFFF00")

    def computerHint(self):
        if not self.runningHint:
            self.runningHint = True
            thread = algorithms.GreedySearch(self.game, self.getNextMove)
            thread.start()        

    def playerMove(self, i, j):
        """
        Executing a player move on the game board

        Attributes
        ----------
        i : int
            - position of the first selected piece from the pair to remove from the board

        j : int
            - position of the last selected piece from the pair to remove from the board

        """
        index = i * self.game.columns + j
        if index > len(self.game.matrix) - 1:
            return

        if self.game.matrix[index] == None:
            return 

        if self.selected == None:
            self.cells[i][j]["frame"].configure(bg="#7BB9C2")
            self.cells[i][j]["number"].configure(bg="#7BB9C2")
            self.selected = [[i, j],]
            self.update_idletasks()
            return
        elif self.selected[0] == [i, j]:
            self.selected = None
            self.cells[i][j]["frame"].configure(bg="#f2f2f2")
            self.cells[i][j]["number"].configure( bg="#f2f2f2")
            self.update_idletasks()
            return
        else:
            # Verify if it is a pair
            i0 = self.selected[0][0]
            j0 = self.selected[0][1]
            previousIndex = i0 * self.game.columns + j0
            currentIndex = i * self.game.columns + j
            # Bigger should be always the first
            if (previousIndex < currentIndex):
                previousIndex, currentIndex = currentIndex, previousIndex

            if not Logic.validMove(self.game, previousIndex, currentIndex):
                self.selected = None
                self.cells[i0][j0]["frame"].configure(bg="#f2f2f2")
                self.cells[i0][j0]["number"].configure(bg="#f2f2f2")
                return

            self.game.removePair(previousIndex, currentIndex)

            i0 = self.selected[0][0]
            j0 = self.selected[0][1]

            self.cells[i0][j0]["frame"].configure(bg="#7BB9C2")
            self.cells[i0][j0]["number"].configure( bg="#7BB9C2")

            self.cells[i][j]["frame"].configure(bg="#7BB9C2")
            self.cells[i][j]["number"].configure(bg="#7BB9C2")
            self.update_idletasks()
            time.sleep(0.15)

            self.cells[i0][j0]["frame"].configure(bg="#f2f2f2")
            self.cells[i0][j0]["number"].configure(text = "", bg="#f2f2f2")

            self.cells[i][j]["frame"].configure(bg="#f2f2f2")
            self.cells[i][j]["number"].configure(text = "", bg="#f2f2f2")
            self.selected = None

        self.update_GUI()

    def make_GUI(self, first_state):
        """
        Initializing the GUI that represents the game

        Attributes
        ----------

        first_state : Game
          - game used to be displayed on the GUI
        """
        self.cells = []
        for i in range(first_state.rows):
            row = []
            for j in range(first_state.columns):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg = "#f2f2f2",
                    width = 100,
                    height = 100
                )
                
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Button(self.main_grid, bg="#F0F0F0", command = lambda i=i, j=j: self.playerMove(i, j), font='Roboto 18 bold', fg='#212121', borderwidth=0, highlightthickness=0)
                cell_number.grid(row=i,column=j, sticky = tk.W + tk.S + tk.N + tk.E, padx = 8, pady = 8)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        # moves counter
        moves_frame = tk.Frame(self, bg="#212121")
        moves_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(
            moves_frame,
            text = "Moves", 
            bg="#212121", #black 
            font='Roboto 16 bold', 
            fg='#ffffff'
        ).grid(row=0)

        self.moves_label = tk.Label(
            moves_frame, 
            text="0",
            bg="#212121", #black
            font='Roboto 16 bold', 
            fg='#ffffff')
        self.moves_label.grid(row=1)
    
    def playerDeal(self):
        """
        Execute the move Deal defined in our game
        """
        Logic.deal(self.game)
        self.update_GUI()
        
    def clearFrame(self):
        """
        Clearing the Frame by destroying all existent widgets
        """
        # destroy all widgets from frame
        for widget in self.winfo_children():
            widget.destroy()
        
        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        self.pack_forget()

    def update_GUI(self):
        """
        Updating the GUI by chaning the board length, matrix, moves and scroll position
        """
        state = self.game
            
        # Extend board
        if len(state.matrix) > len(self.cells) * len(self.cells[0]):
            self.extend_board(state)

        # Update matrix
        for index, cell_value in enumerate(state.matrix):
            col = index % state.columns
            row = index // state.columns
            
            if cell_value == None:
                self.cells[row][col]["frame"].configure(bg="#F0F0F0")
                self.cells[row][col]["number"].configure(text="", bg="#F0F0F0")
            else:                
                self.cells[row][col]["frame"].configure(bg="#F0F0F0")
                self.cells[row][col]["number"].configure(text = str(cell_value), bg="#F0F0F0")

        # Update moves
        self.move_count = state.moves
        self.moves_label.configure(text=self.move_count)
        self.update_idletasks()

        # Update scroll
        self.controller.my_canvas.configure(scrollregion = self.controller.my_canvas.bbox("all"))


    def next_move(self):
        """
        Updating the GUI in order to show the next move of the found solution
        """
        self.update_GUI()
        self.over()

    def over(self):
        pass

    def extend_board(self,state):
        """
        Method for extending the board length

        Attributes
        ----------
        state : Game
          - Game used to caluclate the board extension size that needs to be made
        """
        prev_rows = len(self.cells)

        # Number of rows to add
        extend_rows = state.rows - prev_rows

        for i in range(prev_rows, prev_rows + extend_rows):
            row = []
            for j in range(state.columns):
                cell_frame = tk.Frame(
                    self.main_grid,
                    bg = "#f2f2f2",
                    width = 100,
                    height = 100
                )
                cell_frame.grid(row=i, column=j, padx=5, pady=5)
                cell_number = tk.Button(self.main_grid, bg="#F0F0F0", command = lambda i=i, j=j: self.playerMove(i, j), font='Roboto 18 bold', fg='#212121', borderwidth=0, highlightthickness=0)
                cell_number.grid(row=i,column=j, sticky = tk.W + tk.S + tk.N + tk.E, padx = 8, pady = 8)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)