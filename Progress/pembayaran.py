
import csv
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import win32print
import os


def load_data():
    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            return row[0]
def load_kereta():
    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\kereta dan waktu.csv') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            return row[0]
        
def load_tanggal():
    tanggal_rute = [] 
    try:
        with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\tanggal dan rute.csv') as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                tanggal = row[0]
                rute = row[1]
                tanggal_rute.append((tanggal, rute))  
    except FileNotFoundError:
        messagebox.showerror("Error", "File tanggal dan rute tidak ditemukan!")
    return tanggal_rute 

            
def load_kursi():
    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_kursi.csv') as file:
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

def kereta_berangkat():
    kereta = load_kereta()
    if kereta:
        kereta_entry.delete(0, tk.END)
        kereta_entry.insert(0, kereta)
    else:
        messagebox.showerror("Error", "Tidak bisa memuat kereta")

def kursi():
    kursi = load_kursi()
    if kursi:
        kursi_entry.delete(0, tk.END)
        kursi_entry.insert(0, kursi)


def load_tanggal_rute():
    tanggal_rute_list = load_tanggal()  
    if tanggal_rute_list:
        tanggal_rute_entry.delete(0, tk.END)
        tanggal_rute_string = "\n".join([f"{tanggal}, {rute}" for tanggal, rute in tanggal_rute_list])
        tanggal_rute_entry.insert(0, tanggal_rute_string)
    else:
        messagebox.showerror("Error", "Tidak bisa memuat tanggal dan rute!")


def print_eticket(image_path):
    printer_name = win32print.GetDefaultPrinter()
    os.startfile(image_path, "print", printer_name)


def validate_input():

    email = email_entry.get()
    if not isinstance(email, str) or "@" not in email :
        messagebox.showerror("Error", "Email tidak valid!")
        messagebox.showerror("Error", "Pembayaran Error lengkapi dengan benar")
        return False


    nomor_kartu = card_no_entry.get()
    if not nomor_kartu.isdigit():
        messagebox.showerror("Error", "Nomor Kartu harus berupa angka")
        messagebox.showerror("Error", "Pembayaran Error lengkapi dengan benar")
        return False

    nomor_hp = phone_no_entry.get()
    if not nomor_hp.isdigit():
        messagebox.showerror("Error", "Nomor HP harus berupa angka!")
        messagebox.showerror("Error", "Pembayaran Error lengkapi dengan benar")
        return False

    return True

def submit_form():
    if not validate_input():
        return

    nama = name_entry.get()
    gender = gender_var.get()
    
    email = email_entry.get()
    tipe_kartu = card_type_combobox.get()
    nomor_kartu = card_no_entry.get()
    nomor_hp = phone_no_entry.get()
    jumlah_pembayaran = jml_pembayaran_entry.get() 
    kursi = kursi_entry.get()
    kereta = kereta_entry.get() 
    tanggal_dan_rute = tanggal_rute_entry.get()

    if not (nama and email and tipe_kartu and nomor_kartu and nomor_hp and kursi and jumlah_pembayaran and kereta and tanggal_dan_rute):
        messagebox.showerror("Error", "Harap isi semua kolom yang diperlukan!")
        return

    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\payment_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nama", "Jenis Kelamin", "Umur", "Email", "Tipe Kartu", "Nomor Kartu", "Nomor HP", "Jumlah Pembayaran","Tanggal dan Rute"])
        writer.writerow([nama, gender, email, tipe_kartu, nomor_kartu, nomor_hp, jumlah_pembayaran, kereta, tanggal_dan_rute])
    
    messagebox.showinfo("Sukses", "Pembayaran sudah berhasil dan telah disimpan!")
    messagebox.showinfo("Informasi", "Simpan E-ticket anda saat akan berangkat")
    show_ticket(nama, jumlah_pembayaran, kereta,kursi, tanggal_dan_rute)


    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    card_no_entry.delete(0, tk.END)
    phone_no_entry.delete(0, tk.END)
    jml_pembayaran_entry.delete(0, tk.END)
    kereta_entry.delete(0, tk.END)
    tanggal_rute_entry.delete(0, tk.END)
    gender_var.set("Laki-Laki")
    card_type_combobox.set("Pilih Tipe Kartu")

    
def show_ticket(nama, jumlah_pembayaran, kereta, kursi, tanggal_dan_rute):
    e_ticket_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Tiket Kereta fix.png'
    original_image = Image.open(e_ticket_path)
    resized_image = original_image.resize((600, 400), Image.Resampling.LANCZOS)
    
    draw = ImageDraw.Draw(resized_image)
    font = ImageFont.truetype("arial.ttf", 17)
    text_color = (0, 0, 0)

  
    base_x = 30
    base_y = 130
    line_height = 30
    colon_x = base_x + 210  

    def draw_text(label, value, y):
       
        draw.text((base_x, y), label, font=font, fill=text_color)
        
        draw.text((colon_x, y), ":", font=font, fill=text_color)
       
        value_x = colon_x + 10  
        draw.text((value_x, y), value, font=font, fill=text_color)

    # Menggunakan fungsi draw_text untuk setiap baris
    draw_text("Nama Penumpang", nama, base_y)
    draw_text("Jumlah Pembayaran", jumlah_pembayaran, base_y + line_height)
    draw_text("Keberangkatan", kereta, base_y + 2 * line_height)
    draw_text("Kursi dan Kelas", kursi, base_y + 3 * line_height)
    draw_text("Tanggal dan Rute", tanggal_dan_rute, base_y + 4 * line_height)

    ticket_image = ImageTk.PhotoImage(resized_image)
    
    ticket_window = tk.Toplevel(root)
    ticket_window.title("E-Ticket")
    ticket_frame = ttk.Frame(ticket_window, padding="20")
    ticket_frame.grid(row=0, column=0)

    image_label = ttk.Label(ticket_frame, image=ticket_image)
    image_label.image = ticket_image
    image_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

    ttk.Button(ticket_frame, text="Tutup", command=ticket_window.destroy and root.destroy).grid(row=1, column=0, columnspan=2, pady=(10, 0))


root = tk.Tk()
root.title("Formulir Pembayaran")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(row=0, column=0)

ttk.Label(main_frame, text="Formulir Pembayaran", font=("Helvetica", 16)).grid(row=0, column=0, columnspan=2, pady=(0, 10))

image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Pembayaran.png'
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


ttk.Label(main_frame, text="Email ").grid(row=5, column=0, sticky="e")
email_entry = ttk.Entry(main_frame)
email_entry.grid(row=5, column=1, sticky="w")

ttk.Label(main_frame, text="Informasi Pembayaran", font=("Helvetica", 12)).grid(row=6, column=0, columnspan=2, pady=(10, 5))

ttk.Label(main_frame, text="Tipe Kartu").grid(row=7, column=0, sticky="e")
card_types = ["Mandiri", "BNI", "BCA", "BRI"]
card_type_combobox = ttk.Combobox(main_frame, values=card_types)
card_type_combobox.grid(row=7, column=1, sticky="w")

ttk.Label(main_frame, text="Nomor Kartu *").grid(row=8, column=0, sticky="e")
card_no_entry = ttk.Entry(main_frame)
card_no_entry.grid(row=8, column=1, sticky="w")

ttk.Label(main_frame, text="Nomor HP").grid(row=9, column=0, sticky="e")
phone_no_entry = ttk.Entry(main_frame)
phone_no_entry.grid(row=9, column=1, sticky="w")

ttk.Label(main_frame, text="Kursi").grid(row=10, column=0, sticky="e")
kursi_entry = ttk.Entry(main_frame)
kursi_entry.grid(row=10, column=1, sticky="w")

ttk.Label(main_frame, text="Jumlah Pembayaran").grid(row=11, column=0, sticky="e")
jml_pembayaran_entry = ttk.Entry(main_frame)
jml_pembayaran_entry.grid(row=11, column=1, sticky="w")

ttk.Label(main_frame, text="Kereta").grid(row=12, column=0, sticky="e")
kereta_entry = ttk.Entry(main_frame)
kereta_entry.grid(row=12, column=1, sticky="w")

ttk.Label(main_frame, text="Tanggal dan Rute").grid(row=13, column=0, sticky="e")
tanggal_rute_entry = ttk.Entry(main_frame)
tanggal_rute_entry.grid(row=13, column=1, sticky="w")


submit_button = ttk.Button(main_frame, text="Bayar sekarang", command=submit_form)
submit_button.grid(row=14, column=0, columnspan=2, pady=(20, 0))


load_tanggal_rute()
fill_payment_amount()
kereta_berangkat()
kursi()

root.mainloop()

