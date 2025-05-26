import streamlit as st
import pandas as pd

# 🎯 Set browser tab title and icon
st.set_page_config(page_title="My Health Dashboard", page_icon="🩺")

# 🌟 Main App Heading
st.title("Health Risk Predictor Dashboard")

# 🎛️ Initial screen: Show only choices
choice = st.radio("Please choose what you want to do:", ["Select", "🔮 Check My Health Risk", "📊 View Health Data & Stats"], horizontal=True)

# 🧠 Risk Prediction Logic
def predict_risk(age, smoking, alcohol, physical_activity, bmi, blood_pressure, diabetes, cholesterol):
    score = 0
    if age > 50:
        score += 2
    elif age > 35:
        score += 1
    if smoking == "Yes":
        score += 2
    if alcohol == "Yes":
        score += 1
    if physical_activity == "Low":
        score += 2
    elif physical_activity == "Medium":
        score += 1
    if bmi >= 30:
        score += 2
    elif bmi >= 25:
        score += 1
    if blood_pressure == "High":
        score += 2
    elif blood_pressure == "Low":
        score += 1
    if diabetes == "Yes":
        score += 2
    if cholesterol == "High":
        score += 1
    elif cholesterol == "Low":
        score += 1  
    

    return "High" if score >= 7 else "Medium" if score >= 4 else "Low"

# 📝 If user selects "Check My Health Risk"
if choice == "🔮 Check My Health Risk":
    st.subheader("📝 Enter your details to predict your health risk")

    with st.form("risk_form"):
        name = st.text_input("Name")
        age = st.number_input("Age", min_value=1, max_value=120, step=1)
        smoking = st.selectbox("Do you smoke?", ["Select", "Yes", "No"])
        alcohol = st.selectbox("Do you consume alcohol?", ["Select", "Yes", "No"])
        physical_activity = st.selectbox("Physical Activity Level", ["Select", "Low", "Medium", "High"])
        bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
        blood_pressure = st.selectbox("Blood Pressure Level", ["Select", "High", "Normal","Low"])
        diabetes = st.selectbox("Do you have diabetes?", ["Select", "Yes", "No"])
        cholesterol = st.selectbox("Cholesterol Level", ["Select", "High", "Normal","Low"])

        submitted = st.form_submit_button("Predict Risk")

        if submitted:
            if "Select" in [smoking, alcohol, physical_activity, blood_pressure, diabetes, cholesterol] or not name:
                st.warning("Please fill in all fields correctly.")
            else:
                risk = predict_risk(age, smoking, alcohol, physical_activity, bmi, blood_pressure, diabetes, cholesterol)
                st.success(f"👤 {name}, your predicted health risk level is: **{risk}**")

            # Save the user input and risk to CSV
            import csv
        
            new_data = [name, age, smoking, alcohol, physical_activity, bmi, blood_pressure, diabetes, cholesterol, risk]
        
            with open('health-data.csv', 'a', newline='') as f:
               writer = csv.writer(f)
               writer.writerow(new_data)

# 📊 If user selects "View Health Data & Stats"
elif choice == "📊 View Health Data & Stats":
    try:
        df = pd.read_csv("health-data.csv")
        st.success("Dataset loaded successfully!")
        st.subheader("📋 Full Health Dataset")
        st.dataframe(df)

        st.subheader("📈 Risk Level Distribution")
        st.bar_chart(df['RiskLevel'].value_counts())
    except FileNotFoundError:
        st.error("⚠️ Could not find 'health-data.csv'. Make sure it exists in the same folder.")

# 👀 If no choice is made
elif choice == "Select":
    st.info("⬆️ Please select an option to get started.")