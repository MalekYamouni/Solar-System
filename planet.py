import pygame
import math
class planeten:
    def __init__(self, display, x, y, velocity, radius, color, angle,angle2, radius2, Screensize):
        self.x = x
        self.y = y
        self.velocity = velocity
        self.radius = radius
        self.color = color
        self.angle = angle
        self.angle2 = angle2
        self.radius2 = radius2
        self.display = display
        self.Screensize = Screensize
    
    def drawstatic(self):
        pygame.draw.circle(self.display, color=self.color, center=(self.x,self.y),radius=self.radius)

    def drawmove(self):
        pygame.draw.circle(self.display,color=self.color, center=(self.x*math.cos(self.angle)+self.Screensize/2,self.y*math.sin(self.angle)+self.Screensize/2), radius=self.radius)
        self.angle += 0.001+self.velocity

    def getx(self):
        self.currentx = self.x*math.cos(self.angle)+self.Screensize/2
        self.angle += 0.001
        return self.currentx
    def gety(self):
        self.currenty = self.y*math.sin(self.angle)+self.Screensize/2
        self.angle += 0.001
        return self.currenty