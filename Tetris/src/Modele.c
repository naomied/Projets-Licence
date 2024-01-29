// Modele.c

#include <stdio.h>
#include <stdlib.h>
#include "Modele.h"
#include "Couleur.h"

// Déclaration et initialisation des variables globales
char Table[LIGNES][COLONNES] = {};
int Score = 0;
char JeuEnCours = VRAI;
double Minuteur = 500000;
Tetrimino Courante;
Tetrimino Prochain;

Couleur listeCouleurs[] = {
        {203, 67, 53},   // Rouge
        {40, 180, 99},   // Vert
        {40, 116, 166},   // Bleu
        {241, 196, 15}, // Jaune
        {155, 89, 182},  // Magenta
        {253, 108, 158}  // Rose
};

// Déclaration des formes de tétriminos avec leurs rotations possibles
const Tetrimino TableauTetriminos[7]= {
    {(char *[]){(char []){0,1,1},(char []){1,1,0}, (char []){0,0,0}}, 3}, // S_tetrimino
    {(char *[]){(char []){1,1,0},(char []){0,1,1}, (char []){0,0,0}}, 3}, // Z_tetrimino
    {(char *[]){(char []){0,1,0},(char []){1,1,1}, (char []){0,0,0}}, 3}, // T_tetrimino
    {(char *[]){(char []){0,0,1},(char []){1,1,1}, (char []){0,0,0}}, 3}, // L_tetrimino
    {(char *[]){(char []){1,0,0},(char []){1,1,1}, (char []){0,0,0}}, 3}, // J_tetrimino
    {(char *[]){(char []){1,1},(char []){1,1}}, 2}, // O_tetrimino
    {(char *[]){(char []){0,0,0,0}, (char []){1,1,1,1}, (char []){0,0,0,0}, (char []){0,0,0,0}}, 4} // I_tetrimino
};

// Fonction pour copier un tétrimino
Tetrimino CopierTetrimino(Tetrimino tetrimino){
    Tetrimino nouveauTetrimino = tetrimino;
    char **copieTetrimino = tetrimino.tableau;
    nouveauTetrimino.tableau = (char**)malloc(nouveauTetrimino.largeur * sizeof(char*));
    int i, j;
    for(i = 0; i < nouveauTetrimino.largeur; i++){
        nouveauTetrimino.tableau[i] = (char*)malloc(nouveauTetrimino.largeur * sizeof(char));
        for(j = 0; j < nouveauTetrimino.largeur; j++) {
            nouveauTetrimino.tableau[i][j] = copieTetrimino[i][j];
        }
    }
    return nouveauTetrimino;
}

// Fonction pour libérer la mémoire occupée par un tétrimino
void SupprimerTetrimino(Tetrimino tetrimino){
    int i;
    for(i = 0; i < tetrimino.largeur; i++){
        free(tetrimino.tableau[i]);
    }
    free(tetrimino.tableau);
}

// Fonction pour vérifier la position d'un tétrimino dans le tableau
int VerifierPosition(Tetrimino tetrimino){
    char **tableau = tetrimino.tableau;
    int i, j;
    for(i = 0; i < tetrimino.largeur; i++) {
        for(j = 0; j < tetrimino.largeur ;j++){
            if((tetrimino.colonne+j < 0 || tetrimino.colonne+j >= COLONNES || tetrimino.ligne+i >= LIGNES)){
                if(tableau[i][j])
                    return FAUX;
            }
            else if(Table[tetrimino.ligne+i][tetrimino.colonne+j] && tableau[i][j])
                return FAUX;
        }
    }
    return VRAI;
}

// Fonction pour obtenir un nouveau tétrimino aléatoire
Tetrimino ObtenirNouveauTetrimino(){
    Tetrimino nouveauTetrimino = CopierTetrimino(TableauTetriminos[rand()%7]);

    nouveauTetrimino.colonne = (COLONNES-nouveauTetrimino.largeur)/2;
    nouveauTetrimino.ligne = 0;
    nouveauTetrimino.couleurIndex = rand() % (sizeof(listeCouleurs) / sizeof(listeCouleurs[0]));
    
    return nouveauTetrimino;
}

// Fonction pour initialiser le jeu
void InitialiserJeu(){
    Prochain = ObtenirNouveauTetrimino();
    Score = 0;
}

// Fonction pour tourner un tétrimino
void TournerTetrimino(Tetrimino tetrimino){
    Tetrimino temp = CopierTetrimino(tetrimino);
    int i, j, k, largeur;
    largeur = tetrimino.largeur;
    for(i = 0; i < largeur ; i++){
        for(j = 0, k = largeur-1; j < largeur ; j++, k--){
                tetrimino.tableau[i][j] = temp.tableau[k][i];
        }
    }
    SupprimerTetrimino(temp);
}

// Fonction pour écrire le tétrimino dans le tableau de jeu
void EcrireDansTableau(){
    int i, j;
    for(i = 0; i < Courante.largeur ;i++){
        for(j = 0; j < Courante.largeur ; j++){
            if(Courante.tableau[i][j])
                Table[Courante.ligne+i][Courante.colonne+j] = Courante.tableau[i][j];
        }
    }
}

// Fonction pour traiter les lignes complètes
void LigneComplete(){
    int i, j, somme, count=0;
    for(i=0; i < LIGNES; i++){
        somme = 0;
        for(j=0; j < COLONNES; j++) {
            somme += Table[i][j];
        }
        if(somme == COLONNES){
            count++;
            int l, k;
            for(k = i; k >= 1; k--)
                for(l=0; l < COLONNES; l++)
                    Table[k][l] = Table[k-1][l];
            for(l=0; l < COLONNES; l++)
                Table[k][l] = 0;
        }
    }
    Minuteur -= 1000;
    Score += 100*count;
}

// Fonction pour mettre à jour le tétrimino courant et le prochain tétrimino
void MettreAJour() {
    SupprimerTetrimino(Courante);
    Courante = Prochain;
    Prochain = ObtenirNouveauTetrimino();
    if (!VerifierPosition(Courante)) {
        JeuEnCours = FAUX;
    }
}

// Fonctions pour déplacer le tétrimino
void DeplacerGauche(Tetrimino tmp) {
    tmp.colonne--;
    if (VerifierPosition(tmp)) {
        Courante.colonne--;
    }
}

void DeplacerDroite(Tetrimino tmp) {
    tmp.colonne++;
    if (VerifierPosition(tmp)) {
        Courante.colonne++;
    }
}

void Descendre(Tetrimino tmp) {
    tmp.ligne++;
    if (VerifierPosition(tmp)) {
        Courante.ligne++;
    } else {
        EcrireDansTableau();
        LigneComplete();
        MettreAJour();
    }
}

void Tourner(Tetrimino tmp) {
    TournerTetrimino(tmp);
    if (VerifierPosition(tmp)) {
        TournerTetrimino(Courante);
    }
}
