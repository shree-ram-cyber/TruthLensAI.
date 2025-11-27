import streamlit as st
from datetime import datetime

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="TruthLensAI",
    page_icon="🕵️‍♂️",
    layout="centered"
)

# ---------------------- CUSTOM CSS ----------------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1a1a2e, #16213e);
    color: #ffffff;
}

/* Main card */
.card {
    background: rgba(40, 40, 55, 0.85);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    max-width: 800px;
    margin: auto;
    color: #ffffff;
}

/* Heading */
h1 {
    font-family: 'Arial', sans-serif;
    font-size: 3rem;
    background: linear-gradient(to right, #ff8c94, #a18cd1, #fbc2eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subheadings */
h2, h3 {
    color: #ffffff;
}

/* Buttons */
.stButton>button {
    background-color: #a18cd1;
    color: white;
    font-weight: bold;
    padding: 0.6rem 1.7rem;
    border-radius: 10px;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    background-color: #ff8c94;
    transform: scale(1.05);
}

/* Inputs */
.stTextInput > div, .stRadio > div, .stSelectbox > div {
    background-color: rgba(60,60,75,0.9);
    border-radius: 10px;
    padding: 0.5rem;
    color: #ffffff;
}

/* Make the gender radio options white only */
div[role="radiogroup"] label {
    color: #ffffff !important;
}
div[role="radiogroup"] div {
    color: #ffffff !important;
}

/* FAQ box */
.faq-box {
    background: rgba(255,255,255,0.15);
    padding: 1rem;
    border-radius: 10px;
    margin-top: 10px;
    border: 1px solid rgba(255,255,255,0.3);
}

/* 🔥 Translucent white box */
.translucent-box {
    background: rgba(255, 255, 255, 0.18);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    padding: 1.5rem;
    border-radius: 15px;
    margin-top: 1rem;
    border: 1px solid rgba(255, 255, 255, 0.3);
    color: #ffffff;
}

</style>
""", unsafe_allow_html=True)


# ---------------------- FAQ DATA ----------------------
faq = {
    "What is TruthLensAI?": "TruthLensAI analyzes headlines to detect potential fake news.",
    "How do I use the app?": "Enter a headline, select gender & platform, then click Analyze News.",
    "Any tips for spotting fake news?": "Check multiple sources, verify images, avoid sensational claims.",
    "Why ask gender & platform?": "To analyze how misinformation spreads differently across groups."
}


# ---------------------- NAVIGATION ----------------------
page = st.sidebar.radio("Navigate", ["Home", "Fake News Detector"])


# ---------------------- HOME PAGE ----------------------
if page == "Home":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown("<h1>TruthLensAI</h1>", unsafe_allow_html=True)
    st.markdown("### Your companion for spotting misinformation 🔍")

    st.write("---")

    # 🔥🔥 HOW TO USE IN TRANSLUCENT BOX 🔥🔥
    st.markdown("""
    <div class="translucent-box">
        <h3>How to Use</h3>
        <p>1️⃣ Go to the Fake News Detector screen using the menu on
