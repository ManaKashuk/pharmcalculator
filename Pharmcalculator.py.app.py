
import streamlit as st
from PIL import Image

# Load and display logo
try:
    logo = Image.open("logo.jpg")
    st.image(logo, width=200)
except:
    st.warning("Logo image not found. Please ensure 'logo.jpg' is in the working directory.")

# Title and tagline
st.title("Dosage Calculators")
st.markdown(
    "<p style='font-size:16px; font-style:italic; color:#34495E;'>"
    "A free dosage calculator for pharmacists, undergraduate and graduate students in pharmaceutics and biomedical research"
    "</p>",
    unsafe_allow_html=True
)

# Tabs for different calculator categories
tabs = st.tabs([
    "Clinical Pharmacy",
    "Analytical Chemistry",
    "Cleaning Validation",
    "Process Engineering",
    "In-Process Calculations",
    "Medication Dose Calculators",
    "IV Rate & Time Calculators",
    "Pediatric Dosing Calculators",
    "Clinical Tools",
    "IV Medication Conversions"
])

# Function to generate clinical explanation
def generate_explanation(calculator_type, value):
    if calculator_type == "bioavailability":
        return f"""
        A bioavailability of {value}% means that the drug administered orally reaches the systemic circulation at {value}% efficiency compared to intravenous administration.
        This is considered {'high' if value > 80 else 'moderate' if value > 50 else 'low'}, and may influence dosing frequency or formulation choice.
        """
    elif calculator_type == "molarity":
        return f"""
        A molarity of {value} mol/L indicates the concentration of solute in the solution. This value is essential for preparing accurate chemical solutions in analytical procedures.
        """
    elif calculator_type == "MACO":
        return f"""
        A MACO value of {value} mg represents the maximum allowable carryover of a substance into the next product. This ensures safety and compliance in cleaning validation protocols.
        """
    elif calculator_type == "OPEE":
        return f"""
        An Overall Production Equipment Effectiveness (OPEE) of {value}% reflects the efficiency of equipment in pharmaceutical manufacturing. Higher values indicate better utilization and productivity.
        """
    elif calculator_type == "IV flow rate":
        return f"""
        An IV flow rate of {value} mL/hr determines the speed at which intravenous fluids are administered. Accurate flow rates are critical for patient safety and therapeutic effectiveness.
        """
    else:
        return "Explanation not available for this calculator."

# Clinical Pharmacy Tab
with tabs[0]:
    st.header("Bioavailability Calculator")
    dose_iv = st.number_input("IV Dose (mg)", min_value=0.0, format="%.2f")
    dose_po = st.number_input("PO Dose (mg)", min_value=0.0, format="%.2f")
    auc_iv = st.number_input("AUC IV", min_value=0.0, format="%.2f")
    auc_po = st.number_input("AUC PO", min_value=0.0, format="%.2f")

    if st.button("Calculate Bioavailability"):
        try:
            result = (auc_po / dose_po) / (auc_iv / dose_iv) * 100
            st.success(f"Relative Bioavailability: {result:.2f}%")
            if st.button("Explain this result"):
                explanation = generate_explanation("bioavailability", result)
                st.markdown(explanation)
        except ZeroDivisionError:
            st.error("Invalid input. Please ensure none of the values are zero.")

# Analytical Chemistry Tab
with tabs[1]:
    st.header("Molarity Calculator")
    moles = st.number_input("Moles of solute", min_value=0.0, format="%.4f")
    volume = st.number_input("Volume of solution (L)", min_value=0.0, format="%.4f")

    if st.button("Calculate Molarity"):
        try:
            result = moles / volume
            st.success(f"Molarity: {result:.4f} mol/L")
            if st.button("Explain this result", key="explain_molarity"):
                explanation = generate_explanation("molarity", result)
                st.markdown(explanation)
        except ZeroDivisionError:
            st.error("Volume cannot be zero.")

# Cleaning Validation Tab
with tabs[2]:
    st.header("MACO Calculator")
    batch_size = st.number_input("Next product batch size (mg)", min_value=0.0, format="%.2f")
    safety_factor = st.number_input("Safety factor", min_value=0.0, format="%.2f")
    min_daily_dose = st.number_input("Minimum daily dose of previous product (mg)", min_value=0.0, format="%.2f")

    if st.button("Calculate MACO"):
        try:
            result = (min_daily_dose * batch_size) / safety_factor
            st.success(f"MACO: {result:.2f} mg")
            if st.button("Explain this result", key="explain_maco"):
                explanation = generate_explanation("MACO", result)
                st.markdown(explanation)
        except ZeroDivisionError:
            st.error("Safety factor cannot be zero.")

# Process Engineering Tab
with tabs[3]:
    st.header("OPEE Calculator")
    actual_output = st.number_input("Actual Output", min_value=0.0, format="%.2f")
    ideal_output = st.number_input("Ideal Output", min_value=0.0, format="%.2f")

    if st.button("Calculate OPEE"):
        try:
            result = (actual_output / ideal_output) * 100
            st.success(f"OPEE: {result:.2f}%")
            if st.button("Explain this result", key="explain_opee"):
                explanation = generate_explanation("OPEE", result)
                st.markdown(explanation)
        except ZeroDivisionError:
            st.error("Ideal output cannot be zero.")

# In-Process Calculations Tab
with tabs[4]:
    st.header("IV Flow Rate Calculator")
    volume_ml = st.number_input("Volume to be infused (mL)", min_value=0.0, format="%.2f")
    time_hr = st.number_input("Time (hours)", min_value=0.0, format="%.2f")

    if st.button("Calculate IV Flow Rate"):
        try:
            result = volume_ml / time_hr
            st.success(f"IV Flow Rate: {result:.2f} mL/hr")
            if st.button("Explain this result", key="explain_iv"):
                explanation = generate_explanation("IV flow rate", result)
                st.markdown(explanation)
        except ZeroDivisionError:
            st.error("Time cannot be zero.")

# Medication Dose Calculators Tab
with tabs[5]:
    st.header("Medication Dose Calculators")
    dose = st.number_input("Dose per unit (mg)", min_value=0.0, format="%.2f")
    units = st.number_input("Number of units", min_value=0.0, format="%.2f")
    if st.button("Calculate Total Dose"):
        result = dose * units
        st.success(f"Total Dose: {result:.2f} mg")

# IV Rate & Time Calculators Tab
with tabs[6]:
    st.header("IV Rate & Time Calculators")
    volume = st.number_input("Volume (mL)", min_value=0.0, format="%.2f")
    rate = st.number_input("Rate (mL/hr)", min_value=0.0, format="%.2f")
    if st.button("Calculate Infusion Time"):
        try:
            time = volume / rate
            st.success(f"Infusion Time: {time:.2f} hours")
        except ZeroDivisionError:
            st.error("Rate cannot be zero.")

# Pediatric Dosing Calculators Tab
with tabs[7]:
    st.header("Pediatric Dosing Calculators")
    weight = st.number_input("Child's Weight (kg)", min_value=0.0, format="%.2f")
    dose_per_kg = st.number_input("Dose per kg (mg/kg)", min_value=0.0, format="%.2f")
    if st.button("Calculate Pediatric Dose"):
        result = weight * dose_per_kg
        st.success(f"Pediatric Dose: {result:.2f} mg")

# Clinical Tools Tab
with tabs[8]:
    st.header("Clinical Tools")
    weight = st.number_input("Weight (kg)", min_value=0.0, format="%.2f")
    height = st.number_input("Height (cm)", min_value=0.0, format="%.2f")
    if st.button("Calculate BMI"):
        try:
            height_m = height / 100
            bmi = weight / (height_m ** 2)
            st.success(f"BMI: {bmi:.2f}")
        except ZeroDivisionError:
            st.error("Height cannot be zero.")

# IV Medication Conversions Tab
with tabs[9]:
    st.header("IV Medication Conversions")
    dose_mg = st.number_input("Dose (mg)", min_value=0.0, format="%.2f")
    concentration = st.number_input("Concentration (mg/mL)", min_value=0.0, format="%.2f")
    if st.button("Calculate Volume to Administer"):
        try:
            volume = dose_mg / concentration
            st.success(f"Volume to Administer: {volume:.2f} mL")
        except ZeroDivisionError:
            st.error("Concentration cannot be zero.")
