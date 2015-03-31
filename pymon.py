##Petit message :
#Pymon (c) Antoine Bouquin et Quentin Albertone. Bienvenue dans le code source. Vous avez le droit de le modifier et/ou de le redistribuer en précisant que l'original vient de nous et sans le vendre. Merci.

#-------------- Nota bene :-----------------------
#Le programme est conçu pour tourner sous Windows et UNIX. Les tailles des fenêtres sont conçues pour avoir la dimension parfaite pour Windows 7/Aero désactivé. Ainsi, suivant l'OS/le thème, l'agencement peut ne pas être parfait. Cependant, cela est purement esthétique et n'affecte en rien le fonctionnement global du programme. Bon jeu !

##Importation des modules

from tkinter import * #Interface
from random import * #Aleatoire
from winsound import * #Lecture des sons

##Strings pour une couleur hexadécimale (purement esthétique, pour les boutons)
grisClair="#dedede"
grisFonce="#3d3d3d"
vertClair="#2fab3d"
jauneClair="#fffd47"
orangeClair="#ffab48"
rougeClair="#ff2e2e"
bleuClair="#5367ff"

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
    
    def launcherClose():   #Afin de fermer la fenêtre en ouvrant le menu, on doit définir une fonction codant pour ça, sinon on doit
        launcher.destroy() #coder la fermeture de la fenêtre en tant que commande sur le bouton, mais dans ce cas là, le menu doit s'ouvrir
        menu()             #en fin de fonction car on ne peut pas mettre plus de deux commandes sur un bouton.
                           #On pouvait donc quitter le launcher sans choisir d'OS et le programme se lance quand même.
    
    #Définition des boutons. Ils doivent prendre toute la fenêtre donc pack() est plus utile
    OSquestion=Label(launcher,text="Bienvenue dans Pymon ! Choisissez votre OS :",anchor=CENTER,justify=CENTER)
    OSquestion.pack(fill=BOTH)
    
    unixButton=Button(launcher,text="Windows",command=OSchosenWin and launcherClose,bg="blue",activebackground=bleuClair) 
    unixButton.pack(fill=BOTH)                                                                 #Ainsi, l'utilisateur ne peut pas lancer le
                                                                                               #programme sans choisir d'OS. Il peut quitter
                                                                                               #le launcher, mais dans ce cas le programme
                                                                                               #s'arrête.
    winButton=Button(launcher,text="UNIX",command=OSchosenUnix and launcherClose,bg="orange",activebackground=orangeClair)
    winButton.pack(fill=BOTH)
    
    #Lancement du launcher
    launcher.mainloop()

##Création de l'interface graphique du Menu principal

def menu():
    
    #Création de la fenêtre
    menuWindow=Tk()
    menuWindow.title("Pymon")
    menuWindow.geometry("350x265")
    
    #Création de chaque bouton
    title=Label(menuWindow,text="Bienvenue dans Pymon !",anchor=CENTER,justify=CENTER)
    title.pack(fill=BOTH)
    
    tuto=Button(menuWindow,text="Tutoriel",bg="green",activebackground=vertClair)
    tuto.pack(fill=BOTH)
    
    lvs=Label(menuWindow,text="-=-=-=-=- Niveaux -=-=-=-=-",anchor=CENTER,justify=CENTER)
    lvs.pack(fill=BOTH)
    
    lv1=Button(menuWindow,text="Niveau 1",bg="yellow",activebackground=jauneClair)
    lv1.pack(fill=BOTH)
    
    lv2=Button(menuWindow,text="Niveau 2",bg="orange",activebackground=orangeClair)
    lv2.pack(fill=BOTH)
    
    lv3=Button(menuWindow,text="Niveau 3",bg="red",activebackground=rougeClair)
    lv3.pack(fill=BOTH)
    
    danger=Label(menuWindow,text="!!!! DANGER !!!!",anchor=CENTER,justify=CENTER,fg="red")
    danger.pack(fill=BOTH)
    
    survival=Button(menuWindow,text="Survival !",bg="black",fg="white",activebackground=grisFonce)
    survival.pack(fill=BOTH)
    
    separation=Label(menuWindow,text="-=-=-=-=-=-=-=-=-=-=-=-=-",anchor=CENTER,justify=CENTER)
    separation.pack(fill=BOTH)
    
    menuBest=Button(menuWindow,text="Meilleurs scores",command=bestScore,bg="grey",activebackground=grisClair)
    menuBest.pack(fill=BOTH)
    
    commands=Label(menuWindow,text="Touches : QSDFJKL",fg='grey')
    commands.pack(fill=BOTH)
    
    vide=Label(menuWindow,text="",anchor=CENTER,justify=CENTER)
    vide.pack(fill=BOTH)
    
    #Lancement de la fenêtre
    menuWindow.mainloop()
    
## Choix aléatoire d'un nombre puis d'une note

def note():
    note=['do.wav','re.wav','mi.wav','fa.wav','sol.wav','la.wav','si.wav'] #TODO : corriger les chemins
    clavier=['q','s','d','f','j','k','l']
    c=randrange(6)
    keyboard=clavier[c]
    winsound.PlaySound(note [c],winsound.SND_FILENAME)
    
    #fin fonction programme - Début aide diagnostique
    
    print (c)
    print(note[c])
    print(keyboard)
    
    # Réponse de l'utilisateur
    
    reponse=input('donner la lettre correspondant à cett note : ')
    if keyboard==r :
        print('bravo') #TODO : faire une fenêtre, c'est mieux
    else :
        print('hiiinnn faux')
    
    #TODO : ajouter dans la liste la touche et le son, histoire d'avoir la série de notes.

##Définition de la fonction codant pour les meilleurs scores du Survival

def bestScore():
    
    #Ouverture du fichier
    best=open("best.txt","r")
    highscore=best.readlines() #"highscore" est une liste qui compte chaque ligne comme un élément de la liste
    
    #Création de la fenêtre
    displayHS=Tk()
    displayHS.title("Pymon - Meilleurs scores")
    
    phraseHS=Label(displayHS,text="Ceci sont les meilleurs scores obtenus par les joueurs sur le Survival :")
    phraseHS.pack(fill=BOTH)
    
    #Création de la listbox pour afficher les scores
    printHighscore=Listbox(displayHS)
    
    listHS=len(highscore) #Définition de la variable correspondant a la longueur de la liste highscore
    i=0
    
    #Boucle pour afficher chaque élément de highscore dans la listbox
    for i in range(listHS):
        printHighscore.insert(i,highscore[i])
        i+=1
    printHighscore.pack(fill=BOTH)
    
    #Bouton de retour au menu
    menuBack=Button(displayHS,text="Retour au menu",command=menu and displayHS.destroy,bg="grey",activebackground=grisClair)
    menuBack.pack(fill=BOTH)
    
    #Fermeture du fichier
    best.close()
    
    #Lancement de la fenêtre
    displayHS.mainloop()
    
########################
#Lancement du programme#
########################
launch()
