from tkinter import *
from tkinter import ttk

COLOR_BG = "#e1edfa"
CONFIG_FRAME = {"color": "#8cabba"}
CONFIG_BTN = {"border": 3, "color": "#fff", "bg": "#91afcf"}
FONT = ("Courie", 16, "bold")
BTN = (7, 8, 9, "/", 4, 5, 6, "*", 1, 2, 3, "-", 0, "+")


class App:
    def __init__(self) -> None:
        self.app = Tk()
        self.screen()
        self.res_frame()
        self.create_btn()
        self.app.mainloop()

    def screen(self):
        self.app.title("Calculator - Python")
        self.app.geometry("400x450")
        self.app.resizable(False, False)
        self.app.config(bg=COLOR_BG)

    def res_frame(self):
        self.res_frame = Frame(self.app, bg=CONFIG_FRAME["color"])
        self.res_frame.place(x=10, y=40, relwidth=0.95, relheight=0.1)

    def create_btn(self):
        pos_x = 10
        pos_y = 100
        for i in BTN:
            self.btn_frame = Button(
                self.app,
                text=i,
                font=FONT,
                bg=CONFIG_BTN["bg"],
                border=CONFIG_BTN["border"],
                foreground=CONFIG_BTN["color"],
            )
            if pos_x < 300 and pos_y < 300:
                self.btn_frame.place(x=pos_x, y=pos_y, width=75, height=50)
                pos_x += 101
            elif pos_y < 300:
                self.btn_frame.place(x=pos_x, y=pos_y, width=75, height=50)
                pos_y += 75
                pos_x = 10
            else:
                self.btn_frame.place(x=pos_x, y=pos_y, width=75, height=50)
                pos_x = 313
        self.btn_frame = Button(
            self.app,
            text="=",
            font=FONT,
            bg=CONFIG_BTN["bg"],
            border=CONFIG_BTN["border"],
            foreground=CONFIG_BTN["color"],
        )
        self.btn_frame.place(x=212, y=395, width=178, height=50)


App()
