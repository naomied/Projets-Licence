from random import *

class Case:
    """Classe Case qui modélise une bille du jeu Same."""
    
    def __init__(self, couleur):
        """Case, int -> Case
        constructeur de la classe Case
        """
        self.__couleur = couleur
        self.__compo = -1
    
    def couleur(self):
        """Case -> int
        retourne la valeur de la couleur de la bille
        """
        return self.__couleur
    
    def change_couleur(self, valeur):
        """Case, int -> Case
        modifie la couleur de la bille
        """
        self.__couleur = valeur
    
    def supprime(self):
        """Case -> Case
        enlève la bille de la case (passe la couleur à -1)
        """
        self.__couleur = -1
        self.__compo = 0
    
    def est_vide(self):
        """Case -> Boolean
        indique si la case est vide
        """
        return (self.__couleur == -1)
    
    def composante(self):
        """Case -> int
        retourne le numéro de la composante
        """
        return self.__compo
    
    def pose_composante(self,i):
        """Case, int -> Case
        affecte l'entier en paramètre comme numéro de composante pour la case
        """
        self.__compo = i
        
    def supprime_compo(self):
        """Case -> Case
        désaffecte un numéro de composante à la case en le remettant à −1.
        Si la case est vide son numéro de composante sera égal à 0 :
        """
        if self.__compo != 0:
            self.__compo = -1
    
    def parcourue(self):
        """Case -> Case
        teste si la case a eté affectée à un numéro de composante
        """
        if self.__compo == -1:
            return False
        return True

class ModeleSame:
    """Classe ModeleSame qui modélise le modèle pour le jeu Same."""
    
    def __init__(self, nblig=15, nbcol=20, nbcolor=6):
        """ModeleSame, int, int, int -> ModeleSame
        constructeur de la classe ModeleSame
        """
        self.__nblig = nblig
        self.__nbcol = nbcol
        self.__nbcolor = nbcolor
        self.__mat = []
        for i in range(self.__nblig):
            lig = []
            for j in range(self.__nbcol):
                lig.append(Case(randint(0, (self.__nbcolor - 1))))
            self.__mat.append(lig)
        self.__score = 0
        self.__nb_elts_compo = []
        
        #lance le calcul des composantes
        self.calcule_composantes()
    
    def nb_elts_compo(self, compo):
        return self.__nb_elts_compo[compo]
    
    def score(self):
        """ModeleSame -> int
        retourne le score du joueur
        """
        return self.__score
    
    def nblig(self):
        """ModeleSame -> int
        retourne le nombre de ligne du jeu
        """
        return self.__nblig
    
    def nbcol(self):
        """ModeleSame -> int
        retourne le nombre de colonne du jeu
        """
        return self.__nbcol
    
    def nbcolor(self):
        """ModeleSame -> int
        retourne le nombre de couleur du jeu
        """
        return self.__nbcolor
    
    def mat(self):
        """ModeleSame -> list
        retourne la matrice du jeu
        """
        return self.__mat
    
    def coords_valides(self, i, j):
        """ModeleSame, int, int -> boolean
        indique si les coordonnées (i, j) sont valides pour le jeu
        """
        return (i >= 0 and i < self.__nblig and j >= 0 and j < self.__nbcol)
    
    def couleur(self, i, j):
        """ModeleSame, int, int -> int
        retourne la couleur de la bille en (i, j)
        """
        return self.__mat[i][j].couleur()
    
    def supprime_bille(self, i, j):
        """ModeleSame, int, int -> ModeleSame
        supprime la bille en (i, j)
        """
        self.__mat[i][j].supprime()
    
    def nouvelle_partie(self):
        """ModeleSame -> void
        ré-initialise toutes les cases en changeant leur couleur
        (par une couleur choisie aleatoirement dans l’intervalle des couleurs possibles)
        Il n’y a plus de cases vides apres l’appel à cette méthode
        """
        self.__mat = []
        for i in range(self.__nblig):
            lig = []
            for j in range(self.__nbcol):
                lig.append(Case(randint(0, (self.__nbcolor - 1))))
            self.__mat.append(lig)
        self.__score = 0
    
    def affiche_matrice(self):
        case=0
        for i in range(self.__nblig):
            for j in range(self.__nbcol):
                case+=1
                print("Case"+str(case)+" ligne: "+str(i)+" colone:"+str(j)+" couleur: "+str(self.couleur(i,j))+" composante:"+str(self.composante(i,j)))
        
    def composante(self,i,j):
        """ModeleSame, int, int -> ModeleSame
        retourne la composante de la case (i,j)
        """
        return self.__mat[i][j].composante()
    
    def calcule_composantes(self):
        """ModeleSame -> void
        calcule la composante pour toutes les cases du plateau
        """
        self.__nb_elts_compo = [0]
        num_compo = 1
        for i in range(len(self.__mat)):
            for j in range(len(self.__mat[i])):
                if self.composante(i,j) == -1:
                    coul = self.couleur(i,j)
                    self.__nb_elts_compo.append(self.calcule_composante_numero(i, j,num_compo,coul))
                    num_compo+=1
                    
    def calcule_composante_numero(self,i,j,num_compo,couleur):
        """ModeleSame, int, int, int, int -> int
        calcule la composante de la case(i,j) et ses cases adjacentes
        retourne le nombre d'éléments de num_compo
        """
        if  self.coords_valides(i,j) and self.couleur(i,j)==couleur and  not self.__mat[i][j].parcourue():
            self.__mat[i][j].pose_composante(num_compo)
            
            return self.calcule_composante_numero(i+1,j,num_compo,couleur) + self.calcule_composante_numero(i-1,j,num_compo,couleur) + self.calcule_composante_numero(i,j+1,num_compo,couleur) + self.calcule_composante_numero(i,j-1,num_compo,couleur)+1
        else:
            return 0
        
    def recalcule_composantes(self):
        """ModeleSame -> void
        supprime la composante attribuée à chaque case et relance le calcule des composantes
        """
        for i in range(len(self.__mat)):
            for j in range(len(self.__mat[i])):
                self.__mat[i][j].supprime_compo()

        self.calcule_composantes()
    
    def supprime_composante(self, num_compo):
        """ModeleSame(modif) -> void
           Méthode qui supprime toutes les billes de la composante seulement si elle contient au minimum 2 billes"""
        if self.__nb_elts_compo[num_compo] > 1:
            self.__score += (self.__nb_elts_compo[num_compo]-2)**2
            for j in range(len(self.__mat[0])):
                self.supprime_composante_colonne(j, num_compo)
            self.supprime_colonnes_vides()
            self.calcule_composantes()
            return True
        return False
        
    def est_vide(self, i, j):
        """ ModeleSame, int, int --> Booleen """

        return self.__mat[i][j].est_vide()

    def supprime_composante_colonne(self, j, num):
        """ModeleSame, int, int --> void"""

        for ligne in range(len(self.__mat)):
            if self.__mat[ligne][j].composante() == num:
                self.supprime_bille(ligne, j)
                if ligne !=0:
                    var = self.__mat[ligne][j]
                    for i in range(ligne,0,-1):
                        self.__mat[i][j] = self.__mat[i-1][j]
                    self.__mat[0][j] = var
        
    def supprime_colonnes_vides(self):
        """ ModeleSame -> void
        Décale les colonnes vides vers la droite de la matrice
        """
        for i in range(len(self.__mat[0])):
            if self.est_colonne_vide(i):
                col_vide = self.trouve_colonne_vide()
                for i in range(len(col_vide)):
                    self.decale_colonne(col_vide[i]-i)

    def est_colonne_vide(self,j):
        '''ModeleSame, int -> None
        '''
        for i in range(len(self.__mat)):
            if (not(self.est_vide(i,j))):
                return False
        return True

    def trouve_colonne_vide(self):
        '''Modelesame -> list
        '''
        l_var =[]
        l_cmpt= []
        for i in range(len(self.__mat[0])):
            if self.est_colonne_vide(i):
                l_cmpt += [i]
            else:
                l_var += l_cmpt
                l_cmpt = []
        return l_var

    def decale_colonne(self,j):
        '''ModeleSame, int -> None
        '''
        for ligne in range(len(self.__mat)):
            var = self.__mat[ligne][j]
            for i in range(j,len(self.__mat[0])-1):
                self.__mat[ligne][i] = self.__mat[ligne][i+1]
            self.__mat[ligne][len(self.__mat[0])-1] = var
                    
                    
        
        
        
        
                
        
