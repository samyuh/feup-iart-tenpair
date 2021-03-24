# -- Imports -- #
# -- External Libraries -- #
import tkinter as tk

# -- Costum Libraries -- #
import algorithms

from tkinter import Button
from tkinter.font import Font
from core import Game

import time


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
        self.config(background="#212121")
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
        self.resizable(2560, 1440)
        self.title("Tenpair Game") 
        self.y = self.winfo_screenheight()
        self.x = self.winfo_screenwidth()


    def create_widgets(self):
        """
        Create the widgets for the frame.
        """             
        #  Frame Container
        self.attributes('-zoomed', True)
        self.container = tk.Frame(self)
        #self.container.pack(fill = "both")
        self.container.pack(fill = tk.BOTH, expand = "true")
        self.container.rowconfigure(0, weight=1) # this needed to be added
        self.container.columnconfigure(0, weight=1) # as did this

        #   Frames
        self.frames = {}
        for f in (HomeFrame, ExecuteFrame, ShowResultsFrame): # defined subclasses of BaseFrame
            frame = f(self.container, self)
            
            frame.grid(row = 0, column = 0, sticky = "nsew")
            self.frames[f] = frame
        self.show_frame(HomeFrame)

    def show_frame(self, cls):
        """Show the specified frame.

        Args:
          cls (tk.Frame): The class of the frame to show. 

        """
        self.frames[cls].tkraise()    


class ExecuteFrame(BaseFrame):
    """
    The application processing page.
    """

    def create_widgets(self):
        """Create the base widgets for the frame."""
        
        frame2_title = tk.Label(self, text='Processing Nodes', font='times 35', bg='light blue')
        frame2_title.pack(fill='both', expand=True)
        """
        tk.Label(self, text="Visited Nodes: XY", bg="black", fg="#FFBD09").place(x=300, y=100)
        tk.Label(self, text="Remaining Nodes: XY", bg="black", fg="#FFBD09").place(x=300, y=125)
        tk.Label(self, text="Loading...", bg="black", fg="#FFBD09").place(x=400, y=150)

        for i in range(16):
            tk.Label(self, bg="#1F2732", width=2, height=1).place(x=(i+12)*22, y=200)

        self.play_animation()
        """
        
    def play_animation(self):
        """
        for i in range(200):
            for j in range(16):
                tk.Label(self, bg="#FFBD09", width=2, height=1).place(x=(j+12)*22, y=200)
                self.update()
                time.sleep(0.1)
                tk.Label(self, bg="#1F2732", width=2, height=1).place(x=(j+12)*22, y=200)
        else:
            self.destroy()
            exit()
        """


class ShowResultsFrame(BaseFrame):
    def __init__(self, master, controller):
        BaseFrame.__init__(self, master, controller)
    
    def setState(self, state):
        self.loading = False
        self.clearFrame()
        self.states = state

        self.actual_state = 0
        self.move_count = 0

        first_state = self.states[self.actual_state]

        # todo: adjust frame size as desired
        self.main_grid = tk.Frame(self, bg = "#c7c7c7", bd = "3")
        
        self.main_grid.rowconfigure(0, weight=1) # this needed to be added
        self.main_grid.columnconfigure(0, weight=1) # as did this
        self.main_grid.pack(pady=100)
        #self.main_grid.grid()

        # Create Gui and represent first state
        self.make_GUI(first_state)
        self.update_GUI()

        # Next Move Button
        self.moveBtn = Button(self, text="Next Move", command = self.next_move, font='Roboto 11 bold', fg='#ffffff', bg='#1D8EA0')
        self.moveBtn.place(relx=0.7, y=45)
        self.moveBtn.config(highlightbackground='#1D8EA0')

    def create_widgets(self):
        """Create the base widgets for the frame."""
        
        """
        frame2_title = tk.Label(self, text='Processing Nodes', font='times 35', bg='light blue')
        frame2_title.pack(fill='both', expand=True)
        """
        self.loadingNext = 0
        
        
    def play_animation(self):
        self.loadingText = tk.Label(self, text='Processing Nodes...', font='Monoid 35 bold', bg='#212121', fg="#ffffff")
        self.loadingText.pack(fill='both', expand=True)

        self.loading = True
        while(self.loading):
            if self.loadingText:
                self.loadingText.destroy()
            self.loadingText = tk.Label(self, text='Processing Nodes' + self.loadingNext * '.' + ' ' * (3 - self.loadingNext), font='Monoid 35 bold', bg='#212121', fg="#ffffff")
            self.loadingText.pack(fill='both', expand=True)
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

    def next_move(self):
        self.update_GUI()
        self.over()

    def over(self):
        if self.actual_state == len(self.states):
            self.moveBtn['text']='Quit'
            self.moveBtn['command'] = lambda: self.controller.show_frame(HomeFrame)

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

        for key in algorithmsDict:
            tk.Button(self, text=key, font='Roboto 16 bold', fg='#ffffff', bg='#1D8EA0', 
                command= algorithmsDict[key], height=3, width=30).pack(pady=5)

    def threadAStar(self):
        thread = algorithms.AStar(self.setState)
        thread.start()
        self.controller.show_frame(ShowResultsFrame)
        self.controller.frames[ShowResultsFrame].play_animation()

    def threadBreathFirstSearch(self):
        thread = algorithms.BreathFirstSearch(self.setState)
        thread.start()
        self.controller.show_frame(ShowResultsFrame)
        self.controller.frames[ShowResultsFrame].play_animation()

    def threadDepthFirstSearch(self):
        thread = algorithms.DepthFirstSearch(self.setState)
        thread.start()
        self.controller.show_frame(ShowResultsFrame)

    def threadGreedySearch(self):
        thread = algorithms.GreedySearch(self.setState)
        thread.start()
        self.controller.show_frame(ShowResultsFrame)

    def threadIterative(self):
        thread = algorithms.IterativeDeepening(self.setState)
        thread.start()
        self.controller.show_frame(ShowResultsFrame)

    def setState(self, game):
        self.controller.frames[ShowResultsFrame].setState(game)
