import streamlit as st
from datetime import datetime

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

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Poppins', sans-serif;
}

/* Animated Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
    animation: shift 14s ease infinite;
    background-size: 400% 400%;
    color: #ffffff;
}

@keyframes shift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}


@keyframes floaty {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-6px); }
    100% { transform: translateY(0px); }
}

/* Card Container */
.card {
    background: rgba(40, 40, 55, 0.75);
    padding: 2.3rem;
    border-radius: 22px;
    box-shadow: 0 0 25px rgba(255, 160, 255, 0.28);
    backdrop-filter: blur(14px);
    max-width: 700px;
    margin: auto;
}

/* Heading */
h1 {
    font-family: 'Poppins', sans-serif;
    font-size: 3.1rem;
    background: linear-gradient(to right, #ff8c94, #a18cd1, #fbc2eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    text-shadow: 0 0 15px rgba(255,255,255,0.25);
}

/* Subheading */
h3 {
    font-family: 'Poppins', sans-serif;
    font-weight: 300;
    color: #ffffff;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #a18cd1, #fbc2eb);
    color: white;
    font-weight: 600;
    padding: 0.7rem 2rem;
    border-radius: 12px;
    border: none;
    font-size: 1rem;
    transition: 0.25s ease;
    box-shadow: 0 0 12px rgba(255, 200, 255, 0.2);
}

.stButton>button:hover {
    transform: scale(1.07);
    box-shadow: 0 0 22px rgba(255, 200, 255, 0.45);
}

/* Inputs & boxes */
.stTextInput > div, .stRadio > div, .stSelectbox > div {
    background: rgba(60, 60, 75, 0.85);
    border-radius: 12px;
    padding: 0.6rem;
    color: #ffffff;
}

/* Input glow on focus */
input:focus {
    border: 1.4px solid #ffbce7 !important;
    box-shadow: 0 0 8px rgba(255, 188, 231, 0.6);
}

/* Fix for label color */
label {
    color: #ffffff !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- APP CONTENT ----------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # ---------- LOGO ----------
    st.markdown(
        '<img src="assets/logo.png" class="logo-style" width="150">',
        unsafe_allow_html=True
    )

    # ---------- TITLE ----------
    st.markdown("<h1>TruthLensAI</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Detect fake news and explore insights</h3>", unsafe_allow_html=True)

    st.write("---")

    # ---------- HEADLINE INPUT ----------
    headline = st.text_input("Enter the news headline here:")

    # ---------- GENDER INPUT ----------
    gender = st.radio("Select your gender:", ["Male", "Female", "Other"])

    # ---------- PLATFORM INPUT ----------
    platform = st.selectbox(
        "Select the platform where you found the news:",
        ["Instagram", "YouTube", "Facebook", "Twitter"],
    )

    st.write("---")

    # ---------- DATE ----------
    st.markdown(f"**Date:** {datetime.today().strftime('%d %B %Y')}")

    # ---------- ANALYZE BUTTON ----------
    if st.button("Analyze News"):
        st.success(
            f"Analyzing headline: **{headline}**\n\nFrom platform: **{platform}** for **{gender}** user... 🔍"
        )

    st.markdown('</div>', unsafe_allow_html=True)
