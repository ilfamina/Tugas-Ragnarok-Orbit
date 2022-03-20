# -*- coding: utf-8 -*-
"""Senin_14_Maret_Sesi Pagi dan Siang

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15gcZAc1qI95A8kwFbUaWixgzOynnBZ1y

Data Manipulation With Pandas

Handling Missing Values
"""

import pandas as pd
import numpy as np
data1 = {'regiment': ['51st','29th', '2nd', '5th', '45th', '3rd', '20th', '198th', '30th', '1st', '4th', '22nd'],
         'trucks': ['MA7160', np.nan, 'BA3211', 'Tatra10', 'none', 'Tatra10', 'WE2323','Tatra10', 'Tatra10', 'WE2323', 'WE2323', 'Tatra10'],
         'tanks': ['Merkava Mark 4', 'none', 'Merkava Mark 4', 'Leopard 2A6M', 'none', 'Arjun MBT', 'Merkava Mark 4', 'Arjun MBT', 'Leopard 2A6M', 'Arjun MBT', 'Leopard 2A6M', 'Arjun MBT'],
         'aircraft':[ np.nan, 'none', 'none','Harbin Z-9', 'Harbin Z-9', 'Harbin Z-9', 'SH-60B Seahawk', 'SH-60B Seahawk', 'SH-60B Seahawk', 'SH-60B Seahawk','SH-60B Seahawk','SH-60B Seahawk' ]
         }

df = pd.DataFrame(data1)
df

df['location'] = np.nan        #Create a new column with all NaN values
df

df.info()

#Melihat banyaknya data yg Kosong -> fungsi hanya bisa menghitung data kosong yg isinya np.nan 
df.isnull().sum()

#Membuat percentage untuk jumlah missing data -> fungsi hanya bisa menghitung data kosong yg isinya np.nan
data_missing = {
    'total_missing' : df.isnull().sum(),
    'percentage' : (df.isnull().sum()/12)*100
}

missing_data = pd.DataFrame(data_missing)
missing_data

df.dropna(axis=1, how='all')  #Drop the column that all the values in NaN

df.dropna(axis=1) #Drop the column which contain Nan Value

df = df.drop(['location'], axis=1)
df

df.dropna() #Secara default axis=0

#Drop the rows that contain at least 3 missing values
df.dropna(thresh=3)
df

#To replace NaN with any other num/char 
df.fillna(0)

df.fillna('Unknown')

"""Missing value di kolom trucks diisi dengan "unknown-truck" dan di kolom aircraft diisi dengan "unknown-aircraft""""

columns = ['trucks', 'aircraft']

df_2 = df.copy()

#Fill NaN Values in Trucks column
df_2['trucks'] = df_2['trucks'].fillna("unknown-truck")

#Fill NaN Values in aircraft column
df_2['aircraft'] = df_2['aircraft'].fillna("unknown-aircraft")


df_2

#Misalkan none adalah missing value dan kita akan menghapusnya
#Menghapus missing value = none

df_2 = df.copy()
columns = df_2.columns

for col in columns:
    df_2 = df_2.loc[df_2[col] != 'none']
    
df_2

#Mengganti nilai none menjadi Unknown

df_2 = df.copy()
columns = df_2.columns

for col in columns:
    df_2[df_2[col] == 'none'] = 'Unknown'

df_2.fillna('Unknown', inplace = True)

df_2

#Misalkan none adalah missing value dan kita akan menghapusnya
#Menghapus missing value = none

df_2 = df.copy()
columns = df_2.columns

#Merubah value none manjadi Nan (np.nan) lalu setelah kita bisa handle seperti missing value biasa (np.nan)
for col in columns:
    df_2[col] = df_2[col].loc[df_2[col] != 'none']
    
df_2

"""Finding Unique Values and Deleting Duplicates</font>"""

import pandas as pd
import numpy as np
data1 = {'regiment': ['51st','29th', '2nd', '5th', '45th', '3rd', '20th', '198th', '30th', '1st', '4th', '22nd'],
         'trucks': ['MA7160', np.nan, 'BA3211', 'Tatra10', 'RT3121', 'Tatra10', 'WE2323','Tatra10', 'Tatra10', 'WE2323', 'WE2323', 'Tatra10'],
         'tanks': ['Merkava Mark 4', 'Merkava Mark 4', 'Merkava Mark 4', 'Leopard 2A6M', 'Arjun MBT', 'Arjun MBT', 'Merkava Mark 4', 'Arjun MBT', 'Leopard 2A6M', 'Arjun MBT', 'Leopard 2A6M', 'Arjun MBT'],
         'aircraft':['none', 'none', 'none','Harbin Z-9', 'Harbin Z-9', 'Harbin Z-9', 'SH-60B Seahawk', 'SH-60B Seahawk', 'SH-60B Seahawk', 'SH-60B Seahawk','SH-60B Seahawk','SH-60B Seahawk' ]
         }

df = pd.DataFrame(data1)
df

#Find unique values by turnign column into a list
set(df_2['trucks'])             #Method 1

df_2['trucks'].unique()      #Method 2

#counting the unique values
df_2['trucks'].value_counts()

#Deleting duplicates in Pandas
import pandas as pd

data1 = {'regiment': ['51st','51st', '51st','51st','29th', '2nd', '5th', '45th', '3rd', '20th', '198th', '30th'],
         'trucks': ['MA7160', 'MA7160', 'MA7160', 'MA7160','MA7160', 'BA3211', 'Tatra10', 'RT3121', 'Tatra10', 'WE2323','Tatra10', 'Tatra10'],
         'tanks': ['Merkava Mark 4', 'Merkava Mark 4', 'Merkava Mark 4', 'Merkava Mark 4', 'Merkava Mark 4', 'Merkava Mark 4', 'Leopard 2A6M', 'Arjun MBT', 'Arjun MBT', 'Merkava Mark 4', 'Arjun MBT', 'Leopard 2A6M'],
         'aircraft':['none', 'none', 'none', 'none', 'Harbin Z-9', 'none','Harbin Z-9', 'Harbin Z-9', 'Harbin Z-9', 'SH-60B Seahawk', 'SH-60B Seahawk', 'SH-60B Seahawk']
         }

df = pd.DataFrame(data1)
df

df.duplicated()   #Finds which row have duplicatees

df.duplicated().sum() #Count how many data that duplicated

"""To remove the duplicates, we use drop_duplicates()"""

df.drop_duplicates()

"""Analysing Outliers"""

height_data = {'name':['Adit', 'Gia', 'Tim', 'Mark', 'Nur', 'Adil', 'Kia', 'Indar', 'Tia', 'Jack', 'Adele', 'Niall', 'Harry', 'Tom'],
               'height': [5.9, 5.2, 5.1, 5.5, 4.9, 5.4, 6.2, 6.5, 7.1, 14.5, 6.1, 5.6, 1.2, 5.5]}
df = pd.DataFrame(height_data)
df

"""Boxplot"""

# Commented out IPython magic to ensure Python compatibility.
#BoxPlot
import pandas as pd

height_data = {'name':['Adit', 'Gia', 'Tim', 'Mark', 'Nur', 'Adil', 'Kia', 'Indar', 'Tia', 'Jack', 'Adele', 'Niall', 'Harry', 'Tom'],
               'height': [5.9, 5.2, 5.1, 5.5, 4.9, 5.4, 6.2, 6.5, 7.1, 14.5, 6.1, 5.6, 1.2, 5.5]}
df = pd.DataFrame(height_data)

df_copy = df.copy()

df_copy = df_copy['height'].astype(int)

import matplotlib.pyplot as plt
# %matplotlib inline
plt.boxplot(df_copy)
plt.show()

Q3 = df['height'].quantile(0.75)
Q1 = df['height'].quantile(0.25)
IQR = Q3-Q1

max_threshold = Q3 + (1.5 * IQR)
max_threshold

min_threshold = Q1 - (1.5 * IQR)
min_threshold

"""We conclude that any value of height above 7.5625 and below 3.60500 is an outlier and we remove them as follows."""

df[df['height']>max_threshold]      #This is an upper outlier, above than the maximum limit

df[df['height'] < min_threshold]    #This is an lower outlier, below the minimum limit

new_df = df[(df['height']<max_threshold) & (df['height']>min_threshold)] #These are the values in between the two limits, i.e. without outliers

new_df

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
new_df = new_df['height'].astype(int)

plt.boxplot(new_df)
plt.show()

"""Creating new categorical features from continuous variable"""

# Creating Age
rng=np.random.RandomState(42)
age = pd.DataFrame({'AGE': rng.randint(1, 100, 20)})
age.head()

age['bins'] = pd.cut(x=age['AGE'], bins=[0,2,17,65,99],
                    labels=['Toddler/Baby','Child', 'Adult','Elderly'])
 
age.head()

"""Groupby Operation"""

df = pd.DataFrame(
    [
        ("bird", "Falconiformes", 389.0),
        ("bird", "Psittaciformes", 24.0),
        ("mammal", "Carnivora", 80.2),
        ("mammal", "Primates", np.nan),
        ("mammal", "Carnivora", 58),
    ],
    index=["falcon", "parrot", "lion", "monkey", "leopard"],
    columns=("class", "order", "max_speed"),
)
df

"""Aggregation"""

# Aggregation
df.groupby(['class'])['max_speed'].sum()

"""Transformation"""

# Transformation
df.groupby(['class'])['max_speed'].transform(lambda x:x.fillna(x.mean()))

"""Filtering"""

# filtering
df.groupby(['class'])['max_speed'].filter(lambda x: x.mean() > 200)

# Getting Groups
groups=df.groupby(['class'])
groups.get_group('bird')

# Iterating through groups
for name,data in groups:
    print("\nName:",name)
    print("\n",data)

"""





Grouby statistical Analysis"""

# Getting the data
import seaborn as sns
df1=sns.load_dataset('tips')
df1.head()

df1.groupby(['sex', 'smoker']).agg({
        'total_bill': ['median'], 
        'tip': ['median', 'min', 'max','count']
    })