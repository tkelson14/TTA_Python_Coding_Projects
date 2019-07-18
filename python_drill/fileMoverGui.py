from tkinter import *
import tkinter as tk


import fileMoverMain
import fileMoverFunc



def load_gui(self):

        self.browseButton = Button(self.master,text="Source",width=13,height=1,command = lambda: fileMoverFunc.sourceDir(self.txt_sourceDir))
        self.browseButton.grid(row=2,column=0,padx=(20,0),pady=(45,0))
        self.browseButton = Button(self.master,text="Destination",width=13,height=1,command = lambda: fileMoverFunc.destinationDir(self.txt_destinationDir))
        self.browseButton.grid(row=3,column=0,padx=(20,0),pady=(10,0))
        self.checkButton = Button(self.master,text="Check for files...",width=13,height=2,command = lambda: fileMoverFunc.transferFiles(self.txt_sourceDir,self.txt_destinationDir))
        self.checkButton.grid(row=4,column=0,padx=(20,0),pady=(10,0))
        self.closeButton = Button(self.master,text="Close Program",width=13,height=2,command = lambda: fileMoverFunc.close(self))
        self.closeButton.grid(row=4,column=4,padx=(0,10),pady=(0,0),sticky=E)

        self.txt_sourceDir = tk.Entry(self.master,width=60,text='')
        self.txt_sourceDir.grid(row=2,column=2,rowspan=1,columnspan=3,padx=(10,10),pady=(45,0),sticky=N+E+W)
        self.txt_destinationDir = tk.Entry(self.master,width=60,text='')
        self.txt_destinationDir.grid(row=3,column=2,rowspan=1,columnspan=3,padx=(10,10),pady=(10,0),sticky=N+E+W)
        



if __name__ == "__main__":
    pass
