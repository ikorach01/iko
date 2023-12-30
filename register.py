import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class registerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Register")
        self.master.geometry("800x500")

        # Load and display background image
        self.load_background_image()

        # Create login form
        self.create_register_form()

        self.login()

    def load_background_image(self):

        image = Image.open("register.png")
        image = image.resize((400, 500), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.master, image=photo)
        self.background_label.image = photo
        self.background_label.place(x=400, y=0)

    def create_register_form(self):
        image = Image.open("logo.png")
        image = image.resize((200, 120), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.master, image=photo)
        self.background_label.image = photo
        self.background_label.place(x=130, y=45)

        frame = ttk.Frame(self.master, padding="20")
        frame.place(x=50, y=190)

        label_username = ttk.Label(frame, text="Username:")
        label_username.grid(row=0, column=0, sticky="e")

        label_password = ttk.Label(frame, text="Password:")
        label_password.grid(row=1, column=0, sticky="e")

        label_email = ttk.Label(frame, text="Email:")
        label_email.grid(row=2, column=0, sticky="e")

        self.entry_username = ttk.Entry(frame, width=30)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)

        self.entry_password = ttk.Entry(frame, width=30, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        self.entry_email = ttk.Entry(frame, width=30)
        self.entry_email.grid(row=2, column=1, padx=5, pady=5)
        style = ttk.Style()
        style.configure("registr.TButton", background="#0C62D4")
        login_button = ttk.Button(frame, text="Register", command=self.register, style="login.TButton")
        login_button.grid(row=4, column=1, pady=25)

    def login(self):
        frame1 = ttk.Frame(self.master, padding="20")
        frame1.place(x=80, y=400)
        label_password = ttk.Label(frame1, text="I already had an account ")
        label_password.grid(row=1, column=0, sticky="e")
        style = ttk.Style()
        style.configure("login.TButton", background="#0C62D4")
        register_button = ttk.Button(frame1, text="Login", style="login.TButton")
        register_button.grid(row=1, column=2, pady=25, padx=5)

    def register(self):
        defined_username = "user"
        defined_password = "password"
        defined_email = "email"

        entered_username = self.entry_username.get()
        entered_password = self.entry_password.get()
        entered_email = self.entry_email.get()

        if entered_username == defined_username and entered_password == defined_password and entered_email == defined_email:
            messagebox.showinfo("Sign In Successful", "Welcome, {}".format(defined_username))
        else:
            messagebox.showerror("Sign In Failed", "Invalid username or password")


if __name__ == "__main__":
    root = tk.Tk()
    ico = Image.open('myicon.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    app = registerApp(root)
    root.mainloop()