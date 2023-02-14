import pygame
import random
import sprite
from planet import planeten

pygame.init()

SCREENSIZE = 1000

display = pygame.display.set_mode((SCREENSIZE, SCREENSIZE))
clock = pygame.time.Clock()
# Titel des Fensters
pygame.display.set_caption("Sonnensystem")

FPS = 120
# Beschleunigung
ACCELERATION = 0.1
        
#################################################################################################################

class stars:
    def __init__(self, x, y, radius, angle,starttime,v):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
        self.time = starttime
        self.R = 0
        self.G = 0
        self.B = 0
        self.R1 = 255
        self.G1 = 255
        self.B1 = 255
        self.v = v
        self.devider = 1*self.v*255*2

    def drawline(self):
        pygame.draw.circle(display, color=(self.R1,self.G1,self.B1), center=(self.x,self.y),radius=self.radius)
        

    def drawstar(self):
        pygame.draw.circle(display, color=(self.R,self.G,self.B), center=(self.x,self.y),radius=self.radius)

    def timer(self):
        if self.time>=0:
            self.time -= self.v

        else:
            self.time = 1
            self.x = random.randint(1,1000)
            self.y = random.randint(1,1000)

    def bright(self):
        if self.time > 0.5 and self.R< 250:
            self.R += self.devider
            self.G += self.devider
            self.B += self.devider
        elif self.R > 5:
            self.R -= self.devider
            self.G -= self.devider
            self.B -= self.devider

    def bright2(self):
        if self.R1> 0:
            self.R1 -= 0.4
            self.G1 -= 0.4
            self.B1 -= 0.4

#################################################################################################################

class Spritesheet(pygame.sprite.Sprite):
    def __init__(self,image) -> None:
        super().__init__()
        self.sheet = image
        

    def get_image(self, frame, width, height, scale, colour):
        image = pygame.Surface((width,height)).convert_alpha()
        # bild, Koordinaten, area vom Sheet Koordinaten
        image.blit(self.sheet, (0,0), (0,frame*height, width, height))
        #größe ändern
        image = pygame.transform.scale(image,(width/scale, height/scale))
        #transparenz
        image.set_colorkey(colour) 
        return image
        
#################################################################################################################

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
                star = stars(random.randint(1,1000),random.randint(1,1000), random.randint(1,3),random.randint(1,360),random.randint(0,1),0.001)
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
        Erde2 = stars(Erde.getx(), Erde.gety(), 1, 30, 5,5)
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