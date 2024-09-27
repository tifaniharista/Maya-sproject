import turtle

class Bintang:
    def __init__(self,ukuran,x,y):
        self.ukuran = ukuran
        self.pen = turtle.Turtle()
        self.pen.color("red")
        self.pen.penup()
        self.pen.goto(x,y)
        self.pen.pendown()

    def gambar(self):
        self.pen.shape("turtle")
        for _ in range(5):
            self.pen.forward(self.ukuran)
            self.pen.right(144)

bintang1 = Bintang(110, -110, 0)
bintang2 = Bintang(110, 0, 0)
bintang3 = Bintang(110, 110, 0)

bintang1.gambar()
bintang2.gambar()
bintang3.gambar()

turtle.done()