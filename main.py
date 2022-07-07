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
def count_down(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)    # add padding to the image

# label
label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "italic"))
label.grid(column=1, row=0)

# create canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img) 
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# call count down method
count_down(5)

# Start button 
button1 = Button(text="Start", highlightthickness=0)
button1.grid(column=0, row=2)

# Reset button 
button2 = Button(text="Reset", highlightthickness=0)
button2.grid(column=2, row=2)

# check mark
check_mark = Label(text="✅",bg=YELLOW, fg=GREEN, highlightthickness=0)
check_mark.grid(column=1, row=3)

window.mainloop()