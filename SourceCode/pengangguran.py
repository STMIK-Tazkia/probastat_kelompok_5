import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("data pengangguran.xlsx")

df["Tingkat Pengangguran (%)"] = (
    df["Jumlah Pengangguran"] / (df["Jumlah Pengangguran"] + df["Jumlah Penduduk Bekerja"])
) * 100

df["Tanggal"] = pd.to_datetime(df["Tanggal"])

df["Tahun"] = df["Tanggal"].dt.year

plt.figure(figsize=(12,6))

plt.bar(df["Tahun"], df["Tingkat Pengangguran (%)"], color="skyblue", label="Tingkat Pengangguran (%)")

plt.plot(df["Tahun"], df["Tingkat Pengangguran (%)"], color="black", marker="o", linewidth=2, label="Tren")

for i, val in enumerate(df["Tingkat Pengangguran (%)"]):
    plt.text(df["Tahun"].iloc[i], val + 0.2, f"{val:.1f}%", ha='center', fontsize=9)

plt.title("Tingkat Pengangguran (%) per Tahun dengan Tren")
plt.xlabel("Tahun")
plt.ylabel("Tingkat Pengangguran (%)")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle="--", alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()