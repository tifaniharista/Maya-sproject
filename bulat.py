import turtle

class Lingkaran: 
    def __init__(self, jarijari, warnagaris):
        self.jarijari = jarijari
        self.warnagaris = warnagaris
        self.pen = turtle.Turtle()

    def gambar(self):
        self.pen.shape('turtle')
        self.pen.penup()
        self.pen.goto(0, 0)
        self.pen.pendown()
        self.pen.pencolor(self.warnagaris)
        self.pen.speed(0.75)
        self.pen.pensize(3)
        self.pen.circle(self.jarijari)

lingkaran = Lingkaran(75, "Purple")

lingkaran.gambar()

turtle.done()