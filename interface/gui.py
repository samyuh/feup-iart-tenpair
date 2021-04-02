# Tkinter
import tkinter as tk
import functools

# Custom imports
from .frame_algorithm import FrameAlgorithm
from .frame_board import FrameBoard
from .frame_game import FrameGame
from .frame_results import FrameResults

from core import Game

class PythonGUI(tk.Tk):
    """
    The main window of the GUI.

    Attributes
    ----------
    container : tk.Frame
        - The frame container for the sub-frames

    frames : dict of tk.Frame
        - The available sub-frames
    
    my_canvas : tk.Canvas
        tkinter object for the GUI canvas
    """
    def __init__(self):
        """
        Constructor for the PythonGUI object
        Parameters
        ----------
        title : String
            Title of the Game
        """
        tk.Tk.__init__(self)
        self.title("Tenpair Game") 
        self.create_widgets()
        self.resizable(2560, 1440)
        self.minsize(1100, 700)

    def create_widgets(self):
        """
        Create the widgets for the frame.
        """            
        #  Frame Container
        # Uncomment this line to expand windows when opening. Only works on linux
        #self.attributes('-zoomed', True)

        # Create Canvas
        self.my_canvas = tk.Canvas(self, bg="#212121", highlightthickness=0)
        self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)

        # Scrollbar
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure canvas
        self.my_canvas.configure(yscrollcommand = my_scrollbar.set)
        self.my_canvas.bind('<Configure>', self.canvas_bind)
        self.my_canvas.bind_all("<MouseWheel>", self._on_mousewheel_w)
        self.my_canvas.bind_all("<Button-4>", functools.partial(self._on_mousewheel, scroll=-1))
        self.my_canvas.bind_all("<Button-5>", functools.partial(self._on_mousewheel, scroll=1))

        # Create Main Frame
        self.container = tk.Frame(self.my_canvas)
        self.container.rowconfigure(0, weight=1) # this needed to be added
        self.container.columnconfigure(0, weight=1) # as did this
        self.container.configure(bg="#212121")
       
        self.canvas_window = self.my_canvas.create_window(0, 0, window = self.container, width=self.winfo_screenwidth())

        #   Frames
        self.frames = {}
        for f in (FrameAlgorithm, FrameBoard, FrameGame, FrameResults): # defined subclasses of BaseFrame
            frame = f(self.container, self)
            frame.grid(row = 0, column = 0, sticky = "nsew")
            self.frames[f] = frame
        
        self.routeBoardSelect()

    def canvas_bind(self,event):
        """
        Binds the canvas to the e parameter

        Parameters
        ----------
        event: Event
          - event after resizing window
        """
        self.my_canvas.itemconfig(self.canvas_window , width=event.width)
        self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all"))

    def routeBoardSelect(self):
        """
        Switches to the board selection page
        """
        self.frames[FrameBoard].tkraise()

    def routeFrameAlgorithm(self, game):
        """
        Switches to the algorithm selection page
        """
        self.frames[FrameAlgorithm].initGame(game)
        self.frames[FrameAlgorithm].tkraise()

    def routePlayerGame(self, game, chosen):
        """
        Switches to the player game menu
        """
        self.frames[FrameGame].initGame(game)
        self.frames[FrameGame].start_game(chosen)
        self.frames[FrameGame].tkraise()

    def routeShowResultsFrame(self):
        """
        Switches to the Show results menu
        """
        self.frames[FrameResults].tkraise()
        self.frames[FrameResults].play_animation()

    def getShowResultsFrame(self):
        """
        Get Method to obtain the frame from the show results menu

        Returns
        -------
        Frame :
            returns the frame used on the show results menu 
        """
        return FrameResults
    

    def _on_mousewheel(self, event, scroll):
        """
        Sets mouseWheel scroll (Windows)

        Parameters
        ----------
        event : Event
            - defines an event on which this method is applied. "In our program, we only use the on_mousewheel event to enable mouse scrolling
        scroll : int
            - binds the ammount moved associated with the scrolling
        """
        if self.my_canvas.yview() == (0.0, 1.0):
            return
        self.my_canvas.yview_scroll(scroll, "units")

    def _on_mousewheel_w(self, event):
        """
        Sets mouseWheel scroll with predefined units (Linux)
        """
        if self.my_canvas.yview() == (0.0, 1.0):
            return
        self.my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
