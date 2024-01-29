#ifndef CONTROLEUR_H
#define CONTROLEUR_H

#ifdef USE_NCURSES
#include <ncurses.h>
void GestionEvenementNcurses(int touche);
#endif

#ifdef USE_SDL
#include <SDL.h>
void GestionEvenementSDL(SDL_Event event);
#endif

#endif // CONTROLEUR_H
