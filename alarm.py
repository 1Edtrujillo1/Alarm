# 0.0 Import Modules  ----

from tkinter import *
import datetime
import time
import winsound


def alarm():

    while True:

        time.sleep(1)

        current_info = datetime.datetime.now()
        time_now = current_info.strftime("%H:%M:%S")

        print("Today day is: ",
              current_info.strftime("%d/%m/%Y"),
              "\n",
              time_now)

        if time_now == f"{hour.get()}:{min.get()}:{sec.get()}":
            print("Wake up little bastard!!!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

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

# 2.0 Required alarm variables ----

hour, min, sec = [StringVar(), StringVar(), StringVar()]

# 3.0 Make the Input Boxes ----

list(map(
    lambda t, x: Entry(master=clock, textvariable=t,
                       bg='pink', width=15).place(x=x, y=30),
    [hour, min, sec],
    [110, 150, 200]
))

# 4.0 Button to execute a command ----

Button(master=clock,
       text='Set Alarm',
       command=alarm,
       fg='red',
       width=10
       ).place(x=110, y=70)

# 5.0 Execution

clock.mainloop()

# Sources ----

# https://data-flair.training/blogs/alarm-clock-python/
