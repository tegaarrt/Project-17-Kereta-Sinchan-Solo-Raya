
import tkinter as tk
from tkinter import Label, Button, messagebox
from tkinter import ttk 
from tkcalendar import DateEntry  
from PIL import Image, ImageTk
import subprocess
import csv
import login


#Halaman login
login

#Main Window
root = tk.Tk()
root.title("PEMESANAN TIKET KERETA SINCHAN")
root.geometry("1200x700")  
root.resizable(False, False)


l1 = Label(root, text="WELCOME TO PEMESANAN TIKET KERETA SINCHAN", font=("Perpetua", 16, "bold"), bg='lightblue')
l1.pack(pady=10)

def starter():
    root1 = tk.Toplevel(root)
    b.config(state=tk.NORMAL)
    root1.title("Pilih Tanggal dan Rute")
    root1.geometry("600x400")
    root1.resizable(False, False)
    kelas_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background Program.png'
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
        kelas_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background Part 2.jpeg'
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
            trainName_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background Program.png'
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
            prabro_image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\PRABORO.jpg'
            prabro_image = Image.open(prabro_image_path)
            prabro_resized_image = prabro_image.resize((200, 160), Image.Resampling.LANCZOS)
            prabro_photo = ImageTk.PhotoImage(prabro_resized_image)
            
            musta_image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Must A Nice Express Logo.png'
            musta_image = Image.open(musta_image_path)
            musta_resized_image = musta_image.resize((200, 160), Image.Resampling.LANCZOS)
            musta_photo = ImageTk.PhotoImage(musta_resized_image)
            
            # Transparent buttons with images
            prabro_button = tk.Button(root3, image=prabro_photo,bg='white', command=lambda: harga("PRABRORO CHAMP (07:05)"),borderwidth=8, highlightthickness=6)
            prabro_button.image = prabro_photo
            prabro_button.place(x=60, y=90, height=140, width=140)
            
            musta_button = tk.Button(root3, image=musta_photo, command=lambda: harga("MUST A NICE EXPRESS (09:20)"),borderwidth=8, highlightthickness=6)
            musta_button.image = musta_photo
            musta_button.place(x=240, y=90, height=140, width=140)
        
        def siang():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Siang")
            root3.geometry("600x400")
            root3.resizable(False, False)
            trainName_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background 2.png'
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
                
                
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI PILIHAN", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA:")
            l.pack()
            prabro_image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\PRABORO.jpg'
            prabro_image = Image.open(prabro_image_path)
            prabro_resized_image = prabro_image.resize((200, 160), Image.Resampling.LANCZOS)
            prabro_photo = ImageTk.PhotoImage(prabro_resized_image)
            
            janggar_image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Janggar Train Logo.png'
            janggar_image = Image.open(janggar_image_path)
            janggar_resized_image = janggar_image.resize((200, 160), Image.Resampling.LANCZOS)
            janggar_photo = ImageTk.PhotoImage(janggar_resized_image)
            
            # Transparent buttons with images
            prabro_button = tk.Button(root3, image=prabro_photo,bg='white', command=lambda: harga("PRABRORO CHAMP (12:00)"),borderwidth=8, highlightthickness=6)
            prabro_button.image = prabro_photo
            prabro_button.place(x=60, y=90, height=140, width=140)
            
            janggar_button = tk.Button(root3, image=janggar_photo, command=lambda: harga("JANGGAR TRAIN (14:00)"),borderwidth=8, highlightthickness=6)
            janggar_button.image = janggar_photo
            janggar_button.place(x=240, y=90, height=140, width=140)
        
        def sore():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Sore")
            root3.geometry("600x400")
            root3.resizable(False, False)
            trainName_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background Program.png'
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
                 
                l = Label(root4, text="Harga Tiket Anda adalah : Rp. 10.000")
                l.pack()
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA:")
            l.pack()
            musta_image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Must A Nice Express Logo.png'
            musta_image = Image.open(musta_image_path)
            musta_resized_image = musta_image.resize((200, 160), Image.Resampling.LANCZOS)
            musta_photo = ImageTk.PhotoImage(musta_resized_image)
            
            musta_button = tk.Button(root3, image=musta_photo, command=lambda: harga("MUST A NICE EXPRESS (16:15)"),borderwidth=8, highlightthickness=6)
            musta_button.image = musta_photo
            musta_button.place(x=240, y=90, height=140, width=140)
        
        def malam():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Sore")
            root3.geometry("600x400")
            root3.resizable(False, False)
            trainName_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background Program.png'
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
                
                
                 
                l = Label(root4, text="Harga Tiket Anda adalah : Rp. 10.000")
                l.pack()
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA:")
            l.pack()
            musta_image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Janggar Train Logo.png'
            musta_image = Image.open(musta_image_path)
            musta_resized_image = musta_image.resize((200, 160), Image.Resampling.LANCZOS)
            musta_photo = ImageTk.PhotoImage(musta_resized_image)
            
            musta_button = tk.Button(root3, image=musta_photo, command=lambda: harga("MUST A NICE EXPRESS (16:15)"),borderwidth=8, highlightthickness=6)
            musta_button.image = musta_photo
            musta_button.place(x=240, y=90, height=140, width=140)
        
        
        l3 = Label(root2, text="PILIH WAKTU KEBERANGKATAN", bg='silver',borderwidth=6, highlightthickness=5)
        l3.place(x = 188, y = 40)
        b2 = Button(root2, text="PAGI", command=pagi,  bg='silver',borderwidth=6, highlightthickness=5)
        b2.place(x=175, y=100, height=70, width=70)

        b3 = Button(root2, text="SIANG", command=siang,  bg='silver',borderwidth=6, highlightthickness=5)
        b3.place(x=325, y=100, height=70, width=70)

        b4 = Button(root2, text="SORE", command=sore,  bg='silver',borderwidth=6, highlightthickness=5)
        b4.place(x=175, y=200, height=70, width=70)

        b5 = Button(root2, text="MALAM", command=malam,  bg='silver',borderwidth=6, highlightthickness=5)
        b5.place(x=325, y=200, height=70, width=70)

       
    
  
    cal = DateEntry(root1, selectmode='day')
    cal.pack(padx=20, pady=20)
    l2 = Label(root1, text="PILIH RUTE", bg='white')
    l2.place(x=265, y=53)

    
    routes = ["SOLO - WONOGIRI", "SOLO - SRAGEN", "SOLO - KARANGANYAR", "SOLO - BOYOLALI", "SOLO - KLATEN", "WONOGIRI - KARANGANYAR", "WONOGIRI - SRAGEN",
              "WONOGIRI - BOYOLALI","KARANGANYAR - SRAGEN", "KARANGANYER - BOYOLALI", "KARANGANYAR - KLATEN "]
    route_combobox = ttk.Combobox(root1, values=routes)
    route_combobox.pack(pady=10)

    b6 = Button(root1, text='Next', bg='light green', font= ('Times New Roman',12), command=show,borderwidth=4, highlightthickness=6)
    b6.place(x=200 , y=300, width=90, height=30)
    b7 = Button(root1, text='Exit', bg='red', font=('Times New Roman',12),command=root1.destroy,borderwidth=4, highlightthickness=6)
    b7.place(x=310 , y=300, width=90, height=30)


def kelas():
            root3=tk.Toplevel()
            root3.geometry("600x400")
            b11.config(state=tk.NORMAL) 
            def bisnis():
                root3.destroy()
                root4=tk.Toplevel()
                root4.resizable(False, False)
                
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
                Button(root4, text="Kursi 01", command=lambda:hargaakhir("01-Bisnis")).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=lambda:hargaakhir("02-Bisnis")).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=lambda:hargaakhir("03-Bisnis")).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=lambda:hargaakhir("04-Bisnis")).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=lambda:hargaakhir("05-Bisnis")).grid(row=1, column=2)
                Button(root4, text="Kursi 06", command=lambda:hargaakhir("06-Bisnis")).grid(row=2, column=2)
                Button(root4, text="Kursi 07", command=lambda:hargaakhir("07-Bisnis")).grid(row=3, column=2)
                Button(root4, text="Kursi 08", command=lambda:hargaakhir("08-Bisnis")).grid(row=4, column=2)
                root4.mainloop()

            def eksekutif():
                root3.destroy()
                root4=tk.Toplevel()
                root4.resizable(False, False)
                def hargaakhir(kursi):
                    harga="Rp 20.000"
                    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv', mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["harga ticket"])
                         writer.writerow([harga])
                    with open (r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_kursi.csv',mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["Kursi"])
                         writer.writerow([kursi])

                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                    messagebox.showinfo("PEMBERITAHUAN", "Silahkan lanjut ke menu pembayaran")
                
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=lambda:hargaakhir("01-Eksekutif")).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=lambda:hargaakhir("02-Eksekutif")).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=lambda:hargaakhir("03-Eksekutif")).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=lambda:hargaakhir("04-Eksekutif")).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=lambda:hargaakhir("05-Eksekutif")).grid(row=5, column=0)
                Button(root4, text="Kursi 06", command=lambda:hargaakhir("06-Eksekutif")).grid(row=1, column=1)
                Button(root4, text="Kursi 07", command=lambda:hargaakhir("07-Eksekutif")).grid(row=2, column=1)
                Button(root4, text="Kursi 08", command=lambda:hargaakhir("08-Eksekutif")).grid(row=3, column=1)
                Button(root4, text="Kursi 09", command=lambda:hargaakhir("09-Eksekutif")).grid(row=4, column=1)
                Button(root4, text="Kursi 10", command=lambda:hargaakhir("10-Eksekutif")).grid(row=5, column=1)
                Button(root4, text="Kursi 11", command=lambda:hargaakhir("11-Eksekutif")).grid(row=1, column=3)
                Button(root4, text="Kursi 12", command=lambda:hargaakhir("12-Eksekutif")).grid(row=2, column=3)
                Button(root4, text="Kursi 13", command=lambda:hargaakhir("13-Eksekutif")).grid(row=3, column=3)
                Button(root4, text="Kursi 14", command=lambda:hargaakhir("14-Eksekutif")).grid(row=4, column=3)
                Button(root4, text="Kursi 15", command=lambda:hargaakhir("15-Eksekutif")).grid(row=5, column=3)
                Button(root4, text="Kursi 16", command=lambda:hargaakhir("16-Eksekutif")).grid(row=1, column=4)
                Button(root4, text="Kursi 17", command=lambda:hargaakhir("17-Eksekutif")).grid(row=2, column=4)
                Button(root4, text="Kursi 18", command=lambda:hargaakhir("18-Eksekutif")).grid(row=3, column=4)
                Button(root4, text="Kursi 19", command=lambda:hargaakhir("19-Eksekutif")).grid(row=4, column=4)
                Button(root4, text="Kursi 20", command=lambda:hargaakhir("20-Eksekutif")).grid(row=5, column=4)
                root4.mainloop()
                
            def ekonomi():
                root3.destroy()
                root4=tk.Toplevel()
                root4.resizable(False, False)
                def hargaakhir(kursi):
                    harga="Rp 15.000"
                    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv', mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["harga ticket"])
                         writer.writerow([harga])
                    with open (r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_kursi.csv',mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["Kursi"])
                         writer.writerow([kursi])
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                    messagebox.showinfo("PEMBERITAHUAN", "Silahkan lanjut ke menu pembayaran")
               
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=lambda:hargaakhir("01-Ekonomi")).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=lambda:hargaakhir("02-Ekonomi")).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=lambda:hargaakhir("03-Ekonomi")).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=lambda:hargaakhir("04-Ekonomi")).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=lambda:hargaakhir("05-Ekonomi")).grid(row=5, column=0)
                Button(root4, text="Kursi 06", command=lambda:hargaakhir("06-Ekonomi")).grid(row=6, column=0)
                Button(root4, text="Kursi 07", command=lambda:hargaakhir("07-Ekonomi")).grid(row=7, column=0)
                Button(root4, text="Kursi 08", command=lambda:hargaakhir("08-Ekonomi")).grid(row=8, column=0)
                Button(root4, text="Kursi 09", command=lambda:hargaakhir("09-Ekonomi")).grid(row=1, column=1)
                Button(root4, text="Kursi 10", command=lambda:hargaakhir("10-Ekonomi")).grid(row=2, column=1)
                Button(root4, text="Kursi 11", command=lambda:hargaakhir("11-Ekonomi")).grid(row=3, column=1)
                Button(root4, text="Kursi 12", command=lambda:hargaakhir("12-Ekonomi")).grid(row=4, column=1)
                Button(root4, text="Kursi 13", command=lambda:hargaakhir("13-Ekonomi")).grid(row=5, column=1)
                Button(root4, text="Kursi 14", command=lambda:hargaakhir("14-Ekonomi")).grid(row=6, column=1)
                Button(root4, text="Kursi 15", command=lambda:hargaakhir("15-Ekonomi")).grid(row=7, column=1)
                Button(root4, text="Kursi 16", command=lambda:hargaakhir("16-Ekonomi")).grid(row=8, column=1)
                Button(root4, text="Kursi 17", command=lambda:hargaakhir("17-Ekonomi")).grid(row=1, column=3)
                Button(root4, text="Kursi 18", command=lambda:hargaakhir("18-Ekonomi")).grid(row=2, column=3)
                Button(root4, text="Kursi 19", command=lambda:hargaakhir("19-Ekonomi")).grid(row=3, column=3)
                Button(root4, text="Kursi 20", command=lambda:hargaakhir("20-Ekonomi")).grid(row=4, column=3)
                Button(root4, text="Kursi 21", command=lambda:hargaakhir("21-Ekonomi")).grid(row=5, column=3)
                Button(root4, text="Kursi 22", command=lambda:hargaakhir("22-Ekonomi")).grid(row=6, column=3)
                Button(root4, text="Kursi 23", command=lambda:hargaakhir("23-Ekonomi")).grid(row=7, column=3)
                Button(root4, text="Kursi 24", command=lambda:hargaakhir("24-Ekonomi")).grid(row=8, column=3)
                Button(root4, text="Kursi 25", command=lambda:hargaakhir("25-Ekonomi")).grid(row=1, column=4)
                Button(root4, text="Kursi 26", command=lambda:hargaakhir("26-Ekonomi")).grid(row=2, column=4)
                Button(root4, text="Kursi 27", command=lambda:hargaakhir("27-Ekonomi")).grid(row=3, column=4)
                Button(root4, text="Kursi 28", command=lambda:hargaakhir("28-Ekonomi")).grid(row=4, column=4)
                Button(root4, text="Kursi 29", command=lambda:hargaakhir("29-Ekonomi")).grid(row=5, column=4)
                Button(root4, text="Kursi 30", command=lambda:hargaakhir("30-Ekonomi")).grid(row=6, column=4)
                Button(root4, text="Kursi 31", command=lambda:hargaakhir("31-Ekonomi")).grid(row=7, column=4)
                Button(root4, text="Kursi 32", command=lambda:hargaakhir("32-Ekonomi")).grid(row=8, column=4)
                root4.mainloop()

            root3.grid_rowconfigure(0, weight=1)
            root3.grid_rowconfigure(2, weight=1)
            root3.grid_rowconfigure(4, weight=1)
            root3.grid_rowconfigure(6, weight=1)
            root3.grid_columnconfigure(0, weight=1)
            root3.grid_columnconfigure(1, weight=1)

            l = tk.Label(root3, text="PILIH KELAS")
            l.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
            kelas_bg_image_path =r'Project-17-Kereta-Sinchan-Solo-Raya\Background Pilih Kelas.png'
            kelas_bg_image = Image.open(kelas_bg_image_path)
            kelas_resized_image = kelas_bg_image.resize((600, 400), Image.Resampling.LANCZOS)
            kelas_bg_photo = ImageTk.PhotoImage(kelas_resized_image)
            kelas_bg_label = tk.Label(root3, image=kelas_bg_photo)
            kelas_bg_label.image = kelas_bg_photo  
            kelas_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            b1 = tk.Button(root3, text="Bisnis(+Rp. 15.000)", command=bisnis, width=20, height=2, bg='silver',borderwidth=6, highlightthickness=5)
            b1.place(x=120,y=80)
            b2 = tk.Button(root3, text="Eksekutif(+Rp. 10.000)", command=eksekutif, width=20, height=2,  bg='silver',borderwidth=6, highlightthickness=5)
            b2.place(x=300,y=80)
            b3 = tk.Button(root3, text="Ekonomi(+Rp. 5.000)", command=ekonomi, width=20, height=2, bg= 'silver',borderwidth=6, highlightthickness=5)
            b3.place(x=210,y=160)
            root3.mainloop()
            
        

def pembayaran():
    subprocess.Popen(["python", "Project-17-Kereta-Sinchan-Solo-Raya\Progress\pembayaran.py"])


image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Home Page.png'
original_image = Image.open(image_path)
resized_image = original_image.resize((1200, 700), Image.Resampling.LANCZOS)
im = ImageTk.PhotoImage(resized_image)


i = Label(root, image=im)  
i.image = im  
i.place(x=0, y=50) 



button_continue = Button(root, text="Booking Tiket", bg='orange', font=("Times New Roman", 12), compound="left", command=starter,borderwidth=8, highlightthickness=6)
button_continue.place(x=220, y=320, width=150, height=50) 

b = Button(root, text="Pilih Kelas", bg='light green', font=("Times New Roman", 12), compound="left",state=tk.DISABLED, command=kelas,borderwidth=8, highlightthickness=6)
b.place(x=420, y=320, width=150, height=50)  

b11 = Button(root, text="Pembayaran", bg='light blue', font=("Times New Roman", 12), compound="left", command=pembayaran,state=tk.DISABLED, borderwidth=8, highlightthickness=6)
b11.place(x=620, y=320, width=150, height=50)  

button_quit = Button(root, text='Exit', bg='red', font=("Times New Roman", 12), compound="left", command=root.quit,borderwidth=8, highlightthickness=6)
button_quit.place(x=820, y=320, width=150, height=50)  

root.mainloop()

