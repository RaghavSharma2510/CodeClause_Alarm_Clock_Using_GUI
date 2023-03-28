import tkinter as tk
from datetime import datetime
from tkinter import messagebox
def set_alarm():
    time_str = entry.get()
    alarm_time = datetime.strptime(time_str, "%H:%M")
    now = datetime.now()
    delta = alarm_time - now
    seconds = delta.seconds
    user.after(seconds * 1000, alarm)
    message = "Alarm set for " + time_str
    label.config(text=message)
def alarm():
    messagebox.showinfo("Time up!")
user = tk.Tk()
user.title("Alarm Clock")
label = tk.Label(user, text="Enter time (HH:MM): ")
label.pack()
entry = tk.Entry(user)
entry.pack()
button = tk.Button(user, text="Set Alarm", command=set_alarm)
button.pack()
user.geometry("250x200")
user.mainloop()


