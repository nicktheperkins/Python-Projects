import time
import shutil
import os
from datetime import datetime
from tkinter import *
import tkinter as tk

now = time.time()
time = datetime.now()
seconds_since_midnight = (time - time.replace(hour=0,minute=0,second=0,microsecond=0)).total_seconds()
before = now - seconds_since_midnight

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(800,170) # (Width, Height)
        self.master.maxsize(800,170)
        self.master.title("File Transfer GUI")
        self.master.configure(bg="#F0F0F0")
        load_gui(self)

def load_gui(self):
    self.lbl_browse1 = tk.Label(self.master,text='Select source folder:')
    self.lbl_browse1.grid(row=0,column=1,padx=(35,0),pady=(10,0),sticky=N+W)
    self.lbl_browse2 = tk.Label(self.master,text='Select destination folder:')
    self.lbl_browse2.grid(row=2,column=1,padx=(35,0),pady=(0,0),sticky=N+W)
    
    self.txt_browse1 = tk.Entry(self.master,text='', width=100)
    self.txt_browse1.grid(row=1,column=1,rowspan=1,columnspan=1,padx=(35,0),pady=(0,0),sticky=N+E+W)
    self.txt_browse2 = tk.Entry(self.master,text='', width=100)
    self.txt_browse2.grid(row=3,column=1,rowspan=1,columnspan=1,padx=(35,0),pady=(0,0),sticky=N+E+W)
    
    self.btn_browse1 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda:choose_folder1(self))
    self.btn_browse1.grid(row=1,column=0,padx=(10,0),pady=(0,0),sticky=W)
    self.btn_browse2 = tk.Button(self.master,width=12,height=1,text='Browse...',command=lambda:choose_folder2(self))
    self.btn_browse2.grid(row=3,column=0,padx=(10,0),pady=(0,0),sticky=W)
    self.btn_check = tk.Button(self.master,width=25,height=2,text='Check for files and transfer...',command=lambda:check_files(self))
    self.btn_check.grid(row=4,column=1,padx=(35,0),pady=(10,0),sticky=W)

def choose_folder1(self):
    path = filedialog.askdirectory(initialdir="/", title="Select file")
    self.txt_browse1.delete(0,END)
    self.txt_browse1.insert(tk.INSERT,path)
    
def choose_folder2(self):
    path = filedialog.askdirectory(initialdir="/", title="Select file")
    self.txt_browse2.delete(0,END)
    self.txt_browse2.insert(tk.INSERT,path)

def check_files(self):
    # set where the source of the files are
    src = self.txt_browse1.get().strip()
    # set the destination path
    dst = self.txt_browse2.get().strip()
    files = os.listdir(src)
    for fname in os.listdir(src):
        src_fname = os.path.join(src, fname)
        if last_mod_time(src_fname) > before:
            dst_fname = os.path.join(dst, fname)
            # move files from source to destination
            shutil.move(src_fname, dst_fname)

def last_mod_time(fname):
    return os.path.getmtime(fname)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()