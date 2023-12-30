import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

from TPSI01.authore import authorApp
from TPSI01.mamber import memberApp
from books import bookApp
from member import *
from pub import pubApp
from authors import *
from login import LoginApp
from register import registerApp


class mainApp():
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("800x500")

        self.title()
        self.load_background_image()
        self.create_class_form()

    def title(self):
        style = ttk.Style()
        style.configure("Custom.TFrame", background="#407BFF")
        frame = ttk.Frame(self.master, padding="20", style="Custom.TFrame", width=800, height=80)
        frame.place(x=0, y=10)

        image = Image.open("myicon.jpg")
        image = image.resize((30, 30), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.master, image=photo)
        self.background_label.image = photo
        button_with_image = ttk.Button(frame, text="Login", image=photo, compound=tk.BOTTOM,
                                       command=self.open_login_window)
        button_with_image.place(x=10, y=2)

        image1 = Image.open("new_user.jpg")
        image1 = image1.resize((30, 30), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(image1)
        self.background_label1 = tk.Label(self.master, image=photo1)
        self.background_label1.image = photo1
        button_with_image1 = ttk.Button(frame, text="New User", image=photo1, compound=tk.BOTTOM,
                                        command=self.open_user_window)
        padding_x = 10
        button_with_image1.place(x=80 + padding_x, y=2)

        style = ttk.Style()
        style.configure("Custom.TLabel", font=("Helvetica", 20), foreground="black", background="#407BFF")
        label_username = ttk.Label(frame, text="Library Management System", style="Custom.TLabel")
        label_username.place(x=300, y=3)

    def load_background_image(self):
        image = Image.open("main.png")
        image = image.resize((400, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.master, image=photo)
        self.background_label.image = photo
        pad_y = 10
        self.background_label.place(x=0, y=80 + pad_y)

    def create_class_form(self):
        style = ttk.Style()
        style.configure("f.TButton", background="#407BFF")
        f1 = ttk.Frame(self.master, width=400, style='f.TButton', height=400)
        f1.place(x=400, y=100)
        style = ttk.Style()
        style.configure("menu.TButton", background="#0C62D4", padding=(0, 27), font=20, foreground="black")
        menu1 = ttk.Button(f1, text="Books management", style="menu.TButton", compound=tk.CENTER, width=36,
                           command=self.open_book_window)
        menu1.place(x=0, y=0)
        menu2 = ttk.Button(f1, text="Loan management", style="menu.TButton", width=36, compound=tk.CENTER,
                           command=self.open_author_window)
        menu2.place(x=0, y=100)
        menu3 = ttk.Button(f1, text="Publishing  information", style="menu.TButton", width=36, compound=tk.CENTER,
                           command=self.open_pub_window)
        menu3.place(x=0, y=200)
        menu4 = ttk.Button(f1, text="Member's information", style="menu.TButton", width=36, compound=tk.CENTER,
                           command=self.open_member_window)
        menu4.place(x=0, y=300)

    def open_book_window(self):
        # Create an instance of the SecondWindow class
        book_window = tk.Toplevel(self.master)
        book_app = bookApp(book_window)

    def open_author_window(self):
        # Create an instance of the SecondWindow class
        author_window = tk.Toplevel(self.master)
        author_app = authorApp(author_window)

    def open_pub_window(self):
        # Create an instance of the SecondWindow class
        pub_window = tk.Toplevel(self.master)
        pub_app = pubApp(pub_window)

    def open_member_window(self):
        # Create an instance of the SecondWindow class
        member_window = tk.Toplevel(self.master)
        member_app = memberApp(member_window)

    def open_login_window(self):
        # Create an instance of the SecondWindow class
        login_window = tk.Toplevel(self.master)
        login_app = LoginApp(login_window)

    def open_user_window(self):
        # Create an instance of the SecondWindow class
        user_window = tk.Toplevel(self.master)
        user_app = registerApp(user_window)


if __name__ == "__main__":
    root = tk.Tk()
    ico = Image.open('myicon.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    app = mainApp(root)
    root.mainloop()