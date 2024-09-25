import turtle

class Pen:
    def __init__(self, speed=10, shape="classic"):
        self.t = turtle.Turtle()
        self.t.speed(speed)
        self.t.shape(shape)
    
    def buat_segi(self, segi, ukuran, warna, offset=360, x=None, y=None, jejer=False):
        if not jejer:
            self.t.penup()
            if x and y:
                self.t.goto(x, y)
            else:
                self.t.goto(-ukuran//2, -ukuran//2)
            self.t.pendown()
        
        self.t.color(warna)
        self.t.begin_fill()
        for _ in range(segi):
            self.t.forward(ukuran)
            self.t.left(offset//segi)
        self.t.end_fill()
    
    def buat_bintang(self, ukuran, warna, x, y, jejer=False):
        self.buat_segi(5, ukuran, warna, -144*5, x, y, jejer)
    
    def buat_bintang_jejer(self, ukuran, warna, jumlah, x, y):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()

        for _ in range(jumlah):
            self.buat_bintang(ukuran, warna, x, y, jejer=True)
            self.t.penup()
            self.t.forward(ukuran)
            self.t.pendown()

[segitiga, persegi, lingkaran, segisembilan, bintang1, bintang2] = (Pen(),)*6

segitiga.buat_segi(3, 500, "red", x=-900, y=50)
persegi.buat_segi(4, 200, "orange", x=-100, y=100)
lingkaran.buat_segi(90, 10, "yellow", x=500, y=100)
segisembilan.buat_segi(9, 150, "green", x=-725, y=-400)

bintang1.buat_bintang_jejer(200, "blue", 5, x=-200, y=-50)
bintang2.buat_bintang_jejer(200, "purple", 5, x=-200, y=-250)

turtle.done()