import os
from os import startfile
import random
import pygame
import sys
import subprocess
import moviepy.editor
import subprocess
from tkinter import *
from moviepy.editor import VideoFileClip
from moviepy import *
# import TkinterVideo
from tkinter import messagebox
import atexit
import subprocess
import sys

# funkcja wyświetlająca filmik za podaniem jego nazwy
import atexit
import subprocess
import sys






# funkcja wyświetlająca filmik za podaniem jego nazwy

def show_clip(filename):
    clip = moviepy.editor.VideoFileClip(filename)
    clip.preview()


# ta funkcja bierze za argument nazwe pliku tekstowego i pokazuje to, co w nim jest

def update_label(filename="empty.txt"):
    with open(filename, encoding='utf-8') as file:
        instruction_text = file.read()
    label1.config(text=instruction_text)
    label1.pack(pady=200)


#TA FUNKCJA MA 1.LOSOWAC NAZWY GESTOW 2.ODLICZAC SEKUNDY 3.ODPALAC FILMIKI  [I TO WSZYSTKO X3]





def play_video():
        clip = VideoFileClip("Testowegesty1.mp4")
        clip2=VideoFileClip("Testowegesty2.mp4")
        clip3=VideoFileClip("Testowegesty3.mp4")

        clip.preview()
        clip2.preview()
        clip3.preview()
        gui.destroy()




# ROBIE OKIENKO
gui = Tk(className='Badanie2023')
gui.geometry("1700x1100")
gui.configure(bg='white')


# ROBIE GUZIKI
button1 = Button(gui,text="Dalej", command=lambda: (screen2(),button1.destroy()), font=("Arial", 24), bg="grey", fg="black")
button2 = Button(gui,text="Dalej", command=lambda: (play_video(),button2.destroy()), font=("Arial", 24), bg="grey", fg="black")
button3 = Button(gui,text="Dalej", command=lambda: (button3.destroy()), font=("Arial", 24), bg="grey", fg="black")

# ROBIE LABEL
label1 = Label(gui, font=("Arial", 20), fg="Black")


def screen1():
    update_label("ins1.txt")
    button1.place(relx=0.5, rely=0.5, anchor=CENTER)


def screen2():
    update_label("ins2.txt")
    button2.place(relx=0.5, rely=0.5, anchor=CENTER)
def screen3():

        update_label("ins4.txt")
        button3.place(relx=0.5, rely=0.5, anchor=CENTER)


# tu sie zaczyna programu dzialanie
screen1()
gui.mainloop()




# Poniższa pętla while jest tylko do celów demonstracyjnych
import tkinter as tk
import time
from PIL import Image, ImageTk
import random

list = ["Like", "Przywitanie się", "Żółwik"]


def gest():
    try:
        x = random.randrange(0, len(list))
    except:
        return window.destroy()
    przechowaj = list[x]
    list.pop(x)
    return przechowaj


def start_countdown():
    button.config(state=tk.DISABLED)
    countdown(5)


def show_text(event):
    # Wyświetlanie tekstu "mleko" na środku ekranu
    button.config(state=tk.NORMAL)
    label.config(text=gest())
    label.config(image="")

    window.unbind("<space>")


def countdown(counter):
    if counter > 0:
        label.config(text=str(counter), font=('Helvatical bold', 80), )
        counter -= 1
        # Opóźnienie o 1 sekundę
        window.after(1000, countdown, counter)

    else:
        # Wyświetlanie obrazka "koniec.png"
        img = Image.open("zielonakropka.png")
        img = img.resize((1700, 1100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo

        window.bind("<space>", show_text)


window = tk.Tk()
window.title("Odliczanie")
window.geometry("1700x1100")
label = tk.Label(window,
                 text="Świetnie! Teraz Twoim zadaniem będzie odtworzenie zapamiętanych gestów.\n Po naciśnięnciu guzika poniżej, wyświetli Ci się funkcja.\n Twoim zadaniem  jest odtworzyć gest. \n Postaraj się trzymać ręce na wyskości kamery.\nCała sekwencja powtórzy się trzy razy \nPowodzenia!",
                 font=('Helvatical bold', 30))
label.pack()

button = tk.Button(window, text="Rozpocznij odliczanie", command=start_countdown)
# button.pack()
button1 = tk.Button(window, text="Dalej", command=lambda: (screen2()), font=("Arial", 24), bg="grey", fg="black")


def screen1():
    label.config(
        text="Świetnie! Teraz Twoim zadaniem będzie odtworzenie zapamiętanych gestów.\n Po naciśnięnciu guzika poniżej, wyświetli Ci się funkcja."
             "\n Twoim zadaniem  jest odtworzyć gest. "
             "\n Postaraj się trzymać ręce na wyskości kamery.\nCała sekwencja powtórzy się trzy razy. \n Powodzenia!", font=('Helvatical bold', 30))

    button1.pack()


def screen2():
    try:
        label.config(text=(gest()))
    except:
        lebel.config(text="Dziękujemy za wykonanie badania")

    button1.destroy()
    button.pack()


# Wywołanie funkcji odliczającej po 1 sekundzie
# window.after(1000, countdown, 5)
screen1()
window.mainloop()

list = ["Like", "Przywitanie się", "Żółwik"]


def gest():

    try:
        x = random.randrange(0, len(list))
    except:
        return window.destroy()

    przechowaj = list[x]
    list.pop(x)
    return przechowaj


def start_countdown():
    button.config(state=tk.DISABLED)
    countdown(5)


def show_text(event):
    # Wyświetlanie tekstu "mleko" na środku ekranu
    button.config(state=tk.NORMAL)
    label.config(text=gest())
    label.config(image="")

    window.unbind("<space>")


def countdown(counter):
    if counter > 0:
        label.config(text=str(counter), font=('Helvatical bold', 80), )
        counter -= 1
        # Opóźnienie o 1 sekundę
        window.after(1000, countdown, counter)

    else:
        # Wyświetlanie obrazka "koniec.png"
        img = Image.open("zielonakropka.png")
        img = img.resize((1700, 1100), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        label.config(image=photo)
        label.image = photo

        window.bind("<space>", show_text)


window = tk.Tk()
window.title("Odliczanie")
window.geometry("1700x1100")
label = tk.Label(window,
                 text="Świetnie! Teraz Twoim zadaniem będzie odtworzenie zapamiętanych gestów.\n Po naciśnięnciu guzika poniżej, wyświetli Ci się funkcja.\n Twoim zadaniem  jest odtworzyć gest. \n Postaraj się trzymać ręce na wyskości kamery.\nCała sekwencja powtórzy się trzy razy \nPowodzenia!",
                 font=('Helvatical bold', 30))
label.pack()

button = tk.Button(window, text="Rozpocznij odliczanie", command=start_countdown)
# button.pack()
button1 = tk.Button(window, text="Dalej", command=lambda: (screen2()), font=("Arial", 24), bg="grey", fg="black")


def screen1():
    label.config(
        text="Świetnie Ci poszło, teraz założymy Tobie rękawiczyki \n po czym powtórzysz zadanie \n Powodzenia! " ,font=('Helvatical bold', 30))

    button1.pack()


def screen2():
    try:
        label.config(text=(gest()))
    except:
        lebel.config(text="Dziękujemy za wykonanie badania")

    button1.destroy()
    button.pack()


# Wywołanie funkcji odliczającej po 1 sekundzie
# window.after(1000, countdown, 5)
screen1()
window.mainloop()
import tkinter as tk


def show_thanks():
    """Funkcja wywoływana po kliknięciu przycisku 'Podziękuj'."""
    # Wyświetl okno dialogowe z podziękowaniem
    thank_you_window = tk.Toplevel()
    thank_you_window.title("Podziękowanie")

    # Utwórz etykietę z podziękowaniem
    thank_you_label = tk.Label(thank_you_window, text="Dziękujemy za udział w badaniu!")
    thank_you_label.pack(padx=20, pady=20)

    # Utwórz przycisk Zamknij
    close_button = tk.Button(thank_you_window, text="Zamknij", command=thank_you_window.destroy)
    close_button.pack(pady=10)


# Utwórz główne okno aplikacji
root = tk.Tk()
root.title("Badanie")

# Utwórz etykietę z instrukcjami
instruction_label = tk.Label(root, text="Kliknij przycisk 'Podziękuj', aby zobaczyć podziękowanie.")
instruction_label.pack(padx=20, pady=20)

# Utwórz przycisk Podziękuj
thank_button = tk.Button(root, text="Podziękuj", command=show_thanks)
thank_button.pack(pady=10)

# Uruchom pętlę główną aplikacji
root.mainloop()
