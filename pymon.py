##Importation des modules

from tkinter import * #Interface

##Création de l'interface graphique du Menu principal

def menu():
    
    #Création de la fenêtre
    menu=Tk()
    menu.title("Pymon")
    menu.geometry("500x300")
    
    #Création de chaque bouton
    title=Label(menu,text="Bienvenue dans Pymon !",anchor=CENTER,justify=CENTER)
    title.grid(sticky=N+S+E+W,row=1,column=2,columnspan=3)
    
    tuto=Button(menu,text="Tutoriel")
    tuto.grid(sticky=N+S+E+W,row=3,column=2,columnspan=3)
    
    lv1=Button(menu,text="Niveau 1")
    lv1.grid(sticky=N+S+E+W,row=5,column=2,columnspan=3)
    
    lv2=Button(menu,text="Niveau 2")
    lv2.grid(sticky=N+S+E+W,row=6,column=2,columnspan=3)
    
    lv3=Button(menu,text="Niveau 3")
    lv3.grid(sticky=N+S+E+W,row=7,column=2,columnspan=3)
    
    survival=Button(menu,text="Survival !")
    survival.grid(sticky=N+S+E+W,row=9,column=2,columnspan=3)
    
    menuBest=Button(menu,text="Meilleurs scores",command=bestScore)
    menuBest.grid(sticky=N+S+E+W,row=11,column=2,columnspan=3)
    
    settings=Button(menu,text="Paramètres")
    settings.grid(sticky=N+S+E+W,row=13,column=2,columnspan=3)
    
    commands=Label(menu,text="Touches : QSDFJKLM",fg='grey')
    commands.grid(sticky=S+W,row=15,column=1)
    
    #Lancement de la fenêtre
    menu.mainloop()

##Définition de la fonction codant pour les meilleurs scores du Survival

def bestScore():
    best=open("best.txt","r")
    highscore=best.readlines()
    print("Ceci sont les meilleurs scores obtenus par les joueurs sur le Survival")
    print(highscore)
    
##Lancement du programme

menu()
