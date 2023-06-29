from tkinter import *


class App:
    def __init__(self):
        self.app = Tk()
        self.screen()
        self.top_frame()
        self.bt_frame()
        self.create_top_widget()
        self.app.mainloop()

    def screen(self):
        self.app.title("Customer records")
        self.app.geometry("700x500")
        self.app.resizable(False, False)
        self.app.config(background="#15036e")

    def top_frame(self):
        self.top_frame = Frame(self.app, background="#b6b4bf")
        self.top_frame.place(x=15, y=10, relwidth=0.95, relheight=0.45)

    def bt_frame(self):
        self.bt_frame = Frame(self.app, background="#b6b4bf")
        self.bt_frame.place(x=15, rely=0.5, relwidth=0.95, relheight=0.45)

    def create_top_widget(self):
        self.create_btn()
        self.create_input()

    def create_btn(self):
        # reset
        self.btn_reset = Button(self.top_frame, text="Reset")
        self.btn_reset.place(relx=0.2, rely=0.15, width=50, height=30)
        # search
        self.btn_search = Button(self.top_frame, text="Search")
        self.btn_search.place(relx=0.3, rely=0.15, width=50, height=30)
        # New
        self.btn_new = Button(self.top_frame, text="New")
        self.btn_new.place(relx=0.6, rely=0.15, width=50, height=30)
        # Edit
        self.btn_edit = Button(self.top_frame, text="Edit")
        self.btn_edit.place(relx=0.7, rely=0.15, width=50, height=30)
        # Delete
        self.btn_delete = Button(self.top_frame, text="Delete")
        self.btn_delete.place(relx=0.8, rely=0.15, width=50, height=30)

    def create_input(self):
        # Id
        self.lb_id = Label(self.top_frame, text="ID.")
        self.lb_id.place(relx=0.05, rely=0.02)
        self.input_id = Entry(self.top_frame)
        self.input_id.place(relx=0.05, rely=0.17, relwidth=0.1)

        # Name
        self.lb_name = Label(self.top_frame, text="Name")
        self.lb_name.place(relx=0.05, rely=0.3)
        self.input_name = Entry(self.top_frame)
        self.input_name.place(relx=0.05, rely=0.45, relwidth=0.8)
        # Phone
        self.lb_phone = Label(self.top_frame, text="Phone")
        self.lb_phone.place(relx=0.05, rely=0.6)
        self.input_phone = Entry(self.top_frame)
        self.input_phone.place(relx=0.05, rely=0.75, relwidth=0.4)
        # City
        self.lb_city = Label(self.top_frame, text="City")
        self.lb_city.place(relx=0.5, rely=0.6)
        self.input_city = Entry(self.top_frame)
        self.input_city.place(relx=0.5, rely=0.75, relwidth=0.4)
