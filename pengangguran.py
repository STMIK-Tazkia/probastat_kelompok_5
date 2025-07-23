import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

file_path = 'datanya.xlsx'
df = pd.read_excel(file_path)

print(df.head())

df['Angkatan Kerja'] = df['Jumlah Penduduk Bekerja'] + df['Jumlah Pengangguran']
df['Proporsi_Pengangguran'] = df['Jumlah Pengangguran'] / df['Angkatan Kerja']
df['Tahun'] = pd.to_datetime(df['Tanggal']).dt.year

rata_nasional = df.groupby('Tahun')[['Jumlah Penduduk Bekerja', 'Jumlah Pengangguran']].sum()
rata_nasional['Angkatan Kerja'] = rata_nasional['Jumlah Penduduk Bekerja'] + rata_nasional['Jumlah Pengangguran']
rata_nasional['Proporsi_Nasional'] = rata_nasional['Jumlah Pengangguran'] / rata_nasional['Angkatan Kerja']
print(rata_nasional[['Proporsi_Nasional']])

plt.figure(figsize=(10, 6))
plt.plot(rata_nasional.index, rata_nasional['Proporsi_Nasional'], marker='o', color='blue')
plt.title("Tren Proporsi Pengangguran Nasional per Tahun")
plt.xlabel("Tahun")
plt.ylabel("Proporsi Pengangguran")
plt.grid(True)
plt.tight_layout()
plt.show()

data_2023 = df[df['Tahun'] == 2023]
penganggur_2023 = data_2023['Jumlah Pengangguran'].sum()
bekerja_2023 = data_2023['Jumlah Penduduk Bekerja'].sum()
n1 = penganggur_2023 + bekerja_2023
p1 = penganggur_2023 / n1

nasional_2023 = rata_nasional.loc[2023]
p2 = nasional_2023['Proporsi_Nasional']
n2 = nasional_2023['Angkatan Kerja']

p_pool = (penganggur_2023 + nasional_2023['Jumlah Pengangguran']) / (n1 + n2)
z = (p1 - p2) / np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
p_value = 2 * (1 - stats.norm.cdf(abs(z)))

print(f"Z = {z:.4f}, p-value = {p_value:.4f}")
if p_value < 0.05:
    print("→ Terdapat perbedaan signifikan.")
else:
    print("→ Tidak terdapat perbedaan signifikan.")
