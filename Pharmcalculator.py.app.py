{
    "chunks": [
        {
            "type": "txt",
            "chunk_number": 1,
            "lines": [
                {
                    "line_number": 1,
                    "text": ""
                },
                {
                    "line_number": 2,
                    "text": "import streamlit as st"
                },
                {
                    "line_number": 3,
                    "text": "from PIL import Image"
                },
                {
                    "line_number": 4,
                    "text": ""
                },
                {
                    "line_number": 5,
                    "text": "# Load logo image"
                },
                {
                    "line_number": 6,
                    "text": "logo = Image.open(\"logo.jpg\")"
                },
                {
                    "line_number": 7,
                    "text": ""
                },
                {
                    "line_number": 8,
                    "text": "# Display logo and title"
                },
                {
                    "line_number": 9,
                    "text": "st.image(logo, width=200)"
                },
                {
                    "line_number": 10,
                    "text": "st.title(\"Dosage Calculators\")"
                },
                {
                    "line_number": 11,
                    "text": "st.markdown("
                },
                {
                    "line_number": 12,
                    "text": "\"<p style='font-size:16px; font-style:italic; color:#34495E;'>\""
                },
                {
                    "line_number": 13,
                    "text": "\"A free dosage calculator for pharmacists, undergraduate and graduate students in pharmaceutics and biomedical research\""
                },
                {
                    "line_number": 14,
                    "text": "\"</p>\","
                },
                {
                    "line_number": 15,
                    "text": "unsafe_allow_html=True"
                },
                {
                    "line_number": 16,
                    "text": ")"
                },
                {
                    "line_number": 17,
                    "text": ""
                },
                {
                    "line_number": 18,
                    "text": "# Styled instruction"
                },
                {
                    "line_number": 19,
                    "text": "st.markdown("
                },
                {
                    "line_number": 20,
                    "text": "\"\"\""
                },
                {
                    "line_number": 21,
                    "text": "<p style='font-size:18px; font-style:italic; color:#6C3483;'>"
                },
                {
                    "line_number": 22,
                    "text": "\u27a1\ufe0f <strong>Select a calculator</strong> from the sidebar or tabs to begin your dosage journey."
                },
                {
                    "line_number": 23,
                    "text": "</p>"
                },
                {
                    "line_number": 24,
                    "text": "\"\"\","
                },
                {
                    "line_number": 25,
                    "text": "unsafe_allow_html=True"
                },
                {
                    "line_number": 26,
                    "text": ")"
                },
                {
                    "line_number": 27,
                    "text": ""
                },
                {
                    "line_number": 28,
                    "text": "# Bioavailability calculation function"
                },
                {
                    "line_number": 29,
                    "text": "def calculate_bioavailability(dose_iv, dose_po, auc_iv, auc_po):"
                },
                {
                    "line_number": 30,
                    "text": "try:"
                },
                {
                    "line_number": 31,
                    "text": "bioavailability = (auc_po / dose_po) / (auc_iv / dose_iv) * 100"
                },
                {
                    "line_number": 32,
                    "text": "return round(bioavailability, 2)"
                },
                {
                    "line_number": 33,
                    "text": "except ZeroDivisionError:"
                },
                {
                    "line_number": 34,
                    "text": "return None"
                },
                {
                    "line_number": 35,
                    "text": ""
                },
                {
                    "line_number": 36,
                    "text": "# Bioavailability Calculator Tab"
                },
                {
                    "line_number": 37,
                    "text": "st.header(\"Bioavailability Calculator\")"
                },
                {
                    "line_number": 38,
                    "text": ""
                },
                {
                    "line_number": 39,
                    "text": "st.markdown(\"This calculator estimates the **relative bioavailability** of a drug based on IV and PO doses and their respective AUCs (Area Under Curve).\")"
                },
                {
                    "line_number": 40,
                    "text": ""
                },
                {
                    "line_number": 41,
                    "text": "# Default example values"
                },
                {
                    "line_number": 42,
                    "text": "st.subheader(\"\ud83d\udccc Example Calculation\")"
                },
                {
                    "line_number": 43,
                    "text": "dose_iv_ex = 100"
                },
                {
                    "line_number": 44,
                    "text": "dose_po_ex = 200"
                },
                {
                    "line_number": 45,
                    "text": "auc_iv_ex = 80"
                },
                {
                    "line_number": 46,
                    "text": "auc_po_ex = 120"
                },
                {
                    "line_number": 47,
                    "text": "result_ex = calculate_bioavailability(dose_iv_ex, dose_po_ex, auc_iv_ex, auc_po_ex)"
                },
                {
                    "line_number": 48,
                    "text": ""
                },
                {
                    "line_number": 49,
                    "text": "st.markdown(f\"\"\""
                },
                {
                    "line_number": 50,
                    "text": "**Inputs:**"
                },
                {
                    "line_number": 51,
                    "text": "- IV Dose: {dose_iv_ex} mg"
                },
                {
                    "line_number": 52,
                    "text": "- PO Dose: {dose_po_ex} mg"
                },
                {
                    "line_number": 53,
                    "text": "- AUC IV: {auc_iv_ex}"
                },
                {
                    "line_number": 54,
                    "text": "- AUC PO: {auc_po_ex}"
                },
                {
                    "line_number": 55,
                    "text": ""
                },
                {
                    "line_number": 56,
                    "text": "**Calculated Bioavailability:** {result_ex}%"
                },
                {
                    "line_number": 57,
                    "text": "\"\"\")"
                },
                {
                    "line_number": 58,
                    "text": ""
                },
                {
                    "line_number": 59,
                    "text": "st.markdown(f\"\"\""
                },
                {
                    "line_number": 60,
                    "text": "> A bioavailability of **{result_ex}%** means that the drug administered orally reaches the systemic circulation at **{result_ex}% efficiency** compared to intravenous administration."
                },
                {
                    "line_number": 61,
                    "text": "> This is considered **moderate bioavailability**."
                },
                {
                    "line_number": 62,
                    "text": "> Clinically, this suggests that the oral formulation is reasonably effective, but may require **higher doses or more frequent administration** than the IV form to achieve the same therapeutic effect."
                },
                {
                    "line_number": 63,
                    "text": "> Factors influencing this include **first-pass metabolism**, **solubility**, and **absorption rate**."
                },
                {
                    "line_number": 64,
                    "text": "> For drugs with narrow therapeutic windows, this value may guide **formulation design** or **route selection**."
                },
                {
                    "line_number": 65,
                    "text": "\"\"\")"
                },
                {
                    "line_number": 66,
                    "text": ""
                },
                {
                    "line_number": 67,
                    "text": "# User input section"
                },
                {
                    "line_number": 68,
                    "text": "st.subheader(\"\ud83d\udd22 Try Your Own Calculation\")"
                },
                {
                    "line_number": 69,
                    "text": "dose_iv = st.number_input(\"IV Dose (mg)\", min_value=0.0, format=\"%.2f\")"
                },
                {
                    "line_number": 70,
                    "text": "dose_po = st.number_input(\"PO Dose (mg)\", min_value=0.0, format=\"%.2f\")"
                },
                {
                    "line_number": 71,
                    "text": "auc_iv = st.number_input(\"AUC IV\", min_value=0.0, format=\"%.2f\")"
                },
                {
                    "line_number": 72,
                    "text": "auc_po = st.number_input(\"AUC PO\", min_value=0.0, format=\"%.2f\")"
                },
                {
                    "line_number": 73,
                    "text": ""
                },
                {
                    "line_number": 74,
                    "text": "if st.button(\"Calculate Bioavailability\"):"
                },
                {
                    "line_number": 75,
                    "text": "result = calculate_bioavailability(dose_iv, dose_po, auc_iv, auc_po)"
                },
                {
                    "line_number": 76,
                    "text": "if result is not None:"
                },
                {
                    "line_number": 77,
                    "text": "st.success(f\"Relative Bioavailability: {result:.2f}%\")"
                },
                {
                    "line_number": 78,
                    "text": "else:"
                },
                {
                    "line_number": 79,
                    "text": "st.error(\"Invalid input. Please ensure none of the values are zero.\")"
                }
            ],
            "token_count": 306
        }
    ]
}
