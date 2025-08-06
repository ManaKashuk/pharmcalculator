import streamlit as st

# Define the bioavailability calculation function
def calculate_bioavailability(dose_iv, dose_po, auc_iv, auc_po):
    """Calculate relative bioavailability as a percentage"""
    try:
        bioavailability = (auc_po / dose_po) / (auc_iv / dose_iv) * 100
        return round(bioavailability, 2)
    except ZeroDivisionError:
        return None

# Streamlit UI
st.title("PharmaCalc: Bioavailability Calculator")

st.markdown("""
This calculator estimates the **relative bioavailability** of a drug based on IV and PO doses and their respective AUCs (Area Under Curve).
""")

# Input fields
dose_iv = st.number_input("IV Dose (mg)", min_value=0.0, format="%.2f")
dose_po = st.number_input("PO Dose (mg)", min_value=0.0, format="%.2f")
auc_iv = st.number_input("AUC IV", min_value=0.0, format="%.2f")
auc_po = st.number_input("AUC PO", min_value=0.0, format="%.2f")

# Calculate button
if st.button("Calculate Bioavailability"):
    result = calculate_bioavailability(dose_iv, dose_po, auc_iv, auc_po)
    if result is not None:
        st.success(f"Relative Bioavailability: {result:.2f}%")
    else:
        st.error("Invalid input. Please ensure none of the values are zero.")

# Footer
st.markdown("---")
st.caption("Powered by Streamlit • PharmaCalc Prototype")
