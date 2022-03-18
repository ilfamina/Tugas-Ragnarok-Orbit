# -*- coding: utf-8 -*-
"""Selasa_08_Maret_Sesi Pagi

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cGxcN8xtweW4881OUIzYNDhzIGcCAtR7
"""

import numpy as np

"""Latihan 2"""

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(A, "\n")
#Lengkapi kodingan berikut
print('banyaknya entry = ', A.size)
print('dimensi array = ', A.ndim)
print('ukuran array = ', A.shape, "\n")

"""Latihan 3"""

#Lengkapi kodingan berikut
print('baris ke-3 =', A[2])
print('entry ke-1 & 2 baris ke-3 = ', A[2][0:2])
print('entry ke-2 & 3 kolom ke-3 = \n', A[1:3,2:]) #Baris 1-2 kolom >= 2

"""Latihan 4"""

A = np.array([[1, 2], [7,8]])
B = np.array([[3, 5], [1,6]])
print("Hasil 2xA : \n", 2*A)
print("Hasil 2+A : \n", 2+A)
print("HasilA+B : \n", A+B)
print("HasilA-B : \n", A-B)
print("Hasil det(A) : \n ", np.linalg.det(A))

#invers dari B, simpan jadi matriks D
D = np.linalg.inv(B)
print("D :\n",D, "\n")

#transpose D
print("D^T : \n", D.transpose(), "\n")

#nilai eigen dan vektor eigen dari A dan B
print("Eigen Value A :", np.linalg.eig(A)[0])
print("Eigen Vector A:\n", np.linalg.eig(A)[1],"\n")
print("Eigen Value B :", np.linalg.eig(B)[0])
print("Eigen Vector B:\n", np.linalg.eig(B)[1])

"""Apa perbedaan dari B*D (perkalian antar entry di B dan D) dan BD (perkalian matriks B dan D)?"""

print("BxD : \n",B*D)
print("BxD : \n",np.matmul(B,D))

"""Perbedaan perkalian entry yang dikalikan pada bilangan baris 1 di matriks B dikalikan bilangan pada baris 1 matriks D, akan tetapi pada kolom 2 matriks B akan dikalikan kolom 2 di matriks D. Sedangkan perkalian matriks yang dikalikan merupakan matrik baris B dengan kolom matrik D dan kolom matriks B dengan baris matrik D

---


"""