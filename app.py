import streamlit as st
from datetime import datetime

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="TruthLensAI",
    page_icon="🕵️‍♂️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #1e1e2f, #2c2c3c);
    color: white;
}

.card {
    background: rgba(40, 40, 55, 0.85);
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    max-width: 750px;
    margin: auto;
}

h1 {
    font-family: 'Arial';
    font-size: 3rem;
    background: linear-gradient(to right, #ff8c94, #a18cd1, #fbc2eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

h2 {
    color: white;
    font-family: 'Arial';
}

h3 {
    color: white;
    font-family: 'Arial';
}

label {
    color: white !important;
}

.stTextInput > div, .stRadio > div, .stSelectbox > div {
    background-color: rgba(60, 60, 75, 0.9);
    border-radius: 10px;
    padding: 0.4rem 0.7rem;
}

div[role="radiogroup"] label {
    color: white !important;
}

.transbox {
    background: rgba(255,255,255,0.12);
    padding: 1.2rem;
    border-radius: 12px;
    margin-top: 1rem;
}

.stButton>button {
    background-color: #a18cd1;
    color: white;
    padding: 0.6rem 1.6rem;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    background-color: #ff8c94;
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
#                    NAVIGATION
# -------------------------------------------------
page = st.sidebar.selectbox("Navigate", ["Home", "Fake News Detector"])


# -------------------------------------------------
#                    HOME PAGE
# -------------------------------------------------
if page == "Home":
    st.markdown('<div class="card">', unsafe_allow_html=True)

    # LOGO
    st.image("assets/logo.png", width=140)

    st.markdown("<h1>TruthLensAI</h1>", unsafe_allow_html=True)
    st.write("Your companion for spotting misinformation 🔍")

    # ---------------- HOW TO USE SECTION ----------------
    st.markdown("<h2>How to Use</h2>", unsafe_allow_html=True)

    st.markdown("""
    <div class="transbox">
        <p>1️⃣ Go to the <b>Fake News Detector</b> screen using the menu on the left.</p>
        <p>2️⃣ Enter the headline you want to verify.</p>
        <p>3️⃣ Select gender & platform.</p>
        <p>4️⃣ Hit <b>Analyze News</b> — instant insights!</p>
    </div>
    """, unsafe_allow_html=True)

    # ---------------- FAQ (Click-based) ----------------
    st.markdown("<h2>Quick Help</h2>", unsafe_allow_html=True)

    faq_question = st.selectbox(
        "Select a question to get help:",
        [
            "",
            "What does this app do?",
            "How accurate is the detection?",
            "Why do we ask for gender and platform?",
            "Does it store my data?"
        ]
    )

    if faq_question == "What does this app do?":
        st.info("It analyzes news headlines and gives insights to help you judge credibility.")
    elif faq_question == "How accurate is the detection?":
        st.info("This version uses rule-based logic. Enough for school projects, not real-world deployment.")
    elif faq_question == "Why do we ask for gender and platform?":
        st.info("Different users experience news differently, and platforms have different misinformation patterns.")
    elif faq_question == "Does it store my data?":
        st.info("Nope! Everything remains only during your session.")

    st.markdown("</div>", unsafe_allow_html=True)



# -------------------------------------------------
#               FAKE NEWS DETECTOR PAGE
# -------------------------------------------------
elif page == "Fake News Detector":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    # Title
    st.markdown("<h1>Fake News Detector</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Enter your details below</h3>", unsafe_allow_html=True)

    st.write("---")

    # HEADLINE
    headline = st.text_input("Enter the news headline:")

    # GENDER
    gender = st.radio("Select your gender:", ["Male", "Female", "Other"])

    # PLATFORM
    platform = st.selectbox(
        "Where did you find this news?",
        ["Instagram", "YouTube", "Facebook", "Twitter"]
    )

    st.write("---")

    # DATE
    st.markdown(f"**Date:** {datetime.today().strftime('%d %B %Y')}")

    # BUTTON
    if st.button("Analyze News"):
        st.success(f"Analyzing headline: **{headline}** from **{platform}** for a **{gender}** user 🔍")

    st.markdown("</div>", unsafe_allow_html=True)
