from tabnanny import check
from tkinter import *
from turtle import bgcolor, fd
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)    # add padding to the image

# label
label = Label(text="Timer")
label.config(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 42, "italic"))
label.grid(column=1, row=0)

# create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) 
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Start button 
button1 = Button(text="Start")
button1.grid(column=0, row=2)

# Reset button 
button2 = Button(text="Reset")
button2.grid(column=2, row=2)

# check mark
check_mark = Label(text="✔✅")
check_mark.config(fg=PINK, bg=YELLOW)
check_mark.grid(column=1, row=3)

window.mainloop()