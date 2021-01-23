import time
import turtle

class aTurtle():

    def __init__(self, startNum, drawlen = 2, drawang = 2):
        self.startNum = startNum 
        self.drawLen = drawlen
        self.ang = drawang
        

    def colla(self, n):
    
        if (n % 2) == 0:
            n = n / 2
        else:
            n = (3*n+1)/2
        return n

    def drawLine(self):
        turtle.width(2)
        turtle.hideturtle()
        Sequence = []

        n = self.startNum
        while True:
            Sequence.append(n)
            n = self.colla(n)
            if n == 1:
                break
        Sequence.append(1)
        Sequence.reverse()

        turtle.up()
        turtle.home()
        turtle.goto(0, -300)
        turtle.left(90) 
        turtle.down()

        for num in Sequence:
            if (num % 2) == 0:
                turtle.color('blue')
                turtle.right(self.ang)
            else:
                turtle.color('red')
                turtle.left(self.ang)

            turtle.forward(self.drawLen)



if __name__=='__main__':
    

    turtle.width(2)
    turtle.hideturtle()
    Sequence = []

    for i in range(1000):
        t = aTurtle(i+1, 10, 10)
        print(i)
        t.drawLine()

    print('done')
    while True:
        time.sleep(5)
