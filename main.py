from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps # global variable not local
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # LONG BREAK
    # if its the 8th rep -> count down 15-30 mins -> long break
    if reps == 8:
        count_down(long_break_sec)
        label.config(text="Long Break", fg=RED)
        reps = 0    # reset reps

    # BREAK
    # if its the 2nd/4th/6th rep -> count down 5min -> BREAK
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
        
    # WORK
    # if its the 1st/3rd/5th/7th rep -> count down 25 min 
    else:   
        # if not even & not == 8
        count_down(work_sec)
        label.config(text="Work!", fg=GREEN)
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    # we need count to be displayed using time format
    count_min = math.floor(count / 60)  # returns largest whole number smaller than count
    count_sec = count % 60              # gives back remainder, eg. 100 % 60 = 1 rem. 40

    # dynamic typing - changing the data type of count
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:   
        # when count goes to 0 -> restart timer using different reps
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)  # divide reps by 2 then take highest whole number lower than it
        for _ in range(work_sessions):
            marks += "✅"   # when it gets to 2 -> marks = "✅✅"
        check_mark.config(text=marks)

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
check_mark = Label(bg=YELLOW, fg=GREEN, highlightthickness=0)
check_mark.grid(column=1, row=3)

window.mainloop()