truthlensai_app/
│
├── app.py          <-- Streamlit code below
└── assets/
    └── logo.png    <-- your logo file
import streamlit as st
from datetime import datetime
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="TruthLensAI",
    page_icon="🕵️‍♂️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1e1e2f, #2c2c3c);
    color: #ffffff;
}
.card {
    background: rgba(40, 40, 55, 0.85);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    max-width: 700px;
    margin: auto;
    color: #ffffff;
}
h1 {
    font-family: 'Arial', sans-serif;
    font-size: 3rem;
    background: linear-gradient(to right, #ff8c94, #a18cd1, #fbc2eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
h3 {
    font-family: 'Arial', sans-serif;
    font-weight: normal;
    color: #ffffff;
}
.stButton>button {
    background-color: #a18cd1;
    color: white;
    font-weight: bold;
    padding: 0.5rem 1.5rem;
    border-radius: 10px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #ff8c94;
    transform: scale(1.05);
}
.stTextInput > div, .stRadio > div, .stSelectbox > div {
    background-color: rgba(60,60,75,0.9);
    border-radius: 10px;
    padding: 0.5rem;
    color: #ffffff;
}
input::placeholder {
    color: #e0e0e0;
}
.css-1okebmr option, .stRadio div, .stSelectbox div {
    color: #ffffff;
}
label {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- APP CONTENT ----------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # ---------- LOGO ----------
    logo_path = os.path.join("assets", "logo.png")
    if os.path.exists(logo_path):
        st.image(logo_path, width=150)
    else:
        st.warning("Logo not found! Make sure assets/logo.png exists.")

    # ---------- TITLE & SUBTITLE ----------
    st.markdown("<h1>TruthLensAI</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Detect fake news and explore insights</h3>", unsafe_allow_html=True)
    
    st.write("---")
    
    # ---------- HEADLINE INPUT ----------
    headline = st.text_input("Enter the news headline here:")
    
    # ---------- GENDER INPUT ----------
    gender = st.radio("Select your gender:", ["Male", "Female", "Other"])
    
    # ---------- PLATFORM INPUT ----------
    platform = st.selectbox("Select the platform where you found the news:", ["Instagram", "YouTube", "Facebook", "Twitter"])
    
    st.write("---")
    
    # ---------- DATE ----------
    st.markdown(f"**Date:** {datetime.today().strftime('%d %B %Y')}")
    
    # ---------- ANALYZE BUTTON ----------
    if st.button("Analyze News"):
        st.success(f"Analyzing headline: **{headline}**\n\nFrom platform: **{platform}** for **{gender}** user... 🔍")
    
    st.markdown('</div>', unsafe_allow_html=True)
