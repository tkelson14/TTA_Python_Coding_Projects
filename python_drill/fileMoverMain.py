from tkinter import *
import tkinter as tk


import fileMoverFunc
import fileMoverGui


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,180)
        self.master.maxsize(500,180)
        self.master.title("Check Files")
        arg = self.master

        fileMoverGui.load_gui(self)





if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
