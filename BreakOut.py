from graphics import *
import random as ran

class Ball():

    def __init__(self, w, x, y, xv, yv, size):
        self.ball = Circle(Point(x, y), size)
        self.xv = xv
        self.yv = yv
        self.w = w
        self.ball.draw(w)

    def update(self):
        x = self.ball.getCenter().getX()
        y = self.ball.getCenter().getY()
        dx = self.xv
        dy = self.yv
        size = self.ball.getRadius()
        if x+self.xv+size > self.w.getWidth():
            dx = 2*(self.w.getWidth()-size-x)-self.xv
            
            self.xv *= -1
        elif x+self.xv-size < 0:
            dx = 2*(size-x)-self.xv
            self.xv *= -1

        if y+size > self.w.getHeight():
            dy = 2*(self.w.getHeight()-size-y)-self.yv
            self.yv *= -1
        elif y-size < 0:
            dy= 2*(size-y)-self.yv
            self.yv *= -1
        
        self.ball.move(dx, dy)
            

def main():
    w = GraphWin("BreakOut", 500, 500)
    b = []
    for _ in range(10):
        b.append(Ball(w, 250, 250, ran.randint(-5, 5), ran.randint(-5, 5), ran.randint(10, 20)))
    while True:
        for i in b:
            time.sleep(0.001)
            i.update()
    
    
if __name__ == "__main__":
    main()
