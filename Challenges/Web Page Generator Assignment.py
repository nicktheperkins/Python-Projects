import webbrowser
from tkinter import *
import tkinter as tk


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(480,170) # (Width, Height)
        self.master.maxsize(480,170)
        self.master.title("Web Page Generator")
        self.master.configure(bg="#F0F0F0")
        load_gui(self)

def load_gui(self):
    # lable with instructions to add text
    self.lbl_enter = tk.Label(self.master,text='Enter text here:')
    self.lbl_enter.grid(row=0,column=0,padx=(20,0),pady=(40,0),sticky=N+W)
    # textbox to add text
    self.txt_browse1 = tk.Entry(self.master,text='', width=50)
    self.txt_browse1.grid(row=1,column=0,rowspan=1,columnspan=1,padx=(20,0),pady=(0,0),sticky=N+E+W)
    # button that points to creat_page function
    self.btn_browse1 = tk.Button(self.master,width=15,height=1,text='Create Web Page',command=lambda:create_page(self))
    self.btn_browse1.grid(row=1,column=1,padx=(10,0),pady=(0,0),sticky=W)
    
def create_page(self):
    # creates new file in directory if file doesn't exist
    f = open("new_web_page.html", "x")
    # pulls text from textbox
    text = self.txt_browse1.get().strip()
    # inserts text into the body of the html file
    f.write("<html>\n<body>\n\t<h1>{}</h1>\n</body>\n</html>".format(text))
    f.close()
    # opens new tab in default browser with new text inserted
    webbrowser.open_new_tab("new_web_page.html")
    

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()