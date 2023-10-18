from tkinter import *
from modele import ModeleSame

class VueSame:
    '''Classe VueSame qui modélise la vue du jeu Same'''
    
    def __init__(self, same):
        #initialisation
        self.__same = same
        self.__mat = same.mat()
        self.__lig = same.nblig()
        self.__col = same.nbcol()
        self.__color = same.nbcolor()
        
        #fenêtre
        fen = Tk()
        fen.title(" Same Game ")
        self.__fen = fen
        
        #sous-fenêtre
        self.__frPlateau = Frame(fen)
        frBtn = Frame(fen)
        
        #initialisation images
        l = ["1", "2", "3", "4", "5", "6", "vide"]
        self.__images = []
        for i in l:
            img = PhotoImage(file="img/medium_sphere"+i+".gif")
            self.__images.append(img)
        
        l = ["1", "2", "3", "4", "5", "6"]
        self.__black_images = []
        for i in l:
            img = PhotoImage(file="img/medium_sphere"+i+"black.gif")
            self.__black_images.append(img)
            
        #frPlateau
        self.__les_btns = []
        for i in range(self.__lig):
            lig = []
            for j in range(self.__col):
                btn = Button(self.__frPlateau, image = self.__images[self.__same.couleur(i, j)], command = self.creer_controleur_btn(i, j))
                btn.grid(row=i, column=j)
                btn.bind('<Motion>', self.creer_ctrl_black(i, j))
                btn.bind('<Leave>', self.creer_ctrl_white(i, j))
                lig.append(btn)
            self.__les_btns.append(lig)
        self.__frPlateau.grid(row = 0, column = 0)
        
        #frBtn
            #LbScoreSurvolée
        self.__LbNewScore = Label(frBtn, fg="blue")
        self.__LbNewScore.pack()
            #LbScore
        self.__LbScore = Label(frBtn, text="Score: " + str(self.__same.score()), fg="red")
        self.__LbScore.pack()
            #Recommencer
        BtnReplay = Button(frBtn, text="Nouveau", command = self.nouvelle_partie)
        BtnReplay.pack()
            #Quitter
        BtnExit = Button(frBtn, text="Au revoir", command = fen.destroy)
        BtnExit.pack()
        frBtn.grid(row = 0, column = 1)
        
        self.__fen.mainloop()
        
    def redessine(self):
        for i in range(self.__lig):
            for j in range(self.__col):
                if self.__same.couleur(i, j) == -1:
                    self.__les_btns[i][j]['image'] = self.__images[self.__color]
                else:
                    self.__les_btns[i][j]['image'] = self.__images[self.__same.couleur(i, j)]
        self.__LbScore['text'] = "Score: " + str(self.__same.score())
        self.__same.recalcule_composantes()
    
    def nouvelle_partie(self):
        self.__same.nouvelle_partie()
        self.redessine()
    
    def creer_controleur_btn(self, i, j):
        def controleur_btn():
            self.__same.supprime_composante(self.__same.composante(i,j))
            self.redessine()
            self.__LbScore['text'] = "Score: " + str(self.__same.score())
        return controleur_btn
    
    def creer_ctrl_black(self, i, j):
        def ctrl_black(event):
            compo = self.__same.composante(i, j)
            for r in range (self.__lig):
                for c in range (self.__col):
                    if self.__same.composante(r, c) == compo and not self.__same.est_vide(r, c):
                        self.__les_btns[r][c]['image'] = self.__black_images[self.__same.couleur(r, c)]
            if compo != 0 and self.__same.nb_elts_compo(compo) > 1:
                self.__LbNewScore['text'] = "Score sélection : " + str((self.__same.nb_elts_compo(compo)-2)**2)
        return ctrl_black
    
    def creer_ctrl_white(self, i, j):
        def ctrl_white(event):
            compo = self.__same.composante(i, j)
            for r in range (self.__lig):
                for c in range (self.__col):
                    if self.__same.composante(r, c) == compo and not self.__same.est_vide(r, c):
                        self.__les_btns[r][c]['image'] = self.__images[self.__same.couleur(r, c)]
            self.__LbNewScore['text'] = "Score sélection : 0"
        return ctrl_white
    
if __name__ == '__main__':
    # création du modèle
    same = ModeleSame()
    # création de la vue qui crée les contrôleurs
    # et lance la boucle d’écoute des évts
    vue = VueSame(same)
        
