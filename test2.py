import pygame,sys

import os
from os import startfile
import moviepy.editor


from tkinter import *
def film():
    video = moviepy.editor.VideoFileClip("gesty2.mp4")
    video.preview()
# Create object
root = Tk()

# Adjust size
root.geometry("1700x1100")

# Add image file
bg = PhotoImage(file="background.png")

# Show image using label
label1 = Label(root, image=bg)
label1.place(x=-95, y=0)

label2 = Label(root, text="Dual Lipa",font=("Arial", 100), bg="Pink", fg="Black")
label2.pack(pady=200)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady=20)



# Funkcja, która zmienia kolor przycisku po najechaniu kursorem myszy
def on_enter(event):
    button.config(bg='lightgrey')
def on_enter2(event):
    button2.config(bg='lightgreen')


# Funkcja, która przywraca kolor przycisku po opuszczeniu myszy
def on_leave(event):
    button.config(bg='grey')

def on_leave2(event):
    button2.config(bg='green')

# Tworzenie przycisku
button = Button(root, text="Start", font=("Arial", 24), bg="grey", fg="white")
button2 = Button(root, text="Start", font=("Arial", 24), bg="green", fg="white",command=lambda:film())
settingButton=Button(root, text="Options",font=("Arial",24), bg="Black", fg="white", )
exitButton=Button(root, text="Exit",font=("Arial",24), bg="Black", fg="white",command=lambda:root.quit())

# Ustawienie pozycji przycisku w oknie
button.place(relx=0.76, rely=0.7, anchor=CENTER)
button2.place(relx=0.26, rely=0.7, anchor=CENTER)
settingButton.place(relx=0.5, rely=0.5, anchor=CENTER)
exitButton.place(relx=0.5, rely=0.7, anchor=CENTER)

# Dodanie funkcji do obsługi zdarzeń "najechanie myszą" i "opuszczenie myszy"
button.bind("<Enter>", on_enter)
button2.bind("<Enter>", on_enter2)

button.bind("<Leave>", on_leave)
button2.bind("<Leave>", on_leave2)

# Execute tkinter
root.mainloop()