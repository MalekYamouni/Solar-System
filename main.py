import pygame
import random
from planet import planeten
from Image import Spritesheet
from Stars import stars
from animation import Animation
from tail import Tail

pygame.init()

SCREENSIZE = 1000

display = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))
clock = pygame.time.Clock()
pygame.display.set_caption("Sonnensystem")

FPS = 120
# Beschleunigung

def main():
    # Planeten Objekte
    #Sonne = planeten(display,SCREENSIZE/2, SCREENSIZE/2, 0, 70, (200, 100, 0),0,0,0, SCREENSIZE)
    #Erde = planeten(display,SCREENSIZE/2-50, SCREENSIZE/2-50, 0.001, 15, "green", 23.5, 23.5, 1, SCREENSIZE)

    # Images werden geladen und in eine Variable gepackt
    sprite_sheet_image = pygame.image.load('earth.png').convert_alpha()
    sprite_sheet_earth = Spritesheet(sprite_sheet_image)

    sprite_sheet_image = pygame.image.load('Sun.png').convert_alpha()
    sprite_sheet_sun = Spritesheet(sprite_sheet_image)

    # Hintergrund
    BLACK = (0,0,0)

    # Animation 
    sun = Animation(display, [], 11, 90, 0, sprite_sheet_sun, 1, (SCREENSIZE/2)-48, (SCREENSIZE/2)-48, 0, SCREENSIZE)
    sun.animate()

    earth = Animation(display, [], 48, 50, 0, sprite_sheet_earth, 2, (SCREENSIZE/2)-48, (SCREENSIZE/2)-48, 23.5, SCREENSIZE)
    earth.animate()

    star = stars(display,random.randint(1,1000),random.randint(1,1000), random.randint(1,3),random.randint(1,360),random.randint(0,1),0.001,[],0)

    earthtail = Tail(display,[],1, 30, SCREENSIZE/2, SCREENSIZE/2, SCREENSIZE, 0)
    

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #update background
        display.fill((0,0,0))

        # Objekt iteriert durch die Liste
        sun.update()
        earth.update()

        # Sterne werden Random erzeugt
        star.drawstars()

        # erzeugt den Schweif hinter dem Planeten
        earthtail.drawtail2()

        # visualisiert die Objekte
        sun.showstatic()
        #earth.showmoving()

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()