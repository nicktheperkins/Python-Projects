
import tkinter
# imports all of tkinters widgets
from tkinter import *

# Frame is the parent class within Tkinter
class ParentWindow(Frame):
    # self references the class and master references the frame
    def __init__ (self, master):
        # These first three lines are oftern used when starting a project like this
        Frame.__init__ (self)
        # The self keyword passes in elements of a class into functions.
        self.master = master
        # Removed the resize window options
        self.master.resizable(width=False, height=False)
        # This gives the window a specific size 700 pixels wide by 400 pixels high
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Learning Tkinter!')
        self.master.config(bg='lightgray')
        
        self.varFName = StringVar()
        self.varLName = StringVar()
        
        self.lblFName = Label(self.master,text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))
        
        self.lblLName = Label(self.master,text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))
        
        self.lblDisplay = Label(self.master,text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))
        
        # adding in text boxes with the Entry widget
        # txtFName is a naming convention txt if for text box then the variable name
        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue')
        # this paints the window with the text box
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))
        
        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue')
        # if I wanted my box to go accross two columns I would add colspan=2 after my column=1
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))
        
        # adding a button to my form
        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)
        
        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)
        
    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        # the config() widget is used to dynamically change content in the GUI
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))
        
    def cancel(self):
        self.master.destroy()


if __name__ == "__main__":
    # call and pass the class object Tk() to root object
    root = Tk()
    # Instantiating our class with the Tkinter instantiated. Passing our class to App with Tkinter instantiated into ParentWindow()
    App = ParentWindow(root)
    # Most important line! This causes the window to coninuously loop and stay open rather than open and close quickly.
    root.mainloop()