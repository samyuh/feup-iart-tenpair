# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk
import time

# -- Costum Libraries -- #
import algorithms
from core import Game
from .frame import BaseFrame

class ShowResultsFrame(BaseFrame):
    def setState(self, state):
        self.loading = False
        self.clearFrame()
        self.states = state
        self.actual_state = 0
        self.move_count = 0

        first_state = self.states[self.actual_state]

        # todo: adjust frame size as desired
        self.main_grid = tk.Frame(self, bg = "#c7c7c7", bd = "3")
        self.main_grid.pack(pady=(100,0))

        # Create Gui and represent first state
        self.make_GUI(first_state)
        self.update_GUI()

        # Next Move Button
        self.moveBtn = tk.Button(self, text="Next Move", command = self.next_move, font='Roboto 11 bold', fg='#ffffff', bg='#1D8EA0')
        self.moveBtn.place(relx=0.7, y=45)
        self.moveBtn.config(highlightbackground='#1D8EA0')

    def create_widgets(self):
        """Create the base widgets for the frame."""
    
        self.loading = True
        self.loadingNext = 0
        
        
    def play_animation(self):
        self.loadingText = tk.Label(self, text='Processing Nodes...', font='Monoid 35 bold', bg='#212121', fg="#ffffff")
        self.loadingText.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
  
        while(self.loading):
            if self.loadingText:
                self.loadingText.destroy()
            self.loadingText = tk.Label(self, text='Processing Nodes' + self.loadingNext * '.' + ' ' * (3 - self.loadingNext), font='Monoid 35 bold', bg='#212121', fg="#ffffff")
            self.loadingText.place(relx=0.5, rely=0.5, anchor = tk.CENTER)
            self.update()
            time.sleep(0.5)
            self.loadingNext = (self.loadingNext + 1) % 4
        self.loadingText.destroy()

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
                cell_number = tk.Label(self.main_grid, bg="#F0F0F0", font='Roboto 18 bold', fg='#212121')
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
    
    def clearFrame(self):
        # destroy all widgets from frame
        for widget in self.winfo_children():
            widget.destroy()
        
        # this will clear frame and frame will be empty
        # if you want to hide the empty panel then
        self.pack_forget()

    def update_GUI(self):
        state = self.states[self.actual_state] # actual state
        
        if (self.actual_state + 1 < len(self.states)) and (self.states[self.actual_state + 1].pair != None):
            markPair = True
        else:
            markPair = False
            
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
            elif markPair and index in self.states[self.actual_state + 1].pair:
                self.cells[row][col]["frame"].configure(bg="#7BB9C2")
                self.cells[row][col]["number"].configure(text = str(cell_value), bg="#7BB9C2")
            else:                
                self.cells[row][col]["frame"].configure(bg="#F0F0F0")
                self.cells[row][col]["number"].configure(text = str(cell_value))

        # Update moves
        self.actual_state += 1
        self.move_count = state.moves
        self.moves_label.configure(text=self.move_count)
        self.update_idletasks()

        # Update scroll
        self.controller.my_canvas.configure(scrollregion = self.controller.my_canvas.bbox("all"))


    def next_move(self):
        self.update_GUI()
        self.over()

    def over(self):
        if self.actual_state == len(self.states):
            self.moveBtn['text']='Quit'
            self.moveBtn['command'] = lambda: self.controller.routeHomeFrame()

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
                cell_number = tk.Label(self.main_grid, bg="#F0F0F0", font='Roboto 18 bold', fg='#212121')
                cell_number.grid(row=i,column=j)
                cell_data = {"frame": cell_frame, "number": cell_number}
                row.append(cell_data)
            self.cells.append(row)