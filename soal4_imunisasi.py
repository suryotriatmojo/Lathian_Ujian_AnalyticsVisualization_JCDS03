import pandas as pd
import matplotlib.pyplot as plt

df_bcg = pd.read_csv('datasets/Balita Terimunisasi BCG 1995-2017.csv', na_values = 'n.a')
df_campak = pd.read_csv('datasets/Balita Terimunisasi Campak 1995-2017.csv', na_values = 'n.a')
df_dpt = pd.read_csv('datasets/Balita Terimunisasi DPT 1995-2017.csv', na_values = 'n.a')
df_polio = pd.read_csv('datasets/Balita Terimunisasi Polio 1995-2017.csv', na_values = 'n.a')

df_bcg = df_bcg.interpolate()
df_campak = df_campak.interpolate()
df_dpt = df_dpt.interpolate()
df_polio = df_polio.interpolate()

# Plotting Figure 1
plt.figure('Persentasi balita terimunisasi 1995-2017', figsize = (15,8))

plt.subplot(221)
plt.bar(df_bcg['Tahun'], df_bcg['% Balita yang pernah mendapat imunisasi BCG'], color = 'r')
plt.title('BCG')
plt.xticks(df_bcg['Tahun'], rotation = 90)

plt.subplot(222)
plt.bar(df_campak['Tahun'], df_campak['% Balita yang pernah mendapat imunisasi Campak'], color = 'g')
plt.title('Campak')
plt.xticks(df_bcg['Tahun'], rotation = 90)

plt.subplot(223)
plt.bar(df_dpt['Tahun'], df_dpt['% Balita yang pernah mendapat imunisasi DPT'], color = 'y')
plt.title('DPT')
plt.xticks(df_bcg['Tahun'], rotation = 90)

plt.subplot(224)
plt.bar(df_polio['Tahun'], df_polio['% Balita yang pernah mendapat imunisasi Polio'], color = 'b')
plt.title('Polio')
plt.xticks(df_bcg['Tahun'], rotation = 90)

# Plotting Figure 2
plt.figure('Persentasi balita tak terimunisasi 1995-2017', figsize = (15,8))

plt.subplot(221)
plt.bar(df_bcg['Tahun'], 100 - df_bcg['% Balita yang pernah mendapat imunisasi BCG'], color = 'r')
plt.title('BCG')
plt.xticks(df_bcg['Tahun'], rotation = 90)

plt.subplot(222)
plt.bar(df_campak['Tahun'], 100 - df_campak['% Balita yang pernah mendapat imunisasi Campak'], color = 'g')
plt.title('Campak')
plt.xticks(df_bcg['Tahun'], rotation = 90)

plt.subplot(223)
plt.bar(df_dpt['Tahun'], 100 - df_dpt['% Balita yang pernah mendapat imunisasi DPT'], color = 'y')
plt.title('DPT')
plt.xticks(df_bcg['Tahun'], rotation = 90)

plt.subplot(224)
plt.bar(df_polio['Tahun'], 100 - df_polio['% Balita yang pernah mendapat imunisasi Polio'], color = 'b')
plt.title('Polio')
plt.xticks(df_bcg['Tahun'], rotation = 90)

plt.tight_layout()
plt.show()

