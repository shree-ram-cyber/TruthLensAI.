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
/* Subtle gradient background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f0e5f9, #fceff9);
    color: #333;
}

/* Card-like container */
.card {
    background: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.15);
    max-width: 700px;
    margin: auto;
}

/* Headings */
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
}

/* Buttons */
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

/* Input styling */
.stTextInput > div, .stRadio > div, .stSelectbox > div {
    background-color: rgba(255,255,255,0.9);
    border-radius: 10px;
    padding: 0.5rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- APP CONTENT ----------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Title
    st.markdown("<h1>TruthLensAI</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Detect fake news and explore insights</h3>", unsafe_allow_html=True)
    
    st.write("---")
    
    # Headline input
    headline = st.text_input("Enter the news headline here:")
    
    # Gender input
    gender = st.radio("Select your gender:", ["Male", "Female", "Other"])
    
    # Platform input
    platform = st.selectbox("Select the platform where you found the news:", ["Instagram", "YouTube", "Facebook", "Twitter"])
    
    st.write("---")
    
    # Current date
    st.markdown(f"**Date:** {datetime.today().strftime('%d %B %Y')}")
    
    # Submit button
    if st.button("Analyze News"):
        st.success(f"Analyzing headline: **{headline}**\n\nFrom platform: **{platform}** for **{gender}** user... 🔍")
    
    st.markdown('</div>', unsafe_allow_html=True)



