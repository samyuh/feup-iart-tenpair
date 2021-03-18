# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk

# -- Costum Libraries -- #
import algorithms


class BaseFrame(tk.Frame):
    """An abstract base class for the frames that sit inside PythonGUI.

    Args:
      master (tk.Frame): The parent widget.
      controller (PythonGUI): The controlling Tk object.

    Attributes:
      controller (PythonGUI): The controlling Tk object.

    """

    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Create the widgets for the frame."""
        raise NotImplementedError


class PythonGUI(tk.Tk):
    """
    The main window of the GUI.

    Attributes:
      container (tk.Frame): The frame container for the sub-frames.
      frames (dict of tk.Frame): The available sub-frames.
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Python GUI")
        self.create_widgets()
        self.resizable(0, 0)
        self.title("Tenpair Game") 

    def create_widgets(self):
        """
        Create the widgets for the frame.
        """             
        #  Frame Container
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky=tk.W+tk.E)

        #   Frames
        self.frames = {}
        for f in (HomeFrame, ExecuteFrame, ShowResultsFrame): # defined subclasses of BaseFrame
            frame = f(self.container, self)
            frame.grid(row=2, column=2, sticky=tk.NW+tk.SE)
            self.frames[f] = frame
        self.show_frame(HomeFrame)

    def show_frame(self, cls):
        """Show the specified frame.

        Args:
          cls (tk.Frame): The class of the frame to show. 

        """
        self.frames[cls].tkraise()    


class ShowResultsFrame(BaseFrame):
    """
    The app results page.
    """
    def create_widgets(self):
        """Create the base widgets for the frame."""
        frame3_title= tk.Label(self, text='Done. Result:',font='times 35', bg='light blue')
        frame3_title.pack(fill='both', expand=True)

        frame3_btn = tk.Button(self, text='Main Menu',command=lambda: self.controller.show_frame(HomeFrame))
        frame3_btn.pack(fill='x',ipady=15)


class ExecuteFrame(BaseFrame):
    """
    The application processing page.
    """

    def create_widgets(self):
        """Create the base widgets for the frame."""
        frame2_title = tk.Label(self, text='Processing Nodes', font='times 35', bg='light blue')
        frame2_title.pack(fill='both', expand=True)


class HomeFrame(BaseFrame):
    """
        The application home page.
    """

    def create_widgets(self):
        """Create the base widgets for the frame."""

        frame1_title = tk.Label(self, text='Choose the Algorithm', font='times 35', bg='light blue')
        frame1_title.pack(fill='both', expand=True)

        algorithmsDict = {
            "A Star": self.threadAStar,
            "Breadth First Search": self.threadBreathFirstSearch,
            "Depth First Search": self.threadDepthFirstSearch,
            "Greedy Search": self.threadGreedySearch,
            "Iterative Deepening": self.threadIterative
        }

        for key in algorithmsDict:
            tk.Button(self, text=key, fg='white', bg='red', 
                command= algorithmsDict[key], height=5, width=50).pack()

    def threadAStar(self):
        thread = algorithms.AStar(self.changeState)
        thread.start()
        self.controller.show_frame(ExecuteFrame)

    def threadBreathFirstSearch(self):
        thread = algorithms.BreathFirstSearch(self.changeState)
        thread.start()
        self.controller.show_frame(ExecuteFrame)

    def threadDepthFirstSearch(self):
        thread = algorithms.DepthFirstSearch(self.changeState)
        thread.start()
        self.controller.show_frame(ExecuteFrame)

    def threadGreedySearch(self):
        thread = algorithms.GreedySearch(self.changeState)
        thread.start()
        self.controller.show_frame(ExecuteFrame) 

    def threadIterative(self):
        thread = algorithms.IterativeDeepening(self.changeState)
        thread.start()
        self.controller.show_frame(ExecuteFrame)

    def changeState(self):
        self.controller.show_frame(ShowResultsFrame)