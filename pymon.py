##Importation des modules

from tkinter import * #Interface

##Définitions des fonctions permettant de définir l'OS de l'utilisateur
def OSchosenWin():
    OSWin=True
    return OSWin
    
def OSchosenUnix():
    OSWin=False
    return OSWin

##Création de l'interface graphique du Menu principal

def menu():
    
    #Création de la fenêtre
    menu=Tk()
    menu.title("Pymon")
    menu.geometry("350x290")
    
    #Création de chaque bouton
    title=Label(menu,text="Bienvenue dans Pymon !",anchor=CENTER,justify=CENTER)
    title.pack(fill=BOTH)
    
    tuto=Button(menu,text="Tutoriel")
    tuto.pack(fill=BOTH)
    
    lvs=Label(menu,text="-=-=-=-=- Niveaux -=-=-=-=-",anchor=CENTER,justify=CENTER)
    lvs.pack(fill=BOTH)
    
    lv1=Button(menu,text="Niveau 1")
    lv1.pack(fill=BOTH)
    
    lv2=Button(menu,text="Niveau 2")
    lv2.pack(fill=BOTH)
    
    lv3=Button(menu,text="Niveau 3")
    lv3.pack(fill=BOTH)
    
    danger=Label(menu,text="!!!! DANGER !!!!",anchor=CENTER,justify=CENTER,fg="red")
    danger.pack(fill=BOTH)
    
    survival=Button(menu,text="Survival !")
    survival.pack(fill=BOTH)
    
    separation=Label(menu,text="-=-=-=-=-=-=-=-=-=-=-=-=-",anchor=CENTER,justify=CENTER)
    separation.pack(fill=BOTH)
    
    menuBest=Button(menu,text="Meilleurs scores",command=bestScore)
    menuBest.pack(fill=BOTH)
    
    settings=Button(menu,text="Paramètres")
    settings.pack(fill=BOTH)
    
    commands=Label(menu,text="Touches : QSDFJKLM",fg='grey')
    commands.pack(fill=BOTH)
    
    vide=Label(menu,text="",anchor=CENTER,justify=CENTER)
    vide.pack(fill=BOTH)
    
    #Lancement de la fenêtre
    menu.mainloop()

##Définition de la fonction codant pour les meilleurs scores du Survival

def bestScore():
    
    best=open("best.txt","r")
    highscore=best.readlines()
    
    displayHS=Tk()
    
    phraseHS=Label(displayHS,text="Ceci sont les meilleurs scores obtenus par les joueurs sur le Survival :")
    phraseHS.pack(fill=BOTH)
    
    printHighscore=Listbox(displayHS)
    
    listHS=len(highscore)
    i=1
    
    while i<=listHS:
        printHighscore.insert(i,highscore[i])
        i+=1
    printHighscore.pack(fill=BOTH)
    
    displayHS.mainloop()
    
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

#Lancement du programme
launch()
