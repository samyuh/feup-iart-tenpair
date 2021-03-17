# Graphic Interface
from tkinter import * 

from threading import Thread

import time

class LoadingSplash:
    def __init__(self):
        self.root = Tk()
        self.root.config(bg="black")
        self.root.title("Processing the algorithm")
        self.root.geometry("900x500")

        Label(self.root, text="Visited Nodes: XY", bg="black", fg="#FFBD09").place(x=300, y=100)
        Label(self.root, text="Remaining Nodes: XY", bg="black", fg="#FFBD09").place(x=300, y=125)
        Label(self.root, text="Loading...", bg="black", fg="#FFBD09").place(x=400, y=150)

        for i in range(16):
            Label(self.root, bg="#1F2732", width=2, height=1).place(x=(i+12)*22, y=200)

        #self.play_animation()
        self.root.mainloop()

    def play_animation(self):
        for i in range(200):
            for j in range(16):
                Label(self.root, bg="#FFBD09", width=2, height=1).place(x=(j+12)*22, y=200)
                self.root.update()
                time.sleep(0.1)
                Label(self.root, bg="#1F2732", width=2, height=1).place(x=(j+12)*22, y=200)
        else:
            self.root.destroy()
            exit()

    def updateText(self):
        pass

# TODO: Cleanup with __init__ file :P
from algorithms.aStar import aStarThread
from algorithms.breathFirstSearch import breathFirstSearchThread
from algorithms.depthFirstSearch import depthFirstSearchThread
from algorithms.greedySearch import greedySearchThread
from algorithms.iterativeDeepening import iterativeDeepeningThread

gui = Tk() 


def show_frame(frame):
    frame.tkraise()
    
gui.state('zoomed')
gui.title("Tenpair Game") 

gui.rowconfigure(0, weight=1)
gui.columnconfigure(0, weight=1)

frame1 = Frame(gui)
frame2 = Frame(gui)
frame3 = Frame(gui)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='nsew')

def threadAStar():
    show_frame(frame2)
    t1=Thread(target=aStarThread) 
    t1.daemon = True 
    t1.start() 

def threadBreathFirstSearch():
    t1=Thread(target=breathFirstSearchThread) 
    t1.daemon = True 
    t1.start() 

def threadDepthFirstSearch():
    t1=Thread(target=depthFirstSearchThread) 
    t1.daemon = True 
    t1.start() 

def threadGreedySearch():
    t1=Thread(target=greedySearchThread) 
    t1.daemon = True 
    t1.start() 

def threadIterative():
    t1=Thread(target=iterativeDeepeningThread) 
    t1.daemon = True 
    t1.start() 
    pass

# ================== Frame 1 code
frame1_title = Label(frame1, text='Choose the Algorithm', font='times 35', bg='light blue')
frame1_title.pack(fill='both', expand=True)

Button(frame1, text=' A-Star ', fg='white', bg='red', 
    command=threadAStar, height=5, width=50).pack()

Button(frame1, text=' Greedy Algorithm ', fg='white', bg='red', 
    command=threadGreedySearch, height=5, width=50).pack()

Button(frame1, text=' Breath First ', fg='white', bg='red', 
    command=threadBreathFirstSearch, height=5, width=50).pack()

Button(frame1, text=' Depth First ', fg='white', bg='red', 
    command=threadDepthFirstSearch, height=5, width=50).pack()

Button(frame1, text=' Iterative ', fg='white', bg='red', 
    command=threadIterative, height=5, width=50).pack()

# ================== Frame 2 code
frame2_title=  Label(frame2, text='Processing Nodes', font='times 35', bg='light blue')
frame2_title.pack(fill='both', expand=True)

frame2_btn = Button(frame2, text='Enter',command=lambda:show_frame(frame3))
frame2_btn.pack(fill='x', ipady=15)

# ================== Frame 3 code
frame3_title=  Label(frame3, text='Done. Result:',font='times 35', bg='light blue')
frame3_title.pack(fill='both', expand=True)

frame3_btn = Button(frame3, text='Enter',command=lambda:show_frame(frame1))
frame3_btn.pack(fill='x',ipady=15)

def main():
    # create a GUI window 
    """
    # set the background colour of GUI window 
    gui.configure(background="light blue") 

    # set the title of GUI window 
    gui.title("Tenpair Game") 

    # set the configuration of GUI window 
    gui.geometry("270x150")
    aStarButton = Button(gui, text=' A-Star ', fg='white', bg='red', 
                    command=threadAStar, height=1, width=20)
    aStarButton.grid(row=5, column=0)

    greedyButton = Button(gui, text=' Greedy Algorithm ', fg='white', bg='red', 
                    command=threadGreedySearch, height=1, width=20)
    greedyButton.grid(row=6, column=0)

    greedyButton = Button(gui, text=' Breath First ', fg='white', bg='red', 
                    command=threadBreathFirstSearch, height=1, width=20)
    greedyButton.grid(row=7, column=0)

    greedyButton = Button(gui, text=' Depth First ', fg='white', bg='red', 
                    command=threadDepthFirstSearch, height=1, width=20)
    greedyButton.grid(row=8, column=0)  

    greedyButton = Button(gui, text=' Iterative ', fg='white', bg='red', 
                    command=threadIterative, height=1, width=20)
    greedyButton.grid(row=9, column=0)    
    # start the GUI 
    gui.mainloop() 
    """
    show_frame(frame1)

    gui.mainloop()