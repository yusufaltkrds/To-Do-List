from customtkinter import *
from tkinter import messagebox
import PIL
from PIL import Image
from tkinter import *
import tkinter as tk


# tamamlandı fonksiyonu
def tamamlandi():
    if len(l_box.curselection()) > 0:  # eleman seçildiyse if bloguna girer
        index = l_box.curselection()[0]  # seçilen görevin index'i tutulur
        tamam = l_box.get(index)  # seçilen görevin text'i alınır
        if tamam[-2] == "✓":
            l_box.delete(index)  # görev silinir
            tamam = tamam[:-3]
            l_box.insert(index, tamam)  # seçilen göreviin text'ine ✓ işareti konur
        else:
            l_box.delete(index)  # görev silinir
            l_box.insert(index, tamam + "(✓)")  # seçilen göreviin text'ine ✓ işareti konur
        kaydet()  # işlem kaydedilir
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev seçiniz")  # görev seçilmediyse uyarı ekranı çıkar


# ekleme fonksiyonu
def ekle():
    try:
        if ent.get() == "":  # girilen bir görev yoksa hata fırlatılır
            raise ValueError("Lütfen geçerli bir görev giriniz")
        else:
            l_box.insert(tk.END, ent.get()[0].upper()+ent.get()[1:])  # girilen bir görev varsa listbox'a eklenir
            ent.delete(0, tk.END)  # entry temizlenir
            kaydet()  # işlem kaydedilir
    except ValueError as ex:
        messagebox.showerror("Uyarı", str(ex))  # fırlatılan hata varsa yakalar ve uyarı mesajı ekrana verilir


# silme fonksiyonu
def sil():
    if len(l_box.curselection()) > 0:  # eleman seçildiyse if bloguna girer
        index = l_box.curselection()[0]  # seçilen görevin index'i tutulur
        l_box.delete(index)  # görev silinir
        kaydet()  # işlem kaydedilir
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev seçiniz")  # görev seçilmediyse uyarı ekranı çıkar


# kaydetme fonksiyonu
def kaydet():
    f = open('gorevler.txt', 'w', encoding='utf-8')  # işlemlerin kaydolması için dosya açılır
    gorevler = l_box.get(0, tk.END)  # yapılan işlemlerin ardından listbox'taki veriler gorevler'e atanır
    f.writelines('\n'.join(gorevler))  # gorevler dosyaya satır satır yazılır
    f.close()  # dosya kapatılır






pencere = CTk()
pencere.title("To Do List")


pencere.geometry("300x450")
set_appearance_mode("dark")

to_do_font = CTkFont(family="Montserrat", size=25, weight="bold")

label = CTkLabel(pencere, text="    TO DO LİST", width=300, height=60,
                 font=to_do_font, fg_color="#6BA1B9", corner_radius=30, text_color="white")
label.place(x=150, y=30, anchor="center")
image = CTkImage(dark_image=PIL.Image.open("to-do.png"), size=(40, 40))
my_label = CTkLabel(pencere, image=image, text="", bg_color="#6BA1B9")
my_label.place(x=43, y=12)



ent_font = CTkFont(family="Tahoma", size=13, weight="normal")
ent = CTkEntry(pencere, fg_color="#d9d9d9", corner_radius=30, font=ent_font, text_color="black", width=190)
ent.place(x=103, y=90, anchor="center")

ekle_buton = CTkButton(pencere, text="Görev Ekle", corner_radius=32, fg_color="transparent",
                       hover_color="#325666", border_color="#6BA1B9", border_width=2, command=ekle, width=50, height=35)
ekle_buton.place(x=248, y=89, anchor="center")

l_font = CTkFont(family="Century Gothic", size=18, weight="bold")

l_box = Listbox(pencere, width=33, height=12, bg="#2B4955", relief="groove", bd=7, font=l_font, fg="white")
l_box.place(x=190, y=300, anchor="center")

photo = CTkImage(dark_image=PIL.Image.open("tik.png"), size=(40, 40))

tamamlandi_buton = CTkButton(pencere, text="", corner_radius=32, fg_color="transparent",
                             hover_color="#325666", border_color="#6BA1B9", border_width=2, command=tamamlandi,
                             width=50, height=40,image=photo)

tamamlandi_buton.place(x=85, y=400, anchor="center")


photo2 = CTkImage(dark_image=PIL.Image.open("bin.png"), size=(40, 40))

sil_buton = CTkButton(pencere, text="", corner_radius=32, fg_color="transparent",
                      hover_color="#325666", border_color="#6BA1B9", border_width=2, command=sil, width=50, height=40, image=photo2)
sil_buton.place(x=215, y=400, anchor="center")










f = open('gorevler.txt', 'r', encoding='utf-8')  # dosya okunmak için açılır
gorevler = f.readlines()  # satırlar tek tek okunur, okunan satırlar gorevler'e atanır
l_box.delete(0, tk.END)  # listbox temizlenir
for gorev in gorevler:  # gorev, gorevler'in satırlarını gezer
    if '\n' in gorev:  # \n varsa atılır
        gorev = gorev.replace('\n', '')
    l_box.insert(tk.END, gorev)
pencere.mainloop()
