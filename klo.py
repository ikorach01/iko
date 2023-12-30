import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from login import *
from register import *


class bookApp():
    def __init__(self, master):
        self.search_entry = None
        self.book_entry = None
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("900x650")

        self.title()
        self.load_background_image()
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
        label_username = ttk.Label(frame, text="Library Management System", style="Custom.TLabel")
        label_username.place(x=300, y=3)

    def load_background_image(self):
        image = Image.open("bbk.png")
        image = image.resize((400, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.master, image=photo)
        self.background_label.image = photo
        pad_y = 80
        self.background_label.place(x=0, y=210 + pad_y)

    def create_class_form(self):
        style = ttk.Style()
        style.configure("f.TButton", background="#407BFF")
        f1 = ttk.Frame(self.master, width=500, style='f.TButton', height=380)
        f1.place(x=10, y=100)

        book_label = ttk.Label(f1, text="The name of Book:")
        book_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.book_entry = ttk.Entry(f1)
        self.book_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
        # Create labels and entry fields
        author_label = ttk.Label(f1, text="Author:")
        author_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.author_entry = ttk.Entry(f1)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        price_label = ttk.Label(f1, text="Publishing House:")
        price_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.price_entry = ttk.Entry(f1)
        self.price_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        quantity_label = ttk.Label(f1, text="the main words:")
        quantity_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.quantity_entry = ttk.Entry(f1)
        self.quantity_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        # Create a Combobox for book status
        status_label = ttk.Label(f1, text="the topic:")
        status_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.status_combobox = ttk.Combobox(f1, values=["Novels", "sciences","Mathematics","physics","history",
                                                        "Religious"])
        self.status_combobox.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        self.status_combobox.set("Novels")  # Set default status

        add_button = ttk.Button(f1, text="Create")
        add_button.grid(row=5, column=1, padx=5, pady=15, sticky="w")

        delete_button = ttk.Button(f1, text="Delete", )
        delete_button.grid(row=5, column=2, padx=5, pady=15, sticky="w")

        # Create a search entry field and button
        search_label = ttk.Label(f1, text="Search:")
        search_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.search_entry = ttk.Entry(f1)
        self.search_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        search_button = ttk.Button(f1, text="Search", command=self.search_books)
        search_button.grid(row=6, column=2, padx=10, pady=5, sticky="w")

    def create_search_form(self):
        style = ttk.Style()
        style.configure("f.TButton", background="#407BFF")
        f2 = ttk.Frame(self.master, width=500, style='f.TButton', height=380)
        f2.place(x=10, y=500)

    def display_books(self):
        f2 = ttk.Frame(self.master, width=450, height=300)
        f2.place(x=400, y=110)
        # Create a Listbox to show the books
        books_treeview = ttk.Treeview(f2, columns=("Title", "Author", "Publishing House", "the main words", "the topic"),
                                      show="headings")
        books_treeview.heading("Title", text="Title")
        books_treeview.heading("Author", text="Author")
        books_treeview.heading("Publishing House", text="Publishing House")
        books_treeview.heading("the main words", text="the main words")
        books_treeview.heading("the topic", text="the topic")
        books_treeview.place(x=0, y=0)

        books_treeview.column("Title", width=90)
        books_treeview.column("Author", width=90)
        books_treeview.column("Publishing House", width=90)
        books_treeview.column("the main words", width=90)
        books_treeview.column("the topic", width=70)

        # Replace this with your actual book data retrieval logic
        # For demonstration purposes, adding some sample books
        books_data = [
            ("Book 1", "Author 1", "dar al", "words", "sciences"),
            ("Book 2", "Author 2", "dar al", "words", "sciences"),
            ("Book 3", "Author 3", "dar al", "words", "sciences"),
            # Add more books as needed
        ]

        # Insert book data into the Treeview
        for book in books_data:
            books_treeview.insert("", tk.END, values=book)

    def search_books(self):
        # Replace this with your actual search logic
        search_query = self.search_entry.get()
        status = self.status_combobox.get()
        print(f"Searching for books with status '{status}': {search_query}")

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
    app = bookApp(root)
    root.mainloop()