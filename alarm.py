from threading import Thread
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
from time import sleep
from pygame import mixer


# color
bg_color = "#d6ebd1"
col1 = "#235914"  
col2 = "#eff5ed"


# window
window = Tk()
window.title("")
window.geometry("400x200")
window.configure(bg=bg_color)

# frames
frame_line = Frame(window, width=400, height=5, bg=col1)
frame_line.grid(row=0, column=0)

frame_body = Frame(window, width=400, height=200, bg=col2)
frame_body.grid(row=1, column=0)


# configuring frame body
img = Image.open("C:\\pythonproject\\Alarm_Clock\\clock.png")
img.resize((100, 100))
img = ImageTk.PhotoImage(img)

app_image = Label(frame_body, height=170, width=130, image=img, bg=bg_color)
app_image.place(x=10, y=10)

name = Label(frame_body, text="ALARM", height=1, font=('Ivy 16 bold'), bg=bg_color)
name.place(x=170, y=10)

# hour
hour = Label(frame_body, text="Hour", height=1, font=('Ivy 12 bold'), bg=bg_color, fg=col1)
hour.place(x=170, y=50)
c_hour = Combobox(frame_body, width=2, font=("arial 12"))
c_hour['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
# c_hour['value'] = list(range(00, 25))
c_hour.current(0)
c_hour.place(x=170, y=80)

# minute
min = Label(frame_body, text="Minute", height=1, font=('Ivy 12 bold'), bg=bg_color, fg=col1)
min.place(x=230, y=50)
c_min = Combobox(frame_body, width=2, font=("arial 12"))
c_min['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
 "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
 "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47",
 "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
c_min.current(0)

# c_min['value'] = list(range(00, 60))
# c_min.current(0)
c_min.place(x=230, y=80)

# second
sec = Label(frame_body, text="Second", height=1, font=('Ivy 12 bold'), bg=bg_color, fg=col1)
sec.place(x=305, y=50)
c_sec = Combobox(frame_body, width=2, font=("arial 12"))
c_sec['value'] = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
 "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
 "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47",
 "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59")
# c_sec['value'] = list(range(00, 60))
c_sec.current(0)
c_sec.place(x=305, y=80)

# period
ampm = Label(frame_body, text="Period", height=1, font=('Ivy 12 bold'), bg=bg_color, fg=col1)
ampm.place(x=170, y=120)
c_ampm = Combobox(frame_body, width=2, font=("arial 12"))
c_ampm['value'] = ("AM", "PM")
c_ampm.current(0)
c_ampm.place(x=170, y=150)


selected = IntVar()


def activate_alarm():
    t = Thread(target = alarm)
    t.start()
 
def deactivate_alarm():
    print("Deactivate Alarm: ", selected.get())
    mixer.music.stop ()
      
# radiobutton activate
rad1 = Radiobutton(frame_body, font=('arial 10 bold'), value = 1, text="Activate", bg=bg_color, command=activate_alarm, variable=selected)
rad1.place(x=270, y=120)
# rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value = 2, text="Deactivate", bg=bg_color, command=deactivate_alarm, variable=selected)
# rad2.place(x=270, y=150)

def sound_alarm():
    mixer.music.load("C:\\pythonproject\\Alarm_Clock\\tone.mp3")
    mixer.music.play()
    selected.set(0)
    
    # radiobutton deactivate
    rad2 = Radiobutton(frame_body, font=('arial 10 bold'), value = 2, text="Deactivate", bg=bg_color, command=deactivate_alarm, variable=selected)
    rad2.place(x=270, y=150)
    

def alarm():
    while True:
        control = 1
        print(control)
        
        alarm_hour = c_hour.get()
        alarm_min = c_min.get()
        alarm_sec = c_sec.get()
        alarm_period = c_ampm.get()
        alarm_period = str(alarm_period).upper()
         
        now = datetime.now()
        print(now)
        
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")
        period = now.strftime("%p")
        
        if control==1: 
            if alarm_period==period:
                if alarm_hour == hour:
                    if alarm_min == minute:
                        if alarm_sec == second:
                            print("Time to take break!!")
                            sound_alarm()
        sleep(1)                
                        
mixer.init()

# sound_alarm()
window.mainloop()
