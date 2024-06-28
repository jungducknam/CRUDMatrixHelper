import tkinter as tk
from tkinter import filedialog
import os

class fileManager:
    def __init__(self, filePath, mode='r'):
        self.filePath = filePath
        self.mode = mode
        self.file = ""

    def readTextFile(self):
        self.file = open(self.filePath, self.mode, encoding="utf-8")
        str = self.file.read()
        self.closeFile()
        return str

    def closeFile(self):
        if self.file:
            self.file.close()

def selectFile():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path