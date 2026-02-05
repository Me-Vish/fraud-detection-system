import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

data = pd.read_csv("C:/Users/Visha/OneDrive/Documents/fraud_detection/transaction_data.csv")

print("\n=== CSV COLUMNS ===")
print(data.columns)

num = data.select_dtypes(include=["number"])
print("\n=== NUMERIC COLUMNS ===")
print(num.columns)

col = num.columns[0]
print("\n=== USING COLUMN ===", col)

X = data[[col]]

model = IsolationForest(contamination=0.02, random_state=42)
model.fit(X)

joblib.dump(model, "fraud_model.pkl")

print("\nMODEL TRAINED SUCCESSFULLY")
