import pygame
import math

class Animation:
    def __init__(self,display, animation_list:list, animation_steps:int, animation_cooldown:int,frame, sprite_sheet,scale, x, y, angle, SCREENSIZE):
        self.animation_list = animation_list
        self.animation_steps = animation_steps
        self.animation_cooldown = animation_cooldown
        self.frame = frame
        self.spritesheet = sprite_sheet
        self.display = display
        self.BG = (0,0,0)
        self.last_update = pygame.time.get_ticks()
        self.x = x
        self.y = y
        self.scale = scale
        self.angle = angle
        self.SCREENSIZE = SCREENSIZE

    # fügt die Spritesheetobjekte einer Liste hinzu
    def animate(self):
        for x in range(self.animation_steps):
            self.animation_list.append(self.spritesheet.get_image(x, 96, 96, self.scale, self.BG))
    # iteriert durch die Liste animation_list um die Koordinate des jeweiligen Orts im Sheet
    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list):
                self.frame = 0

        self.angle += 0.003
        if self.angle >= math.pi*2:
            self.angle -= math.pi*2

    def getx(self):
        self.currentx = self.x*math.cos(self.angle)+self.SCREENSIZE*0.5
        self.currentx -= 24
        return self.currentx

    def gety(self):
        self.currenty = self.y*math.sin(self.angle)+self.SCREENSIZE*0.5
        self.currenty -= 24
        return self.currenty

    def showstatic(self):
        self.display.blit(self.animation_list[self.frame],((self.x),(self.y)))

    def showmoving(self):
        self.display.blit(self.animation_list[self.frame],((self.getx()),(self.gety())))
