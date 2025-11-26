import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="TruthLensAI", layout="wide", page_icon="📰")

# --- Custom CSS for dark gradient and styling ---
st.markdown("""
    <style>
    /* Dark gradient background */
    body, .main {
        background: linear-gradient(135deg, #0d0d0d, #1a1a1a);
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }

    /* Heading style */
    .big-heading {
        font-size: 50px;
        font-weight: bold;
        color: #ff6f3c;
        margin-bottom: 20px;
    }

    /* Textbox styling */
    div.stTextInput>div>input {
        background-color: #1a1a1a;
        color: white;
        border: 1px solid #ff6f3c;
        border-radius: 6px;
        padding: 0.5em;
        font-size: 18px;
    }

    /* Hide Streamlit footer */
    footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# --- Heading ---
st.markdown('<div class="big-heading">TruthLensAI</div>', unsafe_allow_html=True)
st.markdown("Enter a news headline below to analyze:")

# --- Textbox for headline ---
headline = st.text_input("Your Headline Here")

# Optional: Display entered headline
if headline:
    st.markdown(f"**You entered:** {headline}")

