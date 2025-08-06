
import streamlit as st

# -----------------------------
# Clinical Pharmacy Calculator
# -----------------------------
def calculate_bioavailability(dose_iv, dose_po, auc_iv, auc_po):
    try:
        return round((auc_po / dose_po) / (auc_iv / dose_iv) * 100, 2)
    except ZeroDivisionError:
        return None

# -----------------------------
# Analytical Chemistry Calculator
# -----------------------------
def calculate_molarity(moles, volume_liters):
    try:
        return round(moles / volume_liters, 4)
    except ZeroDivisionError:
        return None

# -----------------------------
# Cleaning Validation Calculator
# -----------------------------
def calculate_maco(ldt, batch_size, safety_factor):
    try:
        return round((ldt * batch_size) / safety_factor, 4)
    except ZeroDivisionError:
        return None

# -----------------------------
# Process Engineering Calculator
# -----------------------------
def calculate_opee(actual_output, effective_time):
    try:
        return round(actual_output / effective_time, 2)
    except ZeroDivisionError:
        return None

# -----------------------------
# In-Process Calculations
# -----------------------------
def calculate_iv_flow_rate(volume_ml, time_min):
    try:
        return round(volume_ml / time_min, 2)
    except ZeroDivisionError:
        return None

# -----------------------------
# Streamlit App
# -----------------------------
st.set_page_config(page_title="PharmaCalc Multi-Tab App", layout="centered")
st.title("PharmaCalc Multi-Tab Calculator")

tabs = st.tabs([
    "Clinical Pharmacy",
    "Analytical Chemistry",
    "Cleaning Validation",
    "Process Engineering",
    "In-Process Calculations"
])

# Clinical Pharmacy Tab
with tabs[0]:
    st.header("Bioavailability Calculator")
    dose_iv = st.number_input("IV Dose (mg)", min_value=0.0)
    dose_po = st.number_input("PO Dose (mg)", min_value=0.0)
    auc_iv = st.number_input("AUC IV", min_value=0.0)
    auc_po = st.number_input("AUC PO", min_value=0.0)
    if st.button("Calculate Bioavailability"):
        result = calculate_bioavailability(dose_iv, dose_po, auc_iv, auc_po)
        if result is not None:
            st.success(f"Relative Bioavailability: {result}%")
        else:
            st.error("Invalid input. Please ensure none of the values are zero.")

# Analytical Chemistry Tab
with tabs[1]:
    st.header("Molarity Calculator")
    moles = st.number_input("Moles of solute", min_value=0.0)
    volume_liters = st.number_input("Volume of solution (L)", min_value=0.0)
    if st.button("Calculate Molarity"):
        result = calculate_molarity(moles, volume_liters)
        if result is not None:
            st.success(f"Molarity: {result} mol/L")
        else:
            st.error("Invalid input. Please ensure volume is not zero.")

# Cleaning Validation Tab
with tabs[2]:
    st.header("MACO Calculator")
    ldt = st.number_input("Lowest Therapeutic Dose (mg)", min_value=0.0)
    batch_size = st.number_input("Batch Size (mg)", min_value=0.0)
    safety_factor = st.number_input("Safety Factor", min_value=0.0)
    if st.button("Calculate MACO"):
        result = calculate_maco(ldt, batch_size, safety_factor)
        if result is not None:
            st.success(f"MACO: {result} mg")
        else:
            st.error("Invalid input. Please ensure safety factor is not zero.")

# Process Engineering Tab
with tabs[3]:
    st.header("Overall Production Equipment Effectiveness (OPEE)")
    actual_output = st.number_input("Actual Output (units)", min_value=0.0)
    effective_time = st.number_input("Effective Time (hours)", min_value=0.0)
    if st.button("Calculate OPEE"):
        result = calculate_opee(actual_output, effective_time)
        if result is not None:
            st.success(f"OPEE: {result} units/hour")
        else:
            st.error("Invalid input. Please ensure time is not zero.")

# In-Process Calculations Tab
with tabs[4]:
    st.header("IV Flow Rate Calculator")
    volume_ml = st.number_input("Volume to be infused (mL)", min_value=0.0)
    time_min = st.number_input("Time (minutes)", min_value=0.0)
    if st.button("Calculate IV Flow Rate"):
        result = calculate_iv_flow_rate(volume_ml, time_min)
        if result is not None:
            st.success(f"IV Flow Rate: {result} mL/min")
        else:
            st.error("Invalid input. Please ensure time is not zero.")
