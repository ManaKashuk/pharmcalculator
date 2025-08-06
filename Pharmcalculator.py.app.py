import streamlit as st
from PIL import Image

# Load and display the PharmCalculator logo at the top
logo = Image.open("logo.jpg")
st.image(logo, width=200)

# Update title of the app
st.markdown("<h2>Dosage Calculators</h2>", unsafe_allow_html=True)
st.markdown("<p style='font-size: 20px;'>A free dosage calculator for pharmacists, undergraduate and graduate students in pharmaceutics and biomedical research</p>",
    unsafe_allow_html=True)

# Placeholder for tabs and calculators
st.markdown("---")
st.info("Select a calculator from the sidebar or tabs.")
# Define tabs
tabs = st.tabs([
    "Clinical Pharmacy",
    "Analytical Chemistry",
    "Cleaning Validation",
    "Process Engineering",
    "In-Process Calculations"
])

# Clinical Pharmacy Tab
with tabs[0]:
    st.header("Clinical Pharmacy Calculators")

    st.subheader("Bioavailability Calculator")
    dose_iv = st.number_input("IV Dose (mg)", min_value=0.0, format="%.2f")
    dose_po = st.number_input("PO Dose (mg)", min_value=0.0, format="%.2f")
    auc_iv = st.number_input("AUC IV", min_value=0.0, format="%.2f")
    auc_po = st.number_input("AUC PO", min_value=0.0, format="%.2f")

    def calculate_bioavailability(dose_iv, dose_po, auc_iv, auc_po):
        try:
            return round((auc_po / dose_po) / (auc_iv / dose_iv) * 100, 2)
        except ZeroDivisionError:
            return None

    if st.button("Calculate Bioavailability"):
        result = calculate_bioavailability(dose_iv, dose_po, auc_iv, auc_po)
        if result is not None:
            st.success(f"Relative Bioavailability: {result:.2f}%")
        else:
            st.error("Invalid input. Please ensure none of the values are zero.")

# Analytical Chemistry Tab
with tabs[1]:
    st.header("Analytical Chemistry Calculators")

    st.subheader("Molarity Calculator")
    moles = st.number_input("Moles of solute", min_value=0.0, format="%.4f")
    volume = st.number_input("Volume of solution (L)", min_value=0.0, format="%.4f")

    def calculate_molarity(moles, volume):
        try:
            return round(moles / volume, 4)
        except ZeroDivisionError:
            return None

    if st.button("Calculate Molarity"):
        result = calculate_molarity(moles, volume)
        if result is not None:
            st.success(f"Molarity: {result:.4f} mol/L")
        else:
            st.error("Invalid input. Volume cannot be zero.")

# Cleaning Validation Tab
with tabs[2]:
    st.header("Cleaning Validation Calculators")

    st.subheader("MACO Calculator")
    batch_size = st.number_input("Next product batch size (mg)", min_value=0.0, format="%.2f")
    min_daily_dose = st.number_input("Minimum daily dose of next product (mg)", min_value=0.0, format="%.2f")
    safety_factor = st.number_input("Safety factor", min_value=0.0, format="%.2f")
    previous_dose = st.number_input("Maximum daily dose of previous product (mg)", min_value=0.0, format="%.2f")

    def calculate_maco(batch_size, min_daily_dose, safety_factor, previous_dose):
        try:
            return round((previous_dose * batch_size) / (min_daily_dose * safety_factor), 2)
        except ZeroDivisionError:
            return None

    if st.button("Calculate MACO"):
        result = calculate_maco(batch_size, min_daily_dose, safety_factor, previous_dose)
        if result is not None:
            st.success(f"MACO: {result:.2f} mg")
        else:
            st.error("Invalid input. Please ensure none of the values are zero.")

# Process Engineering Tab
with tabs[3]:
    st.header("Process Engineering Calculators")

    st.subheader("OPEE Calculator")
    actual_output = st.number_input("Actual Output", min_value=0.0, format="%.2f")
    ideal_output = st.number_input("Ideal Output", min_value=0.0, format="%.2f")

    def calculate_opee(actual_output, ideal_output):
        try:
            return round((actual_output / ideal_output) * 100, 2)
        except ZeroDivisionError:
            return None

    if st.button("Calculate OPEE"):
        result = calculate_opee(actual_output, ideal_output)
        if result is not None:
            st.success(f"OPEE: {result:.2f}%")
        else:
            st.error("Invalid input. Ideal output cannot be zero.")

# In-Process Calculations Tab
with tabs[4]:
    st.header("In-Process Calculations")

    st.subheader("IV Flow Rate Calculator")
    volume_ml = st.number_input("Volume to be infused (mL)", min_value=0.0, format="%.2f")
    time_min = st.number_input("Time (minutes)", min_value=0.0, format="%.2f")

    def calculate_iv_flow_rate(volume_ml, time_min):
        try:
            return round(volume_ml / time_min, 2)
        except ZeroDivisionError:
            return None

    if st.button("Calculate IV Flow Rate"):
        result = calculate_iv_flow_rate(volume_ml, time_min)
        if result is not None:
            st.success(f"IV Flow Rate: {result:.2f} mL/min")
        else:
            st.error("Invalid input. Time cannot be zero.")
