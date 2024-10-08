import turtle

class SegiSembilan: 
    def __init__(self, sisi):
        self.t = turtle.Turtle()
        self.sisi = sisi
        self.sudut = 360 / 9

    def gambar(self):
        self.t.shape("turtle")
        self.t.color('Blue')
        for _ in range(9): 
            self.t.forward(self.sisi)
            self.t.left(self.sudut)

segisembilan = SegiSembilan(100)

segisembilan.gambar()

turtle.done()