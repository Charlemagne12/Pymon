##Petit message :
#Pymon (c) Antoine Bouquin et Quentin Albertone. Bienvenue dans le code source. Vous avez le droit de le modifier et/ou de le redistribuer en précisant que l'original vient de nous et sans le vendre. Merci.

#-------------- Nota bene :-----------------------
#Le programme est conçu pour tourner sous Windows et UNIX. Les tailles des fenêtres sont conçues pour avoir la dimension parfaite pour Windows 7/Aero désactivé. Ainsi, suivant l'OS/le thème, l'agencement peut ne pas être parfait. Cependant, cela est purement esthétique et n'affecte en rien le fonctionnement global du programme. Bon jeu !

##Importation des modules

from tkinter import * #Interface
from random import * #Aleatoire
import winsound #Lecture des sons
import pickle # Permet la fonction 'lock' et 'unlock'

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
    
    def launcherClose():
        launcher.destroy()
        menu()

#Afin de fermer la fenêtre en ouvrant le menu, on doit définir une fonction codant pour ça, sinon on doit
#coder la fermeture de la fenêtre en tant que commande sur le bouton, mais dans ce cas là, on doit mettre "menu()"
#en fin de fonction car on ne peut pas mettre plus de deux commandes sur un bouton.
#On pouvait donc quitter le launcher sans choisir d'OS et le menu se lance quand même.
    
    #Définition des boutons. Ils doivent prendre toute la fenêtre donc pack() est plus utile
    OSquestion=Label(launcher,text="Bienvenue dans Pymon ! Choisissez votre OS :",anchor=CENTER,justify=CENTER)
    OSquestion.pack(fill=BOTH)
    
    unixButton=Button(launcher,text="Windows",command=OSchosenWin and launcherClose,bg="blue",activebackground=bleuClair) 
    unixButton.pack(fill=BOTH)
    
#Ainsi, l'utilisateur ne peut pas lancer le programme sans choisir d'OS 
#(grâce a la fonction launcherClose que l'on vient de créer).
#Il peut quitter le launcher manuellement, mais dans ce cas le programme s'arrête.

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
    
    survivalScore=Button(menuWindow,text="Scores du Survival",command=survivalScoreFunc,bg="grey",activebackground=grisClair)
    survivalScore.pack(fill=BOTH)
    
    commands=Label(menuWindow,text="Touches : QSDFJKL",fg='grey')
    commands.pack(fill=BOTH)
    
    vide=Label(menuWindow,text="",anchor=CENTER,justify=CENTER)
    vide.pack(fill=BOTH)
    
    #Lancement de la fenêtre
    menuWindow.mainloop()
    
## Choix aléatoire d'un nombre puis d'une note



##Création de la fonction du déblocage des niveaux

def unlock():
    
    unlock=open("data/unlock.txt")
    checking=unlock.readlines()
    global unlockingStatus
    unlockingStatus=checking[1]+checking[2]+checking[3]

##Définition de la fonction codant pour les meilleurs scores du Survival

def survivalScoreFunc():
    
    #Ouverture du fichier
    survivalScore=open("data/survivalScore.txt","r")
    listScore=survivalScore.readlines() #"listScore" est une liste qui compte chaque ligne comme un élément de la liste
    
    #Création de la fenêtre
    displayScore=Tk()
    displayScore.title("Pymon - Scores du Survival")
    
    phraseScore=Label(displayScore,text="Ceci sont les scores obtenus par les joueurs sur le Survival :")
    phraseScore.pack(fill=BOTH)
    
    #Création de la listbox pour afficher les scores
    printScore=Listbox(displayScore)
    
    sizeListScore=len(listScore) #Définition de la variable correspondant a la longueur de la liste listScore
    i=0
    
    #Boucle pour afficher chaque élément de listScore dans la listbox
    for i in range(sizeListScore):
        printScore.insert(i,listScore[i])
    printScore.pack(fill=BOTH)
    
    #Bouton de retour au menu
    menuBack=Button(displayScore,text="Retour au menu",command=displayScore.destroy,bg="grey",activebackground=grisClair)
    menuBack.pack(fill=BOTH)
    
    #Fermeture du fichier
    survivalScore.close()
    
    #Lancement de la fenêtre
    displayScore.mainloop()
    
##Fenêtres de Game Over et de Level Complete

def gameOver():
    
    gameOverWindow=Tk()
    gameOverWindow.title("Pymon - Game Over !")
    
    gameOverMessage1=Label(gameOverWindow,text="-=-=-=-=-=- GAME OVER -=-=-=-=-=-",bg=rougeClair)
    gameOverMessage1.pack(fill=BOTH)
    
    gameOverMessage2=Label(gameOverWindow,text="Raté ! Vous n'avez pas rentré la bonne suite de notes.",bg=rougeClair)
    gameOverMessage2.pack(fill=BOTH)
    
def levelComplete():
    
    levelCompleteWindow=Tk()
    levelCompleteWindow.title("Pymon - Niveau réussi !")
    
    levelCompleteMessage1=Label(levelCompleteWindow,text="-=-=-=-=-=- LEVEL COMPLETE -=-=-=-=-=-",bg=vertClair)
    levelCompleteMessage1.pack(fill=BOTH)
    
    levelCompleteMessage2=Label(levelCompleteWindow,text="Vous avez réussi le niveau ! Félicitations ! Vous pouvez passer au suivant.",bg=vertClair)
    levelCompleteMessage2.pack(fill=BOTH)
    
########################
#Lancement du programme#
########################
launch()


############ Ajouts Quentin ##############

def note (nb): # Nombre de note à la fin du niveau
    NoteHistory=[] #Liste répertoriant les notes sortie
    KbHistory=[] #Liste répertoriant les keyboard sortie
    RepHistory=[] # Liste répertoriant les réponses utilisateur
    score=0 # Assez explicite 
    
    listNote=['do.wav','re.wav','mi.wav','fa.wav','sol.wav','la.wav','si.wav'] # Fichier audio pouvant sortir
    listKeyboard=['q','s','d','f','k','l','m'] # Lettres associés

    for i in range (nb): # suivant la difficulté changer le 3 #
    # Variable servant aux boucke while plus bas    
        sound=0
        check=0
       
    # Tire un nombre au hasard dans les liste de références plus haut et attribut une note à une touche et les 'stock' dans des list
        c=randrange(6)
        NoteHistory.append(listNote[c])
        KbHistory.append(listKeyboard[c])
    
    # Joue la liste des fichiers audios contenant les 'anciennes' et la nouvelle note
        while sound!=i+1 :
            print (NoteHistory[sound]) # A enlever aide au diagnostique #
            winsound.PlaySound(NoteHistory [sound],winsound.SND_FILENAME)
            sound=sound+1
        print(NoteHistory) # A enlever aide au diagnostique #
        print(KbHistory) # A enlever aide au diagnostique #
        
    # Demande une réponse à l'utilisateur que le prog met dans une liste
        RepHistory=list(input('donner la lettre correspondant à cett note : '))
        
    # Compare un à un les éléments des liste contenant la réponse de l'utilisateur et les réponses attendu
        while check!=i+1 : # Le décompte des points n'est pas au point 
            if KbHistory[check]==RepHistory[check] :
                print('bravo') # A enlever le bravo fait tache #
                score=score+100 # Attribution du score afin de débloquer les niveau suivants 
                check=check+1
            else :
                print ('hiiiinn faut')
                #créer une fenetre pour game over
                menu () # Fin du jeu à la moindre erreur car se jeu est pour les winners
    print ('Bravo vous avez fait un score de',score)




## le tuto
def tutoriel ():
    NoteHistory=[]
    KbHistory=[]
    RepHistory=[]
    
    print ("bonjour, vous voici dans le premier niveau du pymon,\n un niveau ô combien honorable dans se jeu de reconnaissance de                                   note, en effet c'est dans cette partie que vous apprendrez les bases avant d'ètre livré à vous même")
    print ("Pour commencer voyont ensemble à quelle sauce vous allé être mangé les notes à reconnaitre sont : do, re, mi, fa, sol, la, si et on respectivement comme lettres associé : q, s, d, f, j, k, l")
    print ("et bien commençons sans tarder")
    for c in range (6):
        listNote=['do.wav','re.wav','mi.wav','fa.wav','sol.wav','la.wav','si.wav']
        listTuto=['do','re','mi','fa','sol','la','si']
        listKeyboard=['q','s','d','f','j','k','l']
        winsound.PlaySound(listNote[c],winsound.SND_FILENAME)
        print (" la note jouée est un ",listTuto[c]," appuyé sur la touche ",listKeyboard[c])
    
    #fin fonction programme - Début aide diagnostique
    
        print (c)
    
    # Réponse de l'utilisateur
    
        reponse=input('donner la lettre correspondant à cett note : ')
        if listKeyboard[c]==reponse :
            print('bravo')
        else :
            print('hiiinnn faux')
        
    print ("Bon allé un petit récapitulatif :) on va faire toutes es note dans l'ordre ")
    for c in range (6):
        winsound.PlaySound(listNote[c],winsound.SND_FILENAME)
        NoteHistory.append(listNote[c])
        KbHistory.append(listKeyboard[c])
    
    RepHistory=list(input('donner la lettre correspondant à cett note : '))
    
    for j in range (6):
        if KbHistory[j]==RepHistory[j] :
            #print('bravo')
        else :
            print("hiiin faux je t'encourage à recommencer le tutoriel depuis le début")
            menu()
            #créer une fenetre pour game over
    print ('bravo vous pouvez ainsi passer à la suite bonne chance :P')


##### la fonction unlock et son compléments 


 
# A la fin du niveau
def unlock (a, b, c): # 'a, b, c' sont des 0 ou 1 permettant de déterminer si le joueur a fais les lvl précédents (si survival bloquer il faut rajouter un 'd' 
    f = open('fichierUnlock', 'wb')

    # Exporte dans le fichier les types et valeurs de a, b, c
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)

    f.close()

 # Le tutoriel est le lvl 0 et si on veut bloquer le survival il faut modifier le bloc unlock
def lock (lvl):
# Lis les trois variable mis dans 'fichierUnlock'
    f = open('fichierUnlock', 'rb')
    
    j = pickle.load(f)
    k = pickle.load(f)
    l = pickle.load(f)
    
    f.close()
    
# Aide diagnostique
    print(j)
    print(k)
    print(l)

    print (j+k+l)

    verrou=j+k+l
    
    if lvl <= verrou :
        print ('bonne chance pour le lvl', lvl)
        #lancer le lv
    else :
        print ("Vous n'êtes pas assez expérimenté pour faire se niveau faites les niveau inférieurs")
