import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


class LoginApp:
    def __init__(self, master):
        self.master = master
        self.master.title("login")
        self.master.geometry("800x500")

        # Load and display background image
        self.load_background_image()

        # Create login form
        self.create_login_form()

        self.register()

    def load_background_image(self):

        image = Image.open("background_image.jpg")
        image = image.resize((400, 500), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.master, image=photo)
        self.background_label.image = photo
        self.background_label.place(x=400, y=0)

    def create_login_form(self):

        image = Image.open("ico.png")
        image = image.resize((100, 100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(self.master, image=photo)
        self.background_label.image = photo
        self.background_label.place(x=170, y=45)

        frame = ttk.Frame(self.master, padding="20")
        frame.place(x=50, y=170)

        label_username = ttk.Label(frame, text="Username:")
        label_username.grid(row=0, column=0, sticky="e")

        label_password = ttk.Label(frame, text="Password:")
        label_password.grid(row=1, column=0, sticky="e")

        self.entry_username = ttk.Entry(frame, width=30)
        self.entry_username.grid(row=0, column=1, padx=5, pady=5)

        self.entry_password = ttk.Entry(frame, width=30, show="*")
        self.entry_password.grid(row=1, column=1, padx=5, pady=5)

        style = ttk.Style()
        style.configure("Login.TButton", background="#0C62D4")
        login_button = ttk.Button(frame, text="login", command=self.login, style="Login.TButton")
        login_button.grid(row=2, column=1, pady=25)

    def register(self):
        frame1 = ttk.Frame(self.master, padding="20")
        frame1.place(x=80, y=400)
        label_password = ttk.Label(frame1, text="Don't have an account ?")
        label_password.grid(row=1, column=0, sticky="e")
        style = ttk.Style()
        style.configure("register.TButton", background="#0C62D4")
        register_button = ttk.Button(frame1, text="Register Now",
                                     style="register.TButton")  # ,command= self.open_user_window())
        register_button.grid(row=1, column=2, pady=25, padx=5)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Add your authentication logic here (e.g., check against a database)
        # For this example, let's use a simple check
        if username == "admin" and password == "password":
            messagebox.showinfo("Login Successful", "Welcome, admin!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")


if __name__ == "__main__":
    root = tk.Tk()
    ico = Image.open('myicon.jpg')
    photo = ImageTk.PhotoImage(ico)
    root.wm_iconphoto(False, photo)
    app = LoginApp(root)
    root.mainloop()