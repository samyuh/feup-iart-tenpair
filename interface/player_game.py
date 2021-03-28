# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk
import time

# -- Costum Libraries -- #
import algorithms
from core import Game, Logic
from .frame import BaseFrame

class PlayerGame(BaseFrame):
    def start_game(self):
        self.currentHint = [0, 2]
        self.selected = None
        self.runningHint = False
        self.loading = False
        self.clearFrame()

        self.game = Game(0,0,3,9,[1, 2, 3, 4, 5, 6, 7, 8, 9,
                                    1, 1, 1, 2, 1, 3, 1, 4, 1, 
                                    5, 1, 6, 1, 7, 1, 8, 1, 9])
        self.move_count = 0

        # todo: adjust frame size as desired
        self.main_grid = tk.Frame(self, bg="#c7c7c7", bd="3")
        self.main_grid.pack(pady=(100,0))

        # Create Gui and represent first state
        self.make_GUI(self.game)
        self.update_GUI()

        # Quit Button
        self.quitBtn = tk.Button(self, text="Quit", command = lambda self=self: self.controller.routeHomeFrame() , font='Roboto 11 bold', fg='#ffffff', bg='#1D8EA0')
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
        for i in states:
            print(i.matrix)

        self.cells[0][0]["frame"].configure(bg="#FFFF00")
        self.cells[0][0]["number"].configure(bg="#FFFF00")

        self.cells[0][1]["frame"].configure(bg="#FFFF00")
        self.cells[0][1]["number"].configure(bg="#FFFF00")

    def computerHint(self):
        if not self.runningHint:
            self.runningHint = True
            thread = algorithms.GreedySearch(self.game, self.getNextMove)
            thread.start()

            print("Hint!")
            

    def playerMove(self, i, j):
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
            previousIndex = i0 * 9 + j0
            currentIndex = i * 9 + j
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
                cell_number = tk.Button(self.main_grid, bg="#F0F0F0", command = lambda i=i, j=j: self.playerMove(i, j), font='Roboto 18 bold', fg='#212121')
                cell_number.grid(row=i,column=j)
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
        Logic.deal(self.game)
        self.update_GUI()
        
    def clearFrame(self):
        # destroy all widgets from frame
        for widget in self.winfo_children():
            widget.destroy()
        
        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        self.pack_forget()

    def update_GUI(self):
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
                self.cells[row][col]["number"].configure(text = str(cell_value))

        # Update moves
        self.move_count = state.moves
        self.moves_label.configure(text=self.move_count)
        self.update_idletasks()

        # Update scroll
        self.controller.my_canvas.configure(scrollregion = self.controller.my_canvas.bbox("all"))


    def next_move(self):
        self.update_GUI()
        self.over()

    def over(self):
        pass

    def extend_board(self,state):
        prev_rows = len(self.cells)
        prev_cols = len(self.cells[0])

        # Number of rows to add
        extend_rows = (len(state.matrix) - prev_rows * prev_cols) // state.columns + 1

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
                cell_number = tk.Button(self.main_grid, bg="#F0F0F0", command = lambda i=i, j=j: self.playerMove(i, j), font='Roboto 18 bold', fg='#212121')
                cell_number.grid(row=i,column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)