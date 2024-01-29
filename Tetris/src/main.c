#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
#include <unistd.h>
#include "Modele.h"
#include "Controleur.h"
#include "Couleur.h"

#ifdef USE_NCURSES
#include <ncurses.h>

// Fonction pour afficher le tableau du jeu en utilisant NCurses
void AfficherTableau() {
    char Tampon[LIGNES][COLONNES] = {};
    for (int i = 0; i < Courante.largeur; i++) {
        for (int j = 0; j < Courante.largeur; j++) {
            if (Courante.tableau[i][j]) {
                Tampon[Courante.ligne + i][Courante.colonne + j] = Courante.tableau[i][j];
            }
        }
    }
    clear();
    for (int i = 0; i < LIGNES; i++) {
        for (int j = 0; j < COLONNES; j++) {
            //attron(COLOR_PAIR(Courante.couleurIndex + 1));
            printw("%c ", (Table[i][j] + Tampon[i][j]) ? 'O' : '.');
            //attroff(COLOR_PAIR(Courante.couleurIndex + 1));
        }
        printw("\n");
    }
}

// Fonction pour afficher le prochain bloc en utilisant NCurses
void AfficherProchainBloc() {
    mvprintw(1, COLONNES * 2 + 5, "Prochain Bloc:");
    for (int i = 0; i < Prochain.largeur; i++) {
        for (int j = 0; j < Prochain.largeur; j++) {
            if (Prochain.tableau[i][j])
                mvprintw(i + 2, COLONNES * 2 + 5 + j * 2, "O");
        }
    }
}

// Fonction pour afficher les informations du jeu en utilisant NCurses
void AfficherInformations() {
    mvprintw(LIGNES + 2, 0, "Score: %d", Score);
    // Ajoutez d'autres informations pertinentes ici si nécessaire
}

// Fonction pour afficher la vue complète du jeu en utilisant NCurses
void AfficherVue() {
    /**start_color();
    init_pair(1, COLOR_RED, COLOR_BLACK);
    init_pair(2, COLOR_GREEN, COLOR_BLACK);
    init_pair(3, COLOR_BLUE, COLOR_BLACK);
    init_pair(4, COLOR_YELLOW, COLOR_BLACK);
    init_pair(5, COLOR_MAGENTA, COLOR_BLACK);
    init_pair(6, COLOR_CYAN, COLOR_BLACK);
    */
    AfficherTableau();
    AfficherProchainBloc();
    AfficherInformations();
    refresh();
}

#endif

#ifdef USE_SDL
#include <SDL.h>
#include <SDL_ttf.h>

// Variables SDL
SDL_Event event;
SDL_Window* fenetre = NULL;
SDL_Renderer* rendu = NULL;
const int TAILLE_CELLULE = 30;  // Ajustez la taille si nécessaire

// Prototypes de fonctions SDL
void initialiserSDL();
void renduJeu();
void nettoyer();

// Fonction pour afficher le tableau du jeu en utilisant SDL
void AfficherTableau() {
    // Logique de rendu avec SDL
    renduJeu();
}

// Initialisation de la bibliothèque SDL
void initialiserSDL() {
    SDL_Init(SDL_INIT_VIDEO);
    TTF_Init();
    fenetre = SDL_CreateWindow("SDL Tetris", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                              (COLONNES + 6) * TAILLE_CELLULE, (LIGNES) * TAILLE_CELLULE, SDL_WINDOW_SHOWN);
    rendu = SDL_CreateRenderer(fenetre, -1, SDL_RENDERER_ACCELERATED);
}

// Chargement d'une police pour afficher le score en utilisant SDL
TTF_Font* chargerPolice(const char* cheminPolice, int taillePolice) {
    TTF_Font* police = TTF_OpenFont(cheminPolice, taillePolice);
    if (!police) {
        fprintf(stderr, "Erreur lors du chargement de la police TTF : %s\n", TTF_GetError());
        // Gérer l'erreur comme nécessaire
    }
    return police;
}

// Rendu du score en utilisant SDL
void renduScore() {
    char texteScore[50];
    sprintf(texteScore, "Score: %d", Score);
    SDL_Rect rectScore = {(COLONNES + 2) * TAILLE_CELLULE, (LIGNES - 1) * TAILLE_CELLULE, 100, 30};

    TTF_Font* police = chargerPolice("./04B_09__.ttf", 16);

    SDL_Color couleurTexte = {255, 255, 255};  // Noir
    SDL_Surface* surfaceTexte = TTF_RenderText_Solid(police, texteScore, couleurTexte);

    SDL_Texture* textureTexte = SDL_CreateTextureFromSurface(rendu, surfaceTexte);

    SDL_RenderCopy(rendu, textureTexte, NULL, &rectScore);

    SDL_FreeSurface(surfaceTexte);
    SDL_DestroyTexture(textureTexte);
    TTF_CloseFont(police);
}

// Rendu du jeu en utilisant SDL
void renduJeu() {
    SDL_SetRenderDrawColor(rendu, 0, 0, 0, 255);
    SDL_RenderClear(rendu);

    SDL_SetRenderDrawColor(rendu, 255, 255, 255, 255);
    SDL_Rect rectBordure = {0, 0, COLONNES * TAILLE_CELLULE + 2, LIGNES * TAILLE_CELLULE + 2};
    SDL_RenderDrawRect(rendu, &rectBordure);

    for (int i = 0; i < LIGNES; i++) {
        for (int j = 0; j < COLONNES; j++) {
            if (Table[i][j]) {
                SDL_Rect rectCellule = {j * TAILLE_CELLULE, i * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE};
                SDL_SetRenderDrawColor(rendu, 192, 192, 192, 255);
                SDL_RenderFillRect(rendu, &rectCellule);
            }
        }
    }

    SDL_SetRenderDrawColor(rendu, 255, 255, 255, 255);
    for (int i = 0; i <= LIGNES; i++) {
        SDL_RenderDrawLine(rendu, 0, i * TAILLE_CELLULE, COLONNES * TAILLE_CELLULE, i * TAILLE_CELLULE);
    }
    for (int j = 0; j <= COLONNES; j++) {
        SDL_RenderDrawLine(rendu, j * TAILLE_CELLULE, 0, j * TAILLE_CELLULE, LIGNES * TAILLE_CELLULE);
    }

    for (int i = 0; i < Courante.largeur; i++) {
        for (int j = 0; j < Courante.largeur; j++) {
            if (Courante.tableau[i][j]) {
                SDL_Rect rectCellule = {(Courante.colonne + j) * TAILLE_CELLULE, (Courante.ligne + i) * TAILLE_CELLULE,
                                         TAILLE_CELLULE, TAILLE_CELLULE};
                SDL_SetRenderDrawColor(rendu, listeCouleurs[Courante.couleurIndex].r,
                                       listeCouleurs[Courante.couleurIndex].g,
                                       listeCouleurs[Courante.couleurIndex].b, 255);
                SDL_RenderFillRect(rendu, &rectCellule);
            }
        }
    }

    for (int i = 0; i < Prochain.largeur; i++) {
        for (int j = 0; j < Prochain.largeur; j++) {
            if (Prochain.tableau[i][j]) {
                SDL_Rect rectCellule = {(COLONNES + 1 + j) * TAILLE_CELLULE, (i + 1) * TAILLE_CELLULE, TAILLE_CELLULE, TAILLE_CELLULE};
                SDL_SetRenderDrawColor(rendu, listeCouleurs[Prochain.couleurIndex].r,
                                       listeCouleurs[Prochain.couleurIndex].g,
                                       listeCouleurs[Prochain.couleurIndex].b, 255);
                SDL_RenderFillRect(rendu, &rectCellule);
            }
        }
    }
    renduScore();
    SDL_RenderPresent(rendu);
}

// Nettoyage des ressources SDL
void nettoyer() {
    SDL_DestroyRenderer(rendu);
    SDL_DestroyWindow(fenetre);
    SDL_Quit();
}
#endif

// Fonction principale
int main() {
    srand((unsigned int)time(NULL));
    InitialiserJeu();
    MettreAJour();

#ifdef USE_NCURSES
    int touche;
    initscr();
    keypad(stdscr, TRUE);
    struct timeval avant, apres;
    gettimeofday(&avant, NULL);
    nodelay(stdscr, VRAI);
    AfficherVue();
#endif

#ifdef USE_SDL
    initialiserSDL();
    struct timeval avant, apres;
    gettimeofday(&avant, NULL);
    AfficherTableau();
#endif

    // Boucle principale du jeu
    while (JeuEnCours) {
#ifdef USE_NCURSES
        if ((touche = getch()) != ERR) {
            GestionEvenementNcurses(touche);
            AfficherVue();
        }
        gettimeofday(&apres, NULL);
        if (((double)apres.tv_sec * 1000000 + (double)apres.tv_usec) - ((double)avant.tv_sec * 1000000 + (double)avant.tv_usec) > Minuteur) {
            avant = apres;
            GestionEvenementNcurses(KEY_DOWN);
            AfficherVue();
        }
        refresh();
#endif

#ifdef USE_SDL
        while (SDL_PollEvent(&event)) {
            if (event.type == SDL_QUIT) {
                JeuEnCours = FAUX;
            }
            GestionEvenementSDL(event);
        }
        gettimeofday(&apres, NULL);
        if (((double)apres.tv_sec * 1000000 + (double)apres.tv_usec) -
            ((double)avant.tv_sec * 1000000 + (double)avant.tv_usec) > Minuteur) {
            avant = apres;
            SDL_Event event_down;
            event_down.type = SDL_KEYDOWN;
            event_down.key.keysym.sym = SDLK_DOWN;
            GestionEvenementSDL(event_down);
        }
        AfficherTableau();
#endif
    }

    SupprimerTetrimino(Courante);
    SupprimerTetrimino(Prochain);

#ifdef USE_NCURSES
    refresh();
    endwin();
#endif

#ifdef USE_SDL
    nettoyer();
#endif
    return 0;
}
