# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk

# -- Costum Libraries -- #
import algorithms

from tkinter import Button
from tkinter.font import Font
from core import Game

import time

from .frame import BaseFrame

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

        tk.Button(self, text="Play Game", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.play, height=3, width=30).pack(pady=5)

        for key in algorithmsDict:
            tk.Button(self, text=key, font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= algorithmsDict[key], height=3, width=30).pack(pady=5)

    def play(self):
        #p = PlayerGame()
        #thread = p.play
        #thread.start()
        self.controller.routePlayerGame()

    def threadAStar(self):
        thread = algorithms.AStar(self.setState)
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
        thread = algorithms.GreedySearch(self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadIterative(self):
        thread = algorithms.IterativeDeepening(self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def setState(self, game):
        self.controller.frames[self.controller.getShowResultsFrame()].setState(game)
