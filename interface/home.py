# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk

# -- Costum Libraries -- #
import algorithms

from core import Game
from .frame import BaseFrame

# Home where user can select board size and start

# Next where user can choose to play or see AI solving the problem
class HomeFrame(BaseFrame):
    """
        The application home page.
    """

    def create_widgets(self):
        """Create the base widgets for the frame."""

        frame1_title = tk.Label(self, text='Choose the Algorithm', font='Monoid 33 bold', bg="#212121", fg='#dddddd')
        frame1_title.pack(fill='both', pady=(50, 60))

        algorithmsDict = {
            "A Star": self.threadAStar,
            "Breadth First Search": self.threadBreathFirstSearch,
            "Depth First Search": self.threadDepthFirstSearch,
            "Greedy Search": self.threadGreedySearch,
            "Iterative Deepening": self.threadIterative
        }

        # Play Game Button
        tk.Button(self, text="Play Game", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.play, height=3, width=30).pack(pady=5)

        for key in algorithmsDict:
            tk.Button(self, text=key, font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= algorithmsDict[key], height=3, width=30).pack(pady=5)

    def play(self):
        self.controller.routePlayerGame()

    def threadAStar(self):
        matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    1, 1, 1, 2, 1, 3, 1, 4, 1, 
                    5, 1, 6, 1, 7, 1, 8, 1, 9]
        columns = 9
        rows = 3
        game = Game(0, 0, rows, columns, matrix)

        thread = algorithms.AStar(game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadBreathFirstSearch(self):
        thread = algorithms.BreathFirstSearch(self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadDepthFirstSearch(self):
        thread = algorithms.DepthFirstSearch(self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadGreedySearch(self):
        gameState = [1, 2, 3, 4, 5, 6, 7, 8, 9,
                    1, 1, 1, 2, 1, 3, 1, 4, 1, 
                    5, 1, 6, 1, 7, 1, 8, 1, 9]
        columns = 9
        rows = 3
        game = Game(0, 0, rows, columns, gameState)

        thread = algorithms.GreedySearch(game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadIterative(self):
        thread = algorithms.IterativeDeepening(self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def setState(self, game):
        self.controller.frames[self.controller.getShowResultsFrame()].setState(game)
