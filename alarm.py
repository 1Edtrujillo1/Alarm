# 0.0 Import Modules ----

from tkinter import *
import datetime
import time
import winsound

# 1.0 Dialog Box Generator ----

clock = Tk()
clock.geometry('400x200')
clock.title('Alarm Clock')

Label(master=clock, text='Enter time in 24 hrs format.',
      font='Arial', bg='black', fg='red').place(x=60, y=120)
Label(master=clock, text='Hour Min Sec',
      font=60).place(x=110)
Label(master=clock, text='When to wake you up?',
      font=("Helevetica", 7, "bold"), fg='blue',
      relief='solid').place(x=0, y=29)

# 2.0 Make the Input Boxes ----

Entry(master=clock, textvariable=StringVar(),
      bg='pink', width=15).place(x=110, y=30)
Entry(master=clock, textvariable=StringVar(),
      bg='pink', width=15).place(x=150, y=30)
Entry(master=clock, textvariable=StringVar(),
      bg='pink', width=15).place(x=200, y=30)

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
