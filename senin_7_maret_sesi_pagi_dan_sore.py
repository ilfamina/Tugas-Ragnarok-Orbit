# -*- coding: utf-8 -*-
"""Senin_7_Maret_Sesi Pagi dan Sore

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AnNSu67EoLI-T-syaKVlbEEw_3q6dag9

Tugas Sesi Pagi

Buatlah 3 OOP beserta turunannya dari objek sekitar, buat ulang seperti yang diatas (encapsulation, abstaction, inheritance, polymorphism)

Encapsulation
"""

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

class Motor(object):
    
    nama_motor = ""
    def __init__(pcx, input_merk, input_warna, input_barang, input_dayamaksimum):
        pcx.merk = input_merk
        pcx.warna = input_warna
        pcx.barang = input_barang
        pcx.dayamaksimum = input_dayamaksimum
        Motor.nama_motor = input_merk

    def PCX(pcx):
        print("Barang", pcx.merk)

    def info(pcx):
        print(f"merk: {pcx.merk}, warna: {pcx.warna}, barang: {pcx.barang}, dayamaksimum :{pcx.dayamaksimum}")


motor1 = Motor("Honda-PCX", "Gray", "Motor", "8500rpm")

motor1.info()
motor1.PCX()

motor1.info()

"""Abstaction

"""

from abc import abstractmethod, ABC

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

"""Inheritance"""

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

"""Custom module

Polymorphism
"""

import motor as mot

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

motor1 = Motor("PCX-160", "2021", "4-Valve", "V-Matic")

motor1.info()

"""Inhertiance"""

motor1 = Motor("PCX-160", "4-Valve", "2021", "8500rpm")

motor1.info()

"""Encapsulation"""

info_PCX("PCX", "gray", "Motor", "8500rpm")
PCX()