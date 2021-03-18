import tkinter as tk

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


class ExecuteFrame(BaseFrame):
    """The application home page.

    Attributes:
      new_button (tk.Button): The button to switch to HomeFrame.

    """

    def create_widgets(self):
        """Create the base widgets for the frame."""
        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(HomeFrame),
                                    padx=5,
                                    pady=5,
                                    text="Home")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)


class HomeFrame(BaseFrame):
    """The application home page.

    Attributes:
      new_button (tk.Button): The button to switch to ExecuteFrame.

    """

    def create_widgets(self):
        """Create the base widgets for the frame."""
        self.new_button = tk.Button(self,
                                    anchor=tk.W,
                                    command=lambda: self.controller.show_frame(ExecuteFrame),
                                    padx=5,
                                    pady=5,
                                    text="Execute")
        self.new_button.grid(padx=5, pady=5, sticky=tk.W+tk.E)


class PythonGUI(tk.Tk):
    """The main window of the GUI.

    Attributes:
      container (tk.Frame): The frame container for the sub-frames.
      frames (dict of tk.Frame): The available sub-frames.

    """

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Python GUI")
        self.create_widgets()
        self.resizable(0, 0)

    def create_widgets(self):
        """Create the widgets for the frame."""             
        #   Frame Container
        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0, sticky=tk.W+tk.E)

        #   Frames
        self.frames = {}
        for f in (HomeFrame, ExecuteFrame): # defined subclasses of BaseFrame
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

if __name__ == "__main__":
    app = PythonGUI()
    app.mainloop()
    exit()