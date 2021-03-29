# Tkinter
import tkinter as tk
import functools

# Custom imports
from .home import HomeFrame
from .player_game import PlayerGame
from .results import ShowResultsFrame

class PythonGUI(tk.Tk):
    """
    The main window of the GUI.

    Attributes:
      container (tk.Frame): The frame container for the sub-frames.
      frames (dict of tk.Frame): The available sub-frames.
    """
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tenpair Game") 
        self.create_widgets()
        self.resizable(2560, 1440)
        self.minsize(1100, 800)

    def create_widgets(self):
        """
        Create the widgets for the frame.
        """             
        #  Frame Container
        # Create to check if user is on windows/linux
        #self.attributes('-zoomed', True)

        # Create Canvas
        self.my_canvas = tk.Canvas(self, bg="#212121", highlightthickness=0)
        self.my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

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
        for f in (HomeFrame, PlayerGame, ShowResultsFrame): # defined subclasses of BaseFrame
            frame = f(self.container, self)
            frame.grid(row = 0, column = 0, sticky = "nsew")
            self.frames[f] = frame
        
        self.routeHomeFrame()

    def canvas_bind(self,e):
        """
        Binds the canvas to the e parameter

        Parameters
        ----------
        e
        """
        self.my_canvas.itemconfig(self.canvas_window , width=e.width)
        self.my_canvas.configure(scrollregion = self.my_canvas.bbox("all"))

    def routeHomeFrame(self):
        self.frames[HomeFrame].tkraise()

    def routePlayerGame(self):
        self.frames[PlayerGame].tkraise()
        self.frames[PlayerGame].start_game()

    def routeShowResultsFrame(self):
        self.frames[ShowResultsFrame].tkraise()
        self.frames[ShowResultsFrame].play_animation()

    def getShowResultsFrame(self):
        return ShowResultsFrame
    
    def _on_mousewheel(self, event, scroll):
        self.my_canvas.yview_scroll(scroll, "units")

    def _on_mousewheel_w(self, event):
        self.my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")