from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

# connect to server, name cursor
cursor = MongoClient('mongodb://localhost:27017/')

db = cursor['Kampus']   # initiate database Kampus
col_dosen = db['Dosen']      # initiate collection Dosen
col_mahasiswa = db['Mahasiswa']  # initiate collection Mahasiswa

# step to create Dosen Dataframe
db_dosen = []
for i in col_dosen.find():
    db_dosen.append(i)

df_dosen = pd.DataFrame(db_dosen)

status_dosen = []
usia_dosen = []
for j in range(len(df_dosen)):
    status_dosen.append('dosen')
    usia_dosen.append(int(df_dosen['usia'][j]))

df_dosen['status'] = pd.Series(status_dosen)
df_dosen['usia'] = pd.Series(usia_dosen)

# step to create Mahasiswa Dataframe
db_mahasiswa = []
for k in col_mahasiswa.find():
    db_mahasiswa.append(k)

df_mahasiswa = pd.DataFrame(db_mahasiswa)

status_mahasiswa = []
usia_mahasiswa = []
for l in range(len(df_mahasiswa)):
    status_mahasiswa.append('mahasiswa')
    usia_mahasiswa.append(int(df_mahasiswa['usia'][l]))

df_mahasiswa['status'] = pd.Series(status_mahasiswa)
df_mahasiswa['usia'] = pd.Series(usia_mahasiswa)

# show output from 2 dataframe
print(df_dosen[['asal', 'nama', 'status', 'usia']])
print(df_mahasiswa[['asal', 'nama', 'status', 'usia']])

# make bar plot
plt.figure('Kampus')
plt.bar(df_dosen['nama'], df_dosen['usia'])
plt.bar(df_mahasiswa['nama'], df_mahasiswa['usia'])
plt.title('Usia Warga Kampus')
plt.legend(['Dosen', 'Mahasiswa'])
plt.show()