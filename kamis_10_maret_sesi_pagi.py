# -*- coding: utf-8 -*-
"""Kamis_10_Maret_Sesi Pagi

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1MXQ7AycIT0zraPE3VFHIBRU9nxYDfbzB

Tugas Uji Hipotesis

Misalkan kamu adalah data scientist di gojek. Kamu ingin mengetahui apakah kemacetan mempengaruhi tingkat kepuasan pelanggan. Jadi kamu ingin membandingkan nilai "bintang" dari customer saat dia order di jam macet dan tidak macet. (#hint = data dari customer yang sama)

macet = [2, 3, 5, 4, 5, 4, 4, 3, 4, 3, 4, 5, 4, 5, 4, 3, 4, 3, 3, 5, 4, 3, 4, 3, 4, 3, 4, 4, 5]

tidak_macet = [2, 2, 4, 5, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 4, 3, 3, 2, 3, 4, 4, 3, 3, 3, 4, 3, 4, 3, 4]

Buat hipotesisnya
Lakukan uji asumsi normalitasnya
Jika datanya normal lakukan uji parametrik, jika tidak berdistribusi normal lakukan uji nonparametrik
Apa kesimpulan uji hipotesisnya?

1. Buat Hipotesis
"""

import matplotlib as plt
import pandas as pd
import seaborn as sns
import numpy as np
from scipy import stats

macet = np.array([2, 3, 5, 4, 5, 4, 4, 3, 4, 3, 4, 5, 4, 5, 4, 3, 4, 3, 3, 5, 4, 3, 4, 3, 4, 3, 4, 4, 5])
tidak_macet = np.array ( [2, 2, 4, 5, 4, 3, 3, 3, 3, 3, 3, 4, 4, 5, 4, 3, 3, 2, 3, 4, 4, 3, 3, 3, 4, 3, 4, 3, 4])

"""2. Uji Normalitas

Ho = data berdistribusi normal
Ha = data tidak berdistribusi normal

Asumsikan Rentang Kepercayaanya = 95% alpha = 5%
"""

sns.distplot(macet)

sns.distplot(tidak_macet)

#uji kolmogorov-smirnov
z_score_macet = stats.zscore(macet)
z_score_tidak_macet = stats.zscore(tidak_macet)
print('uji kolmogorov smirnov pada data macet = ', stats.kstest(z_score_macet, "norm"))
print('uji kolmogorov smirnov pada data tidak_macet = ', stats.kstest(z_score_tidak_macet, "norm"))

"""diketahui bahwa alpha = 0,05 sehingga hasil p-value pada macet = 0,056 (>0,05) maka data akan terdistribusi normal sedangkan hasil p-value pada tidak_macet = 0,018 (<0,05) maka data tidak akan terdistribusi normal

maka dikarenakan hasil p-value <= 0,05 maka ho akan ditolak, atau data tidak terdistribusi dengan normal

3. Uji Wilcoxon (Non Parametik)

Dikarenakan data pada tidak_macet tidak terdistribusi dengan normal maka selanjutnya akan dilakukan uji beda non-parametik wilcoxon. Uji wilcoxon dilakukan karena 2 kelompok data berhubungan yaitu macet dan tidak_macet
"""

m = macet - tidak_macet
stats.wilcoxon(m)