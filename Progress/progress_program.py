
import tkinter as tk
from tkinter import Label, Button, Checkbutton, messagebox
from tkcalendar import DateEntry  
from PIL import Image, ImageTk


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
            c = Checkbutton(root3, text="PRABRORO CHAMP (7:05 a.m.)", command=harga)
            c.pack()
            c1 = Checkbutton(root3, text="MUST A NICE EXPRESS (9:20 a.m.)", command=harga)
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
            c = Checkbutton(root3, text="JANGGAR TRAIN (12:20 p.m.)", command=harga)
            c.pack()
            c1 = Checkbutton(root3, text="PRABRORO CHAMP (13:30 p.m.)", command=harga)
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
            c = Checkbutton(root3, text="MUST A NICE EXPRESS (16:15 p.m.)", command=harga)
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
            c = Checkbutton(root3, text="JANGGAR TRAIN (20:00 P.M.)", command=harga)
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
    c1 = Checkbutton(root1, text="SOLO - WONOGIRI", command=show)
    c1.pack()
    c2 = Checkbutton(root1, text="SOLO - SRAGEN", command=show)
    c2.pack()
    c3 = Checkbutton(root1, text="SOLO - KARANGANYAR", command=show)
    c3.pack()
    c4 = Checkbutton(root1, text="SOLO - BOYOLALI", command=show)
    c4.pack()
    c5 = Checkbutton(root1, text="SOLO - KLATEN", command=show)
    c5.pack()
    b6 = Button(root1, text='EXIT', bg='red', command=root1.destroy)
    b6.pack()

def kelas():
    print("Kelas")

def pembayaran():
    print("Pembayaran")


image_path = r'kereta sinchan.png'
original_image = Image.open(image_path)
resized_image = original_image.resize((1200, 600), Image.Resampling.LANCZOS)
im = ImageTk.PhotoImage(resized_image)


i = Label(root, image=im)
i.image = im  
i.place(x=0, y=50) 


button_continue = Button(root, text="Booking Tiket", bg='cyan', font=("Arial", 12), command=starter)
button_continue.place(x=100, y=500, width=150, height=50) 

b = Button(root, text="Pilih Kelas", bg='azure', font=("Arial", 12), command=kelas)
b.place(x=300, y=500, width=150, height=50)  

b1 = Button(root, text="Pembayaran", bg='yellow', font=("Arial", 12), command=pembayaran)
b1.place(x=500, y=500, width=150, height=50)  

button_quit = Button(root, text='EXIT', bg='red', font=("Arial", 12), command=root.quit)
button_quit.place(x=700, y=500, width=150, height=50)  


root.mainloop()
