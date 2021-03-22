import tkinter as tk

from tkinter import Button
from tkinter.font import Font

class Game:
    """
    Game manager. Includes user actions
    """
    def __init__(self, moves, dealValue, rows, columns, matrix): 
        self.moves = moves
        self.dealValue = dealValue
        self.columns = columns
        self.rows = rows
        self.matrix = matrix

class Gui(tk.Frame):
    def __init__(self, states):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("Ten Pair")
        self.states = states
        self.actual_state = 0
        self.move_count = 0

        first_state = self.states[self.actual_state]
        self.main_grid = tk.Frame(self, bg = "#c7c7c7", bd = "3", width = str(100 * first_state.columns), height = str(100 * first_state.rows))
        self.main_grid.grid(pady=(100,100), padx=(100,100))
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

        for index, cell_value in enumerate(state.matrix):
            col = index % state.columns
            row = index // state.columns

            if cell_value == None:
                self.cells[row][col]["frame"].configure(bg="#F0F0F0")
                self.cells[row][col]["number"].configure(text="", bg="#F0F0F0")
            else:                
                self.cells[row][col]["frame"].configure(bg="#ffffff")
                self.cells[row][col]["number"].configure(text = str(cell_value))

        for index in range(state.columns * state.rows - len(state.matrix)):
            col = index % state.columns
            row = index // state.rows

            self.cells[row][col]["frame"].configure(bg="#ffffff")
            self.cells[row][col]["number"].configure(text="")

        # Update cells if length > 
        self.main_grid.configure(width = str(100 * state.columns), height = str(100 * state.rows))

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



gameState1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                1, 1, 1, 2, 1, 3, 1, 4, 1, 
                5, 1, 6, 1, 7, 1, 8, 1, 9]
columns = 9
rows = 3

state1 = Game(0, 0, rows, columns, gameState1)

gameState2 = [1, 2, 
3, 4, 5, 6, 7, 8, None,
                None, 1, 1, 2, 1, 3, 1, 4, 1, 
                5, 1, 6, 1, 7, 1, 8, 1, 9]

state2 = Game(1, 0, rows, columns, gameState2)

Gui([state1,state2])