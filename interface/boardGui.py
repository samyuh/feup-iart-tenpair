import tkinter as tk

from tkinter import Button
from tkinter.font import Font

class Gui(tk.Frame):
    def __init__(self, states):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Ten Pair")
        self.states = states
        self.actual_state = 0
        self.move_count = 0

        first_state = self.states[self.actual_state]

        # todo: adjust frame size as desired
        self.main_grid = tk.Frame(self, bg = "#c7c7c7", bd = "3", width = str(100 * first_state.columns), height = str(100 * first_state.rows))
        self.main_grid.grid(pady=(100,100), padx=(100,100))

        # Create Gui and represent first state
        self.make_GUI(first_state)
        self.update_GUI()

        # Next Move Button
        self.moveBtn = Button(self, text="Next Move", command = self.next_move)
        self.moveBtn.place(x=0, y=0)

        self.mainloop()

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
                cell_number = tk.Label(self.main_grid, bg="#ffffff", font="Helvetica")
                cell_number.grid(row=i,column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        # moves counter
        moves_frame = tk.Frame(self)
        moves_frame.place(relx=0.5, y=45, anchor="center")
        tk.Label(
            moves_frame,
            text = "Moves", 
        ).grid(row=0)

        self.moves_label = tk.Label(moves_frame, text="0")
        self.moves_label.grid(row=1)

    def update_GUI(self):
        state = self.states[self.actual_state] # actual state

        # Extend board
        if len(state.matrix) > len(self.cells) * len(self.cells[0]):
            self.extend_board(state)

        for index, cell_value in enumerate(state.matrix):
            col = index % state.columns
            row = index // state.columns

            if cell_value == None:
                self.cells[row][col]["frame"].configure(bg="#F0F0F0")
                self.cells[row][col]["number"].configure(text="", bg="#F0F0F0")
            else:                
                self.cells[row][col]["frame"].configure(bg="#ffffff")
                self.cells[row][col]["number"].configure(text = str(cell_value))

        self.actual_state += 1
        self.moves = state.moves
        self.update_idletasks()

    def next_move(self):
        self.update_GUI()
        self.over()

    def over(self):
        if self.actual_state == len(self.states):
            self.moveBtn['text']='Quit'
            # Change this to go to main menu
            self.moveBtn['command'] = self.main_grid.destroy

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
                cell_number = tk.Label(self.main_grid, bg="#F0F0F0", font="Helvetica")
                cell_number.grid(row=i,column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)

        
# Testing with 2 boards with different rows
""" gameState1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                1, 1, 1, 2, 1, 3, 1, 4, 1, 
                5, 1, 6, 1, 7, 1, 8, 1, 9]
columns = 9
rows = 3

state1 = Game(0, 0, rows, columns, gameState1)

gameState2 = [1, 2, 3, 4, 5, 6, 7, 8, None,
                None, 1, 1, 2, 1, 3, 1, 4, 1, 
                5, 1, 6, 1, 7, 1, 8, 1, 9, 
                7, 8, 9]

state2 = Game(1, 0, 4, columns, gameState2)

Gui([state1,state2]) """