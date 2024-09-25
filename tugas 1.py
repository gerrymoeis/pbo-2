import random

class Barang:
    def __init__(self, nama, kode, jumlah, kondisi):
        self.nama = nama
        self.kode = kode
        self.jumlah = jumlah
        
        KONDISI = ["Baik", "Rusak", "Perlu Perbaikan"]
        self.kondisi = KONDISI[kondisi]
        
    def detailBarang(self):
        for  key, value in vars(self).items():
            print(f"{key.title()}: {value}")
        print()
    
NAMA_BARANG = ["Komputer", "Proyektor", "Meja", "Pulpen", "Laptop"]
list_barang = []
for _ in range(10):
    list_barang.append(Barang(random.choice(NAMA_BARANG),
                              f"BARANG{random.randint(0, 100)}",
                              random.randint(5, 10),
                              random.randint(0, 2)))

for barang in list_barang:
    barang.detailBarang()