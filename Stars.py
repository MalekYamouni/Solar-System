import pygame
import random

class stars:
    def __init__(self,display, x, y, radius, angle,starttime,v):
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

    def drawline(self):
        pygame.draw.circle(self.display, color=(self.R1,self.G1,self.B1), center=(self.x,self.y),radius=self.radius)
        

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

    def bright2(self):
        if self.R1> 0:
            self.R1 -= 0.4
            self.G1 -= 0.4
            self.B1 -= 0.4