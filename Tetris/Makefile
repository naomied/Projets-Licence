# Makefile

# Compilateur
CC = gcc

# Drapeaux du compilateur
CFLAGS = -Wall -std=c99 -g

# Bibliothèques et drapeaux
LIBS = `sdl2-config --libs --cflags` -lcurses -lSDL2_ttf -lm

# Fichiers source
SRC = src/*.c

# Binaire de sortie
TARGET = bin/game

# Définition des drapeaux pour les différentes constructions
NCURSES_FLAGS = -DUSE_NCURSES
SDL_FLAGS = -DUSE_SDL

# Commande pour exécuter le programme avec ncurses
RUN_NCURSE_CMD = ./$(TARGET)
RUN_SDL_CMD = ./$(TARGET)

# Cible par défaut
all: ncurses sdl

# Construction avec ncurses
ncurses:
	$(CC) $(CFLAGS) $(LIBS) $(SRC) -o $(TARGET) $(NCURSES_FLAGS)

# Construction avec SDL
sdl:
	$(CC) $(CFLAGS) $(LIBS) $(SRC) -o $(TARGET) $(SDL_FLAGS)

# Exécuter le programme avec ncurses
run_ncurse: ncurses
	$(RUN_NCURSE_CMD)

# Exécuter le programme avec SDL
run_sdl: sdl
	$(RUN_SDL_CMD)

# Nettoyer
clean:
	rm -f $(TARGET)
