
import streamlit as st
from PIL import Image

# Load logo image
logo = Image.open("logo.jpg")

# Display logo and title
st.image(logo, width=200)
st.title("Dosage Calculators")
st.markdown(
    "<p style='font-size:20px; font-style:italic; color:#34495E;'>"
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
