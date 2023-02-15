
class Tail:
    def __init__(self,display, taillist, radius, angle, starttime, v) -> None:
        self.taillist = taillist
        self.radius = radius
        self.angle = angle
        self.starttime = starttime
        self.v = v
        self.display = display

    def drawtail(self):
        for i in self.taillist:
            i.drawline()
            i.bright2()
            if i.R1 < 1:
                del self.taillist[0]