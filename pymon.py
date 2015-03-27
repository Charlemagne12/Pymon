##Importation des modules

from tkinter import * #Interface
from random import * #Aleatoire

##Définitions des fonctions permettant de définir l'OS de l'utilisateur
def OSchosenWin():
    OSWin=True
    return OSWin
    
def OSchosenUnix():
    OSWin=False
    return OSWin

##Définition du launcher

#Définition d'une fenêtre qui demande a l'utilisateur son OS et adapte la librairie en fonction
def launch():
    
    #Définition de la fenêtre
    launcher=Tk()
    launcher.title("Pymon launcher")
    launcher.geometry("250x75")
    
    #Définition des boutons. Ils doivent prendre toute la fenêtre donc pack() est plus utile
    OSquestion=Label(launcher,text="Bienvenue dans Pymon ! Choisissez votre OS :",anchor=CENTER,justify=CENTER)
    OSquestion.pack(fill=BOTH)
    
    unixButton=Button(launcher,text="Windows",command=OSchosenWin and launcher.destroy)
    unixButton.pack(fill=BOTH)
    
    winButton=Button(launcher,text="UNIX",command=OSchosenUnix and launcher.destroy)
    winButton.pack(fill=BOTH)
    
    #Lancement du launcher
    launcher.mainloop()
    
    #Lancement du menu
    menu()

##Création de l'interface graphique du Menu principal

def menu():
    
    #Création de la fenêtre
    menuWindow=Tk()
    menuWindow.title("Pymon")
    menuWindow.geometry("350x290")
    
    #Création de chaque bouton
    title=Label(menuWindow,text="Bienvenue dans Pymon !",anchor=CENTER,justify=CENTER)
    title.pack(fill=BOTH)
    
    tuto=Button(menuWindow,text="Tutoriel")
    tuto.pack(fill=BOTH)
    
    lvs=Label(menuWindow,text="-=-=-=-=- Niveaux -=-=-=-=-",anchor=CENTER,justify=CENTER)
    lvs.pack(fill=BOTH)
    
    lv1=Button(menuWindow,text="Niveau 1")
    lv1.pack(fill=BOTH)
    
    lv2=Button(menuWindow,text="Niveau 2")
    lv2.pack(fill=BOTH)
    
    lv3=Button(menuWindow,text="Niveau 3")
    lv3.pack(fill=BOTH)
    
    danger=Label(menuWindow,text="!!!! DANGER !!!!",anchor=CENTER,justify=CENTER,fg="red")
    danger.pack(fill=BOTH)
    
    survival=Button(menuWindow,text="Survival !")
    survival.pack(fill=BOTH)
    
    separation=Label(menuWindow,text="-=-=-=-=-=-=-=-=-=-=-=-=-",anchor=CENTER,justify=CENTER)
    separation.pack(fill=BOTH)
    
    menuBest=Button(menuWindow,text="Meilleurs scores",command=bestScore)
    menuBest.pack(fill=BOTH)
    
    commands=Label(menuWindow,text="Touches : QSDFJKL",fg='grey')
    commands.pack(fill=BOTH)
    
    vide=Label(menuWindow,text="",anchor=CENTER,justify=CENTER)
    vide.pack(fill=BOTH)
    
    #Lancement de la fenêtre
    menuWindow.mainloop()
    
## Choix aléatoire d'un nombre puis d'une note

def note():
    note=['do.mp3','re.mp3','mi.mp3','fa.mp3','sol.mp3','la.mp3','si.mp3']
    clavier=['q','s','d','f','j','k','l']
    c=randrange(6)
    keyboard=clavier[c]
    
    #fin fonction programme - Début aide diagnostique
    
    print (c)
    print(note[c])
    print(keyboard)
    
    # Réponse de l'utilisateur
    
    r=input('donner la lettre correspondant à cett note : ')
    if keyboard==r :
        print('bravo')
    else :
        print('hiiinnn faux')

##Définition de la fonction codant pour les meilleurs scores du Survival

def bestScore():
    
    best=open("best.txt","r")
    highscore=best.readlines()
    
    displayHS=Tk()
    displayHS.title("Pymon - Meilleurs scores")
    
    phraseHS=Label(displayHS,text="Ceci sont les meilleurs scores obtenus par les joueurs sur le Survival :")
    phraseHS.pack(fill=BOTH)
    
    printHighscore=Listbox(displayHS)
    
    listHS=len(highscore)
    i=0
    
    for i in range(listHS):
        printHighscore.insert(i,highscore[i])
        i+=1
    printHighscore.pack(fill=BOTH)
    
    menuBack=Button(displayHS,text="Retour au menu",command=menu and displayHS.destroy)
    menuBack.pack(fill=BOTH)
    
    best.close()
    
    displayHS.mainloop()
    
########################
#Lancement du programme#
########################
launch()
