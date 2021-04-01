import tkinter as tk

class BaseFrame(tk.Frame):
    """An abstract base class for the frames that sit inside PythonGUI.

    Attributes
    ----------
    master (tk.Frame):
      - The parent widget

    controller (PythonGUI): 
      - The controlling Tk object

    Attributes
    ----------
    controller (PythonGUI): 
      The controlling Tk object.

    """
    def __init__(self, master, controller):
        """
        Constructor for the Base Frame Object

        Parameters
        ----------
        master : tk.Frame
          - parent Widget 

        controller : PythonGUI
          - The controlling Tk object.

        """
        tk.Frame.__init__(self, master)
        self.controller = controller
        self.create_widgets()
        self.configure(bg="#212121")

    def create_widgets(self):
        """
        Create the widgets for the frame.

        Raises 
        ------
        NotImplementedError
          - No implementation has yet been made
        """
        raise NotImplementedError  