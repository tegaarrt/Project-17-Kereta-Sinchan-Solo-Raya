
import tkinter as tk
from tkinter import Label, Button, messagebox
from tkinter import ttk 
from tkcalendar import DateEntry  
from PIL import Image, ImageTk
import subprocess
import csv
# import login


# login

root = tk.Tk()
root.title("PEMESANAN TIKET KERETA SINCHAN")
root.geometry("1200x700")  
root.resizable(False, False)


l1 = Label(root, text="WELCOME TO PEMESANAN TIKET KERETA SINCHAN", font=("Helvetica", 16, "bold"), bg='lightblue')
l1.pack(pady=10)

def starter():
    root1 = tk.Toplevel(root)
    b.config(state=tk.NORMAL)
    root1.title("Pilih Tanggal dan Rute")
    root1.geometry("600x400")
    root1.resizable(False, False)
    kelas_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Home Page.png'
    kelas_bg_image = Image.open(kelas_bg_image_path)
    kelas_resized_image = kelas_bg_image.resize((600, 400), Image.Resampling.LANCZOS)
    kelas_bg_photo = ImageTk.PhotoImage(kelas_resized_image)
    kelas_bg_label = tk.Label(root1, image=kelas_bg_photo)
    kelas_bg_label.image = kelas_bg_photo  
    kelas_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    def show():
        selected_date = cal.get()
        selected_route = route_combobox.get()
        with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\tanggal dan rute.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Tanggal", "Rute"])
            writer.writerow([selected_date, selected_route])
        root1.destroy()
        root2 = tk.Toplevel(root)
        root2.geometry("600x400")
        kelas_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Home Page.png'
        kelas_bg_image = Image.open(kelas_bg_image_path)
        kelas_resized_image = kelas_bg_image.resize((600, 400), Image.Resampling.LANCZOS)
        kelas_bg_photo = ImageTk.PhotoImage(kelas_resized_image)
        kelas_bg_label = tk.Label(root2, image=kelas_bg_photo)
        kelas_bg_label.image = kelas_bg_photo  
        kelas_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        root2.title("Pilih Waktu Keberangkatan")
        root2.resizable(False, False)
        
        def pagi():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Pagi")
            root3.geometry("600x400")
            root3.resizable(False, False)
            trainName_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Kumpulan Logo.png'
            trainName_image_path = Image.open(trainName_image_path)
            trainName_image_path_resized_image = trainName_image_path.resize((600, 400), Image.Resampling.LANCZOS)
            trainName_bg_photo = ImageTk.PhotoImage(trainName_image_path_resized_image)
            trainName_bg_label = tk.Label(root3, image=trainName_bg_photo)
            trainName_bg_label.image = trainName_bg_photo  
            trainName_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            def harga(train_name):
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                root4.resizable(False, False)
                with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\kereta dan waktu.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Kereta"])
                    writer.writerow([train_name])
                
                
                def konfirmasi():
                    while True:
                        if messagebox.askyesno("Konfirmasi", "Pilih Kelas yang anda inginkan?"):
                            messagebox.showinfo("Lanjut", "Silahkan Pilih ke menu Pemilihan Kelas")
                            break
                        else:
                            root4.destroy()
                            return starter()
                    root4.destroy()
                
                l = Label(root4, text="Harga Tiket Anda adalah : Rp. 10.000")
                l.pack()
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA :")
            l.pack()
            c = tk.Checkbutton(root3, text="PRABRORO CHAMP (07:05 Pagi)", command=lambda:harga("PRABRORO CHAMP (07:05)"))
            c.pack()
            c1 = tk.Checkbutton(root3, text="MUST A NICE EXPRESS (09:20 Pagi)", command=lambda:harga("MUST A NICE EXPRESS (09.20)")
            )
            c1.pack()
        
        def siang():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Siang")
            root3.geometry("600x400")
            root3.resizable(False, False)
            trainName_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Kumpulan Logo.png'
            trainName_image_path = Image.open(trainName_image_path)
            trainName_image_path_resized_image = trainName_image_path.resize((600, 400), Image.Resampling.LANCZOS)
            trainName_bg_photo = ImageTk.PhotoImage(trainName_image_path_resized_image)
            trainName_bg_label = tk.Label(root3, image=trainName_bg_photo)
            trainName_bg_label.image = trainName_bg_photo  
            trainName_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            def harga(train_name):
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\kereta dan waktu.csv', mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["Kereta"])
                         writer.writerow([train_name])
                
                def konfirmasi():
                    while True:
                        if messagebox.askyesno("Konfirmasi", "Pilih Kelas yang anda inginkan?"):
                            messagebox.showinfo("Lanjut", "Silahkan Pilih ke menu Pemilihan Kelas")
                            break
                        else:
                            root4.destroy()
                            return starter()
                    root4.destroy()
                
                l = Label(root4, text="Harga Tiket Anda : Rp.10.000")
                l.pack()
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA:")
            l.pack()
            c = tk.Checkbutton(root3, text="JANGGAR TRAIN (12:20 Siang)", command=lambda: harga("JANGGAR TRAIN (12:20)"))
            c.pack()
            c1 = tk.Checkbutton(root3, text="PRABRORO CHAMP (13:30 Siang)", command=lambda: harga("PRABRORO CHAMP (13:30)"))
            c1.pack()
        
        def sore():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Sore")
            root3.geometry("600x400")
            root3.resizable(False, False)
            trainName_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Kumpulan Logo.png'
            trainName_image_path = Image.open(trainName_image_path)
            trainName_image_path_resized_image = trainName_image_path.resize((600, 400), Image.Resampling.LANCZOS)
            trainName_bg_photo = ImageTk.PhotoImage(trainName_image_path_resized_image)
            trainName_bg_label = tk.Label(root3, image=trainName_bg_photo)
            trainName_bg_label.image = trainName_bg_photo  
            trainName_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            def harga(train_name):
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\kereta dan waktu.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Kereta"])
                    writer.writerow([train_name])
                
                def konfirmasi():
                    while True:
                        if messagebox.askyesno("Konfirmasi", "Pilih Kelas yang anda inginkan?"):
                            messagebox.showinfo("Lanjut", "Silahkan Pilih ke menu Pemilihan Kelas")
                            break
                        else:
                            root4.destroy()
                            return starter()
                    root4.destroy()
                
                l = Label(root4, text="Harga Tiket Anda : Rp.10.000")
                l.pack()
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA:")
            l.pack()
            c = tk.Checkbutton(root3, text="MUST A NICE EXPRESS (16:15 Sore)", command=lambda:harga("MUST A NICE EXPRESS(16:15)"))
            c.pack()
        
        def malam():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Malam")
            root3.geometry("600x400")
            root3.resizable(False, False)
            trainName_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Kumpulan Logo.png'
            trainName_image_path = Image.open(trainName_image_path)
            trainName_image_path_resized_image = trainName_image_path.resize((600, 400), Image.Resampling.LANCZOS)
            trainName_bg_photo = ImageTk.PhotoImage(trainName_image_path_resized_image)
            trainName_bg_label = tk.Label(root3, image=trainName_bg_photo)
            trainName_bg_label.image = trainName_bg_photo  
            trainName_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            
            def harga(train_name):
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\kereta dan waktu.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Kereta"])
                    writer.writerow([train_name])
                
                
                def konfirmasi():
                    while True:
                        if messagebox.askyesno("Konfirmasi", "Pilih Kelas yang anda inginkan?"):
                            messagebox.showinfo("Lanjut", "Silahkan Pilih ke menu Pemilihan Kelas")
                            break
                        else:
                            root4.destroy()
                            return starter()
                    root4.destroy()
                
                l = Label(root4, text="Harga Tiket Anda : Rp.10.000")
                l.pack()
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA:")
            l.pack()
            c = tk.Checkbutton(root3, text="JANGGAR TRAIN (19:00 Malam)", command=lambda:harga("JANGGAR TRAIN (19:00)"))
            c.pack()
        
        l3 = Label(root2, text="PILIH WAKTU KEBERANGKATAN:", bg='light blue')
        l3.place(x = 180, y = 120)
        b2 = Button(root2, text="Keberangkatan Pagi", command=pagi,  bg='light blue')
        b2.place(x=120, y=150)

        b3 = Button(root2, text="Keberangkatan Siang", command=siang,  bg='light blue')
        b3.place(x=300, y=150)

        b4 = Button(root2, text="Keberangkatan Sore", command=sore,  bg='light blue')
        b4.place(x=120, y=250)

        b5 = Button(root2, text="Keberangkatan Malam", command=malam,  bg='light blue')
        b5.place(x=300, y=250)

        b6 = Button(root2, text='EXIT', bg='red', command=root2.destroy)
        b6.place(x= 270, y=350)
    
    ll = Label(root1, text="Pilih Tanggal Keberangkatan (mm/dd/yy):")
    ll.pack()
    cal = DateEntry(root1, selectmode='day')
    cal.pack(padx=20, pady=20)
    l2 = Label(root1, text="PILIH RUTE")
    l2.pack()

    
    routes = ["SOLO - WONOGIRI", "SOLO - SRAGEN", "SOLO - KARANGANYAR", "SOLO - BOYOLALI", "SOLO - KLATEN", "WONOGIRI - KARANGANYAR", "WONOGIRI - SRAGEN",
              "WONOGIRI - BOYOLALI","KARANGANYAR - SRAGEN", "KARANGANYER - BOYOLALI", "KARANGANYAR - KLATEN "]
    route_combobox = ttk.Combobox(root1, values=routes)
    route_combobox.pack(pady=10)

    b6 = Button(root1, text='NEXT', command=show)
    b6.pack()
    b7 = Button(root1, text='EXIT', bg='red', command=root1.destroy)
    b7.pack()


def kelas():
            root3=tk.Toplevel()
            root3.geometry("600x400")
            def bisnis():
                root3.destroy()
                root4=tk.Toplevel()
                root4.geometry("600x400")
                root4.resizable(False, False)
                eko_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background.png'
                eko_bg_image = Image.open(eko_bg_image_path)
                eko_resized_image = eko_bg_image.resize((600, 400), Image.Resampling.LANCZOS)
                eko_bg_photo = ImageTk.PhotoImage(eko_resized_image)
                eko_bg_label = tk.Label(root4, image=eko_bg_photo)
                eko_bg_label.image = eko_bg_photo  
                eko_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                def hargaakhir(kursi):
                    harga="Rp 25.000"
                    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv', mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["harga ticket"])
                         writer.writerow([harga])
                    with open (r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_kursi.csv',mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["Kursi"])
                         writer.writerow([kursi])

                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                    messagebox.showinfo("PEMBERITAHUAN", "Silahkan lanjut ke menu pembayaran")
                  
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=lambda:hargaakhir("01")).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=lambda:hargaakhir("02")).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=lambda:hargaakhir("03")).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=lambda:hargaakhir("04")).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=lambda:hargaakhir("05")).grid(row=1, column=2)
                Button(root4, text="Kursi 06", command=lambda:hargaakhir("06")).grid(row=2, column=2)
                Button(root4, text="Kursi 07", command=lambda:hargaakhir("07")).grid(row=3, column=2)
                Button(root4, text="Kursi 08", command=lambda:hargaakhir("08")).grid(row=4, column=2)
                b = Button(root4, text="NEXT").grid(row=6, column=1)
                b.grid(row=3, column=0, columnspan=5)
                root4.mainloop()

            def eksekutif():
                root3.destroy()
                root4=tk.Toplevel()
                root4.geometry("600x400")
                root4.resizable(False, False)
                eko_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background.png'
                eko_bg_image = Image.open(eko_bg_image_path)
                eko_resized_image = eko_bg_image.resize((600, 400), Image.Resampling.LANCZOS)
                eko_bg_photo = ImageTk.PhotoImage(eko_resized_image)
                eko_bg_label = tk.Label(root4, image=eko_bg_photo)
                eko_bg_label.image = eko_bg_photo  
                eko_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                def hargaakhir():
                    harga="Rp 20.000"
                    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv', mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["harga ticket"])
                         writer.writerow([harga])
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                    messagebox.showinfo("PEMBERITAHUAN", "Silahkan lanjut ke menu pembayaran")
                
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=hargaakhir).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=hargaakhir).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=hargaakhir).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=hargaakhir).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=hargaakhir).grid(row=5, column=0)
                Button(root4, text="Kursi 06", command=hargaakhir).grid(row=1, column=1)
                Button(root4, text="Kursi 07", command=hargaakhir).grid(row=2, column=1)
                Button(root4, text="Kursi 08", command=hargaakhir).grid(row=3, column=1)
                Button(root4, text="Kursi 09", command=hargaakhir).grid(row=4, column=1)
                Button(root4, text="Kursi 10", command=hargaakhir).grid(row=5, column=1)
                Button(root4, text="Kursi 11", command=hargaakhir).grid(row=1, column=3)
                Button(root4, text="Kursi 12", command=hargaakhir).grid(row=2, column=3)
                Button(root4, text="Kursi 13", command=hargaakhir).grid(row=3, column=3)
                Button(root4, text="Kursi 14", command=hargaakhir).grid(row=4, column=3)
                Button(root4, text="Kursi 15", command=hargaakhir).grid(row=5, column=3)
                Button(root4, text="Kursi 16", command=hargaakhir).grid(row=1, column=4)
                Button(root4, text="Kursi 17", command=hargaakhir).grid(row=2, column=4)
                Button(root4, text="Kursi 18", command=hargaakhir).grid(row=3, column=4)
                Button(root4, text="Kursi 19", command=hargaakhir).grid(row=4, column=4)
                Button(root4, text="Kursi 20", command=hargaakhir).grid(row=5, column=4)
                b = Button(root4, text="NEXT").grid(row=6, column=2)
                b.grid(row=3, column=0, columnspan=5)
                root4.mainloop()
                
            def ekonomi():
                root3.destroy()
                root4=tk.Toplevel()
                root4.geometry("600x400")
                root4.resizable(False, False)
                eko_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background.png'
                eko_bg_image = Image.open(eko_bg_image_path)
                eko_resized_image = eko_bg_image.resize((600, 400), Image.Resampling.LANCZOS)
                eko_bg_photo = ImageTk.PhotoImage(eko_resized_image)
                eko_bg_label = tk.Label(root4, image=eko_bg_photo)
                eko_bg_label.image = eko_bg_photo  
                eko_bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                def hargaakhir():
                    harga="Rp 15.000"
                    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv', mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["harga ticket"])
                         writer.writerow([harga])
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                    messagebox.showinfo("PEMBERITAHUAN", "Silahkan lanjut ke menu pembayaran")
               
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=hargaakhir).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=hargaakhir).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=hargaakhir).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=hargaakhir).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=hargaakhir).grid(row=5, column=0)
                Button(root4, text="Kursi 06", command=hargaakhir).grid(row=6, column=0)
                Button(root4, text="Kursi 07", command=hargaakhir).grid(row=7, column=0)
                Button(root4, text="Kursi 08", command=hargaakhir).grid(row=8, column=0)
                Button(root4, text="Kursi 09", command=hargaakhir).grid(row=1, column=1)
                Button(root4, text="Kursi 10", command=hargaakhir).grid(row=2, column=1)
                Button(root4, text="Kursi 11", command=hargaakhir).grid(row=3, column=1)
                Button(root4, text="Kursi 12", command=hargaakhir).grid(row=4, column=1)
                Button(root4, text="Kursi 13", command=hargaakhir).grid(row=5, column=1)
                Button(root4, text="Kursi 14", command=hargaakhir).grid(row=6, column=1)
                Button(root4, text="Kursi 15", command=hargaakhir).grid(row=7, column=1)
                Button(root4, text="Kursi 16", command=hargaakhir).grid(row=8, column=1)
                Button(root4, text="Kursi 17", command=hargaakhir).grid(row=1, column=3)
                Button(root4, text="Kursi 18", command=hargaakhir).grid(row=2, column=3)
                Button(root4, text="Kursi 19", command=hargaakhir).grid(row=3, column=3)
                Button(root4, text="Kursi 20", command=hargaakhir).grid(row=4, column=3)
                Button(root4, text="Kursi 21", command=hargaakhir).grid(row=5, column=3)
                Button(root4, text="Kursi 22", command=hargaakhir).grid(row=6, column=3)
                Button(root4, text="Kursi 23", command=hargaakhir).grid(row=7, column=3)
                Button(root4, text="Kursi 24", command=hargaakhir).grid(row=8, column=3)
                Button(root4, text="Kursi 25", command=hargaakhir).grid(row=1, column=4)
                Button(root4, text="Kursi 26", command=hargaakhir).grid(row=2, column=4)
                Button(root4, text="Kursi 27", command=hargaakhir).grid(row=3, column=4)
                Button(root4, text="Kursi 28", command=hargaakhir).grid(row=4, column=4)
                Button(root4, text="Kursi 29", command=hargaakhir).grid(row=5, column=4)
                Button(root4, text="Kursi 30", command=hargaakhir).grid(row=6, column=4)
                Button(root4, text="Kursi 31", command=hargaakhir).grid(row=7, column=4)
                Button(root4, text="Kursi 32", command=hargaakhir).grid(row=8, column=4)
                root4.mainloop()

            root3.grid_rowconfigure(0, weight=1)
            root3.grid_rowconfigure(2, weight=1)
            root3.grid_rowconfigure(4, weight=1)
            root3.grid_rowconfigure(6, weight=1)
            root3.grid_columnconfigure(0, weight=1)
            root3.grid_columnconfigure(1, weight=1)

            l = tk.Label(root3, text="PILIH KELAS")
            l.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
            kelas_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Home Page.png'
            kelas_bg_image = Image.open(kelas_bg_image_path)
            kelas_resized_image = kelas_bg_image.resize((600, 400), Image.Resampling.LANCZOS)
            kelas_bg_photo = ImageTk.PhotoImage(kelas_resized_image)
            kelas_bg_label = tk.Label(root3, image=kelas_bg_photo)
            kelas_bg_label.image = kelas_bg_photo  
            kelas_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            b1 = tk.Button(root3, text="Bisnis(+Rp. 15.000)", command=bisnis, width=20, height=2, bg='light blue')
            b2 = tk.Button(root3, text="Eksekutif(+Rp. 10.000)", command=eksekutif, width=20, height=2,  bg='light blue')
            b3 = tk.Button(root3, text="Ekonomi(+Rp. 5.000)", command=ekonomi, width=20, height=2, bg= 'light blue')


            b1.grid(row=3, column=0, padx=10, pady=5, sticky="e")
            b2.grid(row=3, column=1, padx=10, pady=5, sticky="w")
            b3.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

            root3.mainloop()
        

def pembayaran():
    subprocess.Popen(["python", "Project-17-Kereta-Sinchan-Solo-Raya\Progress\pembayaran.py"])


image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Home Page.png'
original_image = Image.open(image_path)
resized_image = original_image.resize((1200, 650), Image.Resampling.LANCZOS)
im = ImageTk.PhotoImage(resized_image)


i = Label(root, image=im)  
i.image = im  
i.place(x=0, y=50) 



button_continue = Button(root, text="Booking Tiket", bg='orange', font=("Arial", 12), compound="left", command=starter)
button_continue.place(x=220, y=290, width=150, height=50) 

b = Button(root, text="Pilih Kelas", bg='light green', font=("Arial", 12), compound="left", command=kelas)
b.place(x=420, y=290, width=150, height=50)  

b1 = Button(root, text="Pembayaran", bg='light blue', font=("Arial", 12), compound="left",  command=pembayaran)
b1.place(x=620, y=290, width=150, height=50)  

button_quit = Button(root, text='EXIT', bg='red', font=("Arial", 12), compound="left", command=root.quit)
button_quit.place(x=820, y=290, width=150, height=50)  

root.mainloop()




