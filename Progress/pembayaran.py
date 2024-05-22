# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from PIL import Image, ImageTk, ImageDraw, ImageFont
# import csv

# def load_data():
#     data = []
#     with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv') as file:
#         reader = csv.reader(file)
#         next(reader) 
#         for row in reader:
#             data.append(row)
#     return data

# def submit_form():
#     nama = name_entry.get()
#     gender = gender_var.get()
#     umur = age_entry.get()
#     email = email_entry.get()
#     tipe_kartu = card_type_combobox.get()
#     nomor_kartu = card_no_entry.get()
#     nomor_hp = phone_no_entry.get()
#     jumlah_pembayaran = load_data()
    

#     if not (nama and umur and email and tipe_kartu and nomor_kartu and nomor_hp and jumlah_pembayaran):
#         messagebox.showerror("Error", "Harap isi semua kolom yang diperlukan!")
#         return

#     with open(r'C:\Users\asus\Documents\TUBES\PROGRESS TUBES\Project-17-Kereta-Sinchan-Solo-Raya\Progress\payment_data.csv', mode='w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(["Nama", "Jenis Kelamin", "Umur", "Email", "Tipe Kartu", "Nomor Kartu", "Nomor HP", "Jumlah Pembayaran"])
#         writer.writerow([nama, gender, umur, email, tipe_kartu, nomor_kartu, nomor_hp, jumlah_pembayaran])
    

 
#     messagebox.showinfo("Sukses", "Pembayaran sudah berhasil dan telah disimpan!")
#     show_ticket(nama, gender, umur, email, nomor_hp, jumlah_pembayaran)

#     name_entry.delete(0, tk.END)
#     age_entry.delete(0, tk.END)
#     email_entry.delete(0, tk.END)
#     card_no_entry.delete(0, tk.END)
#     phone_no_entry.delete(0, tk.END)
#     jml_pembayaran_entry.delete(0, tk.END)
#     gender_var.set("Laki-Laki")
#     card_type_combobox.set("Pilih Tipe Kartu")

# def show_ticket(nama, gender, umur, email, nomor_hp, jumlah_pembayaran):
#     e_ticket= r'C:\Users\asus\Documents\TUBES\PROGRESS TUBES\Project-17-Kereta-Sinchan-Solo-Raya\Tiket Kereta.png'
#     original_image = Image.open(e_ticket)
#     resized_image = original_image.resize((600, 400), Image.Resampling.LANCZOS)
    
#     draw = ImageDraw.Draw(resized_image)
#     font = ImageFont.truetype("arial.ttf", 19)
#     text_color = (0, 0, 0)

#     draw.text((70, 130), f"Nama : {nama}", font=font, fill=text_color)
#     draw.text((70, 160), f"Jenis Kelamin : {gender}", font=font, fill=text_color)
#     draw.text((70, 190), f"Umur : {umur}", font=font, fill=text_color)
#     draw.text((70, 220), f"Email : {email}", font=font, fill=text_color)
#     draw.text((70, 250), f"Nomor HP : {nomor_hp}", font=font, fill=text_color)
#     draw.text((70, 280), f"Jumlah Pembayaran : {jumlah_pembayaran}", font=font, fill=text_color)

#     ticket_image = ImageTk.PhotoImage(resized_image)
    
#     ticket_window = tk.Toplevel(root)
#     ticket_window.title("E-Ticket")
#     ticket_frame = ttk.Frame(ticket_window, padding="20")
#     ticket_frame.grid(row=0, column=0)

#     image_label = ttk.Label(ticket_frame, image=ticket_image)
#     image_label.image = ticket_image
#     image_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

#     ttk.Button(ticket_frame, text="Tutup", command=ticket_window.destroy).grid(row=1, column=0, columnspan=2, pady=(10, 0))

# root = tk.Tk()
# root.title("Formulir Pembayaran")

# main_frame = ttk.Frame(root, padding="20")
# main_frame.grid(row=0, column=0)

# ttk.Label(main_frame, text="Formulir Pembayaran", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

# image_path = r'C:\Users\asus\Documents\TUBES\PROGRESS TUBES\Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Pembayaran.png'
# try:
#     original_image = Image.open(image_path)
#     resized_image = original_image.resize((597, 350), Image.Resampling.LANCZOS)
#     im = ImageTk.PhotoImage(resized_image)
#     image_label = ttk.Label(main_frame, image=im)
#     image_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))
# except Exception as e:
#     print(f"Error loading image: {e}")

# ttk.Label(main_frame, text="Data Pribadi", font=("Helvetica", 12)).grid(row=2, column=0, columnspan=2, pady=(0, 5))

# ttk.Label(main_frame, text="Nama").grid(row=3, column=0, sticky="e")
# name_entry = ttk.Entry(main_frame)
# name_entry.grid(row=3, column=1, sticky="w")

# ttk.Label(main_frame, text="Jenis Kelamin").grid(row=4, column=0, sticky="e")
# gender_var = tk.StringVar()
# gender_var.set("Laki-Laki")
# male_radio = ttk.Radiobutton(main_frame, text="Laki-Laki", variable=gender_var, value="Male")
# male_radio.grid(row=4, column=1, sticky="w")
# female_radio = ttk.Radiobutton(main_frame, text="Perempuan", variable=gender_var, value="Female")
# female_radio.grid(row=4, column=1, sticky="w", padx=(70, 0))

# ttk.Label(main_frame, text="Umur").grid(row=5, column=0, sticky="e")
# age_entry = ttk.Entry(main_frame)
# age_entry.grid(row=5, column=1, sticky="w")

# ttk.Label(main_frame, text="Email ").grid(row=6, column=0, sticky="e")
# email_entry = ttk.Entry(main_frame)
# email_entry.grid(row=6, column=1, sticky="w")

# ttk.Label(main_frame, text="Informasi Pembayaran", font=("Helvetica", 12)).grid(row=7, column=0, columnspan=2, pady=(10, 5))

# ttk.Label(main_frame, text="Tipe Kartu").grid(row=8, column=0, sticky="e")
# card_types = ["Mandiri", "BNI", "BCA", "BRI"]
# card_type_combobox = ttk.Combobox(main_frame, values=card_types)
# card_type_combobox.grid(row=8, column=1, sticky="w")

# ttk.Label(main_frame, text="Nomor Kartu *").grid(row=9, column=0, sticky="e")
# card_no_entry = ttk.Entry(main_frame)
# card_no_entry.grid(row=9, column=1, sticky="w")

# ttk.Label(main_frame, text="Nomor HP").grid(row=10, column=0, sticky="e")
# phone_no_entry = ttk.Entry(main_frame)
# phone_no_entry.grid(row=10, column=1, sticky="w")

# ttk.Label(main_frame, text="Jumlah Pembayaran").grid(row=11, column=0, sticky="e")
# jml_pembayaran_entry = ttk.Entry(main_frame)
# jml_pembayaran_entry.grid(row=11, column=1, sticky="w")

# submit_button = ttk.Button(main_frame, text="Bayar sekarang", command=submit_form)
# submit_button.grid(row=12, column=0, columnspan=2, pady=(20, 0))

# root.mainloop()

import csv
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

def load_data():
    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            return row[0] 

def fill_payment_amount():
    jumlah_pembayaran = load_data()
    if jumlah_pembayaran:
        jml_pembayaran_entry.delete(0, tk.END)
        jml_pembayaran_entry.insert(0, jumlah_pembayaran)
    else:
        messagebox.showerror("Error", "Tidak bisa memuat jumlah pembayaran!")

def submit_form():
    nama = name_entry.get()
    gender = gender_var.get()
    umur = age_entry.get()
    email = email_entry.get()
    tipe_kartu = card_type_combobox.get()
    nomor_kartu = card_no_entry.get()
    nomor_hp = phone_no_entry.get()
    jumlah_pembayaran = jml_pembayaran_entry.get()  

    if not (nama and umur and email and tipe_kartu and nomor_kartu and nomor_hp and jumlah_pembayaran):
        messagebox.showerror("Error", "Harap isi semua kolom yang diperlukan!")
        return

    with open(r'C:\Users\asus\Documents\TUBES\PROGRESS TUBES\Project-17-Kereta-Sinchan-Solo-Raya\Progress\payment_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nama", "Jenis Kelamin", "Umur", "Email", "Tipe Kartu", "Nomor Kartu", "Nomor HP", "Jumlah Pembayaran"])
        writer.writerow([nama, gender, umur, email, tipe_kartu, nomor_kartu, nomor_hp, jumlah_pembayaran])
    
    messagebox.showinfo("Sukses", "Pembayaran sudah berhasil dan telah disimpan!")
    show_ticket(nama, gender, umur, email, nomor_hp, jumlah_pembayaran)

    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    card_no_entry.delete(0, tk.END)
    phone_no_entry.delete(0, tk.END)
    jml_pembayaran_entry.delete(0, tk.END)
    gender_var.set("Laki-Laki")
    card_type_combobox.set("Pilih Tipe Kartu")

def show_ticket(nama, gender, umur, email, nomor_hp, jumlah_pembayaran):
    e_ticket= r'C:\Users\asus\Documents\TUBES\PROGRESS TUBES\Project-17-Kereta-Sinchan-Solo-Raya\Tiket Kereta.png'
    original_image = Image.open(e_ticket)
    resized_image = original_image.resize((600, 400), Image.Resampling.LANCZOS)
    
    draw = ImageDraw.Draw(resized_image)
    font = ImageFont.truetype("arial.ttf", 19)
    text_color = (0, 0, 0)

    draw.text((70, 130), f"Nama : {nama}", font=font, fill=text_color)
    draw.text((70, 160), f"Jenis Kelamin : {gender}", font=font, fill=text_color)
    draw.text((70, 190), f"Umur : {umur}", font=font, fill=text_color)
    draw.text((70, 220), f"Email : {email}", font=font, fill=text_color)
    draw.text((70, 250), f"Nomor HP : {nomor_hp}", font=font, fill=text_color)
    draw.text((70, 280), f"Jumlah Pembayaran : {jumlah_pembayaran}", font=font, fill=text_color)

    ticket_image = ImageTk.PhotoImage(resized_image)
    
    ticket_window = tk.Toplevel(root)
    ticket_window.title("E-Ticket")
    ticket_frame = ttk.Frame(ticket_window, padding="20")
    ticket_frame.grid(row=0, column=0)

    image_label = ttk.Label(ticket_frame, image=ticket_image)
    image_label.image = ticket_image
    image_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    ttk.Button(ticket_frame, text="Tutup", command=ticket_window.destroy).grid(row=1, column=0, columnspan=2, pady=(10, 0))

root = tk.Tk()
root.title("Formulir Pembayaran")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0)

ttk.Label(main_frame, text="Formulir Pembayaran", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

image_path = r'C:\Users\asus\Documents\TUBES\PROGRESS TUBES\Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Pembayaran.png'
try:
    original_image = Image.open(image_path)
    resized_image = original_image.resize((597, 350), Image.Resampling.LANCZOS)
    im = ImageTk.PhotoImage(resized_image)
    image_label = ttk.Label(main_frame, image=im)
    image_label.grid(row=1, column=0, columnspan=2, pady=(0, 10))
except Exception as e:
    print(f"Error loading image: {e}")

ttk.Label(main_frame, text="Data Pribadi", font=("Helvetica", 12)).grid(row=2, column=0, columnspan=2, pady=(0, 5))

ttk.Label(main_frame, text="Nama").grid(row=3, column=0, sticky="e")
name_entry = ttk.Entry(main_frame)
name_entry.grid(row=3, column=1, sticky="w")

ttk.Label(main_frame, text="Jenis Kelamin").grid(row=4, column=0, sticky="e")
gender_var = tk.StringVar()
gender_var.set("Laki-Laki")
male_radio = ttk.Radiobutton(main_frame, text="Laki-Laki", variable=gender_var, value="Laki-Laki")
male_radio.grid(row=4, column=1, sticky="w")
female_radio = ttk.Radiobutton(main_frame, text="Perempuan", variable=gender_var, value="Perempuan")
female_radio.grid(row=4, column=1, sticky="w", padx=(70, 0))

ttk.Label(main_frame, text="Umur").grid(row=5, column=0, sticky="e")
age_entry = ttk.Entry(main_frame)
age_entry.grid(row=5, column=1, sticky="w")

ttk.Label(main_frame, text="Email ").grid(row=6, column=0, sticky="e")
email_entry = ttk.Entry(main_frame)
email_entry.grid(row=6, column=1, sticky="w")

ttk.Label(main_frame, text="Informasi Pembayaran", font=("Helvetica", 12)).grid(row=7, column=0, columnspan=2, pady=(10, 5))

ttk.Label(main_frame, text="Tipe Kartu").grid(row=8, column=0, sticky="e")
card_types = ["Mandiri", "BNI", "BCA", "BRI"]
card_type_combobox = ttk.Combobox(main_frame, values=card_types)
card_type_combobox.grid(row=8, column=1, sticky="w")

ttk.Label(main_frame, text="Nomor Kartu *").grid(row=9, column=0, sticky="e")
card_no_entry = ttk.Entry(main_frame)
card_no_entry.grid(row=9, column=1, sticky="w")

ttk.Label(main_frame, text="Nomor HP").grid(row=10, column=0, sticky="e")
phone_no_entry = ttk.Entry(main_frame)
phone_no_entry.grid(row=10, column=1, sticky="w")

ttk.Label(main_frame, text="Jumlah Pembayaran").grid(row=11, column=0, sticky="e")
jml_pembayaran_entry = ttk.Entry(main_frame)
jml_pembayaran_entry.grid(row=11, column=1, sticky="w")

submit_button = ttk.Button(main_frame, text="Bayar sekarang", command=submit_form)
submit_button.grid(row=12, column=0, columnspan=2, pady=(20, 0))

fill_payment_amount()

root.mainloop()
