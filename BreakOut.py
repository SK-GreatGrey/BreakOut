from graphics import *
import random as ran



class BreakOut():

    def __init__(self, w):
        self.w = w
        self.balls = []
        self.lives = 3
        self.livesT = []
        self.drawGame()

    def drawGame(self):
        self.balls.append(Ball(self.w, 250, 250, ran.randint(-10, 10), ran.randint(-10, 10), ran.randint(10, 15)))
        for i in range(self.lives):
            self.livesT.append(makeHeart(Point(20 + 40*i, 450), 20))
            for j in self.livesT[i]:
                j.draw(self.w)
        
    def update(self):
        for b in self.balls:
            b.update()
    
    def loseLife(self):
        if self.lives > 0:
            self.lives -= 1
            for s in self.livesT[self.lives]:
                s.undraw()
        if(self.lives == 0):
            self.gameOver()
            return True
        return False

    def gameOver(self):
        t = Text(Point(230, 250), "GAME OVER")
        t.draw(self.w)
        self.w.getMouse()
        t.undraw()
        self.clear()

    def clear(self):
        for i in self.balls:
            i.undraw()
        for i in self.livesT:
            for j in i:
                j.undraw()
        

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

    def undraw(self):
        self.ball.undraw()

def makeHeart(p, size):
    heart = []
    t1 = Polygon([Point(p.getX(), p.getY()+size/4), Point(p.getX()+size/2, p.getY()+size), Point(p.getX()+size, p.getY()+size/4)])
    heart.append(t1)
    c1 = Circle(Point(p.getX()+size/4, p.getY()+size/4), size/4)
    heart.append(c1)
    c2 = Circle(Point(p.getX()+3*size/4, p.getY()+size/4), size/4)
    heart.append(c2)
    for s in heart:
        s.setFill("Red")
        s.setOutline("Red")
    return heart

def drawMenu():
    menu = []
    startBox = Rectangle(Point(50, 50), Point(150, 100))
    startBox.setFill("Grey")
    menu.append(startBox)
    startText = Text(Point(100, 75), "Start")
    menu.append(startText)
    exitBox = Rectangle(Point(50, 125), Point(150, 175))
    exitBox.setFill("Grey")
    menu.append(exitBox)
    exitText = Text(Point(100, 150), "Exit")
    menu.append(exitText)
    
    return menu

def main():
    w = GraphWin("BreakOut", 500, 500)
    end = False
    gameOver = True
    menu = drawMenu()
    for e in menu:
        e.draw(w)
    while not end:
        click = w.getMouse()
        x = click.getX()
        y = click.getY()
        if x > 50 and x < 150 and y > 125 and y < 175:
            end = True
        if x > 50 and x < 150 and y > 50 and y < 100:
            for e in menu:
                e.undraw()
            B = BreakOut(w)
            gameOver = False
            frames = 0
            while not gameOver:
                time.sleep(0.01)
                frames += 1
                print frames
                B.update()
                if frames%200 == 0:
                    gameOver = B.loseLife()
            for e in menu:
                e.draw(w)
    
if __name__ == "__main__":
    main()
