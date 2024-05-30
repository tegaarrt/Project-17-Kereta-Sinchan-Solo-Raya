
# import tkinter as tk
# from tkinter import messagebox
# import csv
# from PIL import Image, ImageTk

# user_data = {}

# try:
#     with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\user_data.csv') as file:
#         reader = csv.reader(file)
#         user_data = {rows[0]: rows[1] for rows in reader}
# except FileNotFoundError:
#     pass

# def register(username, password):
#     if username in user_data:
#         messagebox.showerror("Error", "Username sudah terdaftar!")
#     elif not username or not password:
#         messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
#     else:
#         user_data[username] = password
#         with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\user_data.csv', mode="w", newline="") as file:
#             writer = csv.writer(file)
#             writer.writerow([username, password])
#         messagebox.showinfo("Sukses", "Registrasi berhasil!")
#         register_window.destroy()

# def login(username, password):
#     if username in user_data and user_data[username] == password:
#         messagebox.showinfo("Sukses", "Login berhasil!")
#         login_window.destroy()
#         root.destroy()  # Close the main window
#     else:
#         messagebox.showerror("Error", "Login gagal!")

# def show_register_window():
#     global register_window
#     register_window = tk.Toplevel(root)
#     register_window.title("Register")
#     register_window.geometry("400x300")
    
#     # Load background image
#     reg_bg_image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Home Page.png'
#     reg_bg_image = Image.open(reg_bg_image_path)
#     reg_resized_image = reg_bg_image.resize((400, 300), Image.Resampling.LANCZOS)
#     reg_bg_photo = ImageTk.PhotoImage(reg_resized_image)
#     reg_bg_label = tk.Label(register_window, image=reg_bg_photo)
#     reg_bg_label.image = reg_bg_photo  # Keep a reference
#     reg_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
#     tk.Label(register_window, text="Username:", bg='light blue', font=("Arial", 12)).place(x=160, y=80)
#     username_entry = tk.Entry(register_window, font=("Arial", 12))
#     username_entry.place(x= 110, y=120)

#     tk.Label(register_window, text="Password:", bg='light blue',font=("Arial", 12)).place(x=160, y=150)
#     password_entry = tk.Entry(register_window, font=("Arial", 12))
#     password_entry.place(x=110 , y=180)

#     tk.Button(register_window, text="Register", bg='light blue', font=("Arial", 12), command=lambda: register(username_entry.get(), password_entry.get())).place(x= 160, y= 220)

# def show_login_window():
#     global login_window
#     login_window = tk.Toplevel(root)
#     login_window.title("Login")
#     login_window.geometry("400x300")
    
#     # Load background image
#     login_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Home Page.png'
#     login_bg_image = Image.open(login_bg_image_path)
#     login_resized_image = login_bg_image.resize((400, 300), Image.Resampling.LANCZOS)
#     login_bg_photo = ImageTk.PhotoImage(login_resized_image)
#     login_bg_label = tk.Label(login_window, image=login_bg_photo)
#     login_bg_label.image = login_bg_photo  
#     login_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
#     tk.Label(login_window, text="Username:", font=("Arial", 12)).place(x=160, y=80)
#     username_entry = tk.Entry(login_window, font=("Arial", 12))
#     username_entry.place(x= 110, y=120)

#     tk.Label(login_window, text="Password:", font=("Arial", 12)).place(x=160, y=150)
#     password_entry = tk.Entry(login_window, font=("Arial", 12), show="*")
#     password_entry.place(x=110 , y=180)

#     tk.Button(login_window, text="Login", font=("Arial", 12), command=lambda: login(username_entry.get(), password_entry.get())).place(x= 160, y= 220)

# # Main window
# root = tk.Tk()
# root.title("Program Pemesanan Tiket Sinchan")
# root.geometry("1200x800")

# # Load background image
# image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Home Page.png'
# original_image = Image.open(image_path)
# resized_image = original_image.resize((1200, 800), Image.Resampling.LANCZOS)
# bg_photo = ImageTk.PhotoImage(resized_image)
# bg_label = tk.Label(root, image=bg_photo)
# bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# # Add title label
# title_label = tk.Label(root, text="Program Pemesanan Tiket Sinchan", font=("Arial", 24), bg="light blue")
# title_label.pack(pady=20)

# # Add register and login buttons
# register_button = tk.Button(root, text="Register", font=("Arial", 14), command=show_register_window, bg='light blue')
# register_button.place(x=450, y=350, width=150, height=50)  

# login_button = tk.Button(root, text="Login", font=("Arial", 14), command=show_login_window, bg='light blue')
# login_button.place(x=650, y=350, width=150, height=50)  

# root.mainloop()


import tkinter as tk
from tkinter import messagebox
import csv
from PIL import Image, ImageTk

user_data = {}

try:
    with open(r'Progress\user_data.csv') as file:
        reader = csv.reader(file)
        user_data = {rows[0]: rows[1] for rows in reader}
except FileNotFoundError:
    pass

def register(username, password):
    if username in user_data:
        messagebox.showerror("Error", "Username sudah terdaftar!")
    elif not username or not password:
        messagebox.showerror("Error", "Username dan password tidak boleh kosong!")
    else:
        user_data[username] = password
        with open(r'Progress\user_data.csv', mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        messagebox.showinfo("Sukses", "Registrasi berhasil!")
        register_window.destroy()

def login(username, password):
    if username in user_data and user_data[username] == password:
        messagebox.showinfo("Sukses", "Login berhasil!")
        login_window.destroy()
        root.destroy()  # Close the main window
    else:
        messagebox.showerror("Error", "Login gagal!")

def show_register_window():
    global register_window
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("600x360")
    
    # Load background image
<<<<<<< HEAD
    reg_bg_image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Background 2.png'
=======
    reg_bg_image_path = r'Background.png'
>>>>>>> ca9f328ea7d9e798abd1efd3dfe174a58c9d3fd9
    reg_bg_image = Image.open(reg_bg_image_path)
    reg_resized_image = reg_bg_image.resize((600, 360), Image.Resampling.LANCZOS)
    reg_bg_photo = ImageTk.PhotoImage(reg_resized_image)
    reg_bg_label = tk.Label(register_window, image=reg_bg_photo)
    reg_bg_label.image = reg_bg_photo  # Keep a reference
    reg_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    tk.Label(register_window, text="Username:", font=("Arial", 12)).pack(pady=10)
    username_entry = tk.Entry(register_window, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(register_window, text="Password:", font=("Arial", 12)).pack(pady=10)
    password_entry = tk.Entry(register_window, font=("Arial", 12))
    password_entry.pack(pady=5)

    tk.Button(register_window, text="Register", font=("Arial", 12), command=lambda: register(username_entry.get(), password_entry.get())).pack(pady=20)

def show_login_window():
    global login_window
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("600x360")
    
    # Load background image
<<<<<<< HEAD
    login_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background 2.png'
=======
    login_bg_image_path =r'Background.png'
>>>>>>> ca9f328ea7d9e798abd1efd3dfe174a58c9d3fd9
    login_bg_image = Image.open(login_bg_image_path)
    login_resized_image = login_bg_image.resize((600, 360), Image.Resampling.LANCZOS)
    login_bg_photo = ImageTk.PhotoImage(login_resized_image)
    login_bg_label = tk.Label(login_window, image=login_bg_photo)
    login_bg_label.image = login_bg_photo  
    login_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    tk.Label(login_window, text="Username:", font=("Arial", 12)).pack(pady=10)
    username_entry = tk.Entry(login_window, font=("Arial", 12))
    username_entry.pack(pady=5)

    tk.Label(login_window, text="Password:", font=("Arial", 12)).pack(pady=10)
    password_entry = tk.Entry(login_window, font=("Arial", 12), show="*")
    password_entry.pack(pady=5)

    tk.Button(login_window, text="Login", font=("Arial", 12), command=lambda: login(username_entry.get(), password_entry.get())).pack(pady=20)

# Main window
root = tk.Tk()
root.title("Program Pemesanan Tiket Sinchan")
root.geometry("900x540")

# Load background image
image_path = r'Kereta Sinchan Home Page.png'
original_image = Image.open(image_path)
resized_image = original_image.resize((900, 540), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(resized_image)
bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add register and login buttons
register_button = tk.Button(root, text="Register", font=("Arial", 14), command=show_register_window, bg='light blue')
register_button.place(x=260, y=240, width=150, height=50)  

login_button = tk.Button(root, text="Login", font=("Arial", 14), command=show_login_window, bg='light blue')
login_button.place(x=470, y=240, width=150, height=50)  

root.mainloop()
