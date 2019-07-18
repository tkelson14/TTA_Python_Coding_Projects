from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.filedialog
import os
import time
import shutil
import sqlite3

import fileMoverMain
import fileMoverGui

# Ask to close program
def close(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        
# Allows the user to select their source folder, and displays the directory path in the text box
def sourceDir(txt_sourceDir): 
    sourceName = tk.filedialog.askdirectory()
    if sourceName:
        txt_sourceDir.delete(0, END)
        txt_sourceDir.insert(0, sourceName)
    return sourceName


# Allows the user to select their destination folder, and displays the directory path in the text box
def destinationDir(txt_destinationDir): 
    destinationName = tk.filedialog.askdirectory()
    if destinationName:
        txt_destinationDir.delete(0, END)
        txt_destinationDir.insert(0, destinationName)
    return destinationName


# Create the database to log file transfers
def createDB():
    conn = sqlite3.connect("fileTransferLog.db")
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_fileLog( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
            col_fileName TEXT NOT NULL, \
            col_modTime TEXT NOT NULL \
            );")
        conn.commit()
    conn.close()


# Moves all .txt files from source folder to destination folder and calls the createDB function to insert file information
def transferFiles(txt_sourceDir, txt_destinationDir):
    createDB()
    
    sourcePath = txt_sourceDir.get()
    destinationPath = txt_destinationDir.get()

    for txtFile in os.listdir(path = sourcePath):
        abPath = os.path.join(sourcePath, txtFile)
        if txtFile.endswith('.txt'):
            shutil.move(os.path.join(sourcePath, txtFile), os.path.join(destinationPath, txtFile))
            txtTime = os.path.getmtime(destinationPath)
            print(txtFile, txtTime)

            conn = sqlite3.connect("fileTransferLog.db")        
            with conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_fileLog(col_fileName, col_modTime) VALUES(?, ?)", (txtFile, txtTime))
                conn.commit()
            conn.close()
    messagebox.showinfo("Request Completed Successfully", \
                        "Your text files have been successfully transfered to the destination folder. The transfer log database has been updated with the effected file information.")

    
if __name__ == "__main__":
    pass
