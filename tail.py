import pygame
import math

class Tail:
    def __init__(self,display, taillist, radius, angle, x, y, SCREENSIZE, counter) -> None:
        self.taillist = taillist
        self.radius = radius
        self.angle = angle
        self.display = display
        self.R = 255
        self.G = 255
        self.B = 255
        self.x = x
        self.y = y
        self.SCREENSIZE =SCREENSIZE
        self.counter = counter

    def brightness(self):
        if self.R> 0:
            self.R -= 0.1
            self.G -= 0.1
            self.B -= 0.1

    def getx(self):
        self.currentx = self.x*math.cos(self.angle)+self.SCREENSIZE/2
        self.angle += 0.001
        return self.currentx

    def gety(self):
        self.currenty = self.y*math.sin(self.angle)+self.SCREENSIZE/2
        self.angle += 0.001
        return self.currenty

    def drawparticle(self):
        pygame.draw.circle(self.display, color=(self.R,self.G,self.B), center=(self.x,self.x),radius=self.radius)

    # def drawtail(self):
    #     tailor = Tail(self.display, self.taillist, self.radius, self.angle, self.v, self.x, self.y, self.SCREENSIZE, 0 )
    #     self.taillist.append(tailor)
    #     if len(self.taillist)<500:
    #         for i in self.taillist:
    #             i.drawparticle()
    #             i.brightness()
    #             if i.R < 1:
    #                 del self.taillist[0]

    def drawtail2(self):
        if len(self.taillist)<200:
            if self.counter<200:
                tailor = Tail(self.display, self.taillist, self.radius, self.angle, self.x, self.y, self.SCREENSIZE, 0)
                self.taillist.append(tailor)
                self.counter += 1
                print(self.counter)
            else:
                self.counter += 0

        for i in self.taillist:
                i.drawparticle()
                i.brightness()
                if i.R < 1:
                    del self.taillist[0]