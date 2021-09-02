# TKINTER PART ONE ASSIGNMENT


# The first thing to do is import the Tkinter module. Usually this is done by importing the module into our local namespace
# so that we can use the classes and constants by their names (like Label, Button, TOP) instead of having to constantly qualify
# everything (like Tkinter.Label, Tkinter.Button, Tkinter.TOP).
from tkinter import *

# Now if this produced an error message, it means that either Tk/Tcl is not installed on your system or that Python is not linked
# to it. If you received an error message, fix this before continuing. Otherwise, try the first command which will create a window
# and assign it to the variable “win.”
win = Tk()

# Create a couple of buttons for this window.
b1 = Button(win, text="One")
b2 = Button(win, text="Two")

# The clas "Button" takes the parent window as the first argument.
# You might be suprised that the buttons did not appear in the window.
# They must first be placed with one of the so-called geometry managers.
# The two most common ones are "pack" and "grid".


# TKINTER PART TWO ASSIGNMENT

# With "pack," you tell your widget to pack itself into its parent. You may specify a side (TOP, LEFT, RIGHT, BOTTOM),
# then your widget will be packed against either that paretn's wall or a previous widget with the same packing. If you don't
# specify a side, the default will be TOP.
b1.pack()
b1.pack()

# Notice that after the first command the button is placed in the window. The window itself is shrunk to the size of the button.
# When the second button is packed, the window is expanded to accommodate it. The default TOP stacked them vertically in the
# order they were packed.
b1.pack(side=LEFT)
b2.pack(side=LEFT)

# In practice, the pack geometry manager is generally used in one of these two modes to place a set of widgets in either
# a vertical column or a horizontal row.

# Our buttons look a little squished. We can fix that by packing them with a little padding. “padx” adds
# pixels to the left and right, while “pady” adds them to the top and bottom.
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)


# TKINTER PART THREE ASSIGNMENT

# Another way to place widgets (buttons, labels and whatnot) is in a table or grid. Here, the parent window is divided
# into rows and columns. Each widget is placed in a given cell. The grid manager keeps track of how many rows and columns
# are actually needed and fills out the window accordingly. It also keeps track of how wide and tall each column and row
# must be respectively to accommodate the largest widget in that row or column. Rows do not all have to be the same height;
# and columns do not have to all be the same width.

# Make a new window with the same buttons, but this time lay them out in a two-by-two grid.
win = Tk()
b1 = Button(win, text="One")
b2 = Button(win, text="Two")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)

# You can see that some empty space is left since nothing was put into row 0, column 1 or into row1, column 0.
# Let's use this as an opportunity to look at a new widget type. A label widget is used to place text into the window
# and is very simple.
l = Label(win, text="This is a label")
l.grid(row=1, column=0)
# Notice how the label pushed the width of column 0 out to accommodate the text.

# A frame is a widget whose sole purpose is to contain other widgets. Groups of widgets, whether packed or placed in a grid,
# may be combined into a single Frame. Frames may then be packed with other widgets and frames. This feature lets us create
# just about any kind of layout. As an example, place a label over 3 buttons in a row. First pack the buttons into a frame
# horizontally, then pack the label and frame vertically in the window.
win = Tk()
f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(win, text="This label is over all buttons")
l.pack()
f.pack()

# In addition to pack and grid, there is a place method to position a widget at a precise location within a frame or window.
# It is not often used because it is frankly easier to let pack and grid just spread things out as needed, especially if you
# use the mouse to shrink or expand a window.

# There are other keyword arguments that are common when using either pack or grid. We saw padx and pady above.
# With grids there is a "sticky" parameter which takes a map coordinate like N, E, S, W, NE, etc. If the grid cell is larger
# than your widget because a larger widget is in the same row or column, sticky helps you put the widget where you want it in
# the cell.


# TKINTER PART FOUR ASSINGMENT

# You may have tried clicking the buttons. If so, you noticed that they highlight and depress fine, but they just don't do
# anything. Let's fix that. As we've seen, widgets are objects and have methods. We've been using their pack and grid methods.
# Now we'll use a new method, “configure.” Any keyword argument that we can pass when creating a widget may also be passed to
# its “configure” method.
b1.configure(text="Uno")

# Buttons are tied to callback functions using the parameter “command,” either when the button is created or with configure.
# Let's start by defining a function that simply prints a message.
def but1():
    print("Button one was pushed")

b1.configure(command=but1)
# Now when we click the button "Uno" the  message is printed.


# TKINTER PART FIVE ASSIGNMENT

# To input text from the user, we use an entry widget. Just as in the case of buttons, we need some way to communicate with
# the entry widget. In this case, it will be to set and retrieve text. This is done with a special Tkinter object called a
# StringVar that simply holds a string of text and allows us to set its contents and read it (with get). Let's start with
# a clean window.
win = Tk()
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()
# Now let's type "This is a test" into the entry and then retrieve it from our linked StringVar object
v.get()

# We can also set text into our StringVar object and have it appear in the entry widget.
v.set("this is set by the program")


# TKINTER PART SIX ASSIGNMENT

# Our last widget in the project will let us have a menu of items to choose from. A listbox is created with the following
# command (after opening a window). The "height" parameter limits how many lines will show.
win = Tk()
lb = Listbox(win, height=3)
lb.pack()
lb.insert(END, "first entry")
lb.insert(END, "second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")

# The fourth entry doesn't show since the listbox is set to just three lines.
# Items in the listbox may be also inserted not only at the end (END) but also at the beginning or even the middle.
# They may also be deleted. In fact we'll use the command “lb.delete(0,END)” later to clear the listbox.
# A listbox may be used in conjunction with a scroll bar. Let's start by making a scroll bar and packing it next to the list box.
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)

# This looks good, but if you operate the scroll bar, you'll see that it doesn't do anything yet.
# The scroll bar and the list box need to know about each other.
# This is done in a manner similar to how we tied buttons to call back functions.
# Two calls are needed, one to tell each about the other.
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

# If you have selected an item in the listbox, the method "curselection" will return the selected item for you.
# Actually, it returns a tuple of items selected. It is possible to configure the listbox to allow multiple items
# to be selected together. An empty tuple is returned if no item is selected. Otherwise, the tuple contains the index(es)
# of the selected items. (but as strings!)

# For example, click on the 3rd item and do the following (as a reminder, indexes start at zero).
lb.curselection()
