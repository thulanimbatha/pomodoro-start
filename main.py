from tkinter import *
import math
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

def start_timer():
    count_down(10 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    # we need count to be displayed using time format
    count_min = math.floor(count / 60)  # returns largest whole number smaller than count
    count_sec = count % 60              # gives back remainder, eg. 100 % 60 = 1 rem. 40

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
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

# Start button -> call countdown method
button1 = Button(text="Start", highlightthickness=0, command=start_timer)
button1.grid(column=0, row=2)

# Reset button 
button2 = Button(text="Reset", highlightthickness=0)
button2.grid(column=2, row=2)

# check mark
check_mark = Label(text="✅",bg=YELLOW, fg=GREEN, highlightthickness=0)
check_mark.grid(column=1, row=3)

window.mainloop()