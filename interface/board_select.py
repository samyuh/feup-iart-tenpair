# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk

# -- Costum Libraries -- #
from .frame import BaseFrame
from core import Game

class BoardSelect(BaseFrame):
    """
        The application home page.
    """
    def create_widgets(self):
        """Create the base widgets for the frame."""

        frame1_title = tk.Label(self, text='Choose the Board', font='Monoid 33 bold', bg="#212121", fg='#dddddd')
        frame1_title.pack(fill='both', pady=(50, 60))

        # Play Game Button
        tk.Button(self, text="Small Board", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.small, height=3, width=34).pack(pady=5)
        
        tk.Button(self, text="Normal Board", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.normal, height=3, width=45).pack(pady=5)

        tk.Button(self, text="Random Board (Board can be impossible to solved)", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.random, height=3, width=55).pack(pady=5)

    def small(self):
        matrix = [9, 3, 8, 7, 3, 7,
                    2, 1, 1, 8, 9, 2]

        columns = 6
        rows = 2
        game = Game(0, 0, rows, columns, matrix) 

        self.controller.routeHomeFrame(game)

    def normal(self):
        matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    1, 1, 1, 2, 1, 3, 1, 4, 1, 
                    5, 1, 6, 1, 7, 1, 8, 1, 9]
        columns = 9
        rows = 3
        game = Game(0, 0, rows, columns, matrix) 

        self.controller.routeHomeFrame(game)

    def random(self):
        matrix = [9, 3, 8, 7, 3, 7,
            2, 1, 1, 8, 9, 2]

        columns = 6
        rows = 2
        game = Game(0, 0, rows, columns, matrix) 

        self.controller.routeHomeFrame(game)