import turtle

class Persegi: 
    def __init__ (self, sisi, warnagaris):
        self.sisi = sisi 
        self.warnagaris = warnagaris
        self.pen = turtle.Turtle()

    def gambar(self):
        self.pen.shape("turtle")
        self.pen.pencolor(self.warnagaris)
        self.pen.speed(0.75)
        self.pen.pensize(2)

        for _ in range(4):
            self.pen.forward(self.sisi)
            self.pen.right(90)


persegi = Persegi(350, "Green")

persegi.pen.penup()
persegi.pen.goto(-150, 150)
persegi.pen.pendown()

persegi.gambar()

turtle.done()