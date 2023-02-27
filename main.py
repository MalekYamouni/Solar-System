import pygame
from pygame import mixer
from random import randint
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

def main():
    # Background Sound
    mixer.music.load('background.mp3')
    mixer.music.play(loops=-1)

    # Images werden geladen und in eine Variable gepackt
    sprite_sheet_image = pygame.image.load('C:/Users/TN-35011/Desktop/Malek/Sonnensystem/earth.png').convert_alpha()
    sprite_sheet_earth = Spritesheet(sprite_sheet_image)

    sprite_sheet_image = pygame.image.load('C:/Users/TN-35011/Desktop/Malek/Sonnensystem/Sun.png').convert_alpha()
    sprite_sheet_sun = Spritesheet(sprite_sheet_image)

    # Planetenobjekte
    sun = Animation(display, [], 11, 90, 0, sprite_sheet_sun, 1, (SCREENSIZE/2)-48, (SCREENSIZE/2)-48, 0, SCREENSIZE)
    sun.animate()
    earth = Animation(display, [], 48, 50, 0, sprite_sheet_earth, 2, 500, 500, 0, SCREENSIZE)
    earth.animate()

    # Sternobjekte 
    Stars = stars(display, randint(1,1000), randint(1,1000), randint(1,3), randint(1,360), 1, 0.001, 0)

    # Schweifobjekte
    earthTail = Tail()
    

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update background
        display.fill((0,0,0))

        # Objekt iteriert durch die Liste
        sun.update()
        earth.update()
        Stars.update()

        # Sterne werden Random erzeugt
        Stars.addStarIfNotEnough()

        # erzeugt den Schweif hinter dem Planeten
        earthTail.newParticle(display, SCREENSIZE)
        earthTail.update()

        # visualisiert die Objekte
        sun.showstatic()
        earth.showmoving()

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
