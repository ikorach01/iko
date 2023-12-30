import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

class MemberApp():
    def __init__(self, master):
        self.master = master
        self.master.title("Library Management System")
        self.master.geometry("900x650")

        self.title()
        self.load_background_image()
        self.display_books()
        self.create_class_form()
        self.plot_pie_chart()

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
        button_with_image = ttk.Button(frame, text="Login", image=photo, compound=tk.BOTTOM, command=self.open_login_window)
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
        label_username = ttk.Label(frame, text="Member's information", style="Custom.TLabel")
        label_username.place(x=300, y=3)

    def load_background_image(self):
        image = Image.open("member.png")
        image = image.resize((160, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.master, image=photo)
        self.background_label.image = photo
        pad_y = 10
        self.background_label.place(x=680, y=80 + pad_y)

    def display_books(self):
        f2 = ttk.Frame(self.master, width=160, height=200)
        f2.place(x=630, y=200)
        books_listbox = tk.Listbox(f2, width=60, height=10)
        books_listbox.pack(padx=0, pady=10)
        books_data = [
            "Ahmed - Email 1 - 1234567  ",
            "Mouna - Email 2 - 8765322 ",
            "Adel -  Email 3 - 9876543  ",
            # Add more books as needed
        ]

        # Insert book data into the Listbox
        for book in books_data:
            books_listbox.insert(tk.END, book)

        # Matplotlib figure and axis
        self.fig = Figure(figsize=(4, 2), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # Canvas to embed the matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().place(x=200, y=300)

    def plot_pie_chart(self):
        # Replace this with your actual data and plotting logic
        labels = ['new members', 'old members']
        sizes = np.random.rand(len(labels))

        # Clear the previous plot
        self.ax.clear()

        # Plot pie chart
        self.ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        self.ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        self.canvas.get_tk_widget().place(x=280, y=400)
        self.canvas.draw()
        # Set title
        self.ax.set_title('Pie Chart of the members in this year')

        # Redraw the canvas
        self.canvas.draw()

    def create_class_form(self):
        form = ttk.Frame(self.master, padding="2", width=250, height=400)
        form.place(x=0, y=100)

        style = ttk.Style()
        style.configure("titre.TLabel", font=("Helvetica", 14), foreground="black", background="#407BFF")

        author_label = ttk.Label(form, text="First Name:")
        author_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.author_entry = ttk.Entry(form, width=50)
        self.author_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        author2_label = ttk.Label(form, text="Last Name:")
        author2_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.author2_entry = ttk.Entry(form, width=50)
        self.author2_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        # Create labels and entry fields
        datebirth_label = ttk.Label(form, text="Date of Birth:")
        datebirth_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

        self.datebirth_entry = ttk.Entry(form, width=50)
        self.datebirth_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        phone_label = ttk.Label(form, text="The Phone Number:")
        phone_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")

        self.phone_entry = ttk.Entry(form, width=50)
        self.phone_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        address_label = ttk.Label(form, text="The Address:")
        address_label.grid(row=5, column=0, padx=10, pady=5, sticky="e")

        self.address_entry = ttk.Entry(form, width=50)
        self.address_entry.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        occupation_label = ttk.Label(form, text="Occupation:")
        occupation_label.grid(row=6, column=0, padx=10, pady=5, sticky="e")

        self.occupation_entry = ttk.Entry(form, width=50)
        self.occupation_entry.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        add_button = ttk.Button(form, text="Create")
        add_button.grid(row=7, column=1, padx=180, pady=15, sticky="w")

        # Create a search entry field and button
        search_label = ttk.Label(form, text="Search:")
        search_label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.search_entry = ttk.Entry(form)
        self.search_entry.grid(row=8, column=1, padx=10, pady=5, sticky="w")

        search_button = ttk.Button(form, text="Search", command=self.search_member)
        search_button.grid(row=7, column=1, padx=10, pady=5, sticky="w")

    def open_login_window(self):
        # Create an instance of the SecondWindow class
        login_window = tk.Toplevel(self.master)
        login_app = LoginApp(login_window)

    def search_member(self):
        # Replace this with your actual search logic
        search_query = self.search_entry.get()
        print(f"Searching for member: {search_query}")


class LoginApp():
    def __init__(self, master):
        # Implement your login window here
        pass

if __name__ == "__main__":
    root = tk.Tk()
    ico = Image.open('myicon.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    app = MemberApp(root)
    root.mainloop()


def memberApp(window):
    return None