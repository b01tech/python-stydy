from tkinter import *
from tkinter import ttk
import sqlite3

CONFIG_BTN = {"border": 3, "bg": '#0342a6', "color": '#fff'}
CONFIG_LABEL = {"bg": '#b6b4bf', "color": '#0342a6'}
CONFIG_FRAME = {"color": "#b6b4bf"}
FONT = ("Courie", 12, "bold")


class Functions():
    def reset(self):
        self.input_id.delete(0, END)
        self.input_name.delete(0, END)
        self.input_phone.delete(0, END)
        self.input_city.delete(0, END)

    def connect_db(self):
        self.conn = sqlite3.connect("customers.db")
        self.cursor = self.conn.cursor()
        print("DataBase connected.")

    def disconnect_db(self):
        self.conn.close()
        print("DataBase disconnected.")

    def create_tb(self):
        self.connect_db()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers(
                id INTEGER PRIMARY KEY,
                name CHAR(40) NOT NULL,
                phone INTEGER(20),
                city CHAR(40)
            );
        """)
        self.conn.commit()
        self.disconnect_db()

    def get_values(self):
        self.id = self.input_id.get()
        self.name = self.input_name.get()
        self.phone = self.input_phone.get()
        self.city = self.input_city.get()

    def refresh_tb(self):
        self.tb_view.delete(*self.tb_view.get_children())
        self.connect_db()
        cust_list = self.cursor.execute("""
            SELECT id, name, phone, city FROM customers
            ORDER BY id ASC;
        """)
        for i in cust_list:
            self.tb_view.insert("", END, values=i)
        self.disconnect_db()

    def select(self, event):
        self.reset()
        self.tb_view.selection()
        for n in self.tb_view.selection():
            id, name, phone, city = self.tb_view.item(n, "values")
            self.input_id.insert(END, id)
            self.input_name.insert(END, name)
            self.input_phone.insert(END, phone)
            self.input_city.insert(END, city)

    def add_customer(self):
        self.get_values()
        self.connect_db()
        self.cursor.execute("""
            INSERT INTO customers (name, phone, city) VALUES (?, ?, ?)
        """, (self.name, self.phone, self.city))
        self.conn.commit()
        self.disconnect_db()
        self.refresh_tb()
        self.reset()

    def del_customer(self):
        self.get_values()
        self.connect_db()
        self.cursor.execute(""" 
            DELETE FROM customers WHERE id = ?
        """, self.id)
        self.conn.commit()
        self.disconnect_db()
        self.reset()
        self.refresh_tb()

    def update_customer(self):
        self.get_values()
        self.connect_db()
        self.cursor.execute("""
            UPDATE customers SET name = ?, phone = ?, city = ? WHERE id = ?
        """, (self.name, self.phone, self.city, self.id))
        self.conn.commit()
        self.disconnect_db()
        self.refresh_tb()
        self.reset()


class App(Functions):
    def __init__(self):
        self.app = Tk()
        self.screen()
        self.top_frame()
        self.bt_frame()
        self.create_top_widget()
        self.create_bt_widget()
        self.create_tb()
        self.refresh_tb()
        self.app.mainloop()

    def screen(self):
        self.app.title("Customer records")
        self.app.geometry("700x500")
        self.app.resizable(False, False)
        self.app.config(background="#15036e")

    def top_frame(self):
        self.top_frame = Frame(self.app, background=CONFIG_FRAME["color"])
        self.top_frame.place(x=15, y=10, relwidth=0.95, relheight=0.45)

    def bt_frame(self):
        self.bt_frame = Frame(self.app, background=CONFIG_FRAME["color"])
        self.bt_frame.place(x=15, rely=0.5, relwidth=0.95, relheight=0.45)

    def create_top_widget(self):
        self.create_btn()
        self.create_input()

    def create_btn(self):
        # reset
        self.btn_reset = Button(
            self.top_frame, text="Reset", border=CONFIG_BTN["border"], background=CONFIG_BTN["bg"], foreground=CONFIG_BTN["color"], command=self.reset)
        self.btn_reset.place(relx=0.2, rely=0.15, width=60, height=30)
        # search
        self.btn_search = Button(self.top_frame, text="Search",
                                 border=CONFIG_BTN["border"], background=CONFIG_BTN["bg"], foreground=CONFIG_BTN["color"])
        self.btn_search.place(relx=0.3, rely=0.15, width=60, height=30)
        # New
        self.btn_new = Button(self.top_frame, text="New",
                              border=CONFIG_BTN["border"], background=CONFIG_BTN["bg"], foreground=CONFIG_BTN["color"], command=self.add_customer)
        self.btn_new.place(relx=0.6, rely=0.15, width=60, height=30)
        # Edit
        self.btn_edit = Button(self.top_frame, text="Edit",
                               border=CONFIG_BTN["border"], background=CONFIG_BTN["bg"], foreground=CONFIG_BTN["color"], command=self.update_customer)
        self.btn_edit.place(relx=0.7, rely=0.15, width=60, height=30)
        # Delete
        self.btn_delete = Button(self.top_frame, text="Delete",
                                 border=CONFIG_BTN["border"], background=CONFIG_BTN["bg"], foreground=CONFIG_BTN["color"], command=self.del_customer)
        self.btn_delete.place(relx=0.8, rely=0.15, width=60, height=30)

    def create_input(self):
        # Id
        self.lb_id = Label(self.top_frame, text="ID.",
                           background=CONFIG_LABEL["bg"], foreground=CONFIG_LABEL["color"], font=FONT)
        self.lb_id.place(relx=0.05, rely=0.03)
        self.input_id = Entry(self.top_frame)
        self.input_id.place(relx=0.05, rely=0.17, relwidth=0.1)

        # Name
        self.lb_name = Label(self.top_frame, text="Name",
                             background=CONFIG_LABEL["bg"], foreground=CONFIG_LABEL["color"], font=FONT)
        self.lb_name.place(relx=0.05, rely=0.3)
        self.input_name = Entry(self.top_frame)
        self.input_name.place(relx=0.05, rely=0.45, relwidth=0.8)
        # Phone
        self.lb_phone = Label(self.top_frame, text="Phone",
                              background=CONFIG_LABEL["bg"], foreground=CONFIG_LABEL["color"], font=FONT)
        self.lb_phone.place(relx=0.05, rely=0.6)
        self.input_phone = Entry(self.top_frame)
        self.input_phone.place(relx=0.05, rely=0.75, relwidth=0.4)
        # City
        self.lb_city = Label(self.top_frame, text="City",
                             background=CONFIG_LABEL["bg"], foreground=CONFIG_LABEL["color"], font=FONT)
        self.lb_city.place(relx=0.5, rely=0.6)
        self.input_city = Entry(self.top_frame)
        self.input_city.place(relx=0.5, rely=0.75, relwidth=0.4)

    def create_bt_widget(self):
        self.tb_view = ttk.Treeview(
            self.bt_frame, height=3, show="headings", columns=("id", "name", "phone", "city"))

        self.tb_view.heading("id", text="Id")
        self.tb_view.heading("name", text="Name")
        self.tb_view.heading("phone", text="Phone")
        self.tb_view.heading("city", text="City")

        self.tb_view.column("id", width=50)
        self.tb_view.column("name", width=200)
        self.tb_view.column("phone", width=150)
        self.tb_view.column("city", width=150)
        self.tb_view.place(relx=0.05, rely=0.02, relwidth=0.9, relheight=0.9)

        self.scroll = ttk.Scrollbar(
            self.bt_frame, orient="vertical", command=self.tb_view.yview)
        self.tb_view.configure(yscrollcommand=self.scroll.set)
        self.scroll.place(relx=0.95, rely=0.02, width=20, relheight=0.9)

        self.tb_view.bind("<Double-1>", self.select)
