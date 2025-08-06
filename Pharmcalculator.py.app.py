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
st.markdown(
    """
    <p style='font-size:18px; font-style:italic; color:#6C3483;'>
    ➡️ <strong>Select a calculator</strong> from the sidebar or tabs to begin your dosage journey.
    </p>
    """,
    unsafe_allow_html=True
)

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

import streamlit as st
from PIL import Image

# Load logo image
logo = Image.open("logo.jpg")

# Display logo and title
st.image(logo, width=200)
st.title("Dosage Calculators")
st.markdown(
    "<p style='font-size:16px; font-style:italic; color:#34495E;'>"
    "A free dosage calculator for pharmacists, undergraduate and graduate students in pharmaceutics and biomedical research"
    "</p>",
    unsafe_allow_html=True
)

# Styled instruction
st.markdown(
    """
    <p style='font-size:18px; font-style:italic; color:#6C3483;'>
    ➡️ <strong>Select a calculator</strong> from the sidebar or tabs to begin your dosage journey.
    </p>
    """,
    unsafe_allow_html=True
)

# Bioavailability calculation function
def calculate_bioavailability(dose_iv, dose_po, auc_iv, auc_po):
    try:
        bioavailability = (auc_po / dose_po) / (auc_iv / dose_iv) * 100
        return round(bioavailability, 2)
    except ZeroDivisionError:
        return None

# Bioavailability Calculator Tab
st.header("Bioavailability Calculator")

st.markdown("This calculator estimates the **relative bioavailability** of a drug based on IV and PO doses and their respective AUCs (Area Under Curve).")

# Default example values
st.subheader("📌 Example Calculation")
dose_iv_ex = 100
dose_po_ex = 200
auc_iv_ex = 80
auc_po_ex = 120
result_ex = calculate_bioavailability(dose_iv_ex, dose_po_ex, auc_iv_ex, auc_po_ex)

st.markdown(f"""
**Inputs:**
- IV Dose: {dose_iv_ex} mg  
- PO Dose: {dose_po_ex} mg  
- AUC IV: {auc_iv_ex}  
- AUC PO: {auc_po_ex}  

**Calculated Bioavailability:** {result_ex}%
""")

st.markdown(f"""
> A bioavailability of **{result_ex}%** means that the drug administered orally reaches the systemic circulation at **{result_ex}% efficiency** compared to intravenous administration.  
> This is considered **moderate bioavailability**.  
> Clinically, this suggests that the oral formulation is reasonably effective, but may require **higher doses or more frequent administration** than the IV form to achieve the same therapeutic effect.  
> Factors influencing this include **first-pass metabolism**, **solubility**, and **absorption rate**.  
> For drugs with narrow therapeutic windows, this value may guide **formulation design** or **route selection**.
""")

# User input section
st.subheader("🔢 Try Your Own Calculation")
dose_iv = st.number_input("IV Dose (mg)", min_value=0.0, format="%.2f")
dose_po = st.number_input("PO Dose (mg)", min_value=0.0, format="%.2f")
auc_iv = st.number_input("AUC IV", min_value=0.0, format="%.2f")
auc_po = st.number_input("AUC PO", min_value=0.0, format="%.2f")

if st.button("Calculate Bioavailability"):
    result = calculate_bioavailability(dose_iv, dose_po, auc_iv, auc_po)
    if result is not None:
        st.success(f"Relative Bioavailability: {result:.2f}%")
    else:
        st.error("Invalid input. Please ensure none of the values are zero.")

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
