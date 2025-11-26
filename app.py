import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="TruthLensAI", layout="wide", page_icon="📰")

# --- Custom CSS ---
st.markdown("""
    <style>
    /* Dark gradient background */
    body, .main {
        background: linear-gradient(135deg, #0d0d0d, #1a1a1a);
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }

    /* Gradient heading style */
    .big-heading {
        font-size: 50px;
        font-weight: bold;
        background: linear-gradient(45deg, #ff6f3c, #ffa94d);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }

    /* Input boxes styling */
    div.stTextInput>div>input, div.stSelectbox>div>div>div>select {
        background-color: #1a1a1a;
        color: white;
        border: 1px solid #ff6f3c;
        border-radius: 6px;
        padding: 0.5em;
        font-size: 18px;
    }

    /* Buttons style */
    .stButton>button {
        background-color: #ff6f3c;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.2em;
        border: none;
    }

    .stButton>button:hover {
        background-color: #ff4500;
        color: white;
    }

    /* Hide footer */
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Heading ---
st.markdown('<div class="big-heading">TruthLensAI</div>', unsafe_allow_html=True)
st.markdown("Enter a news headline and select options below:")

# --- Inputs ---
headline = st.text_input("Your Headline Here")

col1, col2 = st.columns(2)
with col1:
    platform = st.selectbox("Select Platform", ["Instagram", "YouTube", "Facebook"])
with col2:
    gender = st.selectbox("Select Gender", ["Male", "Female", "Other"])

# Optional: Show what user entered
if headline:
    st.markdown(f"**Headline:** {headline}")
    st.markdown(f"**Platform:** {platform}")
    st.markdown(f"**Gender:** {gender}")

