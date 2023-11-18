from tkinter import Label, Tk
import time

app_window = Tk()
app_window.title("Time, Dr. Freeman?")
app_window.geometry("640x400")

text_font= ("Arial", 70, 'bold')
background = "#fb7e14"
border_width = 145

label = Label(app_window, font=text_font, bg=background, bd=border_width)
label.grid(row=0, column=1)

def digital_clock():
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live)
   label.after(100, digital_clock)

digital_clock()
app_window.mainloop()
