# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk

from random import randint

# -- Costum Libraries -- #
from .frame import BaseFrame
from core import Game

class FrameBoard(BaseFrame):
    """
        The application home page.
    """
    def create_widgets(self):
        """Create the base widgets for the frame."""

        frame_title = tk.Label(self, text='TenPair', font='Monoid 50 bold', bg="#212121", fg='#dddddd')
        frame_title.pack(pady=(50, 10))

        frame1_title = tk.Label(self, text='Choose the Board', font='Monoid 33 bold', bg="#212121", fg='#dddddd')
        frame1_title.pack(pady=(10, 60))

        # Play Game Button
        tk.Button(self, text="6x2 Board", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.small, height=3, width=55).pack(pady=5)

        tk.Button(self, text="6x3 Board", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.small2, height=3, width=55).pack(pady=5)
        
        tk.Button(self, text="9x2 Board", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.medium, height=3, width=55).pack(pady=5)
        
        tk.Button(self, text="9x3 Board (Original)", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.normal, height=3, width=55).pack(pady=5)

        tk.Button(self, text="Random Board (Can take to long to be solved)", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.random, height=3, width=55).pack(pady=(5,0))

    def small(self):
        matrix = [9, 3, 8, 7, 3, 7,
                    2, 1, 1, 8, 9, 2]

        columns = 6
        rows = 2
        game = Game(0, 0, rows, columns, matrix) 

        self.controller.routeFrameAlgorithm(game)

    def small2(self):
        matrix = [7, 4, 4, 2, 3, 1,
                  5 , 5, 3, 1, 9, 3,
                  5, 2, 1, 1, 7, 3]

        columns = 6
        rows = 3
        game = Game(0, 0, rows, columns, matrix) 

        self.controller.routeFrameAlgorithm(game)

    def medium(self):
        matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9, 
                  1, 1, 1, 2, 1, 3, 1, 4, 1,]

        columns = 9
        rows = 2
        game = Game(0, 0, rows, columns, matrix) 

        self.controller.routeFrameAlgorithm(game)


    def normal(self):
        matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    1, 1, 1, 2, 1, 3, 1, 4, 1, 
                    5, 1, 6, 1, 7, 1, 8, 1, 9]
        columns = 9
        rows = 3
        game = Game(0, 0, rows, columns, matrix) 

        self.controller.routeFrameAlgorithm(game)

    def random(self):
        columns = randint(2, 4)
        rows = randint(3, 6)

        n = columns * rows
        matrix = [randint(1,9) for _ in range(n)]

        # Just to test
        print(matrix)
        print(columns)
        print(rows)

        game = Game(0, 0, rows, columns, matrix) 
        self.controller.routeFrameAlgorithm(game)