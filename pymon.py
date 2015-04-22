##Petit message :
#Pymon (c) Antoine Bouquin et Quentin Albertone. Bienvenue dans le code source. Vous avez le droit de le modifier et/ou de le redistribuer en précisant que l'original vient de nous et sans le vendre. Merci.

#-------------- Nota bene :-----------------------
#Le programme est conçu pour tourner sous Windows et UNIX. Les tailles des fenêtres sont conçues pour avoir la dimension parfaite pour Windows 7/Aero désactivé. Ainsi, suivant l'OS/le thème, l'agencement peut ne pas être parfait. Cependant, cela est purement esthétique et n'affecte en rien le fonctionnement global du programme. Bon jeu !

##Importation des modules

from tkinter import * #Interface
from random import * #Aleatoire
import winsound #Lecture des sons # /!\ winsound s'importe comme sa et pas autrement 

## Listes permetant de faire fonctionner le jeu
    # Les differentes listes de références suivant les niveau ( à mettre juste après les importations )
listNote_tuto=['sons/tuto_do.wav','sons/tuto_re.wav','sons/tuto_mi.wav','sons/tuto_fa.wav','sons/tuto_sol.wav','sons/tuto_la.wav','sons/tuto_si.wav'] # Fichier audio pouvant sortir au tuto
listNote_lvl1=['sons/lvl1_do.wav','sons/lvl1_re.wav','sons/lvl1_mi.wav','sons/lvl1_fa.wav','sons/lvl1_sol.wav','sons/lvl1_la.wav','sons/lvl1_si.wav'] # Fichier audio pouvant sortir au lvl 1
listNote_lvl2=['sons/lvl2_do.wav','sons/lvl2_re.wav','sons/lvl2_mi.wav','sons/lvl2_fa.wav','sons/lvl2_sol.wav','sons/lvl2_la.wav','sons/lvl2_si.wav'] # Fichier audio pouvant sortir au lvl 2
listNote_lvl3=['sons/lvl3_do.wav','sons/lvl3_re.wav','sons/lvl3_mi.wav','sons/lvl3_fa.wav','sons/lvl3_sol.wav','sons/lvl3_la.wav','sons/lvl3_si.wav'] # Fichier audio pouvant sortir au lvl 3
listNote_sur=['sons/sur_do.wav','sons/sur_re.wav','sons/sur_mi.wav','sons/sur_fa.wav','sons/sur_sol.wav','sons/sur_la.wav','sons/sur_si.wav'] # Fichier audio pouvant sortir au survival
    # Les différentes touches qui seront liés plus tard aux notes
listKeyboard=['q','s','d','f','k','l','m']

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

##Création de la fonction a invoquer en cas de niveau bloqué : une fenêtre avec un message d'erreur.

def unlockError():
    unlockingError=Tk()
    unlockingError.title("Pymon - Erreur !")
    
    unlockingErrorMessage=Label(unlockingError,text="Veuillez finir le niveau précédent avant !",bg=rougeClair)
    unlockingErrorMessage.pack(fill=BOTH)

##Création du Menu Principal

def menu():
    
    #Vérification du déblocage des niveaux a l'aide d'un fichier
    unlock=open("data/unlock.txt","r")
    unlockingStatus=unlock.readline()
    unlockingStatus=int(unlockingStatus)
    
    #Initialisation des variables
    level1Unlock=False
    level2Unlock=False
    level3Unlock=False
    
    #Paramétrage des variables
    if unlockingStatus==0:
        level1Unlock=False
        level2Unlock=False
        level3Unlock=False
    elif unlockingStatus==1:
        level1Unlock=True
        level2Unlock=False
        level3Unlock=False
    elif unlockingStatus==2:
        level1Unlock=True
        level2Unlock=True
        level3Unlock=False
    elif unlockingStatus==3:
        level1Unlock=True
        level2Unlock=True
        level3Unlock=True
    else:
        print("C'était marqué dans le readme de pas toucher aux fichiers. Pourquoi vous l'avez fait ?!")
        
    #Ces fonctions sont appellées par les boutons pour le déblocage des niveaux.
    #Au départ, nous avions fait une fonction qui prenait des paramètres, mais ça ne fonctionnait pas
    #avec le command des boutons de Tkinter. Il a donc fallu faire des fonctions sans paramètres
    #qui vérifient si telles variables sont True ou False et agit en fonction.
    def unlockLevel1():
        if level1Unlock==True:
            print("Level 1 Unlock") #todo: virer cette phrase de test quand on aura tout et lancer le niveau
        else:
            unlockError()
    
    def unlockLevel2():
        if level2Unlock==True:
            print("Level 2 Unlock") #todo: virer cette phrase de test quand on aura tout
        else:
            unlockError()
    
    def unlockLevel3():
        if level3Unlock==True:
            print("Level 3 Unlock") #todo: virer cette phrase de test quand on aura tout
        else:
            unlockError()
        
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
    
    lv1=Button(menuWindow,text="Niveau 1",bg="yellow",activebackground=jauneClair,command=unlockLevel1)
    lv1.pack(fill=BOTH)
    
    lv2=Button(menuWindow,text="Niveau 2",bg="orange",activebackground=orangeClair,command=unlockLevel2)
    lv2.pack(fill=BOTH)
    
    lv3=Button(menuWindow,text="Niveau 3",bg="red",activebackground=rougeClair,command=unlockLevel3)
    lv3.pack(fill=BOTH)
    
    danger=Label(menuWindow,text="!!!! DANGER !!!!",anchor=CENTER,justify=CENTER,fg="red")
    danger.pack(fill=BOTH)
    
    survival=Button(menuWindow,text="Survival !",bg="black",fg="white",activebackground=grisFonce)
    survival.pack(fill=BOTH)
    
    separation=Label(menuWindow,text="-=-=-=-=-=-=-=-=-=-=-=-=-",anchor=CENTER,justify=CENTER)
    separation.pack(fill=BOTH)
    
    survivalScore=Button(menuWindow,text="Scores du Survival",command=survivalScoreFunc,bg="grey",activebackground=grisClair)
    survivalScore.pack(fill=BOTH)
    
    commands=Label(menuWindow,text="Touches : QSDFKLM - H pour un joker",fg='grey')
    commands.pack(fill=BOTH)
    
    vide=Label(menuWindow,text="",anchor=CENTER,justify=CENTER)
    vide.pack(fill=BOTH)
    
    #Lancement de la fenêtre
    menuWindow.mainloop()

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
    
##Fenêtres de Game Over et de Level Complete et de Try Again

def gameOver():
    
    gameOverWindow=Tk()
    gameOverWindow.title("Pymon - Game Over !")
    
    gameOverMessage1=Label(gameOverWindow,text="-=-=-=-=-=- GAME OVER -=-=-=-=-=-",bg=rougeClair)
    gameOverMessage1.pack(fill=BOTH)
    
    gameOverMessage2=Label(gameOverWindow,text="Raté ! Vous n'avez pas rentré la bonne suite de notes.",bg=rougeClair)
    gameOverMessage2.pack(fill=BOTH)
    
    gameOverWindow.mainloop()
    
def levelComplete():
    
    levelCompleteWindow=Tk()
    levelCompleteWindow.title("Pymon - Niveau réussi !")
    
    levelCompleteMessage1=Label(levelCompleteWindow,text="-=-=-=-=-=- LEVEL COMPLETE -=-=-=-=-=-",bg=vertClair)
    levelCompleteMessage1.pack(fill=BOTH)
    
    levelCompleteMessage2=Label(levelCompleteWindow,text="Vous avez réussi le niveau ! Félicitations ! Vous pouvez passer au suivant.",bg=vertClair)
    levelCompleteMessage2.pack(fill=BOTH)
    
    levelCompleteWindow.mainloop()
    
def tryAgain():
    
    tryAgainWindow=Tk()
    tryAgainWindow.title("Pymon - Score insuffisant !")
    
    tryAgainMessage1=Label(tryAgainWindow,text="Vous avez réussi le niveau !",bg=jauneClair)
    tryAgainMessage1.pack(fill=BOTH)
    
    tryAgainMessage2=Label(tryAgainWindow,text="La prochaine fois, faites le avec moins de jokers, cependant.",bg=jauneClair)
    tryAgainMessage2.pack(fill=BOTH)
    
    tryAgainWindow.mainloop()
    
########################
#Lancement du programme#
########################
launch()

############ Ajouts Quentin ##############

## le tuto
def tutoriel (ref, lvl):
    NoteHistory=[] # Initialise la liste qui collecte les notes sorties précédement
    KbHistory=[] # Initialise la liste qui collecte les lettres attendu pour avoir tous les points
    RepHistory=[] # Initialise la liste qui collecte les réponses de l'utilisateur
    
    print ("bonjour, vous voici dans le premier niveau du pymon,\n un niveau ô combien honorable dans se jeu de reconnaissance de                                   note, en effet c'est dans cette partie que vous apprendrez les bases avant d'ètre livré à vous même")
    print ("Pour commencer voyont ensemble à quelle sauce vous allé être mangé les notes à reconnaitre sont : do, re, mi, fa, sol, la, si et on respectivement comme lettres associé : q, s, d, f, j, k, l")
    print ("et bien commençons sans tarder")
    
    for c in range (6): # Boucle qui joue une à une les notes
        listTuto=['do','re','mi','fa','sol','la','si']
        
        winsound.PlaySound(ref[c],winsound.SND_FILENAME)
        print (" la note jouée est un ",listTuto[c]," appuyé sur la touche ",listKeyboard[c]) # Affiche les notes joué et les reponses attendu
    
    # todo : fin fonction programme - Début aide diagnostique ( a virer)
    
        print (c)
    
    # Réponse de l'utilisateur
    
        reponse=input('donner la lettre correspondant à cett note : ')
        if listKeyboard[c]==reponse :
            print('bravo')
        else :
            print('hiiinnn faux')
        
    print ("Bon allé un petit récapitulatif :) on va faire toutes es note dans l'ordre ")
    for c in range (6):
        winsound.PlaySound(ref[c],winsound.SND_FILENAME)
        NoteHistory.append(ref[c])
        KbHistory.append(listKeyboard[c])
    
    RepHistory=list(input('donner la lettre correspondant à cett note : '))
    
    for j in range (6):
        if KbHistory[j]==RepHistory[j] :
            print('bravo')
        else:
            print("hiiin faux je t'encourage à recommencer le tutoriel depuis le début")
            gameOver()
    lock (lvl)
    levelComplete()
    

####### voici le bloc important de notre programme #######

## Fonction note

def note (ref, nb, lvlUp): # Nombre de note à la fin du niveau, 'ref' est la liste de note pour le lvl
    
    NoteHistory=[] #Liste répertoriant les notes sortie
    KbHistory=[] #Liste répertoriant les keyboard sortie
    RepHistory=[] # Liste répertoriant les réponses utilisateur
    score=0 # Assez explicite 
    

    for i in range (nb): # suivant la difficulté changer le 3 #
    # Variable servant aux boucke while plus bas    
        sound=0
        check=0
       
    # Tire un nombre au hasard dans les liste de références plus haut et attribut une note à une touche et les 'stock' dans des list
        c=randrange(6)
        NoteHistory.append(ref [c])
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
            
            elif 'h'==RepHistory[check]: # Vérifie si la liste ne contient pas d'aide           
                print ('Un trou de mémoire, voila la suite mais vous perdez 200 points ils ne vous en reste que :', )
                if score<200 : # Pas de score négatif c'est peu encourageant
                    score=0
                else :
                    score=score-200
                check=check+1
                
            else:
                gameOver()
                
    print ('Bravo vous avez fait un score de',score) #todo : la limite de score au cas ou le joueur parvient à la fin avec beaucoup d'aides
    if score<lvlUp :
        tryAgain()
    else :
        levelComplete()
        
        
## Fonction 'lock' super simple a la fin du lvl

def lock (lvl) :
    fichier=open("data/unlock.txt","r")
    unlockingStatus=fichier.readline()
    unlockingStatus=int(unlockingStatus)
    fichier.close()
    
    if unlockingStatus>lvl : # Si le joueur à déja fais les lvl sup il ne faut pas pénaliser sa progression (ex qq'un qui refait le lvl1 il ne faut pas marquer 1 dans le fichier :)
        menu ()
        
    else : # et s'il n'a jamais fais se niveau il faut le faire paser au niveu sup
        lvl=lvl+1
        fichier=open("data/unlock.txt","w")
        fichier.write(str(lvl))
        fichier.close ()
        print ("vous pouvez ainsi passer au niveau", lvl)
        

## Fonction des niveaux

def lvl (lvl, ref, nb, lvlUp): 
    note (ref, nb, lvlUp)
    lock (lvl)
