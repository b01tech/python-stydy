from tkinter import *
import math


COLOR_BG = "#f75e61"
COLOR_TEXT = "#fcfc62"
FONT_BTN = ("Courier", 14, "bold")
FONT_TIMER = ("Courier", 28, "bold")
cycle = 0
timer_count = None


def reset_timer():
    window.after_cancel(timer_count)
    canvas.itemconfig(timer, text="00:00")
    title.config(text="TIMER")
    check.config(text="")
    global cycle
    cycle = 0


def start_timer():
    POMODORO_TIME = 1 * 30
    SHORT_BREAK = 1 * 20
    LONG_BREAK = 2 * 60
    global cycle
    cycle += 1

    if cycle == 8:
        count_down(LONG_BREAK)
        title.config(text="LONG BREAK")
        reset_timer()
    elif cycle % 2 == 0:
        count_down(SHORT_BREAK)
        title.config(text="SHORT BREAK")
    else:
        count_down(POMODORO_TIME)
        title.config(text="WORK")


def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer_count
        timer_count = window.after(500, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(cycle/2)):
            marks += "✔"
        check.config(text=marks)


window = Tk()
window.config(padx=50, pady=50, bg=COLOR_BG)
window.title("Pomodoro Timer")
window.resizable(False, False)

title = Label(text="TIMER",
              font=FONT_TIMER, bg=COLOR_BG, fg=COLOR_TEXT)
title.grid(column=1, row=0)

canvas = Canvas(width=300, height=300, bg=COLOR_BG, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(150, 162, image=tomato_img)
timer = canvas.create_text(150, 180, text="00:00",
                           font=FONT_TIMER, fill="#fff")
canvas.grid(column=1, row=1)

start_btn = Button(font=FONT_BTN, text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

pause_btn = Button(font=FONT_BTN, text="Pause")
pause_btn.grid(column=0, row=3)

reset_btn = Button(font=FONT_BTN, text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)

check = Label(text="", font=FONT_TIMER, fg=COLOR_TEXT, bg=COLOR_BG)
check.grid(column=1, row=2)


window.mainloop()
