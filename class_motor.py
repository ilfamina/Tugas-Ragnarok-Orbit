# -*- coding: utf-8 -*-
"""Class Motor

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LRjTWDnEdLZemMm6dHe76xRhH5VN9Fb-
"""

from abc import abstractmethod, ABC

class motor(object):
    def __init__(self, jenis, tahun, mesin):
        self.jenis = jenis
        self.tahun = tahun
        self.mesin = mesin
    
    def h(self, durasi):
        for i in range(durasi):
            print("jenis ")
            
    def info(self):
        print(f"jenis: {self.jenis}\nTahun: {self.tahun}\nMesin: {self.mesin}")

        
class PCX(motor):
    def __init__(self, jenis, tahun, mesin, keturunan):
        super().__init__(jenis, tahun, mesin)
        self.keturunan= keturunan
        
        
    def ab(self, durasi):
        for i in range(durasi):
            print("brumbrumbrum...")

            class Motor(object):
    
    def __init__(mtr, input_merk, input_mesin, input_tahun, input_dayamaksimum):
        mtr.merk = input_merk
        mtr.mesin = input_mesin
        mtr.tahun = input_tahun
        mtr.dayamaksimum=input_dayamaksimum

    def jm(mtr, mot):
        for x in range(mot):
            print(" 6inline")

    def info(mtr):
        print(f"merk: {mtr.merk}, mesin: {mtr.mesin}, tahun :{mtr.tahun}, dayamaksimum :{mtr.dayamaksimum}")


motor1 = Motor("PCX-160", "4-Valve", "2021", "8500rpm")

motor1.info()    


merk= "PCX"
warna= "gray"
barang = "Motor"
dayamaksimum = "8500rpm"

def PCX():
    print("brum brum....")
    
def info_PCX(merk,warna,barang,dayamaksimum):
    print(f"merk: {merk}, warna: {warna}, barang :{barang}, dayamaksimum :{dayamaksimum}") 

info_PCX(merk,warna,barang,dayamaksimum)
PCX()


class Motor(ABC):
    
    @abstractmethod
    def caramengemudi(self):
        pass
    
class PCX(Motor):
    def caramengemudi(self):
        print("Mobil ini bisa digunakan untuk Drag, Harian, maupun Drift.\n")
        
class Aerox(Motor):
    def caramengemudi(self):
        print("Mobil ini dapat digunakan untuk harian namun lebih sering digunakan untuk ajang drift.")
      

pcx1=PCX()
aerox1=Aerox()

pcx1.caramengemudi()
aerox1.caramengemudi()