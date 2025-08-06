import streamlit as st
from PIL import Image

# Load and display the logo with smaller width
logo = Image.open("logo.jpg")
st.image(logo, width=200)

# Updated title and tagline
st.markdown("<h2>Dosage Calculators</h2>", unsafe_allow_html=True)
st.markdown(
    "<p style='font-size: 16px;'>A free dosage calculator for pharmacists, undergraduate and graduate students in pharmaceutics and biomedical research</p>",
    unsafe_allow_html=True
)

# Placeholder for tabs and calculators
st.markdown("---")
st.info("Select a calculator from the sidebar or tabs.")
