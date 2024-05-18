import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import csv

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

    with open(r'Progress\payment_data.csv', mode='w', newline='') as file:
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
    ticket_window = tk.Toplevel(root)
    ticket_window.title("E-Ticket")
    ticket_frame = ttk.Frame(ticket_window, padding="20")
    ticket_frame.grid(row=0, column=0)
    
    ttk.Label(ticket_frame, text="E-Ticket", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))
    ttk.Label(ticket_frame, text="Nama:").grid(row=1, column=0, sticky="e")
    ttk.Label(ticket_frame, text=nama).grid(row=1, column=1, sticky="w")
    
    ttk.Label(ticket_frame, text="Jenis Kelamin:").grid(row=2, column=0, sticky="e")
    ttk.Label(ticket_frame, text=gender).grid(row=2, column=1, sticky="w")
    
    ttk.Label(ticket_frame, text="Umur:").grid(row=3, column=0, sticky="e")
    ttk.Label(ticket_frame, text=umur).grid(row=3, column=1, sticky="w")
    
    ttk.Label(ticket_frame, text="Email:").grid(row=4, column=0, sticky="e")
    ttk.Label(ticket_frame, text=email).grid(row=4, column=1, sticky="w")
    
    ttk.Label(ticket_frame, text="Nomor HP:").grid(row=5, column=0, sticky="e")
    ttk.Label(ticket_frame, text=nomor_hp).grid(row=5, column=1, sticky="w")
    
    ttk.Label(ticket_frame, text="Jumlah Pembayaran:").grid(row=6, column=0, sticky="e")
    ttk.Label(ticket_frame, text=jumlah_pembayaran).grid(row=6, column=1, sticky="w")
    
    ttk.Button(ticket_frame, text="Tutup", command=ticket_window.destroy).grid(row=7, column=0, columnspan=2, pady=(10, 0))

root = tk.Tk()
root.title("Formulir Pembayaran")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0)

ttk.Label(main_frame, text="Formulir Pembayaran", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

image_path = r'kereta sinchan.png'
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
male_radio = ttk.Radiobutton(main_frame, text="Laki-Laki", variable=gender_var, value="Male")
male_radio.grid(row=4, column=1, sticky="w")
female_radio = ttk.Radiobutton(main_frame, text="Perempuan", variable=gender_var, value="Female")
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

root.mainloop()