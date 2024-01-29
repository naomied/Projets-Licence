// modele.h

#ifndef MODELE_H
#define MODELE_H

#define LIGNES 20
#define COLONNES 11
#define VRAI 1
#define FAUX 0

typedef struct {
    char **tableau;
    int largeur, ligne, colonne;
    int couleurIndex;
} Tetrimino;

extern char Table[LIGNES][COLONNES];
extern int Score;
extern char JeuEnCours;
extern double Minuteur;
extern Tetrimino Courante;
extern Tetrimino Prochain;

Tetrimino CopierTetrimino(Tetrimino tetrimino);
void SupprimerTetrimino(Tetrimino tetrimino);
int VerifierPosition(Tetrimino tetrimino);
Tetrimino ObtenirNouveauTetrimino();
void TournerTetrimino(Tetrimino tetrimino);
void EcrireDansTableau();
void LigneComplete();
void InitialiserJeu();
void MettreAJour();
void DeplacerGauche(Tetrimino tmp);
void DeplacerDroite(Tetrimino tmp);
void Descendre(Tetrimino tmp);
void Tourner(Tetrimino tmp);
#endif  // MODELE_H
