from tkinter import *
import tkinter as tk
from tkinter import messagebox


# Be sure to import our other modules 
# so we can have access to them
import student_tracking_gui
import student_tracking_func


# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(500,350) #(Height, Width)
        self.master.maxsize(500,350)
        # This CenterWindow method will center our app on the user's screen
        student_tracking_func.center_window(self,500,350)
        self.master.title("Student Tracking")
        self.master.configure(bg="#F0F0F0")
        # This protocol method is a tkinter built-in method to catch if 
        # the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module, 
        # keeping your code comparmentalized and clutter free
        student_tracking_gui.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()