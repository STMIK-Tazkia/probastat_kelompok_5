import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.read_excel("data pengangguran.xlsx")

df["Tingkat Pengangguran (%)"] = (
    df["Jumlah Pengangguran"] / (df["Jumlah Pengangguran"] + df["Jumlah Penduduk Bekerja"])
) * 100

df["Tanggal"] = pd.to_datetime(df["Tanggal"])
df["Tahun"] = df["Tanggal"].dt.year

rata2 = df["Tingkat Pengangguran (%)"].mean()
df["Kategori"] = df["Tingkat Pengangguran (%)"].apply(lambda x: "Tinggi" if x >= rata2 else "Rendah")

X = df[["Jumlah Pengangguran", "Jumlah Penduduk Bekerja"]]
y = df["Kategori"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = GaussianNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Akurasi:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

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
