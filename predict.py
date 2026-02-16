import pandas as pd
import joblib

# ===============================
# Load model
# ===============================
model = joblib.load("attrition_model.joblib")
print("Model berhasil dimuat.")

# ===============================
# Load data karyawan
# ===============================
df = pd.read_csv("employee_attrition_ready.csv")

# Drop kolom yang tidak dipakai model
drop_cols = ["employee_id", "attrition"]
df_model = df.drop(columns=[c for c in drop_cols if c in df.columns])

# ===============================
# Prediksi
# ===============================
prob_attrition = model.predict_proba(df_model)[:, 1]
df["attrition_probability"] = prob_attrition
df["attrition_prediction"] = (prob_attrition >= 0.35).astype(int)

# ===============================
# Output
# ===============================
print("\nHasil prediksi:")
print(df[["employee_id", "attrition_probability", "attrition_prediction"]])

# Simpan hasil
df.to_csv("prediction_result.csv", index=False)
print("\nHasil disimpan ke prediction_result.csv")
