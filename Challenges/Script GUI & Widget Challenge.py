from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(480,170) # (Width, Height)
        self.master.maxsize(480,170)
        self.master.title("Check files")
        self.master.configure(bg="#F0F0F0")
        load_gui(self)

def load_gui(self):
    self.txt_browse1 = tk.Entry(self.master,text='', width=50)
    self.txt_browse1.grid(row=0,column=1,rowspan=1,columnspan=1,padx=(35,0),pady=(40,0),sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master,text='', width=50)
    self.txt_browse2.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(35,0),pady=(10,0),sticky=N+E+W)
    
    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda:choose_folder(self))
    self.btn_browse1.grid(row=0,column=0,padx=(10,0),pady=(40,0),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...')
    self.btn_browse2.grid(row=1,column=0,padx=(10,0),pady=(10,0),sticky=W)
    self.btn_check = tk.Button(self.master,width=12,height=2,text='Check for files...')
    self.btn_check.grid(row=2,column=0,padx=(10,0),pady=(10,0),sticky=W)
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close Program')
    self.btn_close.grid(row=2,column=1,padx=(0,0),pady=(10,0),sticky=E)
    
def choose_folder(self):
    path = filedialog.askdirectory(initialdir="/", title="Select file")
    self.txt_browse1.delete(0,END)
    self.txt_browse1.insert(tk.INSERT,path)
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()