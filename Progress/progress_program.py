
import tkinter as tk
from tkinter import Label, Button, messagebox
from tkinter import ttk  # Import ttk for the Combobox
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

    # Combobox for route selection
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
                def satu():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def dua():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def tiga():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def empat():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def lima():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def enam():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def tujuh():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def delapan():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")    
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=satu).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=dua).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=tiga).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=empat).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=lima).grid(row=1, column=2)
                Button(root4, text="Kursi 06", command=enam).grid(row=2, column=2)
                Button(root4, text="Kursi 07", command=tujuh).grid(row=3, column=2)
                Button(root4, text="Kursi 08", command=delapan).grid(row=4, column=2)
                b = Button(root4, text="NEXT").grid(row=6, column=1)
                b.grid(row=3, column=0, columnspan=5)
                
                root4.mainloop()
            def eksekutif():
                root4=tk.Toplevel()
                def satu():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def dua():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def tiga():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def empat():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def lima():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def enam():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def tujuh():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def delapan():
                    root4.destroy()
                def sembilan():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def sepuluh():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def sebelas():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def duabelas():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def tigabelas():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def empatbelas():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def limabelas():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def enambelas():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def tujuhbelas():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def delapanbelas():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def sembilanbelas():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def duapuluh():
                    root4.destroy()
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                l = Label(root4, text="PILIH KURSI ANDA")
                l.grid(row=0, column=0, columnspan=5)
                Button(root4, text="Kursi 01", command=satu).grid(row=1, column=0)
                Button(root4, text="Kursi 02", command=dua).grid(row=2, column=0)
                Button(root4, text="Kursi 03", command=tiga).grid(row=3, column=0)
                Button(root4, text="Kursi 04", command=empat).grid(row=4, column=0)
                Button(root4, text="Kursi 05", command=lima).grid(row=5, column=0)
                Button(root4, text="Kursi 06", command=enam).grid(row=1, column=1)
                Button(root4, text="Kursi 07", command=tujuh).grid(row=2, column=1)
                Button(root4, text="Kursi 08", command=delapan).grid(row=3, column=1)
                Button(root4, text="Kursi 09", command=sembilan).grid(row=4, column=1)
                Button(root4, text="Kursi 10", command=sepuluh).grid(row=5, column=1)
                Button(root4, text="Kursi 11", command=sebelas).grid(row=1, column=3)
                Button(root4, text="Kursi 12", command=duabelas).grid(row=2, column=3)
                Button(root4, text="Kursi 13", command=tigabelas).grid(row=3, column=3)
                Button(root4, text="Kursi 14", command=empatbelas).grid(row=4, column=3)
                Button(root4, text="Kursi 15", command=limabelas).grid(row=5, column=3)
                Button(root4, text="Kursi 16", command=enambelas).grid(row=1, column=4)
                Button(root4, text="Kursi 17", command=tujuhbelas).grid(row=2, column=4)
                Button(root4, text="Kursi 18", command=delapanbelas).grid(row=3, column=4)
                Button(root4, text="Kursi 19", command=sembilanbelas).grid(row=4, column=4)
                Button(root4, text="Kursi 20", command=duapuluh).grid(row=5, column=4)
                b = Button(root4, text="NEXT").grid(row=6, column=2)
                b.grid(row=3, column=0, columnspan=5)
                
                root4.mainloop()
            def ekonomi():
                root4=tk.Toplevel()
                def satu():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def dua():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def tiga():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def empat():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def lima():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def enam():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def tujuh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def delapan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def sembilan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def sepuluh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")

                l=Label(root4,text="PILIH KURSI ANDA").pack()
                c1=tk.Checkbutton(root4,text="Kursi 01",command=satu).pack()
                c2=tk.Checkbutton(root4,text="Kursi 02",command=dua).pack()
                c3=tk.Checkbutton(root4,text="Kursi 03",command=tiga).pack()
                c4=tk.Checkbutton(root4,text="Kursi 04",command=empat).pack()
                c5=tk.Checkbutton(root4,text="Kursi 05",command=lima).pack()
                c6=tk.Checkbutton(root4,text="Kursi 06",command=enam).pack()
                c7=tk.Checkbutton(root4,text="Kursi 07",command=tujuh).pack()
                c8=tk.Checkbutton(root4,text="Kursi 08",command=delapan).pack()
                c9=tk.Checkbutton(root4,text="kursi 09",command=sembilan).pack()
                c10=tk.Checkbutton(root4,text="Kursi 10",command=sepuluh).pack()
                b=Button(root4,text="NEXT",command=next).pack()
                root4.mainloop()

            l=Label(root3,text="PILIH KELAS").pack()
            c1=tk.Checkbutton(root3,text="Bisnis(+Rp. 15.000)",command=bisnis).pack()
            c2=tk.Checkbutton(root3,text="Eksekutif(+Rp. 10.000)",command=eksekutif).pack()
            c3=tk.Checkbutton(root3,text="Ekonomi(+Rp. 5.000)",command=ekonomi).pack()
            root3.mainloop()
        def siang():
            root3=tk.Toplevel()
            def bisnis():
                root4=tk.Toplevel()
                def satu():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def dua():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def tiga():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def empat():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def lima():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def enam():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def tujuh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def delapan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def sembilan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def sepuluh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")

                l=Label(root4,text="PILIH KURSI ANDA").pack()
                c1=tk.Checkbutton(root4,text="Kursi 01",command=satu).pack()
                c2=tk.Checkbutton(root4,text="Kursi 02",command=dua).pack()
                c3=tk.Checkbutton(root4,text="Kursi 03",command=tiga).pack()
                c4=tk.Checkbutton(root4,text="Kursi 04",command=empat).pack()
                c5=tk.Checkbutton(root4,text="Kursi 05",command=lima).pack()
                c6=tk.Checkbutton(root4,text="Kursi 06",command=enam).pack()
                c7=tk.Checkbutton(root4,text="Kursi 07",command=tujuh).pack()
                c8=tk.Checkbutton(root4,text="Kursi 08",command=delapan).pack()
                c9=tk.Checkbutton(root4,text="kursi 09",command=sembilan).pack()
                c10=tk.Checkbutton(root4,text="Kursi 10",command=sepuluh).pack()
                b=Button(root4,text="NEXT",command=next).pack()
                root4.mainloop()
            def eksekutif():
                root4=tk.Toplevel()
                def satu():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def dua():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def tiga():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def empat():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def lima():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def enam():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def tujuh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def delapan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def sembilan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def sepuluh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                l=Label(root4,text="PILIH KURSI ANDA").pack()
                c1=tk.Checkbutton(root4,text="Kursi 01",command=satu).pack()
                c2=tk.Checkbutton(root4,text="Kursi 02",command=dua).pack()
                c3=tk.Checkbutton(root4,text="Kursi 03",command=tiga).pack()
                c4=tk.Checkbutton(root4,text="Kursi 04",command=empat).pack()
                c5=tk.Checkbutton(root4,text="Kursi 05",command=lima).pack()
                c6=tk.Checkbutton(root4,text="Kursi 06",command=enam).pack()
                c7=tk.Checkbutton(root4,text="Kursi 07",command=tujuh).pack()
                c8=tk.Checkbutton(root4,text="Kursi 08",command=delapan).pack()
                c9=tk.Checkbutton(root4,text="kursi 09",command=sembilan).pack()
                c10=tk.Checkbutton(root4,text="Kursi 10",command=sepuluh).pack()
                b=Button(root4,text="NEXT",command=next).pack()
                root4.mainloop()
            def ekonomi():
                root4=tk.Toplevel()
                def satu():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def dua():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def tiga():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def empat():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def lima():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def enam():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def tujuh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def delapan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def sembilan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def sepuluh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")

                l=Label(root4,text="PILIH KURSI ANDA").pack()
                c1=tk.Checkbutton(root4,text="Kursi 01",command=satu).pack()
                c2=tk.Checkbutton(root4,text="Kursi 02",command=dua).pack()
                c3=tk.Checkbutton(root4,text="Kursi 03",command=tiga).pack()
                c4=tk.Checkbutton(root4,text="Kursi 04",command=empat).pack()
                c5=tk.Checkbutton(root4,text="Kursi 05",command=lima).pack()
                c6=tk.Checkbutton(root4,text="Kursi 06",command=enam).pack()
                c7=tk.Checkbutton(root4,text="Kursi 07",command=tujuh).pack()
                c8=tk.Checkbutton(root4,text="Kursi 08",command=delapan).pack()
                c9=tk.Checkbutton(root4,text="kursi 09",command=sembilan).pack()
                c10=tk.Checkbutton(root4,text="Kursi 10",command=sepuluh).pack()
                b=Button(root4,text="NEXT",command=next).pack()
                root4.mainloop()

            l=Label(root3,text="PILIH KELAS").pack()
            c1=tk.Checkbutton(root3,text="Bisnis(+Rp. 15.000)",command=bisnis).pack()
            c2=tk.Checkbutton(root3,text="Eksekutif(+Rp. 10.000)",command=eksekutif).pack()
            c3=tk.Checkbutton(root3,text="Ekonomi(+Rp. 5.000)",command=ekonomi).pack()
            root3.mainloop()
        def sore():
            root3=tk.Toplevel()
            def bisnis():
                root4=tk.Toplevel()
                def satu():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def dua():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def tiga():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def empat():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def lima():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def enam():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def tujuh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def delapan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def sembilan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def sepuluh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")

                l=Label(root4,text="PILIH KURSI ANDA").pack()
                c1=tk.Checkbutton(root4,text="Kursi 01",command=satu).pack()
                c2=tk.Checkbutton(root4,text="Kursi 02",command=dua).pack()
                c3=tk.Checkbutton(root4,text="Kursi 03",command=tiga).pack()
                c4=tk.Checkbutton(root4,text="Kursi 04",command=empat).pack()
                c5=tk.Checkbutton(root4,text="Kursi 05",command=lima).pack()
                c6=tk.Checkbutton(root4,text="Kursi 06",command=enam).pack()
                c7=tk.Checkbutton(root4,text="Kursi 07",command=tujuh).pack()
                c8=tk.Checkbutton(root4,text="Kursi 08",command=delapan).pack()
                c9=tk.Checkbutton(root4,text="kursi 09",command=sembilan).pack()
                c10=tk.Checkbutton(root4,text="Kursi 10",command=sepuluh).pack()
                b=Button(root4,text="NEXT",command=next).pack()
            def eksekutif():
                root4=tk.Toplevel()
                def satu():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def dua():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def tiga():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def empat():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def lima():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def enam():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def tujuh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def delapan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def sembilan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def sepuluh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                l=Label(root4,text="PILIH KURSI ANDA").pack()
                c1=tk.Checkbutton(root4,text="Kursi 01",command=satu).pack()
                c2=tk.Checkbutton(root4,text="Kursi 02",command=dua).pack()
                c3=tk.Checkbutton(root4,text="Kursi 03",command=tiga).pack()
                c4=tk.Checkbutton(root4,text="Kursi 04",command=empat).pack()
                c5=tk.Checkbutton(root4,text="Kursi 05",command=lima).pack()
                c6=tk.Checkbutton(root4,text="Kursi 06",command=enam).pack()
                c7=tk.Checkbutton(root4,text="Kursi 07",command=tujuh).pack()
                c8=tk.Checkbutton(root4,text="Kursi 08",command=delapan).pack()
                c9=tk.Checkbutton(root4,text="kursi 09",command=sembilan).pack()
                c10=tk.Checkbutton(root4,text="Kursi 10",command=sepuluh).pack()
                b=Button(root4,text="NEXT",command=next).pack()

            def ekonomi():
                root4=tk.Toplevel()
                def satu():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def dua():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def tiga():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def empat():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def lima():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def enam():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def tujuh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def delapan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def sembilan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def sepuluh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")


                l=Label(root4,text="PILIH KURSI ANDA").pack()
                c1=tk.Checkbutton(root4,text="Kursi 01",command=satu).pack()
                c2=tk.Checkbutton(root4,text="Kursi 02",command=dua).pack()
                c3=tk.Checkbutton(root4,text="Kursi 03",command=tiga).pack()
                c4=tk.Checkbutton(root4,text="Kursi 04",command=empat).pack()
                c5=tk.Checkbutton(root4,text="Kursi 05",command=lima).pack()
                c6=tk.Checkbutton(root4,text="Kursi 06",command=enam).pack()
                c7=tk.Checkbutton(root4,text="Kursi 07",command=tujuh).pack()
                c8=tk.Checkbutton(root4,text="Kursi 08",command=delapan).pack()
                c9=tk.Checkbutton(root4,text="kursi 09",command=sembilan).pack()
                c10=tk.Checkbutton(root4,text="Kursi 10",command=sepuluh).pack()
                b=Button(root4,text="NEXT",command=next).pack()
                root4.mainloop()
            l=Label(root3,text="PILIH KELAS").pack()
            c1=tk.Checkbutton(root3,text="Bisnis(+Rp. 15.000)",command=bisnis).pack()
            c2=tk.Checkbutton(root3,text="Eksekutif(+Rp. 10.000)",command=eksekutif).pack()
            c3=tk.Checkbutton(root3,text="Ekonomi(+Rp. 5.000)",command=ekonomi).pack()
            root3.mainloop()
        def malam():
            root3=tk.Toplevel()
            def bisnis():
                root4=tk.Toplevel()
                def satu():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def dua():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def tiga():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def empat():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def lima():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def enam():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def tujuh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def delapan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def sembilan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")
                def sepuluh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 25.000")

                l=Label(root4,text="PILIH KURSI ANDA").pack()
                c1=tk.Checkbutton(root4,text="Kursi 01",command=satu).pack()
                c2=tk.Checkbutton(root4,text="Kursi 02",command=dua).pack()
                c3=tk.Checkbutton(root4,text="Kursi 03",command=tiga).pack()
                c4=tk.Checkbutton(root4,text="Kursi 04",command=empat).pack()
                c5=tk.Checkbutton(root4,text="Kursi 05",command=lima).pack()
                c6=tk.Checkbutton(root4,text="Kursi 06",command=enam).pack()
                c7=tk.Checkbutton(root4,text="Kursi 07",command=tujuh).pack()
                c8=tk.Checkbutton(root4,text="Kursi 08",command=delapan).pack()
                c9=tk.Checkbutton(root4,text="kursi 09",command=sembilan).pack()
                c10=tk.Checkbutton(root4,text="Kursi 10",command=sepuluh).pack()
                b=Button(root4,text="NEXT",command=next).pack()
            def eksekutif():
                root4=tk.Toplevel()
                def satu():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def dua():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def tiga():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def empat():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def lima():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def enam():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def tujuh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def delapan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def sembilan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")
                def sepuluh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 20.000")

                l=Label(root4,text="PILIH KURSI ANDA").pack()
                c1=tk.Checkbutton(root4,text="Kursi 01",command=satu).pack()
                c2=tk.Checkbutton(root4,text="Kursi 02",command=dua).pack()
                c3=tk.Checkbutton(root4,text="Kursi 03",command=tiga).pack()
                c4=tk.Checkbutton(root4,text="Kursi 04",command=empat).pack()
                c5=tk.Checkbutton(root4,text="Kursi 05",command=lima).pack()
                c6=tk.Checkbutton(root4,text="Kursi 06",command=enam).pack()
                c7=tk.Checkbutton(root4,text="Kursi 07",command=tujuh).pack()
                c8=tk.Checkbutton(root4,text="Kursi 08",command=delapan).pack()
                c9=tk.Checkbutton(root4,text="kursi 09",command=sembilan).pack()
                c10=tk.Checkbutton(root4,text="Kursi 10",command=sepuluh).pack()
                b=Button(root4,text="NEXT",command=next).pack()
                root4.mainloop()
            def ekonomi():
                root4=tk.Toplevel()
                def satu():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def dua():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def tiga():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def empat():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def lima():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def enam():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def tujuh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def delapan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def sembilan():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")
                def sepuluh():
                    messagebox.showinfo("PEMBERITAHUAN", "Harga Tiket Total Anda adalah Rp. 15.000")

                l=Label(root4,text="PILIH KURSI ANDA").pack()
                c1=tk.Checkbutton(root4,text="Kursi 01",command=satu).pack()
                c2=tk.Checkbutton(root4,text="Kursi 02",command=dua).pack()
                c3=tk.Checkbutton(root4,text="Kursi 03",command=tiga).pack()
                c4=tk.Checkbutton(root4,text="Kursi 04",command=empat).pack()
                c5=tk.Checkbutton(root4,text="Kursi 05",command=lima).pack()
                c6=tk.Checkbutton(root4,text="Kursi 06",command=enam).pack()
                c7=tk.Checkbutton(root4,text="Kursi 07",command=tujuh).pack()
                c8=tk.Checkbutton(root4,text="Kursi 08",command=delapan).pack()
                c9=tk.Checkbutton(root4,text="kursi 09",command=sembilan).pack()
                c10=tk.Checkbutton(root4,text="Kursi 10",command=sepuluh).pack()
                b=Button(root4,text="NEXT",command=next).pack()
                root4.mainloop()
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
    print("Pembayaran")

image_path = r'Kereta Sinchan Home Page.png'
original_image = Image.open(image_path)
resized_image = original_image.resize((1200, 600), Image.Resampling.LANCZOS)
im = ImageTk.PhotoImage(resized_image)

i = Label(root, image=im)
i.image = im  
i.place(x=0, y=50) 

# Modify the buttons to include an icon image
button_continue = Button(root, text="Booking Tiket", bg='cyan', font=("Arial", 12), compound="left", command=starter)
button_continue.place(x=100, y=500, width=150, height=50) 

b = Button(root, text="Pilih Kelas", bg='azure', font=("Arial", 12), compound="left", command=kelas)
b.place(x=300, y=500, width=150, height=50)  

b1 = Button(root, text="Pembayaran", bg='yellow', font=("Arial", 12), compound="left", command=pembayaran)
b1.place(x=500, y=500, width=150, height=50)  

button_quit = Button(root, text='EXIT', bg='red', font=("Arial", 12), compound="left", command=root.quit)
button_quit.place(x=700, y=500, width=150, height=50)  

root.mainloop()

