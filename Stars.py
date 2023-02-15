import pygame
import random

class stars:
    def __init__(self,display, x, y, radius, angle,starttime,v, liste, counter):
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
        self.display = display
        self.liste = liste
        self.counter = counter

    def drawstar(self):
        pygame.draw.circle(self.display, color=(self.R,self.G,self.B), center=(self.x,self.y),radius=self.radius)

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

    def drawstars(self):
        if len(self.liste)<200:
            if self.counter>20:
                star = stars(self.display,random.randint(1,1000),random.randint(1,1000), random.randint(1,3),random.randint(1,360),random.randint(0,1),0.001,[],0)
                self.liste.append(star)
                self.counter = 0
            else:
                self.counter += 1
                
        # Sterne werden gezeichnet haben einen timer, wenn timer 0 erreicht wird das Objekt gelöscht
        for star in self.liste:
            star.drawstar()
            star.timer()
            star.bright()
