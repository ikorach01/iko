import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from login import LoginApp
from register import *

class pubApp():
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("800x500")

        self.title()
        self.load_background_image()
        self.create_class_form()
        self.display_books()

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
        button_with_image1 = ttk.Button(frame, text="New User", image=photo1, compound=tk.BOTTOM)
        padding_x = 10
        button_with_image1.place(x=80 + padding_x, y=2)

        style = ttk.Style()
        style.configure("Custom.TLabel", font=("Helvetica", 20), foreground="black", background="#407BFF")
        label_username = ttk.Label(frame, text="Publishing  information", style="Custom.TLabel")
        label_username.place(x=300, y=3)

    def create_class_form(self):
        form = ttk.Frame(self.master, padding="20", width=300, height=400)
        form.place(x=0, y=100)

        author_label = ttk.Label(form, text="The name of publishing house:")
        author_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.author_entry = ttk.Entry(form, width=50)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
        # Create labels and entry fields
        email_label = ttk.Label(form, text="Email:")
        email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.email_entry = ttk.Entry(form, width=50)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        phone_label = ttk.Label(form, text="The phone number:")
        phone_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.phone_entry = ttk.Entry(form, width=50)
        self.phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        adress_label = ttk.Label(form, text="Adress:")
        adress_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.adress_entry = ttk.Entry(form, width=50)
        self.adress_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        add_button = ttk.Button(form, text="Create")
        add_button.grid(row=5, column=1, padx=130, pady=15, sticky="w")

    def display_books(self):
        f2 = ttk.Frame(self.master, width=450, height=200)
        f2.place(x=230, y=350)
        # Create a Listbox to show the books
        books_treeview = ttk.Treeview(f2, columns=("The name of publishing", "Email", "Phone number", "Adress"),
                                      show="headings")
        books_treeview.heading("The name of publishing", text="The name of publishing")
        books_treeview.heading("Email", text="Email")
        books_treeview.heading("Phone number", text="Phone number")
        books_treeview.heading("Adress", text="Adress")
        books_treeview.place(x=0, y=0)

        books_treeview.column("The name of publishing", width=80)
        books_treeview.column("Email", width=80)
        books_treeview.column("Phone number", width=80)
        books_treeview.column("Adress", width=80)

        # Replace this with your actual book data retrieval logic
        # For demonstration purposes, adding some sample books
        books_data = [
            ("Author 1", "email 1 ", "3344555656", " Adress 1"),
            ("Author 2", "email 2", "1765545345", " Adress 2"),
            ("Author 3", "email 3", "24534565675", "Adress 3"),
            # Add more books as needed
        ]

        for book in books_data:
            books_treeview.insert("", tk.END, values=book)

    def load_background_image(self):
        image = Image.open("writing.png")
        image = image.resize((200, 200), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.master, image=photo)
        self.background_label.image = photo
        pad_y = 10
        self.background_label.place(x=530, y=80 + pad_y)

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
    app = pubApp(root)
    root.mainloop()