##Petit message :
#Pymon (c) Antoine Bouquin et Quentin Albertone. Bienvenue dans le code source. Vous avez le droit de le modifier et/ou de le redistribuer en précisant que l'original vient de nous et sans le vendre. Merci.

#-------------- Nota bene :-----------------------
#Le programme est conçu pour tourner sous Windows uniquement pour l'instant, Linux devait être implanté, mais la documentation sur la librairie destinée a jouer les sons sous Linux (ossaudiodev) est insuffisante. Les tailles des fenêtres sont conçues pour avoir la dimension parfaite pour Windows 7/Aero désactivé. Ainsi, suivant l'OS/le thème, l'agencement peut ne pas être parfait. Cependant, cela est purement esthétique et n'affecte en rien le fonctionnement global du programme. Bon jeu !

##Importation des modules

from tkinter import * #Interface
from random import * #Aleatoire
import winsound #Lecture des sons # /!\ winsound s'importe comme sa et pas autrement 

## Listes permetant de faire fonctionner le jeu

# Les differentes listes de références suivant les niveau
listNote_tuto=['sounds/tutorial/tuto_do.wav','sounds/tutorial/tuto_re.wav','sounds/tutorial/tuto_mi.wav','sounds/tutorial/tuto_fa.wav','sounds/tutorial/tuto_sol.wav','sounds/tutorial/tuto_la.wav','sounds/tutorial/tuto_si.wav'] # Fichier audio pouvant sortir au tuto
listNote_lvl1=['sounds/lv1/lvl1_do.wav','sounds/lv1/lvl1_re.wav','sounds/lv1/lvl1_mi.wav','sounds/lv1/lvl1_fa.wav','sounds/lv1/lvl1_sol.wav','sounds/lv1/lvl1_la.wav','sounds/lv1/lvl1_si.wav'] # Fichier audio pouvant sortir au lvl 1
listNote_lvl2=['sounds/lv2/lvl2_do.wav','sounds/lv2/lvl2_re.wav','sounds/lv2/lvl2_mi.wav','sounds/lv2/lvl2_fa.wav','sounds/lv2/lvl2_sol.wav','sounds/lv2/lvl2_la.wav','sounds/lv2/lvl2_si.wav'] # Fichier audio pouvant sortir au lvl 2
listNote_lvl3=['sounds/lv3/lvl3_do.wav','sounds/lv3/lvl3_re.wav','sounds/lv3/lvl3_mi.wav','sounds/lv3/lvl3_fa.wav','sounds/lv3/lvl3_sol.wav','sounds/lv3/lvl3_la.wav','sounds/lv3/lvl3_si.wav'] # Fichier audio pouvant sortir au lvl 3
listNote_sur=['sounds/survival/sur_do.wav','sounds/survival/sur_re.wav','sounds/survival/sur_mi.wav','sounds/survival/sur_fa.wav','sounds/survival/sur_sol.wav','sounds/survival/sur_la.wav','sounds/survival/sur_si.wav'] # Fichier audio pouvant sortir au survival
    # Les différentes touches qui seront liés plus tard aux notes
listKeyboard=['q','s','d','f','k','l','m']

##Strings pour une couleur hexadécimale (purement esthétique)
grisClair="#dedede"
grisFonce="#3d3d3d"
vertClair="#2fab3d"
jauneClair="#fffd47"
orangeClair="#ffab48"
rougeClair="#ff2e2e"
bleuClair="#5367ff"

##Définitions des fonctions permettant de définir l'OS de l'utilisateur

global OSWin #Pour le réutiliser dans le reste du programme

def OSchosenWin():
    global OSWin
    OSWin=1
    
def OSchosenUnix():
    global OSWin
    OSWin=0

##Définition du launcher

#Définition d'une fenêtre qui demande a l'utilisateur son OS et adapte la librairie en fonction
def launch():
    
    #Définition de la fenêtre
    launcher=Tk()
    launcher.title("Pymon launcher")
    
    def launcherCloseWin():
        launcher.destroy()
        menu()
        OSchosenWin()
        
    def launcherCloseUnix():
        launcher.destroy()
        menu()
        OSchosenUnix()

#Afin de fermer la fenêtre en ouvrant le menu, on doit définir une fonction codant pour ça, sinon on doit
#coder la fermeture de la fenêtre en tant que commande sur le bouton, mais dans ce cas là, on doit mettre "menu()"
#en fin de fonction car on ne peut pas mettre plus de deux commandes sur un bouton.
#On pouvait donc quitter le launcher sans choisir d'OS et le menu se lance quand même.
    
    #Définition des boutons. Ils doivent prendre toute la fenêtre donc pack() est plus utile
    OSquestion=Label(launcher,text="Bienvenue dans Pymon ! Choisissez votre OS :",anchor=CENTER,justify=CENTER)
    OSquestion.pack(fill=BOTH)
    
    unixButton=Button(launcher,text="Windows",command=launcherCloseWin,bg="blue",activebackground=bleuClair) 
    unixButton.pack(fill=BOTH)
    
#Ainsi, l'utilisateur ne peut pas lancer le programme sans choisir d'OS 
#(grâce a la fonction launcherClose que l'on vient de créer).
#Il peut quitter le launcher manuellement, mais dans ce cas le programme s'arrête.

    winButton=Button(launcher,text="UNIX",command=launcherCloseUnix,bg="orange",activebackground=orangeClair)
    winButton.pack(fill=BOTH)
    
    #Lancement du launcher
    launcher.mainloop()

##Création de la fonction a invoquer en cas de niveau bloqué : une fenêtre avec un message d'erreur.

def unlockError():
    unlockingError=Tk()
    unlockingError.title("Pymon - Erreur !")
    
    unlockingErrorMessage=Label(unlockingError,text="Veuillez finir le niveau précédent avant !",bg=rougeClair)
    unlockingErrorMessage.pack(fill=BOTH)
    
##Fenêtres de Game Over, de Level Complete et de Try Again

def gameOver():
    
    gameOverWindow=Tk()
    gameOverWindow.title("Pymon - Game Over !")
    
    gameOverMessage1=Label(gameOverWindow,text="-=-=-=-=-=- GAME OVER -=-=-=-=-=-",bg=rougeClair)
    gameOverMessage1.pack(fill=BOTH)
    
    gameOverMessage2=Label(gameOverWindow,text="Raté ! Vous n'avez pas rentré la bonne suite de notes.",bg=rougeClair)
    gameOverMessage2.pack(fill=BOTH)
    
    gameOverWindow.mainloop()
    
    menu()
    
def levelComplete():
    
    levelCompleteWindow=Tk()
    levelCompleteWindow.title("Pymon - Niveau réussi !")
    
    levelCompleteMessage1=Label(levelCompleteWindow,text="-=-=-=-=-=- LEVEL COMPLETE -=-=-=-=-=-",bg=vertClair)
    levelCompleteMessage1.pack(fill=BOTH)
    
    levelCompleteMessage2=Label(levelCompleteWindow,text="Vous avez réussi le niveau ! Félicitations ! Vous pouvez passer au suivant.",bg=vertClair)
    levelCompleteMessage2.pack(fill=BOTH)
    
    levelCompleteWindow.mainloop()
    
    menu()
    
def tryAgain():
    
    tryAgainWindow=Tk()
    tryAgainWindow.title("Pymon - Score insuffisant !")
    
    tryAgainMessage1=Label(tryAgainWindow,text="Vous avez réussi le niveau !",bg=jauneClair)
    tryAgainMessage1.pack(fill=BOTH)
    
    tryAgainMessage2=Label(tryAgainWindow,text="La prochaine fois, faites le avec moins de jokers, cependant.",bg=jauneClair)
    tryAgainMessage2.pack(fill=BOTH)
    
    tryAgainWindow.mainloop()
    
    menu()
    
## Fonction 'lock' super simple a la fin du lvl

def lock (lvl) :
    fichier=open("data/unlock.txt","r")
    unlockingStatus=fichier.readline()
    unlockingStatus=int(unlockingStatus)
    fichier.close()
    
    if unlockingStatus<lvl : #s'il n'a jamais fais se niveau il faut le faire paser au niveu sup
        lvl=lvl+1
        fichier=open("data/unlock.txt","w")
        fichier.write(str(lvl))
        fichier.close ()
        levelComplete()
        
## Fonction des niveaux

def lvlFunc(lvl, ref, nb, lvlUp): # Nombre de note à la fin du niveau, 'ref' est la liste de note pour le lvl
    
    global RepHistory #Ces deux variables doivent être en global pour leur réutilisation avec valider().
    global reponse    #Elles sont de toute manière réinitialisées a chaque lancement du niveau.
    NoteHistory=[] #Liste répertoriant les notes sortie
    KbHistory=[] #Liste répertoriant les keyboard sortie
    RepHistory=[] # Liste répertoriant les réponses utilisateur
    score=0 # Comptabilise le total des points du joueur le long du niveau
    error=0 # Comptabilise les erreurs fait par l'utilisateur
    reponse=''
    
    #Création de la fenêtre
    levelWindow=Tk()
    levelWindow.title("Pymon - Niveau")
    
    levelMessage=Label(levelWindow,text="Bienvenue dans un des niveaux de Pymon !\nRépétez correctement la suite de notes jouées\npour réussir le niveau. Bonne chance !",bg=bleuClair)
    levelMessage.pack(fill=BOTH)
    
    answer=Entry(levelWindow) #La zone ou la réponse sera saisie
    answer.pack()
    
    def valider(): #Cette fonction sert pour le bouton "Valider". Elle prend la réponse, la transforme et permet la vérification de la réponse.
        reponse=answer.get()
        global RepHistory #Il faut redéfinir RepHistory comme global ici, sinon on ne peut pas l'utiliser.
        RepHistory=list(reponse)
        answer.delete(0,END) #Vide le widget Entry
        levelWindow.quit() #Pour quitter la fenêtre
        
    validerButton=Button(levelWindow,text="Valider",command=valider)
    validerButton.pack()
        
    for i in range (nb): # suivant la difficulté changer le 3 #
        #Evite de relancer la boucle après un game over
        if error==0:
            #Variables servant aux boucles while plus bas    
            sound=0
            check=0
        
            # Tire un nombre au hasard dans les liste de références plus haut et attribut une note à une touche et les 'stock' dans des list
            c=randrange(0,6)
            NoteHistory.append(ref [c])
            KbHistory.append(listKeyboard[c])
        
            # Joue la liste des fichiers audios contenant les 'anciennes' et la nouvelle note
            while sound!=i+1 :
                #Ici, il devait y avoir "if OSWin==1:" pour lancer le son avec Winsound, ne fonctionnant que sous Windows.
                #Le problème, c'est qu'on nous dit qu'"OSWin n'est pas défini" (alors qu'il l'est)
                winsound.PlaySound(NoteHistory [sound],winsound.SND_FILENAME)
                #else:
                    #On comptait utiliser ossaudiodev pour jouer le son sous Linux, mais la documentation étant insuffisante, on n'a pas pu.
                    #Cependant, nous sommes conscients que le programme ne marche par conséquent qu'avec Windows.
                sound=sound+1
                
            levelWindow.mainloop()
            
            # Compare un à un les éléments des liste contenant la réponse de l'utilisateur et les réponses attendu
            try :
                while check!=i+1 :
                    if KbHistory[check]==RepHistory[check] :
                        score=score+100 # Attribution du score afin de débloquer les niveau suivants 
                        check=check+1
                    
                    elif 'h'==RepHistory[check]: # Vérifie si la liste ne contient pas d'aide
                        if score<200 : # Pas de score négatif c'est peu encourageant
                            score=0
                        else :
                            score=score-200
                        check=check+1
                        
                    elif KbHistory[check]!=RepHistory[check]: # Compte les erreurs
                        error=error+1
                        levelWindow.destroy() #si une erreur est détectée, on quitte la fenêtre et la boucle for.
                        break                 #Cela évite de continuer la vérification.
            except IndexError :
                error=error+1
                levelWindow.destroy()
                break
    if error!=0 : # Et n'affiche qu'une page de 'gameOver' pour toutes les erreurs
        gameOver()
    
    #Fermeture de la fenêtre à la fin de la boucle for si il a réussi (s'il a raté, la fenêtre se ferme dans le while plus haut)
    #En réalité, c'est limite surperflu, cela évite juste de fermer une deuxième fois la fenêtre en sortant de la boucle si
    #l'utilisateur a raté le niveau. Ca évite juste un message d'erreur mais n'empêche pas le bon fonctionnement du programme.
        
    # Bloc qui permet ou non au joueur d'aller au niveau supérieur grâce à son score
    if score>lvlUp :
        levelComplete()
        lock(lvl)
    elif score<lvlUp and error==0: # si son score est inférieur au minimum fixé en arguments (lvlUp) et que ce n'est pas du à un game over :
        tryAgain()
        
## le tuto
def tutoriel():
    
    global RepHistory #Ces deux variables doivent être en global pour leur réutilisation avec valider().
    global reponse    #Elles sont de toute manière réinitialisées a chaque lancement du niveau.
    NoteHistory=[] # Initialise la liste qui collecte les notes sorties précédement
    KbHistory=[] # Initialise la liste qui collecte les lettres attendu pour avoir tous les points
    RepHistory=[]
    global reponse
    reponse=""
    error=0 # Comptabilise les erreurs fait par l'utilisateur
    
    #Création de la fenêtre tutorielWindowP(resentation) 
    tutorielWindowP=Tk()
    tutorielWindowP.title("Pymon - Tutoriel")
    
    tutorielMessage=Label(tutorielWindowP,text="bonjour, vous voici dans le premier niveau du pymon,\n un niveau ô combien honorable dans se jeu de reconnaissance de note, \n en effet c'est dans cette partie que vous apprendrez les bases avant d'être livré à vous même", bg=bleuClair)
    tutorielMessage.pack(fill=BOTH)
   
    tutorielMessage1=Label(tutorielWindowP,text="Pour commencer voyont ensemble à quelle sauce vous allé être mangé \n les notes à reconnaitre sont : do, re, mi, fa, sol, la, si et on respectivement comme lettres associé : q, s, d, f, k, l, m", bg=bleuClair)
    tutorielMessage1.pack(fill=BOTH)
    
    suiteButton=Button(tutorielWindowP,text="Passons à la suite ",command=tutorielWindowP.destroy)
    suiteButton.pack()
    
    tutorielWindowP.mainloop ()
    def valider(): #Cette fonction sert pour le bouton "Valider". Elle prend la réponse, la transforme et permet la vérification de la réponse.
            reponse=answer.get()
            answer.delete(0,END) #Vide le widget Entry
            tutorielWindow.destroy() #Pour quitter la fenêtre
    
    for c in range (7): # Boucle qui joue une à une les notes
        listTuto=['do','re','mi','fa','sol','la','si'] # Liste qui permet d'aider le joueur pour le tutoriel
        
        #Création de la fenêtre tutorielWindow 
        tutorielWindow=Tk()
        tutorielWindow.title("Pymon - Tutoriel")
    
       
        tutorielMessage4=Label(tutorielWindow, text= "la note joué est un ")
        tutorielMessage4.pack(fill=BOTH)
        tutorielMessage5=Label(tutorielWindow, text= listTuto[c])
        tutorielMessage5.pack(fill=BOTH)
        tutorielMessage6=Label(tutorielWindow, text= "il faut taper la lettre :")
        tutorielMessage6.pack(fill=BOTH)
        tutorielMessage7=Label(tutorielWindow, text= listKeyboard[c])
        tutorielMessage7.pack(fill=BOTH)
        
        answer=Entry(tutorielWindow) #La zone ou la réponse sera saisie
        answer.pack()
        
        validerButton=Button(tutorielWindow,text="Valider",command=valider)
        validerButton.pack()
        
        winsound.PlaySound(listNote_tuto[c],winsound.SND_FILENAME)
        
        tutorielWindow.mainloop()
    
    # Petit récapitulatif dans les conditions normal d'utilisation du jeu
    

    
    for c in range (7):
        winsound.PlaySound(listNote_tuto[c],winsound.SND_FILENAME)
        NoteHistory.append(listNote_tuto[c])
        KbHistory.append(listKeyboard[c])
    
    #Création de la fenêtre
    tutoRecapWindow=Tk()
    tutoRecapWindow.title("Pymon - Tutoriel")
    
    tutoRecapMessage=Label(tutoRecapWindow,text="Un petit récapitulatif nous allons jouer toutes les notes dans l'ordre \n Bonne chance !",bg=bleuClair)
    tutoRecapMessage.pack(fill=BOTH)
    
    recap=Entry(tutoRecapWindow) #La zone ou la réponse sera saisie
    recap.pack()
    
    def valider1 (): #Cette fonction sert pour le bouton "Valider". Elle prend la réponse, la transforme et permet la vérification de la réponse.
        reponse=recap.get()
        global RepHistory #Il faut redéfinir RepHistory comme global ici, sinon on ne peut pas l'utiliser.
        RepHistory=list(reponse)
        recap.delete(0,END) #Vide le widget Entry
        tutorielWindow.quit() #Pour quitter la fenêtre
        
    validerButton=Button(tutoRecapWindow,text="Valider",command=valider1)
    validerButton.pack()
    
    tutoRecapWindow.mainloop ()
    
    
    for j in range (7):
        if KbHistory[j]==RepHistory[j] :
            error+=0 #histoire de pas avoir un if vide, et de limiter les possibles erreurs, on laisse la variable error telle quelle
        else: # Compte les erreurs
            error=error+1
            tutorielWindow.destroy() #si une erreur est détectée, on quitte la fenêtre et la boucle for.
            break                 #Cela évite de continuer la vérification.
    
    if error!=0 : # Et n'affiche qu'une page de 'gameOver' pour toutes les erreurs
        gameOver()
    
    #Fermeture de la fenêtre à la fin de la boucle for si il a réussi (s'il a raté, la fenêtre se ferme dans le while plus haut)
    #l'utilisateur a raté le niveau. Ca évite juste un message d'erreur mais n'empêche pas le bon fonctionnement du programme.
    else :   
        levelComplete()
        lock (0)

##Le SURVIVAL DE LA MORT

#Fenêtre de game over du survival
def survivalGameOver():
    
    survivalGOWindow=Tk()
    survivalGOWindow.title=("Pymon - Survival : Game Over...")
    
    survivalGameOverMessage=Label(survivalGOWindow,text="Dommage... Veuillez rentrer votre nom.\nVotre score est de :")
    survivalGameOverMessage.pack(fill=BOTH)
    
    survivalScorePrint=Label(survivalGOWindow,text=scoreSurvival)
    survivalScorePrint.pack(fill=BOTH)
    
    survivalPseudoEntry=Entry(survivalGOWindow)
    survivalPseudoEntry.pack()
    
    def survivalWrite(): #La fonction qui écrit le score dans un fichier
        survivalPseudo=survivalPseudoEntry.get()
        survivalScore=open("data/survivalScore.txt","a")
        survivalScore.write(survivalPseudo)
        survivalScore.write(" : ")
        survivalScore.write(str(scoreSurvival)) #On doit le convertir en string pour l'écrire dans le fichier des meilleurs scores
        survivalScore.write("\n")
        survivalScore.close()
        survivalGOWindow.destroy()
        menu()
        
    survivalScoreValider=Button(survivalGOWindow,text="Valider",command=survivalWrite) #Bouton pour valider le nom et lancer l'enregistrement
    survivalScoreValider.pack()
    
    survivalGOWindow.mainloop()
    
#Le Survival en lui-même
def survival():
    
    #Initialisation des variables
    global RepHistory #Tout comme dans la fonction des niveaux, il faut définir les variables comme global.
    global reponse
    NoteHistory=[] #Liste répertoriant les notes sortie
    KbHistory=[] #Liste répertoriant les keyboard sortie
    RepHistory=[] # Liste répertoriant les réponses utilisateur
    global scoreSurvival #En global aussi, pour la fonction survivalGameOver
    scoreSurvival=0 # Comptabilise le total des points du joueur le long du niveau
    error=0 # Comptabilise les erreurs fait par l'utilisateur
    i=0 #Pour remplacer le i de la boucle for du niveau
    
    survivalWindow=Tk()
    survivalWindow.title("Pymon - SURVIVAL !!")
        
    survivalMessage=Label(survivalWindow,text="Bienvenue dans le Survival. Les développeurs déclinent toute responsabilité\nen cas de mort, trouble mental, folie, ou toute autre altération\nqui pourrait vous être causée.",bg=rougeClair)
    survivalMessage.pack(fill=BOTH)
        
    survivalMessage2=Label(survivalWindow,text="Ce niveau est sans fin. La liste de notes s'allongera a l'infini, jusqu'a la moindre erreur.\nUne note juste : +100. Une fausse ? -200.\nVotre score sera comptabilisé.\n\nBonne chance.",bg=rougeClair)
    survivalMessage2.pack(fill=BOTH)
        
    answer=Entry(survivalWindow)
    answer.pack()
        
    def valider(): #Cette fonction sert pour le bouton "Valider". Elle prend la réponse, la transforme et permet la vérification de la réponse.
        reponse=answer.get()
        global RepHistory #Il faut redéfinir RepHistory comme global ici, sinon on ne peut pas l'utiliser.
        RepHistory=list(reponse)
        answer.delete(0,END) #Vide le widget Entry
        survivalWindow.quit() #Pour quitter la fenêtre
    
    validerButton=Button(survivalWindow,text="Valider",command=valider)
    validerButton.pack()
    
    while error==0:
        
        #Variables pour les boucles while plus bas
        sound=0
        check=0
        
        # Tire un nombre au hasard dans les liste de références plus haut et attribut une note à une touche et les 'stock' dans des list
        c=randrange(0,6)
        NoteHistory.append(listNote_sur[c])
        KbHistory.append(listKeyboard[c])
        
        # Joue la liste des fichiers audios contenant les 'anciennes' et la nouvelle note
        while sound!=i+1 :
            winsound.PlaySound(NoteHistory[sound],winsound.SND_FILENAME)
            sound=sound+1
            
        survivalWindow.mainloop()
            
        # Compare un à un les éléments des liste contenant la réponse de l'utilisateur et les réponses attendu
        while check!=i+1 :
            if KbHistory[check]==RepHistory[check] :
                scoreSurvival=scoreSurvival+100 # Attribution du score pour l'enregidtrer plus tard
                check=check+1
            
            elif 'h'==RepHistory[check]: # Vérifie si la liste ne contient pas d'aide    
                scoreSurvival=scoreSurvival-200
                check=check+1
                
            elif KbHistory[check]!=RepHistory[check]: # Compte les erreurs
                error=error+1
                survivalWindow.destroy() #si une erreur est détectée, on quitte la fenêtre et la boucle for.
                break                 #Cela évite de continuer la vérification.
        
        if error!=0 : # Et n'affiche qu'une page de 'gameOver' pour toutes les erreurs
            survivalGameOver()
        i+=1

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
    
    #Label précisant que la liste est défilable
    infoDefil=Label(displayScore,text="Il est possible de faire défiler la liste",fg="grey")
    infoDefil.pack(fill=BOTH)
    
    #Bouton de retour au menu
    menuBack=Button(displayScore,text="Retour au menu",command=displayScore.destroy,bg="grey",activebackground=grisClair)
    menuBack.pack(fill=BOTH)
    
    #Fermeture du fichier
    survivalScore.close()
    
    #Lancement de la fenêtre
    displayScore.mainloop()
    
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
    # else:
        # print("C'était marqué dans le readme de pas toucher aux fichiers. Pourquoi vous l'avez fait ?!")
        
    #Ces fonctions sont appellées par les boutons pour le déblocage des niveaux.
    #Au départ, nous avions fait une fonction qui prenait des paramètres, mais ça ne fonctionnait pas
    #avec le command des boutons de Tkinter. Il a donc fallu faire des fonctions sans paramètres
    #qui vérifient si telles variables sont True ou False et agit en fonction.
    def unlockLevel1():
        if level1Unlock==True:
            menuWindow.destroy()
            lvlFunc(1,listNote_lvl1,5,1100)
        else:
            unlockError()
    
    def unlockLevel2():
        if level2Unlock==True:
            menuWindow.destroy()
            lvlFunc(2,listNote_lvl2,10,4700)
        else:
            unlockError()
    
    def unlockLevel3():
        if level3Unlock==True:
            menuWindow.destroy()
            lvlFunc(3,listNote_lvl3,15,10200)
        else:
            unlockError()
        
    #Création de la fenêtre
    menuWindow=Tk()
    menuWindow.title("Pymon")
    menuWindow.geometry("350x300")
    
    #Création d'une mini-fonction pour la fermeture du menu et lancement du tutoriel/survival afin de fonctionner avec les boutons.
    def tutoStart():
        menuWindow.destroy()
        tutoriel()
        
    def survivalStart():
        menuWindow.destroy()
        survival()
    
    #Création de chaque bouton et Labels décoratifs
    title=Label(menuWindow,text="Bienvenue dans Pymon !",anchor=CENTER,justify=CENTER)
    title.pack(fill=BOTH)
    
    tuto=Button(menuWindow,text="Tutoriel",bg="green",activebackground=vertClair,command=tutoStart)
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
    
    survivalButton=Button(menuWindow,text="Survival !",bg="black",fg="white",activebackground=grisFonce,command=survivalStart)
    survivalButton.pack(fill=BOTH)
    
    separation=Label(menuWindow,text="-=-=-=-=-=-=-=-=-=-=-=-=-",anchor=CENTER,justify=CENTER)
    separation.pack(fill=BOTH)
    
    survivalScore=Button(menuWindow,text="Scores du Survival",command=survivalScoreFunc,bg="grey",activebackground=grisClair)
    survivalScore.pack(fill=BOTH)
    
    commands=Label(menuWindow,text="Commandes : qsdfklm - h pour un joker",fg='grey')
    commands.pack(fill=BOTH)
    
    warning=Label(menuWindow,text="ATTENTION ! Ce programme est calibré avec des minuscules.\nPar conséquent, veuillez ne pas utiliser de majuscules.",fg='grey')
    warning.pack(fill=BOTH)
    
    vide=Label(menuWindow,text="",anchor=CENTER,justify=CENTER)
    vide.pack(fill=BOTH)
    
    #Lancement de la fenêtre
    menuWindow.mainloop()

## Lancement du programme ##
launch()
