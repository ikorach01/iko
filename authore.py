import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from login import *
from register import *


class authorApp():
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("900x600")

        self.title()
        # self.load_background_image()
        self.create_class_form()
        self.display_books()

    def title(self):
        style = ttk.Style()
        style.configure("Custom.TFrame", background="#407BFF")
        frame = ttk.Frame(self.master, padding="20", style="Custom.TFrame", width=900, height=80)
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
        button_with_image1 = ttk.Button(frame, text="New User", image=photo1, compound=tk.BOTTOM)
        padding_x = 10
        button_with_image1.place(x=80 + padding_x, y=2)

        style = ttk.Style()
        style.configure("Custom.TLabel", font=("Helvetica", 20), foreground="black", background="#407BFF")
        label_username = ttk.Label(frame, text="Loan management", style="Custom.TLabel")
        label_username.place(x=300, y=3)

    def create_class_form(self):
        form = ttk.Frame(self.master, padding="20", width=300, height=400)
        form.place(x=0, y=100)

        Membern_label = ttk.Label(form, text="Member name:")
        Membern_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.Membern_entry = ttk.Entry(form, width=50)
        self.Membern_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        # Create labels and entry fields
        Bookn_label = ttk.Label(form, text="Book name:")
        Bookn_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.Bookn_entry = ttk.Entry(form, width=50)
        self.Bookn_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        Loand_label = ttk.Label(form, text="Loan date:")
        Loand_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.Loand_entry = ttk.Entry(form, width=50)
        self.Loand_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        returnd_label = ttk.Label(form, text="return date:")
        returnd_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.returnd_entry = ttk.Entry(form, width=50)
        self.returnd_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        add_button = ttk.Button(form, text="Create")
        add_button.grid(row=5, column=1, padx=120, pady=15, sticky="w")

    def display_books(self):
        f2 = ttk.Frame(self.master, width=900, height=250)
        f2.place(x=50, y=350)
        # Create a Listbox to show the books
        books_treeview = ttk.Treeview(f2, columns=("member name", "Book name", "Loan date", "return date"),
                                      show="headings")
        books_treeview.heading("member name", text="member name")
        books_treeview.heading("Book name", text="Book name")
        books_treeview.heading("Loan date", text="Loan date")
        books_treeview.heading("return date", text="return date")
        books_treeview.place(x=0, y=0)

        books_treeview.column("member name", width=200)
        books_treeview.column("Book name", width=200)
        books_treeview.column("Loan date", width=200)
        books_treeview.column("return date", width=200)

        # Replace this with your actual book data retrieval logic
        # For demonstration purposes, adding some sample books
        books_data = [
            ("member name 1", "nadaraiat al fostok ", "2022/11/20", " 2022/11/5"),
            ("member name 2", "book 2", "2022/11/20", " 2022/11/5"),
            ("member name 3", "book 3", "2022/11/20", "2022/11/5"),
            # Add more books as needed
        ]
        for book in books_data:
            books_treeview.insert("", tk.END, values=book)

    def open_login_window(self):
        # Create an instance of the SecondWindow class
        login_window = tk.Toplevel(self.master)
        loginApp = LoginApp(login_window)

    def open_user_window(self):
        # Create an instance of the SecondWindow class
        user_window = tk.Toplevel(self.master)
        user_app = registerApp(user_window)


if __name__ == "__main__":
    root = tk.Tk()
    ico = Image.open('myicon.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    app = authorApp(root)
    root.mainloop()