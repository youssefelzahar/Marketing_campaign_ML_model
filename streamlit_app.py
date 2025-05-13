import streamlit as st
import pandas as pd
import joblib

# تحميل الموديل وأسماء الأعمدة
model = joblib.load("logistic_model.pkl")
feature_names = joblib.load("model_features.pkl")  # <-- الأعمدة الأصلية

st.title("🚀 Logistic Regression Classifier")

st.subheader("📥 Input Features")
input_data = {}
for feature in feature_names:
    input_data[feature] = st.number_input(f"Enter value for {feature}")

# تأكد إن الأعمدة بنفس الترتيب
input_df = pd.DataFrame([input_data], columns=feature_names)

# توقع
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0]
    st.success(f"🎯 Prediction: {prediction} (Confidence: {max(prob):.2f})")
