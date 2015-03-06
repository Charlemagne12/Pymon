##Importation des modules

from tkinter import * #Interface

##Création de l'interface graphique du Menu principal

def interfaceMenu():
    menu=Tk()
    menu.title("Pymon")
    menu.geometry("500x300")
    title=Label(menu,text="Bienvenue dans Pymon !",anchor=CENTER,justify=CENTER)
    title.grid(row=1,column=2,columnspan=3)
    tuto=Button(menu,text="Tutoriel")
    tuto.grid(row=3,column=2,columnspan=3)
    menu.mainloop()
    
interfaceMenu()

##Définition de la fonction codant pour les meilleurs scores du Survival

def bestScore():
    best=open("best.txt","r")
    highscore=best.readlines()
    highscore=highscore.split(';')
    print("Ceci sont les meilleurs scores obtenus par les joueurs sur le Survival")
    print(highscore)
