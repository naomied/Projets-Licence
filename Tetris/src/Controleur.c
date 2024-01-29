#include "Controleur.h"
#include "Modele.h"
#include <ncurses.h>
#include <SDL.h>

// Fonction pour gérer les événements ncurses
void GestionEvenementNcurses(int touche)
{
    Tetrimino tmp = CopierTetrimino(Courante); // Copie du tetrimino courant
    switch (touche) // Selon la touche appuyée
    {
    case KEY_LEFT:
        DeplacerGauche(tmp); // Déplacer le tetrimino vers la gauche
        break;
    case KEY_RIGHT:
        DeplacerDroite(tmp); // Déplacer le tetrimino vers la droite
        break;
    case KEY_DOWN:
        Descendre(tmp); // Faire descendre le tetrimino
        break;
    case KEY_UP:
        Tourner(tmp); // Faire tourner le tetrimino
        break;
    }
    SupprimerTetrimino(tmp); // Suppression de la copie du tetrimino
}

// Fonction pour gérer les événements SDL
void GestionEvenementSDL(SDL_Event event)
{
    Tetrimino tmp = CopierTetrimino(Courante); // Copie du tetrimino courant
    switch (event.type) // Selon le type d'événement
    {
    case SDL_KEYDOWN: // Si une touche est enfoncée
        switch (event.key.keysym.sym) // Selon la touche
        {
        case SDLK_LEFT:
            DeplacerGauche(tmp); // Déplacer le tetrimino vers la gauche
            break;
        case SDLK_RIGHT:
            DeplacerDroite(tmp); // Déplacer le tetrimino vers la droite
            break;
        case SDLK_DOWN:
            Descendre(tmp); // Faire descendre le tetrimino
            break;
        case SDLK_UP:
            Tourner(tmp); // Faire tourner le tetrimino
            break;
        }
        break;
    }
    SupprimerTetrimino(tmp); // Suppression de la copie du tetrimino
}