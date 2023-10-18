from random import *
from tkinter import *

# debut de la class Domino

class Domino:
    """Definition d'un Domino"""

    def __init__(self, face1=-1, face2=-1):
        """Domino, int, int → Domino
        Construit un domino avec ses deux faces
        """
        self.__face1 = face1
        self.__face2 = face2

    def estDouble(self):
        """Domino → boolean
        Teste si c'est un domino double
        """
        if self.__face1 == self.__face2:
            return True
        return False

    def peutEtrePlaceApres(self, domino):
        """Domino, Domino → boolean
        Teste si le domino peut etre mis apres celui-ci
        """
        return self.__face1 == domino.__face2

    def __str__(self):
        """Domino → str
        Affichage d'un domino
        """
        if self.__face2==-1 and self.__face1==-1:
            return ""
        return str(self.__face1) + "-" + str(self.__face2)

    def permute(self):
        """(modif)Domino → None
        Echange les deux faces du domino
        """
        x = self.__face1
        self.__face1 = self.__face2
        self.__face2 = x
    
    def getPermute(self):
        """Domino → Domino
        Retourne le domino permute
        """
        return Domino(self.__face2, self.__face1)
    
    def getValeur1(self):
        """Domino → int
        Retourne la valeur de la face1 du domino
        """
        return self.__face1

    def getValeur2(self):
        """Domino → int
        Retourne la valeur de la face2 du domino
        """
        return self.__face2
    
    def somme(self):
        """Domino → int
        Retourne la somme des deux faces du domino
        """
        return self.__face1 + self.__face2

def listeDominos(n=12):
    """Int → Liste
    Fonction qui creer la pioche entiere
    """
    liste = []
    for i in range(n + 1):
        for j in range(i, n + 1):
            liste.append(Domino(i, j))
    return liste


# fin de la classe Domino

# debut de la classe Train

class Train:
    """Definition d'un train - structure de donnees LIFO (Last In First Out)"""

    def __init__(self):
        """Train → Train
        Construit un train vide
        """
        # base sur un train
        self.__train = []

    def estDemarre(self):
        """Train → boolean
        Teste si le train n'est pas vide
        """
        return len(self.__train) != 0

    def ajouter(self, elt):
        """(modif) Train, Objet → None
        Ajoute un element au sommet du train.
        """
        self.__train.append(elt)

    def estVide(self):
        """Train → Boolean
        Teste si le train est vide.
        """
        return len(self.__train) == 0

    def dernierDomino(self):
        """Train → Objet
        Retourne l'element au sommet du train.
        """
        return self.__train[-1]

    def enlever(self):
        """(modif) Train → Objet
        Enleve l'element au sommet du train.
        """
        assert not self.estVide()
        elt = self.__train[-1]
        del self.__train[-1]
        return elt
    
    def getElement(self,ind):
        """Train, int → Objet
        Retourne l'element en indice
        """
        return self.__train[ind]
    
    def getTrain(self):
        """Train → Train
        Retourne le train
        """
        return self.__train
    
    def __str__(self):
        """Train → str
        Affichage du train
        """
        while not self.estVide():
            print(self.dernierDomino())
            self.enlever()


# fin de la classe Train

# debut de la classe JeuMexicain

class JeuMexicain:
    """Definition du jeu"""

    def __init__(self, dominoDepart=None, pioche=listeDominos(), trainMexicain=Train()):
        """JeuMexicain, Domino, list, Train → JeuMexicain
        Construit le jeu mexicain
        """
        self.__dominoDepart = dominoDepart
        self.__trainMexicain = trainMexicain
        self.__pioche = pioche
    
    def reinit_train(self):
        """JeuMexicain(modif) → None
        Réinitialise le jeu avec les paramètres par défault
        """
        self.__dominoDepart = None
        self.__trainMexicain = Train()
        self.__pioche = listeDominos()
        
    def getDominoDepart(self):
        """JeuMexicain → Domino
        Retourne le domino de départ
        """
        return self.__dominoDepart

    def choixDominoDepart(self):
        """JeuMexicain → boolean
        Teste si le domino de depart est choisi
        """
        return self.__dominoDepart != None

    def setDominoDepart(self,domino):
        """JeuMexicain(modif), Domino → None
        Initialise le domino de départ
        """
        self.__dominoDepart = domino

    def getTrainMexicain(self):
        """JeuMexicain → Train
        Retourne le train mexicain
        """
        return self.__trainMexicain
    
    def setTrainMexicain(self,domino):
        """JeuMexicain(modif), Domino → None
        Ajoute un domino au train mexicain
        """
        self.__trainMexicain.ajouter(domino)
    
    def getPioche(self):
        """JeuMexicain → List
        Retourne la pioche du jeu
        """
        return self.__pioche
    
    def setPioche(self,liste):
        """JeuMexicain(modif), list → None
        Change la pioche
        """
        self.__pioche = liste
    
    def delIemePioche(self, ind):
        """JeuMexicain(modif), int → None
        Supprime le domino de la pioche
        """
        del self.__pioche[ind]
        
    def dernierDomino(self):
        """JeuMexicain → Domino
        Retourne le dernier domino du train mexicain
        """
        return self.__trainMexicain.dernierDomino()
    
    def peutPoserDomino(self,domino):
        """JeuMexicain, Domino → boolean
        Teste si le domino peut être poser sur le train mexicain
        """
        return domino.peutEtrePlaceApres(self.dernierDomino())
    
    def piocheVide(self):
        """JeuMexicain → boolean
        Teste si la pioche est vide
        """
        return len(self.__pioche) == 0
    
    def trainMexicainDemarre(self):
        """JeuMexicain → boolean
        Teste si le train à demarrer
        """
        return self.__trainMexicain.estDemarre()
    
    def piocheAlea(self):
        """JeuMexicain → Domino
        Retourne un domino de la pioche au hasard et le supprime de la pioche
        """
        ind = randint(0, len(self.__pioche) - 1)
        alea = self.__pioche[ind]
        del self.__pioche[ind]
        return alea
    
    def plusGrandDouble(self):
        """JeuMexicain → Domino
        Retourne le plus grand double de la pioche
        """
        doubles=[]
        ind=0
        maxi=0
        for i in range(len(self.__pioche)):
            if self.__pioche[i].estDouble():
                doubles.append(self.__pioche[i])
        if len(doubles)!=0:
            for i in range(len(doubles)):
                if maxi < doubles[i].getValeur1():
                    maxi = doubles[i].getValeur1()
                    ind=i
            return doubles[ind]
        return None
    
    def indicePlusGrandDouble(self):
        """JeuMexicain → int
        Retourne l'indice du plus grand double de la pioche
        """
        double=self.plusGrandDouble()
        for i in range(len(self.__pioche)):
            if self.__pioche[i]==double:
                return i

# fin de la classe JeuMexicain

# debut de la class Joueur

class Joueur:
    """Définition d'un joueur"""
    
    def __init__(self, nom, reserve=[]):
        """Joueur, str, list → Joueur
        Construit le joueur
        """
        self.__train = Train()
        self.__reserve = reserve
        self.__nom = nom
    
    def getName(self):
        """Joueur → str
        Retourne le nom du joueur
        """
        return self.__nom
    
    def getTrain(self):
        """Joueur → Train
        Retourne le train du joueur
        """
        return self.__train
    
    def setTrain(self, domino):
        """Joueur(modif), Domino → None
        Ajoute un domino dans le train du joueur
        """
        self.__train.ajouter(domino)
    
    def reinit_joueur(self):
        """Joueur(modif) → None
        reinitialise le joueur
        """
        self.__train = Train()
        self.__reserve = []
        
    def getReserve(self):
        """Joueur → List
        Retourne la réserve du joueur
        """
        return self.__reserve
    
    def setReserveEntiere(self, liste):
        """Joueur(modif), list → None
        Modifie la réserve entière du joueur
        """
        self.__reserve = liste
    
    def setReserve(self, domino):
        """Joueur(modif), Domino → None
        Ajoute un domino dans la réserve du joueur
        """
        self.__reserve.append(domino)
        
    def trainDemarre(self):
        """Joueur → boolean
        Retourne si le train du joueur est démarré
        """
        return self.__train.estDemarre()
    
    def dernierDominoTrain(self):
        """Joueur → Domino
        Retourne le dernier domino du train du joueur
        """
        return self.__train.dernierDomino()

    def plusGrandDouble(self):
        """Joueur → Domino
        Retourne le plus grand domino double de la réserve s'il existe
        """
        doubles=[]
        ind=0
        maxi=0
        for i in range(len(self.__reserve)):
            if self.__reserve[i].estDouble():
                doubles.append(self.__reserve[i])
        if len(doubles)!=0:
            for i in range(len(doubles)):
                if maxi < doubles[i].getValeur1():
                    maxi = doubles[i].getValeur1()
                    ind=i
            return doubles[ind]
        return None
    
    def indicePlusGrandDouble(self):
        """Joueur → int
        Retourne l'indice du plus grand domino double de la réserve s'il existe
        """
        double=self.plusGrandDouble()
        for i in range(len(self.__reserve)):
            if self.__reserve[i]==double:
                return i
    
    def peutEtrePoserQuelconque(self,domino,jeu):
        """Joueur, Domino, JeuMexicain → boolean
        Teste si un domino peut etre placé sur n'importe quel train
        """
        return self.peutEtrePoserTrain(domino,jeu) == True or self.peutEtrePoserTrainMexicain(domino,jeu) == True
        
    def peutEtrePoserTrain(self,domino,jeu):
        """Joueur, Domino, JeuMexicain → boolean
        Teste si un domino peut etre placé sur le train du joueur
        """
        if self.trainDemarre() == True:
            return domino.peutEtrePlaceApres(self.dernierDominoTrain())
        return domino.peutEtrePlaceApres(jeu.getDominoDepart())
        
    def peutEtrePoserTrainMexicain(self,domino,jeu):
        """Joueur, Domino, JeuMexicain → boolean
        Teste si un domino peut etre placé sur le train mexicain
        """
        if jeu.trainMexicainDemarre() == True:
            return domino.peutEtrePlaceApres(jeu.dernierDomino())
        return domino.peutEtrePlaceApres(jeu.getDominoDepart())
            
    def dominoTrain(self,jeu):
        """Joueur, JeuMexicain → Domino, int
        Retourne le premier domino de la réserve qui peut être posé sur le train du joueur ainsi que son indice
        """
        assert len(self.__reserve)!=0
        if self.trainDemarre() == True:
            for i in range(len(self.__reserve)):
                if self.__reserve[i].peutEtrePlaceApres(self.dernierDominoTrain()):
                    return self.__reserve[i], i
                elif (self.__reserve[i].getPermute()).peutEtrePlaceApres(self.dernierDominoTrain()):
                    return self.__reserve[i].getPermute(), i
        else:
            for i in range(len(self.__reserve)):
                if self.__reserve[i].peutEtrePlaceApres(jeu.getDominoDepart()):
                    return self.__reserve[i], i
                elif self.__reserve[i].getPermute().peutEtrePlaceApres(jeu.getDominoDepart()):
                    return self.__reserve[i].getPermute(), i
        return None, None

    def dominoTrainMexicain(self,jeu):
        """Joueur, JeuMexicain → Domino, int
        Retourne le premier domino de la réserve qui peut être posé sur le train mexicain ainsi que son indice
        """
        assert len(self.__reserve)!=0
        if jeu.trainMexicainDemarre() == True:
            for i in range(len(self.__reserve)):
                if self.__reserve[i].peutEtrePlaceApres(jeu.dernierDomino()):
                    return self.__reserve[i], i
                elif (self.__reserve[i].getPermute()).peutEtrePlaceApres(jeu.dernierDomino()):
                    return self.__reserve[i].getPermute(), i
        else:
            for i in range(len(self.__reserve)):
                if self.__reserve[i].peutEtrePlaceApres(jeu.getDominoDepart()):
                    return self.__reserve[i], i
                elif self.__reserve[i].getPermute().peutEtrePlaceApres(jeu.getDominoDepart()):
                    return self.__reserve[i].getPermute(), i
        return None, None
    
    def pioche(self,jeu):
        """Joueur, JeuMexicain → Domino
        Retourne le domino pioché dans la pioche du jeu et le retire de la Pioche
        """
        d = None
        if not jeu.piocheVide():
            ind = randint(0,len(jeu.getPioche())-1)
            d = jeu.getPioche()[ind]
            jeu.delIemePioche(ind)
        return d
    
    def poserDominoDansTrain(self,jeu,domino=None,fait=False):
        """Joueur, JeuMexicain, Domino, Boolean → Boolean
        Pose un domino dans le train du joueur si choisi et retourne si il a pu être poser
        """
        if domino != None:
            if self.peutEtrePoserTrain(domino,jeu):
                self.__train.ajouter(domino)
                fait = True
        return fait

    def poserDomino(self,jeu,domino=None,indice=None,train=None):
        """Joueur, JeuMexicain, Domino, Int, Str → Domino
        Pose un domino choisi dans un train choisi
        Par défaut il posera le premier domino qui peut être posé dans le train du joueur ou dan sle train mexicain
        Sinon pioche et pose dans la réserve
        Retourne le domino qui a était posé
        """
        dominoPlace=None
        dominoTrain, indiceTrain = self.dominoTrain(jeu)
        dominoTrainMexicain, indiceTrainMexicain = self.dominoTrainMexicain(jeu)
        fait=False
        if train != None:
            if train == "train mexicain":
                if domino != None:
                    if self.peutEtrePoserTrainMexicain(domino,jeu):
                        jeu.getTrainMexicain().ajouter(domino)
                        self.delIemeReserve(indice)
                        fait=True
                        dominoPlace=domino
        if fait == False:
            if dominoTrain != None:
                self.__train.ajouter(dominoTrain)
                self.delIemeReserve(indiceTrain)
                fait = True
                dominoPlace=dominoTrain
            elif dominoTrainMexicain != None:
                jeu.getTrainMexicain().ajouter(dominoTrainMexicain)
                self.delIemeReserve(indiceTrainMexicain)
                fait = True
                dominoPlace=dominoTrainMexicain
            elif len(jeu.getPioche())!=0:
                pioche = self.pioche(jeu)
                piochePermute = pioche.getPermute()
                if self.trainDemarre() == True:
                    if pioche.peutEtrePlaceApres(self.dernierDominoTrain()) == True:
                        self.__train.ajouter(pioche)
                        fait = True
                        dominoPlace=pioche
                    elif piochePermute.peutEtrePlaceApres(self.dernierDominoTrain()) == True:
                        self.__train.ajouter(piochePermute)
                        fait = True
                        dominoPlace=piochePermute
                    else:
                        self.__reserve.append(pioche)
                        fait = True
                else:
                    if pioche.peutEtrePlaceApres(jeu.getDominoDepart()) == True:
                        self.__train.ajouter(pioche)
                        fait = True
                        dominoPlace=pioche
                    elif piochePermute.peutEtrePlaceApres(jeu.getDominoDepart()) == True:
                        self.__train.ajouter(piochePermute)
                        fait = True
                        dominoPlace=piochePermute
                    else:
                        self.__reserve.append(pioche)
                        fait = True
        return dominoPlace
                
    def dominoPeutEtrePoser(self,domino,jeu):
        """Joueur,Domino,JeuMexicain → boolean
        Teste si un domino de la réserve peut être poser
        """
        return domino.peutEtrePoserTrainMexicain(self.dominoTrainMexicain(jeu),jeu) or domino.peutEtrePoserTrain(self.dominoTrain(jeu),jeu)
            
    def delIemeReserve(self,ind):
        """Joueur(modif), int → None
        Supprime le ieme domino de la reserve
        """
        del self.__reserve[ind]
        
    def lenReserve(self):
        """Joueur → int
        Retourne le nombre de dominos dans la reserve
        """
        return len(self.__reserve)
    
    def reserveVide(self):
        """Joueur → boolean
        Teste si la réserve est vide
        """
        return len(self.__reserve) == 0
    
    def getIemeReserve(self,ind):
        """Joueur, int → Domino
        Retourne le ieme domino de la reserve
        """
        return self.__reserve[ind]
    
    def setIemeReserve(self,ind,domino):
        """Joueur(modif), int, Domino → None
        Modifie le ieme domino de la reserve
        """
        self.__reserve[ind] = domino
    
    def permuteIemeReserve(self,ind):
        """Joueur(modif), int → None
        Permute le ieme domino de la reserve
        """
        self.__reserve[ind].permute()
        
    def sommeReserve(self):
        """Joueur → int
        Retourne la somme de la réserve du joueur
        """
        somme = 0
        for d in self.__reserve:
            somme += d.somme()
        return somme

def donneDomino(jeu):
    """JeuMexicain → None
    Ajoute des dominos aléatoire dans la réserve du joueur
    """
    l = []
    i = 0
    while i!=10:
        l.append(jeu.piocheAlea())
        i+=1
    return l
                
# fin de la classe Joueur

# debut de la classe VueJeu

class VueJeu:
    """Définition de la vue du jeu"""

    def __init__(self,jeu):
        """VueJeu, JeuMexicain → None
        Modélise la vue du jeu
        """
        #fenêtre
        fen = Tk()
        fen.title("Jeu du Train Mexicain")
        self.__fen = fen
        
        #sous-fenêtres
        self.__frDepart = Frame(fen)
        self.__frTrainMex = Frame(fen)
        self.__frNote = Frame(fen)
        self.__frReserve = Frame(fen)
        self.__frButton = Frame(fen)
        
        #sous-fenêtres Joueurs
        self.__frTrain = []
        self.__frJoueur1 = Frame(fen)
        self.__frJoueur2 = Frame(fen)
        self.__frJoueur3= Frame(fen)
        self.__frJoueur4 = Frame(fen)
        self.__frTrain.append(self.__frJoueur1)
        self.__frTrain.append(self.__frJoueur2)
        self.__frTrain.append(self.__frJoueur3)
        self.__frTrain.append(self.__frJoueur4)
        
        #initialisations
        self.__jeu = jeu
        self.__train_select = None
        self.__domino_select = None
        self.__indice_select = None
        self.__dominoPlace = None
        self.__joueurs = []
        
        #initialisation Joueurs
        self.__joueur1 = Joueur("Joueur")
        self.__joueur2 = Joueur("Joueur IA 1")
        self.__joueur3 = Joueur("Joueur IA 2")
        self.__joueur4 = Joueur("Joueur IA 3")

        self.__joueur1.setReserveEntiere(donneDomino(self.__jeu))
        self.__joueur2.setReserveEntiere(donneDomino(self.__jeu))
        self.__joueur3.setReserveEntiere(donneDomino(self.__jeu))
        self.__joueur4.setReserveEntiere(donneDomino(self.__jeu))
                
        self.__joueurs.append(self.__joueur1)
        self.__joueurs.append(self.__joueur2)
        self.__joueurs.append(self.__joueur3)
        self.__joueurs.append(self.__joueur4)
        
        self.__joueurDepart = randint(0,3)
        self.__ind = self.__joueurDepart
        self.__tour = 0
        
        #initialisation images
        l = ["0", "1" , "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
        self.__images = []
        for i in l:
            liste = []
            for j in l:
                img = PhotoImage(file="imagesDominoMexicain/"+i+"-"+j+".gif")
                liste.append(img)
            self.__images.append(liste)
        self.__vide = PhotoImage(file="imagesDominoMexicain/-1--1.gif")
        
        #frDepart
        LbDepart = Label(self.__frDepart, text="Jeu des dominos mexicains - Dominos de départ :")
        LbDepart.grid(row=0, column=0)
        self.__BtnDepart = Button(self.__frDepart, image = self.__vide, width=120)
        self.__BtnDepart.grid(row = 0, column=1)
        
        #frTrainMex
        self.__btnTrainMex = []
        LbTrain = Label(self.__frTrainMex, text="Train Mexicain", width=15)
        LbTrain.grid(row=0, column=0)
        for i in range (5):
            BtnTrain = Button(self.__frTrainMex, image = self.__vide, width=120)
            BtnTrain.grid(row=0, column=i+1)
            self.__btnTrainMex.append(BtnTrain)
                    
        #frTrain
        self.__btnTrain = []
        for j in range(len(self.__joueurs)):
            LbTrain = Label(self.__frTrain[j], text=self.__joueurs[j].getName(), width=15)
            LbTrain.grid(row=0, column=0)
            self.__btnTrain.append([])
            for i in range (5):
                BtnTrain = Button(self.__frTrain[j], image = self.__vide, width=120)
                BtnTrain.grid(row=0, column=i+1)
                self.__btnTrain[j].append(BtnTrain)
        
        #frTour
        self.__LbTour = Label(self.__frNote, fg="red", text=self.__joueurs[self.__joueurDepart].getName()+" commence a jouer !")
        self.__LbTour.grid(row = 0, column=0)
        Lb = Label(self.__frNote,fg="green", text="Cliquez sur un domino pour le sélectionner")
        Lb.grid(row = 1, column=0)
        Lb = Label(self.__frNote,fg="green", text="Cliquez sur le bouton du train que vous voulez remplir")
        Lb.grid(row = 2, column=0)
        Lb = Label(self.__frNote,fg="green", text="Cliquez deux fois de suite sur le domino pour permuter")
        Lb.grid(row = 3, column=0)
        Lb = Label(self.__frNote,fg="green", text="Puis cliquez sur le bouton Go")
        Lb.grid(row = 4, column=0)

        #frReserve
        LbReserve = Label(self.__frReserve, text="Le jeu de "+self.__joueur1.getName())
        LbReserve.grid(row=0, column=0, columnspan=5)
        self.__btnReserve=[]
        if self.__joueur1.lenReserve()%5 == 0:
            for i in range((self.__joueur1.lenReserve()//5)):
                for j in range(5):
                    BtnReserve = Button(self.__frReserve, image = self.__images[self.__joueur1.getIemeReserve(i*5+j).getValeur1()][self.__joueur1.getIemeReserve(i*5+j).getValeur2()], width=120)
                    BtnReserve.grid(row=i+1, column=j)
                    self.__btnReserve.append(BtnReserve)
        else:
            for i in range((self.__joueur1.lenReserve()//5)+1):
                for j in range(5):
                    if (i*5+j)<self.__joueur1.lenReserve():
                        BtnReserve = Button(self.__frReserve, image = self.__images[self.__joueur1.getIemeReserve(i*5+j).getValeur1()][self.__joueur1.getIemeReserve(i*5+j).getValeur2()], width=120)
                        BtnReserve.grid(row=i+1, column=j)
                        self.__btnReserve.append(BtnReserve)
                    else:
                        BtnReserve = Button(self.__frReserve, image = self.__vide, width=120)
                        BtnReserve.grid(row=i+1, column=j)
                        self.__btnReserve.append(BtnReserve)
        self.ctrl_reinit_reserve()
        
        #frButton
        self.__BtnTrainMex = Button(self.__frButton, text="Train Mexicain", command=self.creer_ctrl_boutonTrainMex(), width=15)
        self.__BtnTrainMex.grid(row=0, column=0, pady=10, padx=10)
        self.__BtnTrain1 = Button(self.__frButton, text="Train "+self.__joueur1.getName(), command=self.creer_ctrl_boutonTrain1(), width=15)
        self.__BtnTrain1.grid(row=0, column=1, pady=10, padx=10)
        self.__BtnTrain2 = Button(self.__frButton, text="Train "+self.__joueur2.getName(), command=self.creer_ctrl_boutonTrain2(), width=15)
        self.__BtnTrain2.grid(row=0, column=2, pady=10, padx=10)
        self.__BtnTrain3 = Button(self.__frButton, text="Train "+self.__joueur3.getName(), command=self.creer_ctrl_boutonTrain3(), width=15)
        self.__BtnTrain3.grid(row=0, column=3, pady=10, padx=10)
        self.__BtnTrain4 = Button(self.__frButton, text="Train "+self.__joueur4.getName(), command=self.creer_ctrl_boutonTrain4(), width=15)
        self.__BtnTrain4.grid(row=0, column=4, pady=10, padx=10)
        self.__BtnTrainMex.bind('<Motion>',self.on_enter)
        self.__BtnTrain1.bind('<Motion>',self.on_enter)
        self.__BtnTrain2.bind('<Motion>',self.on_enter)
        self.__BtnTrain3.bind('<Motion>',self.on_enter)
        self.__BtnTrain4.bind('<Motion>',self.on_enter)
        self.__BtnTrainMex.bind('<Leave>',self.on_leave)
        self.__BtnTrain1.bind('<Leave>',self.on_leave)
        self.__BtnTrain2.bind('<Leave>',self.on_leave)
        self.__BtnTrain3.bind('<Leave>',self.on_leave)
        self.__BtnTrain4.bind('<Leave>',self.on_leave)
        self.__LbButton = Label(self.__frButton)
        self.__LbButton.grid(row=1, column=0, columnspan=3)
        self.__BtnGo = Button(self.__frButton, text=" Go ! ", command = self.creer_ctrl_bouton_go(), width=15)
        self.__BtnGo.grid(row=1, column=3, columnspan=2)
        self.__BtnGo.bind('<Motion>',self.on_enter)
        self.__BtnGo.bind('<Leave>',self.on_leave)
        if self.__ind == 0:
            self.__BtnGo['text']=" Go ! "
        else:
            self.__BtnGo['text']=" Suivant "
                
        self.__frDepart.grid(row=0)
        self.__frTrainMex.grid(row=1)
        for i in range(len(self.__frTrain)):
            self.__frTrain[i].grid(row=i+2)
        self.__frNote.grid(row=6)
        self.__frReserve.grid(row=7)
        self.__frButton.grid(row=8)
        
    def reset(self,liste):
        """VueJeu, list → None
        Supprime tous les anciens boutons dans la liste donnée
        """
        for i in liste:
            i.destroy()
    
    def creer_click_double(self,i):
        """VueJeu, int → None
        Gère l'évènement double clic de chaque bouton dans la réserve du joueur
        """
        def click_double(event):
            self.__joueur1.permuteIemeReserve(i)
            self.redessineReserve()
        return click_double
    
    def redessineReserve(self):
        """JeuMexicain → None
        Redessine la réserve du joueur
        """
        self.reset(self.__btnReserve)
        self.__btnReserve = []
        if self.__joueur1.lenReserve()%5 == 0:
            for i in range((self.__joueur1.lenReserve()//5)):
                for j in range(5):
                    BtnReserve = Button(self.__frReserve, image = self.__images[self.__joueur1.getIemeReserve(i*5+j).getValeur1()][self.__joueur1.getIemeReserve(i*5+j).getValeur2()], width=120)
                    BtnReserve.grid(row=i+1, column=j)
                    self.__btnReserve.append(BtnReserve)
        else:
            for i in range((self.__joueur1.lenReserve()//5)+1):
                for j in range(5):
                    if (i*5+j)<self.__joueur1.lenReserve():
                        BtnReserve = Button(self.__frReserve, image = self.__images[self.__joueur1.getIemeReserve(i*5+j).getValeur1()][self.__joueur1.getIemeReserve(i*5+j).getValeur2()], width=120)
                        BtnReserve.grid(row=i+1, column=j)
                        self.__btnReserve.append(BtnReserve)
                    else:
                        BtnReserve = Button(self.__frReserve, image = self.__vide, width=120)
                        BtnReserve.grid(row=i+1, column=j)
                        self.__btnReserve.append(BtnReserve)
        self.ctrl_reinit_reserve()
        self.__frReserve.grid(row=7)            
     
    def ctrl_reinit_reserve(self):
        """VueJeu → None
        Ré-associe les ations associés aux évènements de chaque bouton de la réserve
        """
        for i in range(len(self.__joueur1.getReserve())):
            self.__btnReserve[i].bind('<Button-1>', self.creer_ctrl_selectionner_domino(i))
            self.__btnReserve[i].bind('<Double-1>', self.creer_click_double(i))
    
    def creer_ctrl_selectionner_domino(self,i):
        """VueJeu(modif), int → None
        Récupère le domino à l'indice i dans la réserve du joueur ainsi que son indice
        """
        def ctrl_selectionner_domino(event):
            self.__domino_select = self.__joueur1.getIemeReserve(i)
            self.__indice_select = i
        return ctrl_selectionner_domino
    
    def redessine_train(self):
        """VueJeu → None
        Redessine le train Mexicain et les trains des joueurs
        """
        self.reset(self.__btnTrainMex)
        if len(self.__jeu.getTrainMexicain().getTrain()) > 5:
            for i in range (len(self.__jeu.getTrainMexicain().getTrain())-5,len(self.__jeu.getTrainMexicain().getTrain())):
                BtnTrain = Button(self.__frTrainMex, image = self.__images[self.__jeu.getTrainMexicain().getElement(i).getValeur1()][self.__jeu.getTrainMexicain().getElement(i).getValeur2()], width=120)
                BtnTrain.grid(row = 0, column = i+1)
                self.__btnTrainMex.append(BtnTrain)
        else:
            for i in range (5):
                if i < len(self.__jeu.getTrainMexicain().getTrain()):
                    BtnTrain = Button(self.__frTrainMex , image = self.__images[self.__jeu.getTrainMexicain().getElement(i).getValeur1()][self.__jeu.getTrainMexicain().getElement(i).getValeur2()], width=120)
                    BtnTrain.grid(row=0, column=i+1)
                    self.__btnTrainMex.append(BtnTrain)
                else:
                    BtnTrain = Button(self.__frTrainMex , image = self.__vide, width=120)
                    BtnTrain.grid(row=0, column=i+1)
                    self.__btnTrainMex.append(BtnTrain)
        self.__frTrainMex.grid(row=1)
        for j in range(len(self.__joueurs)):
            self.reset(self.__btnTrain[j])
            if len(self.__joueurs[j].getTrain().getTrain()) > 5:
                for i in range (len(self.__joueurs[j].getTrain().getTrain())-5,len(self.__joueurs[j].getTrain().getTrain())):
                    BtnTrain = Button(self.__frTrain[j], image = self.__images[self.__joueurs[j].getTrain().getElement(i).getValeur1()][self.__joueurs[j].getTrain().getElement(i).getValeur2()], width=120)
                    BtnTrain.grid(row = 0, column = i+1)
                    self.__btnTrain[j].append(BtnTrain)
            else:
                for i in range (5):
                    if i < len(self.__joueurs[j].getTrain().getTrain()):
                        BtnTrain = Button(self.__frTrain[j], image = self.__images[self.__joueurs[j].getTrain().getElement(i).getValeur1()][self.__joueurs[j].getTrain().getElement(i).getValeur2()], width=120)
                        BtnTrain.grid(row=0, column=i+1)
                        self.__btnTrain[j].append(BtnTrain)
                    else:
                        BtnTrain = Button(self.__frTrain[j] , image = self.__vide, width=120)
                        BtnTrain.grid(row=0, column=i+1)
                        self.__btnTrain[j].append(BtnTrain)
            self.__frTrain[j].grid(row=j+2)
    
    def ctrl_reinit(self):
        """VueJeu → None
        Réinitialise le jeu
        """
        self.__jeu.reinit_train()
        self.__joueur1.reinit_joueur()
        self.__joueur2.reinit_joueur()
        self.__joueur3.reinit_joueur()
        self.__joueur4.reinit_joueur()
        self.__joueur1.setReserveEntiere(donneDomino(self.__jeu))
        self.__joueur2.setReserveEntiere(donneDomino(self.__jeu))
        self.__joueur3.setReserveEntiere(donneDomino(self.__jeu))
        self.__joueur4.setReserveEntiere(donneDomino(self.__jeu))
        self.__BtnDepart['image']=self.__vide
        self.__LbButton['text'] = ""
        self.__BtnGo['command'] = self.creer_ctrl_bouton_go()
        self.__joueurDepart = randint(0,3)
        self.__ind = self.__joueurDepart
        self.__tour = 0
        self.__LbTour['text']=self.__joueurs[self.__joueurDepart].getName()+" commence a jouer !"
        self.redessine_train()
        self.redessineReserve()
    
    def gagnant(self):
        """VueJeu → Joueur
        Retourne le joueur ayant sa réserve vide ou ayant la plus petite somme dans sa réserve
        """
        mini=self.__joueur1.sommeReserve()
        ind=0
        for i in range (len(self.__joueurs)):
            print(self.__joueurs[i].sommeReserve())
            if self.__joueurs[i].sommeReserve() < mini:
                mini = self.__joueurs[i].sommeReserve()
                ind=i
        return self.__joueurs[ind]
    
    def creer_ctrl_boutonTrainMex(self):
        """VueJeu(modif) → None
        Initialise le train sélectionné au train mexicain
        """
        def ctrl_bouton_mex():
            self.__train_select = "train mexicain"
        return ctrl_bouton_mex
    
    def creer_ctrl_boutonTrain1(self):
        """VueJeu(modif) → None
        Initialise le train sélectionné au train du joueur 1
        """
        def ctrl_bouton_1():
            self.__train_select = 1
        return ctrl_bouton_1
    
    def creer_ctrl_boutonTrain2(self):
        """VueJeu(modif) → None
        Initialise le train sélectionné au train du joueur 2
        """
        def ctrl_bouton_2():
            self.__train_select = 2
        return ctrl_bouton_2
    
    def creer_ctrl_boutonTrain3(self):
        """VueJeu(modif) → None
        Initialise le train sélectionné au train du joueur 3
        """
        def ctrl_bouton_3():
            self.__train_select = 3
        return ctrl_bouton_3
    
    def creer_ctrl_boutonTrain4(self):
        """VueJeu(modif) → None
        Initialise le train sélectionné au train du joueur 4
        """
        def ctrl_bouton_4():
            self.__train_select = 4
        return ctrl_bouton_4
    
    def creer_ctrl_bouton_go(self):
        '''VueJeu → None
        Pose un domino
        '''
        def ctrl_bouton_go():
            self.boutonGo()
            if self.__ind == 0:
                self.__BtnGo['text']=" Go ! "
            else:
                self.__BtnGo['text']=" Suivant "
            for j in self.__joueurs:
                if j.reserveVide():
                    self.__LbButton['text'] = "Partie Finie ! Joueur "+j.getName()+" a gagné !"
                    self.__BtnGo['text'] = " Reset "
                    self.__BtnGo['bg'] = 'red'
                    self.__BtnGo['command'] = self.ctrl_reinit
            if self.__jeu.piocheVide():
                self.__LbButton['text'] = "Partie Finie ! Joueur "+self.gagnant().getName()+" a gagné !"
                self.__BtnGo['text'] = "Reset"
                self.__BtnGo['command'] = self.ctrl_reinit
        return ctrl_bouton_go
    
    def boutonGo(self):
        """VueJeu → None
        Pose un domino
        """
        if self.__joueurs[self.__ind].plusGrandDouble() != None and self.__jeu.choixDominoDepart() == False:
            self.__jeu.setDominoDepart(self.__joueurs[self.__ind].plusGrandDouble())
            self.__BtnDepart['image'] = image = self.__images[self.__joueurs[self.__ind].plusGrandDouble().getValeur1()][self.__joueurs[self.__ind].plusGrandDouble().getValeur2()]
            self.__joueurs[self.__ind].delIemeReserve(self.__joueurs[self.__ind].indicePlusGrandDouble())
        elif self.__jeu.choixDominoDepart() == False and self.__tour >=4 :
                self.__jeu.setDominoDepart(self.__jeu.plusGrandDouble())
                self.__BtnDepart['image'] = image = self.__images[self.__jeu.plusGrandDouble().getValeur1()][self.__jeu.plusGrandDouble().getValeur2()]
                self.__jeu.delIemePioche(self.__jeu.indicePlusGrandDouble())
                self.__ind+=1
                self.__tour+=1
        elif self.__jeu.choixDominoDepart() == False and self.__joueurs[self.__ind].plusGrandDouble() == None:
            self.__ind+=1
        else:
            if self.__ind == 0:
                self.__BtnGo['text']=" Go ! "
                fait = False
                if self.__train_select == 1:
                    fait = self.__joueur1.poserDominoDansTrain(self.__jeu,self.__domino_select,fait)
                    self.__joueurs[self.__ind].delIemeReserve(self.__indice_select)
                elif self.__train_select == 2:
                    fait = self.__joueur2.poserDominoDansTrain(self.__jeu,self.__domino_select,fait)
                    self.__joueurs[self.__ind].delIemeReserve(self.__indice_select)
                elif self.__train_select == 3:
                    fait = self.__joueur3.poserDominoDansTrain(self.__jeu,self.__domino_select,fait)
                    self.__joueurs[self.__ind].delIemeReserve(self.__indice_select)
                elif self.__train_select == 4:
                    fait = self.__joueur4.poserDominoDansTrain(self.__jeu,self.__domino_select,fait)
                    self.__joueurs[self.__ind].delIemeReserve(self.__indice_select)
                if fait == False:
                    self.__dominoPlace = self.__joueurs[self.__ind].poserDomino(self.__jeu,self.__domino_select,self.__indice_select,self.__train_select)
                else:
                    self.__dominoPlace = self.__domino_select
            else:
                self.__dominoPlace = self.__joueurs[self.__ind].poserDomino(self.__jeu)
            if self.__dominoPlace != None:
                if not self.__dominoPlace.estDouble():
                    self.__ind+=1
            else:
                self.__ind+=1
            self.__domino_select = None
            self.__indice_select = None
            self.__train_select = None
            self.__dominoPlace = None
            self.__tour+=1
        if self.__ind == 4:
            self.__ind = 0
        self.__LbTour['text']="Au tour de "+self.__joueurs[self.__ind].getName()+" de jouer !"
        self.redessine_train()
        self.redessineReserve()
    
    def on_enter(self,e):
        """VueJeu, Objet → None
        Gère le Motion du bouton
        """
        if e.widget['text']==" Go ! ":
            e.widget['background'] = 'green'
        elif e.widget['text']==" Reset ":
            e.widget['background'] = 'red'
        else:
            e.widget['background'] = 'gold'

    def on_leave(self,e):
        """VueJeu, Objet → None
        Gère le Leave du bouton
        """
        if e.widget['text']==" Go ! ":
            e.widget['background'] = 'light green'
        elif e.widget['text']==" Reset ":
            e.widget['background'] = 'coral'
        else:
            e.widget['background'] = 'pale goldenrod'
        
    def demarre(self):
        """VueJeu → None
        Affiche la fenetre principale
        """
        self.__fen.mainloop()
    
if __name__ == '__main__':
    jeu = JeuMexicain()
    vue = VueJeu(jeu)
    vue.demarre()