# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk

# -- Costum Libraries -- #
import algorithms
from .frame import BaseFrame

class FrameAlgorithm(BaseFrame):
    """
    The application home page.

    Attributes
    ----------
    frame1_title : tk.label
      - Title lavel for the Home Page Menu

    algorithmsDict : dictionary of methods
      - dictionary with the name of the algorithm associated with the method that raised a thread that executes it

    controller : PythonGUI
      - The controlling Tk object of the interface
        
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
        tk.Button(self, text="Start with Greedy Hints (Faster)", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.playGreedy, height=3, width=55).pack(pady=5)

        tk.Button(self, text="Start with A* Hints (Precise)", font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= self.playAStar, height=3, width=55).pack(pady=5)

        frame2_title = tk.Label(self, text='Choose an Algorithm to Solve', font='Monoid 23 bold', bg="#212121", fg='#dddddd')
        frame2_title.pack(fill='both', pady=(50, 30))
        for key in algorithmsDict:
            tk.Button(self, text=key, font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= algorithmsDict[key], height=3, width=55).pack(pady=5)

    def playGreedy(self):
        self.controller.routePlayerGame(self.game, algorithms.GreedySearch)

    def playAStar(self):
        self.controller.routePlayerGame(self.game, algorithms.AStar)

    def threadAStar(self):
        """
        Method for initializing the A* thread
        """
        thread = algorithms.AStar(self.game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadBreathFirstSearch(self):
        """
        Method for initializing the Breadth First Search thread
        """
        thread = algorithms.BreathFirstSearch(self.game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadDepthFirstSearch(self):
        """
        Method for initializing the Depth First Search thread
        """
        thread = algorithms.DepthFirstSearch(self.game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadGreedySearch(self):
        """
        Method for initializing the Greedy Algorithm thread
        """
        thread = algorithms.GreedySearch(self.game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def threadIterative(self):
        """
        Method for initializing the Iterative Deepening thread
        """
        thread = algorithms.IterativeDeepening(self.game, self.setState)
        thread.start()
        self.controller.routeShowResultsFrame()

    def setState(self, game):
        """
        Method for setting the current state of the interface

        Parameters
        ----------
        game : Game
          - sets current Game to game
        """
        self.controller.frames[self.controller.getShowResultsFrame()].setState(game)
