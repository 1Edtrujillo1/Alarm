# 0.0 Import Modules ----

from tkinter import *
import datetime
import time
import winsound

# 1.0 Dialog Box Generator ----

clock = Tk()
clock.geometry('400x200')
clock.title('Alarm Clock')

list(map(
    lambda text, font, bg, fg, relief, x, y:
    Label(master=clock, text=text, font=font,
          bg=bg, fg=fg, relief=relief).place(x=x, y=y),
    ['Enter time in 24 hrs format.', 'Hour Min Sec', 'When to wake you up?'],
    ['Arial', 60, ("Helevetica", 7, "bold")],
    ['black', None, None],
    ['red', None, 'blue'],
    [None, None, 'solid'],
    [60, 110, 0],
    [120, None, 29]
))

# 2.0 Make the Input Boxes ----

list(map(
    lambda x: Entry(master=clock, textvariable=StringVar(),
                    bg='pink', width=15).place(x=x, y=30),
    [110, 150, 200]
))

# 3.0 Button to execute a command ----

Button(master=clock,
       text='Set Alarm',
       #command = actual_time,
       fg='red',
       width=10
       ).place(x=110, y=70)

# 4.0 Execution

clock.mainloop()

# Sources ----

# https://data-flair.training/blogs/alarm-clock-python/
