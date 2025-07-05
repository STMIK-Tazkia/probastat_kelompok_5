import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Flight ID': ['FL001', 'FL002', 'FL003', 'FL004'],
    'Maskapai': ['Lion Air', 'Garuda Indonesia', 'Citilink', 'Batik Air'],
    'Jenis Maskapai': ['Berbiaya Rendah', 'Premium', 'Berbiaya Rendah', 'Premium'],
    'Status Keterlambatan': ['Terlambat', 'Tepat Waktu', 'Terlambat', 'Terlambat'],
    'Durasi Delay': [45, 0, 30, 10]
}

df = pd.DataFrame(data)

prob_delay = df[df['Status Keterlambatan'] == 'Terlambat'].groupby('Jenis Maskapai').size() / df.groupby('Jenis Maskapai').size()

print("Probabilitas Keterlambatan per Jenis Maskapai:")
print(prob_delay)

prob_delay.plot(kind='bar', color=['orange', 'green'])
plt.title('Probabilitas Keterlambatan per Jenis Maskapai')
plt.ylabel('Probabilitas')
plt.xlabel('Jenis Maskapai')
plt.xticks(rotation=0)
plt.ylim(0, 1.1)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
