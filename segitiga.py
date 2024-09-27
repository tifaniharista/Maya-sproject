# IMPORT MODUL TURTLE UNTUK MENGGAMBAR
import turtle

class SegitigaSamaSisi:
    def __init__(self, sisi):
        self.sisi = sisi

    def gambar(self):
        turtle.shape("turtle")
        turtle.color("blue")
        turtle.speed(0.75)
        turtle.penup()
        turtle.goto(-self.sisi/2, -self.sisi/2 * 0.5)
        turtle.pendown()

        for _ in range(3):
            turtle.forward(self.sisi)
            turtle.left(120)

segitiga = SegitigaSamaSisi(350)
segitiga.gambar()

turtle.done()