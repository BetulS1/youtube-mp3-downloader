from tkinter import *  
import tkinter as tk 
from pytube import YouTube 
import os
# -*- coding:utf-8 -*-
#** Gerekli kütüphaneler :  pip install tk ve pip install pytube *#

def MP3_download():
    stream = YouTube(str(link.get())) #link 
    stream = stream.streams.filter(only_audio=True).first()
    out_file= stream.download(output_path = str(file_url.get())) #indirme yapılacak dosya url
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(stream.title + " has been successfully downloaded.")
    Label(window, text=stream.title + " Mp3 Olarak İndirildi!.", bg='#66CDAA', font="arial 12", fg="#006400").place(x=200, y=210)
def refresh():
       window.destroy()
       exec(open(r"C:\Users\LENOVO\Desktop\mp3-downloader.py").read())   

#tkinter uı penceresi 
window=tk.Tk(className='Youtube MP3 Downloader') ##pencere başlığı
window.geometry("700x350") ##boyutu
window.configure(bg='#66CDAA')##pencere rengi
window.resizable(width=FALSE, height=FALSE) ##pecrenin boyutu kullanıcı tarafından değiştirilemez
#başlık 
Label(window, text="Youtube MP3 Downloader", font='san-serif 14 bold', bg= "#66CDAA", fg="#191970").place(x=220, y=25)
link = StringVar() 
Label(window, text=" Youtube Link", font='san-serif 10 bold').place(x=10, y=85)
#link giriş alanı input box
link_enter = Entry(window, width=70,  font='san-serif 11 ', textvariable=link).place(x=109, y=85)
Label(window, text="İndirme Konumu", font='san-serif 10 bold').place(x=10, y=162)
file_url = StringVar() 
#dosya yolu giriş alanı input box
url_enter = Entry(window, width=67,  font='san-serif 11 ', textvariable=file_url).place(x=129, y=163)
#indirme butonu
Button(window, text='Download', font='san-serif 12 ', bg='#00CED1' ,padx=2, activebackground = 'blue', activeforeground = 'white', command=lambda: MP3_download()).place(x=300, y=250)
Label(window, text="İndirme İşlemi İçin Lütfen Bekleyin!", bg='#66CDAA', font="arial 12", fg="#006400").place(x=220, y=300)
Button(window, text='Yenile', font='san-serif 12 ', bg='#00CED1' ,padx=2, activebackground = 'blue', activeforeground = 'white', command=lambda: refresh()).place(x=620, y=300)

window.mainloop()
