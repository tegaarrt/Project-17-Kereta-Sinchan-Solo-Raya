
import tkinter as tk
from tkinter import Label, Button, messagebox
from tkinter import ttk 
from tkcalendar import DateEntry  
from PIL import Image, ImageTk
import subprocess
import csv


root = tk.Tk()
root.title("PEMESANAN TIKET KERETA SINCHAN")
root.geometry("1200x700")  


l1 = Label(root, text="WELCOME TO PEMESANAN TIKET KERETA SINCHAN", font=("Helvetica", 16, "bold"), bg='lightblue')
l1.pack(pady=10)

def starter():
    root1 = tk.Toplevel(root)
    root1.title("Pilih Tanggal dan Rute")
    
    def show():
        root1.destroy()
        root2 = tk.Toplevel(root)
        root2.title("Pilih Waktu Keberangkatan")
        
        def pagi():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Pagi")
            
            def harga():
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                
                def konfirmasi():
                    while True:
                        if messagebox.askyesno("Konfirmasi", "Pilih Kelas yang anda inginkan?"):
                            messagebox.showinfo("Lanjut", "Silahkan Pilih ke menu Pemilihan Kelas")
                            break
                        else:
                            return starter()
                    messagebox.showinfo("SELAMAT", "TIKET ANDA TELAH DIPESAN")
                
                l = Label(root4, text="Harga Tiket Anda adalah : Rp. 10.000")
                l.pack()
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA :")
            l.pack()
            c = tk.Checkbutton(root3, text="PRABRORO CHAMP (7:05 a.m.)", command=harga)
            c.pack()
            c1 = tk.Checkbutton(root3, text="MUST A NICE EXPRESS (9:20 a.m.)", command=harga)
            c1.pack()
        
        def siang():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Siang")
            
            def harga():
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                
                def konfirmasi():
                    messagebox.showinfo("SELAMAT", "TIKET ANDA TELAH DIPESAN")
                
                l = Label(root4, text="Harga Tiket Anda : Rp.10.000")
                l.pack()
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA:")
            l.pack()
            c = tk.Checkbutton(root3, text="JANGGAR TRAIN (12:20 p.m.)", command=harga)
            c.pack()
            c1 = tk.Checkbutton(root3, text="PRABRORO CHAMP (13:30 p.m.)", command=harga)
            c1.pack()
        
        def sore():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Sore")
            
            def harga():
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                
                def konfirmasi():
                    messagebox.showinfo("SELAMAT", "TIKET ANDA TELAH DIPESAN")
                
                l = Label(root4, text="Harga Tiket Anda : Rp.10.000")
                l.pack()
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA:")
            l.pack()
            c = tk.Checkbutton(root3, text="MUST A NICE EXPRESS (16:15 p.m.)", command=harga)
            c.pack()
        
        def malam():
            root2.destroy()
            root3 = tk.Toplevel(root)
            root3.title("Pilih Kereta Malam")
            
            def harga():
                root3.destroy()
                root4 = tk.Toplevel(root)
                root4.title("Harga Tiket")
                
                def konfirmasi():
                    messagebox.showinfo("SELAMAT", "TIKET ANDA TELAH DIPESAN")
                
                l = Label(root4, text="Harga Tiket Anda : Rp.10.000")
                l.pack()
                b = Button(root4, text="TEKAN UNTUK KONFIRMASI", command=konfirmasi)
                b.pack()
            
            l = Label(root3, text="KERETA YANG TERSEDIA:")
            l.pack()
            c = tk.Checkbutton(root3, text="JANGGAR TRAIN (20:00 P.M.)", command=harga)
            c.pack()
        
        l3 = Label(root2, text="PILIH WAKTU KEBERANGKATAN:")
        l3.pack()
        b2 = Button(root2, text="Keberangkatan Pagi", command=pagi)
        b2.pack()
        b3 = Button(root2, text="Keberangkatan Siang", command=siang)
        b3.pack()
        b4 = Button(root2, text="Keberangkatan Sore", command=sore)
        b4.pack()
        b5 = Button(root2, text="Keberangkatan Malam", command=malam)
        b5.pack()
        b6 = Button(root2, text='EXIT', bg='red', command=root2.destroy)
        b6.pack()
    
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
    root1=tk.Toplevel()
    def show():
        root1.destroy()
        root2=tk.Toplevel()
        def pagi():
            root2.destroy()
            root3=tk.Toplevel()
            def bisnis():
                root3.destroy()
                root4=tk.Toplevel()
                def hargaakhir():
                    harga="Rp 25.000"
                    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv', mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["harga ticket"])
                         writer.writerow([harga])
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                    messagebox.showinfo("PEMBERITAHUAN", "Silahkan lanjut ke menu pembayaran")
                  
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=hargaakhir).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=hargaakhir).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=hargaakhir).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=hargaakhir).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=hargaakhir).grid(row=1, column=2)
                Button(root4, text="Kursi 06", command=hargaakhir).grid(row=2, column=2)
                Button(root4, text="Kursi 07", command=hargaakhir).grid(row=3, column=2)
                Button(root4, text="Kursi 08", command=hargaakhir).grid(row=4, column=2)
                b = Button(root4, text="NEXT").grid(row=6, column=1)
                b.grid(row=3, column=0, columnspan=5)
                
                root4.mainloop()
            def eksekutif():
                root4=tk.Toplevel()
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
                root4=tk.Toplevel()
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
                b = Button(root4, text="NEXT").grid(row=9, column=2)
                b.grid(row=3, column=0, columnspan=5)
                
                root4.mainloop()

            l=Label(root3,text="PILIH KELAS").pack()
            c1=tk.Checkbutton(root3,text="Bisnis(+Rp. 15.000)",command=bisnis).pack()
            c2=tk.Checkbutton(root3,text="Eksekutif(+Rp. 10.000)",command=eksekutif).pack()
            c3=tk.Checkbutton(root3,text="Ekonomi(+Rp. 5.000)",command=ekonomi).pack()
            root3.mainloop()
        def siang():
            root3=tk.Toplevel()
            def bisnis():
                root3.destroy()
                root4=tk.Toplevel()
                def hargaakhir():
                    harga="Rp 25.000"
                    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv', mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["harga ticket"])
                         writer.writerow([harga])
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                    messagebox.showinfo("PEMBERITAHUAN", "Silahkan lanjut ke menu pembayaran")
                  
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=hargaakhir).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=hargaakhir).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=hargaakhir).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=hargaakhir).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=hargaakhir).grid(row=1, column=2)
                Button(root4, text="Kursi 06", command=hargaakhir).grid(row=2, column=2)
                Button(root4, text="Kursi 07", command=hargaakhir).grid(row=3, column=2)
                Button(root4, text="Kursi 08", command=hargaakhir).grid(row=4, column=2)
                b = Button(root4, text="NEXT").grid(row=6, column=1)
                b.grid(row=3, column=0, columnspan=5)
                  
                root4.mainloop()
            def eksekutif():
                root4=tk.Toplevel()
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
                root4=tk.Toplevel()
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
                b = Button(root4, text="NEXT").grid(row=9, column=2)
                b.grid(row=3, column=0, columnspan=5)
                
                root4.mainloop()

            l=Label(root3,text="PILIH KELAS").pack()
            c1=tk.Checkbutton(root3,text="Bisnis(+Rp. 15.000)",command=bisnis).pack()
            c2=tk.Checkbutton(root3,text="Eksekutif(+Rp. 10.000)",command=eksekutif).pack()
            c3=tk.Checkbutton(root3,text="Ekonomi(+Rp. 5.000)",command=ekonomi).pack()
            root3.mainloop()
        def sore():
            root3=tk.Toplevel()
            def bisnis():
                root3.destroy()
                root4=tk.Toplevel()
                def hargaakhir():
                    harga="Rp 25.000"
                    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv', mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["harga ticket"])
                         writer.writerow([harga])
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                    messagebox.showinfo("PEMBERITAHUAN", "Silahkan lanjut ke menu pembayaran")
                  
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=hargaakhir).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=hargaakhir).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=hargaakhir).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=hargaakhir).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=hargaakhir).grid(row=1, column=2)
                Button(root4, text="Kursi 06", command=hargaakhir).grid(row=2, column=2)
                Button(root4, text="Kursi 07", command=hargaakhir).grid(row=3, column=2)
                Button(root4, text="Kursi 08", command=hargaakhir).grid(row=4, column=2)
                b = Button(root4, text="NEXT").grid(row=6, column=1)
                b.grid(row=3, column=0, columnspan=5)
                
                root4.mainloop()
            def eksekutif():
                root4=tk.Toplevel()
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
                root4=tk.Toplevel()
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
                b = Button(root4, text="NEXT").grid(row=9, column=2)
                b.grid(row=3, column=0, columnspan=5)
                
                root4.mainloop()
            l=Label(root3,text="PILIH KELAS").pack()
            c1=tk.Checkbutton(root3,text="Bisnis(+Rp. 15.000)",command=bisnis).pack()
            c2=tk.Checkbutton(root3,text="Eksekutif(+Rp. 10.000)",command=eksekutif).pack()
            c3=tk.Checkbutton(root3,text="Ekonomi(+Rp. 5.000)",command=ekonomi).pack()
            root3.mainloop()
        def malam():
            root3=tk.Toplevel()
            def bisnis():
                root3.destroy()
                root4=tk.Toplevel()
                def hargaakhir():
                    harga="Rp 25.000"
                    with open(r'Project-17-Kereta-Sinchan-Solo-Raya\Progress\database_pembayaran.csv', mode='w', newline='') as file:
                         writer = csv.writer(file)
                         writer.writerow(["harga ticket"])
                         writer.writerow([harga])
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                    messagebox.showinfo("PEMBERITAHUAN", "Silahkan lanjut ke menu pembayaran")
                  
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=hargaakhir).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=hargaakhir).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=hargaakhir).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=hargaakhir).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=hargaakhir).grid(row=1, column=2)
                Button(root4, text="Kursi 06", command=hargaakhir).grid(row=2, column=2)
                Button(root4, text="Kursi 07", command=hargaakhir).grid(row=3, column=2)
                Button(root4, text="Kursi 08", command=hargaakhir).grid(row=4, column=2)
                b = Button(root4, text="NEXT").grid(row=6, column=1)
                b.grid(row=3, column=0, columnspan=5)
                
                root4.mainloop()
            def eksekutif():
                root4=tk.Toplevel()
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
                root4=tk.Toplevel()
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
                b = Button(root4, text="NEXT").grid(row=9, column=2)
                b.grid(row=3, column=0, columnspan=5)
                
            l=Label(root3,text="PILIH KELAS").pack()
            c1=tk.Checkbutton(root3,text="Bisnis(+Rp. 15.000)",command=bisnis).pack()
            c2=tk.Checkbutton(root3,text="Eksekutif(+Rp. 10.000)",command=eksekutif).pack()
            c3=tk.Checkbutton(root3,text="Ekonomi(+Rp. 5.000)",command=ekonomi).pack()
            root3.mainloop()
        l3=Label(root2,text="PILIH KELAS DAN KURSI:").pack()
        b2=Button(root2,text="KEBERANGKATAN PAGI",command=pagi).pack()
        b3=Button(root2,text="KEBERANGKATAN SIANG",command=siang).pack()
        b4=Button(root2,text="KEBERANGKATAN SORE",command=sore).pack()
        b5=Button(root2,text="KEBERANGKATAN MALAM",command=malam).pack()
        b6=Button(root2,text='EXIT',bg='red',command=root1.quit).pack()
        root2.mainloop()
    l2=Label(root1,text="PILIH RUTE KEBERANGKATAN").pack()
    routes = ["SOLO - WONOGIRI", "SOLO - SRAGEN", "SOLO - KARANGANYAR", "SOLO - BOYOLALI", "SOLO - KLATEN", "WONOGIRI - KARANGANYAR", "WONOGIRI - SRAGEN",
              "WONOGIRI - BOYOLALI","KARANGANYAR - SRAGEN", "KARANGANYER - BOYOLALI", "KARANGANYAR - KLATEN "]
    route_combobox = ttk.Combobox(root1, values=routes)
    route_combobox.pack(pady=10)


    b6 = Button(root1, text='NEXT', command=show)
    b6.pack()
    b7 = Button(root1, text='EXIT', bg='red', command=root1.destroy)
    b7.pack()



def pembayaran():
    subprocess.Popen(["python", "Project-17-Kereta-Sinchan-Solo-Raya\\Progress\\pembayaran.py"])


image_path = r'Project-17-Kereta-Sinchan-Solo-Raya\Kereta Sinchan Home Page.png'
original_image = Image.open(image_path)
resized_image = original_image.resize((1200, 650), Image.Resampling.LANCZOS)
im = ImageTk.PhotoImage(resized_image)


i = Label(root, image=im)  
i.image = im  
i.place(x=0, y=50) 


# Modify the buttons to include an icon image
button_continue = Button(root, text="Booking Tiket", bg='orange', font=("Arial", 12), compound="left", command=starter)
button_continue.place(x=220, y=290, width=150, height=50) 

b = Button(root, text="Pilih Kelas", bg='light green', font=("Arial", 12), compound="left", command=kelas)
b.place(x=420, y=290, width=150, height=50)  

b1 = Button(root, text="Pembayaran", bg='light blue', font=("Arial", 12), compound="left", command=pembayaran)
b1.place(x=620, y=290, width=150, height=50)  

button_quit = Button(root, text='EXIT', bg='red', font=("Arial", 12), compound="left", command=root.quit)
button_quit.place(x=820, y=290, width=150, height=50)  

root.mainloop()

