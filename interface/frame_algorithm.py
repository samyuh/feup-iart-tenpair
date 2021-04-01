# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk

# -- Costum Libraries -- #
import algorithms
from .frame import BaseFrame

class FrameAlgorithm(BaseFrame):
    """
        The application home page.
    """
    def initGame(self, game):
        self.game = game

    def create_widgets(self):
        """Create the base widgets for the frame."""

        frame_title = tk.Label(self, text='TenPair', font='Monoid 50 bold', bg="#212121", fg='#dddddd')
        frame_title.pack(pady=(50, 10))

        algorithmsDict = {
            "A*": self.threadAStar,
            "Breadth First Search": self.threadBreathFirstSearch,
            "Depth First Search": self.threadDepthFirstSearch,
            "Greedy Search": self.threadGreedySearch,
            "Iterative Deepening": self.threadIterative
        }

        frame1_title = tk.Label(self, text='Play the Game', font='Monoid 23 bold', bg="#212121", fg='#dddddd')
        frame1_title.pack(fill='both', pady=(10, 30))

        # Play Game Button
        tk.Button(self, text="Start", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.play, height=3, width=55).pack(pady=5)

        frame2_title = tk.Label(self, text='Choose an Algorithm to Solve', font='Monoid 23 bold', bg="#212121", fg='#dddddd')
        frame2_title.pack(fill='both', pady=(50, 30))
        for key in algorithmsDict:
            tk.Button(self, text=key, font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= algorithmsDict[key], height=3, width=55).pack(pady=5)

    def play(self):
        self.controller.routePlayerGame(self.game)

    def threadAStar(self):
        thread = algorithms.AStar(self.game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadBreathFirstSearch(self):
        thread = algorithms.BreathFirstSearch(self.game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadDepthFirstSearch(self):
        thread = algorithms.DepthFirstSearch(self.game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadGreedySearch(self):
        thread = algorithms.GreedySearch(self.game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadIterative(self):
        thread = algorithms.IterativeDeepening(self.game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def setState(self, game):
        self.controller.frames[self.controller.getShowResultsFrame()].setState(game)
