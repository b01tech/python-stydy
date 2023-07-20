from tkinter import *

COLOR_BG = "#f75e61"
COLOR_TEXT = "#fcfc62"
FONT_BTN = ("Courier", 14, "bold")
FONT_TIMER = ("Courier", 28, "bold")

count = 0


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
canvas.create_text(150, 180, text="00:00", font=FONT_TIMER, fill="#fff")
canvas.grid(column=1, row=1)

# timer = Label(width=10, height=10, text="00:00",
#               font=FONT, bg=COLOR_BG, fg=COLOR_TEXT)
# timer.grid(column=1, row=1)

start_btn = Button(font=FONT_BTN, text="Start")
start_btn.grid(column=0, row=2)

pause_btn = Button(font=FONT_BTN, text="Pause")
pause_btn.grid(column=0, row=3)

reset_btn = Button(font=FONT_BTN, text="Reset")
reset_btn.grid(column=2, row=2)

window.mainloop()
