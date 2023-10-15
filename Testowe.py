import tkinter as tk
from tkinter import font
import os
from tkVideoPlayer import TkinterVideo
import  random
import time

import sys
import moviepy.editor
from moviepy.editor import VideoFileClip
from moviepy import *
from tkinter import messagebox
import time
from PIL import Image, ImageTk

texts = ["Chwytanie obiektu", "Duplikowanie obiektu", "kierowanie wiązką", "klikniecie pewne",
         "klikniecie przycisku","like/serduszko","Następny element","Następny slajd","Obracanie"
         ,"Odesłanie na pierwotną pozycję","Odznaczenie opcji","otwarcie lewego panelu","otwarcie prawego panelu",
         "otwórz witulaną tablicę","otwórz tablice timeline","Pauza","Poprzednia Scena","Poprzedni element",
         "Przewijanie do dołu","Przewijanie w lewo","Przwijanie w prawo","Przwijanie do góry","Przyciąganie odleglego obiektu",
         "skalowanie","tapniecie przycisku","tworzenie dodatkowego obietku","usuniecie awatarów","usuwanie obiektu",
         "wyciszenie miktrofonu","wyciszenie wszystkich uczestników", "zamkniecie_panelu","zdalne usuniecie zaznaczenia",
         "zdalne zaznacznie"]
# texts = ["Chwytanie obiektu","Skalowanie obiektu","Obracanie obiektu"
#       ,"Kierowanie wiązką","Zdalne tapnięcie","Zdalne usunięcie zaznaczenia",
#       "Kliknięcie przycisku","Odznaczanie opcji","Kliknięcie przycisku (pewne)",
#         "Otwarcie lewego panelu","Otwarcie prawego panelu","Zamknięcie panelu","Pauza","Wyciszenie mikrofonu","Wyciszenie wszystkich \n uczestników",
#       'Usunięcie wszystkich awatarów',"Otwórz wirtualną tablicę","Otwórz panel timeline","Następny próg ","Poprzedni próg","Następna scena ","Poprzednia scena"
#       ,"Tworzenie/dodanie obiektu","Przyciąganie odległego obiektu","Odesłanie obiektu \n na pierwotną pozycję","Usuwanie obiektu ","Usuwanie obiektu ","Przewijanie zawartości w lewo,",
#       "Przewijanie zawartości w prawo","Przewijanie zawartości w górę ","Przewijanie zawartości w dół"]

folder="wilmy_test"


files = os.listdir(folder)
files = [file for file in files if os.path.isfile(os.path.join(folder, file))]
gest_index=0
path=folder
os.chdir(path)
strings=""
nazwa_pliku=""
plik = nazwa_pliku
def display_tur():
    label.pack(anchor="center", ipady=350)

    label.config(text=f"tura {count+1}",font=("Helvetica", "32"))
    label.after(2000,display_next_string)
plik=nazwa_pliku
def testo(): # ta funkcja nazywa plik tekstowy kodem badanego, ktory wprowadza sie na poczatku badania
    global nazwa_pliku

    os.chdir("D:\PycharmProjects\pythonProject3\Pilotaz_gesty")
    nazwa_pliku = entry_get_PrivC.get()
    nazwa_pliku=nazwa_pliku+".csv" #mozna zamiast csv zrobic txt jesli zajdzie potrzeba
    os.chdir(path)

    frame_get_private_code.destroy()
    frame_instuckja.pack()

def random_gestures(a):
    dictionary_of_gestures={}
    for count,value in enumerate(files):
        dictionary_of_gestures[texts[count]]=value

    resultList = new_list = list(map(list, dictionary_of_gestures.items()))
    lista_randomow=[]
    for i in range(3):
        random_list= random.sample(resultList, len(resultList))
        lista_randomow.append(random_list)

    return  lista_randomow[a]
#
count=0
current_index = 0
def do_tri_times():
    global count
    global strings
    if count ==1:
        strings = random_gestures(1)
        print(strings, " 1")
        display_tur()



    if count==2:
        strings = random_gestures(1)
        print(strings, " 2")
        display_tur()

    if count==3:
        screen1()

def display_white_screen():

    label.config(text="")
    label.after(2000,display_next_video)
def display_next_string():
    global count
    global current_index
    label.pack(anchor="center", ipady=350)

    if current_index < len(strings):
        # label.pack()
        label.config(text=strings[current_index][0],font=("Helvetica", "32") )
        label.after(2000,display_white_screen)
    else:
        count=count+1

        current_index=0


        do_tri_times()

def display_next_video():
    global current_index


    label.pack_forget()
    if current_index < len(strings):
        videoplayer = TkinterVideo(master=root, scaled=True)

        videoplayer.bind("<<Ended>>", lambda x: (videoplayer.destroy(), display_next_string()))
        videoplayer.load(rf"{strings[current_index][1]}")


        videoplayer.pack(expand=True, fill="both")

        videoplayer.play()  # play the video
        current_index += 1

texts_instukcje = ["Witaj! Przed Tobą badanie, które składać będzie się z dwóch części.\n Przed każdą z nich dostaniesz odpowiednie instrukcje."
    , "Za chwilę przed Tobą pojawią się nagrania gestów wraz z odpowiadającymi im nazwami funkcji. \n Po każdej nazwie nastąpi kilka sekund przerwy, po czym zobaczysz nagranie gestu tej funkcji. \nPostaraj się zapamiętać jak najwięcej gestów i odpowiadające im funkcje. \nWszystkie gesty zobaczysz 3 razy."]
ktory_tekst = 0
def change_text():
    global ktory_tekst
    if ktory_tekst!=1:
        print(ktory_tekst)
        ktory_tekst = (ktory_tekst + 1) % len(texts_instukcje)
        label_instrukcja.config(text=texts_instukcje[ktory_tekst])
    else:
        frame_instuckja.forget()


        strings=random_gestures(0)
        display_tur()




#

def switch_frame(active,where):
    active.forget()
    where.pack(expand=True, fill="both")
root = tk.Tk()
strings=random_gestures(0)

root.geometry("1700x1100")
frame_get_priv=tk.Frame(root)
#====================================================
# frame_gesty=tk.Frame(root)
label=tk.Label(root)
# # label.pack()



#====================================================#
frame_instuckja=tk.Frame(root)

initial_text = texts_instukcje[ktory_tekst]
label_font = font.Font(size=25)

label_instrukcja = tk.Label(frame_instuckja, text=initial_text,font=label_font,wraplength=1500)
label_instrukcja.pack(padx=20, pady=20)

# Tworzenie przycisku do zmiany tekstu
button_instukcja = tk.Button(frame_instuckja, text="Dalej",font=("Arial", 30), command=lambda :change_text())
button_instukcja.pack()

#====================================================#(root)
frame_get_private_code=tk.Frame(root)
frame_get_private_code.place(rely=0.5, relx=0.34)
label_wpisz_dane = tk.Label(frame_get_private_code, text="Wprowadź numer badanego:", font=("Arial", "30"))
label_wpisz_dane.pack()
entry_get_PrivC = tk.Entry(frame_get_private_code, font=('Arial, 24'))
entry_get_PrivC.pack()
button_get_PrivC = tk.Button(frame_get_private_code, text="Zatwierdź", font=("Arial", "30"),command= lambda:(testo()))
button_get_PrivC.pack(pady=10)

# display_tur()
lista_gestow=[]



# funkcja wyświetlająca filmik za podaniem jego nazwy
os.chdir("D:\PycharmProjects\pythonProject3\Pilotaz_gesty")





def text_from_txt(nazwa_pliku_z_dana_instrukcja):
    with open(nazwa_pliku_z_dana_instrukcja, encoding='utf-8') as file:
        instrukcja = file.read()
    return instrukcja


#TA FUNKCJA MA 1.LOSOWAC NAZWY GESTOW 2.ODLICZAC SEKUNDY 3.ODPALAC FILMIKI  [I TO WSZYSTKO X3]

def testo1(): # ta funkcja nazywa plik tekstowy kodem badanego, ktory wprowadza sie na poczatku badania
    global nazwa_pliku

    nazwa_pliku = entry_get_PrivC.get()
    nazwa_pliku=nazwa_pliku+".csv" #mozna zamiast csv zrobic txt jesli zajdzie potrzeba

    # screen1()







plik=nazwa_pliku

#
# with open("lista_gestow.txt", encoding='utf-8') as file:
#     s = file.read()
# list = s.split("\n")
# print(list)


list_to_show=["Chwytanie obiektu","Skalowanie obiektu","Obracanie obiektu"
      ,"Kierowanie wiązką","Zdalne tapnięcie","Zdalne usunięcie zaznaczenia",
      "Kliknięcie przycisku","Odznaczanie opcji","Kliknięcie przycisku (pewne)",
        "Otwarcie lewego panelu","Otwarcie prawego panelu","Zamknięcie panelu","Pauza","Wyciszenie mikrofonu","Wyciszenie wszystkich \n uczestników",
      'Usunięcie wszystkich awatarów',"Otwórz wirtualną tablicę","Otwórz panel timeline","Następny próg ","Poprzedni próg","Następna scena ","Poprzednia scena"
      ,"Tworzenie/dodanie obiektu","Przyciąganie odległego obiektu","Odesłanie obiektu \n na pierwotną pozycję","Usuwanie obiektu ","Usuwanie obiektu ","Przewijanie zawartości w lewo,",
      "Przewijanie zawartości w prawo","Przewijanie zawartości w górę ","Przewijanie zawartości w dół"]

lista_gestow=[]



current_time=0

def get_current_time():
    global current_time

    current_time = time.strftime("%Y-%m-%d %H:%M:%S")

    with open(nazwa_pliku, "a") as file:
        file.write(current_time + "\n") #trzecia kolumna w pliku: drugi czas



new_time=0
def get_new_time():
    global new_time

    new_time = time.strftime("%Y-%m-%d %H:%M:%S")
    # ile=current_time-new_time
    with open(nazwa_pliku, "a") as file:
        file.write(new_time + ",") # druga kolumna w pliku: pierwszy czas
        # file.write(current_time-new_time)

def gest():
    x = random.randrange(0, len(list_to_show))
    przechowaj = list_to_show[x]
    list_to_show.pop(x)

    lista_gestow.append(przechowaj)

    with open(nazwa_pliku, "a") as file:
        file.write(przechowaj+",") # pierwsza kolumna pliku danych: nazwa gestu
    return przechowaj


def start_countdown():
    button.config(state=tk.DISABLED)
    countdown(3)
    get_current_time()

def show_text(event):
    button.config(state=tk.NORMAL)
    fake_label.config(text=gest())
    fake_label.config(image="")
    new_time()



def countdown(counter):
    if counter > 0:
        fake_label.config(text=str(counter),font=("Arial", 50), fg="Black")
        counter -= 1

        # print(counter)
        root.after(1000, countdown, counter)

    elif counter>-5:
        # Wyświetlanie obrazka "koniec.png"

        img = Image.open("zielonkakropka2.png")
        img = img.resize((1700, 1100), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        counter -= 1
        fake_label.config(image=photo)
        fake_label.image = photo
        # print(counter)
        root.after(1000, countdown, counter)

    elif counter > -7:
        img2 = Image.open("szarakropka.png")
        img2 = img2.resize((1700, 1100), Image.LANCZOS)
        photo2 = ImageTk.PhotoImage(img2)
        counter -= 1
        root.after(1000, countdown, counter)



        def change_img():

            fake_label.configure(image=photo2)
            fake_label.image = photo2

        change_img()


    else:
        button.config(state=tk.NORMAL)
        a=gest()
        fake_label.config(text=a)

        fake_label.config(image="")
        get_new_time()



# label = label1
label = tk.Label(root, font=("Arial", 20), fg="Black")
label.pack()
frame_dalsze=tk.Frame(root)
button = tk.Button(root, text="Rozpocznij odliczanie", command=start_countdown, font=("Arial", 24), bg="grey", fg="black")
# button.pack()
button1 = tk.Button(frame_dalsze,text="Dalej", command=lambda: screen3(), font=("Arial", 24), bg="grey", fg="black")
button3 = tk.Button(frame_dalsze,text="Zaczynamy", command=lambda: screen2(), font=("Arial", 24), bg="grey", fg="black")
fake_label = tk.Label(frame_dalsze, text=text_from_txt("ins4.txt"), font=("Arial", 14))


def screen1():
    os.chdir("D:\PycharmProjects\pythonProject3\Pilotaz_gesty")
    label.destroy()
    # label.config(text=text_from_txt("ins4.txt"),font=("Arial",14))
    frame_dalsze.pack( )
    fake_label.pack()
    button1.pack()


def screen3():
    button1.destroy()
    fake_label.config(text=text_from_txt("ins5.txt"),font=("Arial",16))
    button3.pack()
def screen2():
        fake_label.config(font=("Arial", 16), fg="Black")
        fake_label.config(text=(gest()))
        button3.destroy()
        button.pack()
        get_new_time()




current_time=0

root.mainloop()
















