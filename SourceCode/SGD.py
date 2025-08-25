
import pandas as pd
from sklearn.linear_model import SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_excel('data pengangguran.xlsx')
df['Tingkat Pengangguran (%)'] = (
    df['Jumlah Pengangguran'] / (df['Jumlah Pengangguran'] + df['Jumlah Penduduk Bekerja'])
) * 100

X = df[['Jumlah Pengangguran', 'Jumlah Penduduk Bekerja']]
y = df['Tingkat Pengangguran (%)']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = SGDRegressor(max_iter=1000, tol=1e-3)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print('MSE:', mean_squared_error(y_test, y_pred))
print('R²:', r2_score(y_test, y_pred))
