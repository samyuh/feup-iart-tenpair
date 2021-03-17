# Graphic Interface
from tkinter import * 
from threading import Thread

# Personal Libraries

# TODO: Cleanup with __init__ file :P
from algorithms.aStar import aStarThread
from algorithms.breathFirstSearch import breathFirstSearchThread
from algorithms.depthFirstSearch import depthFirstSearchThread
from algorithms.greedySearch import greedySearchThread
   
def threadAStar():
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
    pass

if __name__ == "__main__":
    # create a GUI window 

    gui = Tk() 
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

    
