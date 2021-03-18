"""
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
"""