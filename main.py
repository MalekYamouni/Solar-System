import pygame
import random
import sprite
from planet import planeten
from Image import Spritesheet
from Stars import stars

pygame.init()

SCREENSIZE = 1000

display = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))
clock = pygame.time.Clock()
# Titel des Fensters
pygame.display.set_caption("Sonnensystem")

FPS = 120
# Beschleunigung
ACCELERATION = 0.1

def main():
    # Sonne Objekt
    Sonne = planeten(display,SCREENSIZE/2, SCREENSIZE/2, 0, 70, (200, 100, 0),0,0,0, SCREENSIZE)
    # Erde Objekt
    Erde = planeten(display,SCREENSIZE/2-50, SCREENSIZE/2-50, 0.001, 15, "green", 23.5, 23.5, 1, SCREENSIZE)

    # Image Erde wird geladen und in eine Variable gepackt
    sprite_sheet_image = pygame.image.load('earth.png').convert_alpha()
    sprite_sheet_earth = Spritesheet(sprite_sheet_image)

    # Image Sonne wird geladen und in eine Variable gepackt
    sprite_sheet_image = pygame.image.load('Sun.png').convert_alpha()
    sprite_sheet_sun = Spritesheet(sprite_sheet_image)

    # Hintergrund
    BLACK = (0,0,0)

    # Animation Sonne
    animation_list_sun = []
    animation_steps_sun = 11
    last_update_sun = pygame.time.get_ticks()
    animation_cooldown_sun = 90
    frame_sun = 0

    # Animation Erde
    animation_list_earth = []
    animation_steps_earth = 48
    last_update_earth = pygame.time.get_ticks()
    animation_cooldown_earth = 50
    frame_earth = 0

    for x in range(animation_steps_earth):
       animation_list_earth.append(sprite_sheet_earth.get_image(x, 96, 96, 2, BLACK))

    for x in range(animation_steps_sun):
        animation_list_sun.append(sprite_sheet_sun.get_image(x, 96, 96, 1, BLACK))

    # Sterneliste
    starsi = []
    # Sternedelay Zähler
    waitcounter = 0
    # Schweifliste
    starchain = []
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #update background
        display.fill((0,0,0))

        
        #update animation earth
        current_time_earth = pygame.time.get_ticks()
        if current_time_earth - last_update_earth >= animation_cooldown_earth:
            frame_earth += 1
            last_update_earth = current_time_earth
            if frame_earth >= len(animation_list_earth):
                frame_earth = 0

        # update animation sun
        current_time_sun = pygame.time.get_ticks()
        if current_time_sun - last_update_sun >= animation_cooldown_sun:
            frame_sun += 1
            last_update_sun = current_time_sun
            if frame_sun >= len(animation_list_sun):
                frame_sun = 0


        # Anzahl der Sterne die Random erzeugt werden
        if len(starsi)<200:
            if waitcounter>20:
                star = stars(display,random.randint(1,1000),random.randint(1,1000), random.randint(1,3),random.randint(1,360),random.randint(0,1),0.001)
                starsi.append(star)
                waitcounter = 0
            else:
                waitcounter += 1

        # Sterne werden gezeichnet haben einen timer, wenn timer 0 erreicht wird das Objekt gelöscht
        for star in starsi:
            star.drawstar()
            star.timer()
            star.bright()

        
        # Schweif hat die Werte des Erde2 Objekt
        Erde2 = stars(display,Erde.getx(), Erde.gety(), 1, 30, 5,5)
        starchain.append(Erde2)

        # Schweif wird gezeichnet, Helligkeit sinkt auf 0 und Objekt wird gelöscht
        for i in starchain:
            
            i.drawline()
            i.bright2()
            if i.R1 < 1:
                del starchain[0]

         # show frame image
        display.blit(animation_list_earth[frame_earth],(Erde.getx()-24,Erde.gety()-24))
        display.blit(animation_list_sun[frame_sun],((SCREENSIZE/2)-48,(SCREENSIZE/2)-48))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()