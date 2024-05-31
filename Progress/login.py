
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
from PIL import Image, ImageTk
import csv

# Fungsi untuk beralih ke jendela login
def switch_to_login():
    login_frame.tkraise()

# Fungsi untuk beralih ke jendela sign up
def switch_to_signup():
    signup_frame.tkraise()

# Jendela utama
root = tk.Tk()
root.title('LOGIN KERETA SINCHAN')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

# Fungsi untuk login
def signin():
    username = user.get()
    password = code.get()

    try:
        with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\user_data.csv', mode='r', newline='') as file:
            reader = csv.reader(file)
            users = {rows[0]: rows[1] for rows in reader}

        if username in users and users[username] == password:
            root.destroy()  # Tutup jendela login 
        else:
            messagebox.showerror('Error', 'Username atau Password tidak valid')
    except FileNotFoundError:
        messagebox.showerror('Error', 'Data pengguna tidak ditemukan')

# Fungsi untuk signup
def signup():
    username = user_signup.get()
    password = code_signup.get()

    try:
        with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\user_data.csv', mode='a+', newline='') as file:
            file.seek(0)
            reader = csv.reader(file)
            users = {rows[0]: rows[1] for rows in reader}

            if username in users:
                messagebox.showerror('Error', 'Username sudah terdaftar')
            else:
                writer = csv.writer(file)
                writer.writerow([username, password])
                messagebox.showinfo('Signup', 'Berhasil register')
                switch_to_login()

    except FileNotFoundError:
        with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\user_data.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
            messagebox.showinfo('Signup', 'Berhasil mendaftar')
            switch_to_login()

# Fungsi untuk mengubah visibilitas password
def toggle_password(entry, var):
    if var.get():
        entry.config(show='')
    else:
        entry.config(show='*')

# Memuat gambar menggunakan PIL
image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Login Page.png'
try:
    pil_image = Image.open(image_path)
    pil_image = pil_image.resize((925, 500), Image.LANCZOS)
    bg_img = ImageTk.PhotoImage(pil_image)
except Exception as e:
    messagebox.showerror("Error", f"Gambar tidak ditemukan: {e}")
    root.destroy()

# Label Latar Belakang
bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame Login
login_frame = tk.Frame(root, bg="white", bd=5, relief=tk.RIDGE)

heading = tk.Label(login_frame, text='KERETA SINCHAN', fg='dark green', bg='white', font=('Times New Roman', 23, 'bold'))
heading.place(x=40, y=20)

user = tk.Entry(login_frame, width=25, fg="black", border=0, bg="white", font=('Times New Roman', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', lambda e: user.delete(0, 'end') if user.get() == 'Username' else None)
user.bind('<FocusOut>', lambda e: user.insert(0, 'Username') if user.get() == '' else None)

tk.Frame(login_frame, width=295, height=2, bg='black').place(x=25, y=107)

code = tk.Entry(login_frame, width=25, fg="black", border=0, bg="white", font=('Times New Roman', 11), show='*')
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', lambda e: code.delete(0, 'end') if code.get() == 'Password' else None)
code.bind('<FocusOut>', lambda e: code.insert(0, 'Password') if code.get() == '' else None)

tk.Frame(login_frame, width=295, height=2, bg='black').place(x=25, y=177)

show_password_var = tk.BooleanVar()
show_password_check = tk.Checkbutton(login_frame, text='Tampilkan Password', bg='white', fg='black', font=('Times New Roman', 11), variable=show_password_var, command=lambda: toggle_password(code, show_password_var))
show_password_check.place(x=30, y=180)

tk.Button(login_frame, width=39, pady=7, text='Sign In', bg="dark green", fg='white', border=0, command=signin).place(x=35, y=220)
tk.Label(login_frame, text="Belum punya akun?", fg='black', bg='white', font=('Times New Roman', 11)).place(x=75, y=270)
tk.Button(login_frame, width=6, text="Sign Up", border=0, cursor="hand2", fg='dark green', bg='white', command=switch_to_signup).place(x=200, y=269)

# Frame Signup
signup_frame = tk.Frame(root, bg="white", bd=5, relief=tk.RIDGE)

heading = tk.Label(signup_frame, text='Sign Up', fg='dark green', bg='white', font=('Times New Roman', 23, 'bold'))
heading.place(x=120, y=22)

user_signup = tk.Entry(signup_frame, width=25, fg="black", border=0, bg="white", font=('Times New Roman', 11))
user_signup.place(x=30, y=80)
user_signup.insert(0, 'Username')
user_signup.bind('<FocusIn>', lambda e: user_signup.delete(0, 'end') if user_signup.get() == 'Username' else None)
user_signup.bind('<FocusOut>', lambda e: user_signup.insert(0, 'Username') if user_signup.get() == '' else None)

tk.Frame(signup_frame, width=295, height=2, bg='black').place(x=25, y=107)

code_signup = tk.Entry(signup_frame, width=25, fg="black", border=0, bg="white", font=('Times New Roman', 11), show='*')
code_signup.place(x=30, y=150)
code_signup.insert(0, 'Password')
code_signup.bind('<FocusIn>', lambda e: code_signup.delete(0, 'end') if code_signup.get() == 'Password' else None)
code_signup.bind('<FocusOut>', lambda e: code_signup.insert(0, 'Password') if code_signup.get() == '' else None)

tk.Frame(signup_frame, width=295, height=2, bg='black').place(x=25, y=177)

show_signup_password_var = tk.BooleanVar()
show_signup_password_check = tk.Checkbutton(signup_frame, text='Tampilkan Password', bg='white', fg='black', font=('Times New Roman', 9), variable=show_signup_password_var, command=lambda: toggle_password(code_signup, show_signup_password_var))
show_signup_password_check.place(x=30, y=180)

tk.Button(signup_frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=220)
tk.Label(signup_frame, text='Sudah punya akun?', fg='black', bg='white', font=('Times New Roman', 10)).place(x=90, y=270)
tk.Button(signup_frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='dark green', command=switch_to_login).place(x=200, y=270)

# Tempatkan frame login dan signup pada posisi yang sama
login_frame.place(x=20, y=60, width=350, height=350)
signup_frame.place(x=20, y=60, width=350, height=350)

# Tampilkan frame login pada awal
login_frame.tkraise()

root.mainloop()
