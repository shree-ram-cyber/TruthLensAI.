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
/* Background gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1e1e2f, #2c2c3c);
    color: #ffffff;
}

/* Card container */
.card {
    background: rgba(40, 40, 55, 0.85);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    max-width: 700px;
    margin: auto;
    color: #ffffff;
}

/* Heading styles */
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

/* Inputs */
.stTextInput > div, .stSelectbox > div {
    background-color: rgba(60,60,75,0.9);
    border-radius: 10px;
    padding: 0.5rem;
    color: #ffffff;
}
input::placeholder {
    color: #e0e0e0;
}

/* Make ONLY gender radio option text white */
div[role="radiogroup"] > label, 
div[role="radiogroup"] > div, 
div[role="radiogroup"] span {
    color: #ffffff !important;
}

/* Ensure other labels stay white */
label {
    color: #ffffff !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION STATE FOR HISTORY ----------
if "history" not in st.session_state:
    st.session_state.history = []

# ---------- PAGE SELECTOR ----------
page = st.sidebar.selectbox("Navigate to:", ["Home", "Analyze Headline", "History & Insights"])

# ---------- HOME PAGE ----------
if page == "Home":
    st.image("assets/logo.png", width=150)
    st.markdown("<h1>TruthLensAI</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Detect fake news and explore insights!</h3>", unsafe_allow_html=True)
    st.markdown("""
    Welcome to **TruthLensAI**!  
    This app allows you to:
    - Enter a news headline
    - Analyze it for possible fake news indicators
    - See platform and gender-specific patterns
    - Keep track of analyzed headlines
    """)
    if st.button("Get Started"):
        page = "Analyze Headline"
        st.experimental_rerun()

# ---------- ANALYZE HEADLINE PAGE ----------
elif page == "Analyze Headline":
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        # Logo
        st.image("assets/logo.png", width=150)
        
        # Title & Subtitle
        st.markdown("<h1>TruthLensAI</h1>", unsafe_allow_html=True)
        st.markdown("<h3>Detect fake news and explore insights</h3>", unsafe_allow_html=True)
        
        st.write("---")
        
        # Headline input
        headline = st.text_input("Enter the news headline here:")
        
        # Gender input
        gender = st.radio("Select your gender:", ["Male", "Female", "Other"])
        
        # Platform input
        platform = st.selectbox("Select the platform where you found the news:", 
                                ["Instagram", "YouTube", "Facebook", "Twitter"])
        
        st.write("---")
        
        # Date
        st.markdown(f"**Date:** {datetime.today().strftime('%d %B %Y')}")
        
        # Analyze button
        if st.button("Analyze News"):
            st.success(f"Analyzing headline: **{headline}**\n\nFrom platform: **{platform}** for **{gender}** user... 🔍")
            # Store in history
            st.session_state.history.append({
                "headline": headline,
                "gender": gender,
                "platform": platform,
                "date": datetime.today().strftime("%d %B %Y")
            })
        
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- HISTORY & INSIGHTS PAGE ----------
elif page == "History & Insights":
    st.header("Analysis History")
    if st.session_state.history:
        for i, record in enumerate(st.session_state.history, start=1):
            st.markdown(f"**{i}. {record['headline']}**")
            st

