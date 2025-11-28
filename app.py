import streamlit as st
from datetime import datetime
import random

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
/* Title row (LOGO + HEADING side by side) */
.title-row {
    display: flex;
    align-items: center;
    gap: 12px;
}
/* Heading styles */
h1 {
    font-family: 'Arial', sans-serif;
    font-size: 3rem;
    background: linear-gradient(to right, #ff8c94, #a18cd1, #fbc2eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
/* Subtitle */
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
div[role="radiogroup"] label, div[role="radiogroup"] span, div[role="radiogroup"] div {
    color: #ffffff !important;
}
/* Ensure other labels stay white */
label {
    color: #ffffff !important;
}
/* Tips box styling */
.tips-box {
    background-color: rgba(70,70,90,0.9);
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
    border-left: 5px solid #a18cd1;
}
/* FAQ box styling */
.faq-box {
    background-color: rgba(70,70,90,0.9);
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
    border-left: 5px solid #ff8c94;
}
/* White translucent HOW TO USE box */
.white-box {
    background: rgba(255, 255, 255, 0.15);
    padding: 1.2rem;
    border-radius: 12px;
    margin-top: 1rem;
    backdrop-filter: blur(5px);
}
.feedback-box {
    background-color: rgba(100,100,120,0.85);
    padding: 1rem;
    border-radius: 10px;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ---------- SESSION STATE ----------
if "history" not in st.session_state:
    st.session_state.history = []
if "current_page" not in st.session_state:
    st.session_state.current_page = "Home"

# ---------- SIDEBAR NAVIGATION ----------
st.sidebar.title("Navigation")
st.session_state.current_page = st.sidebar.selectbox(
    "Go to:",
    ["Home", "Analyze Headline", "History & Insights"],
    index=["Home", "Analyze Headline", "History & Insights"].index(st.session_state.current_page)
)

# ---------- ROTATING TIPS ----------
tips_list = [
    "💡 Did you know? Over 50% of news shared on social media is never actually read.",
    "📌 Tip: Check multiple sources before trusting a news headline.",
    "⚠️ Beware: Sensational headlines are more likely to be fake.",
    "📰 Fact: Images and videos can be manipulated to spread misinformation.",
    "🔍 Always verify the publication date and source of the news."
]
current_tip = random.choice(tips_list)

# ---------- FAQ QUESTIONS ----------
faq = {
    "What is TruthLensAI?": "TruthLensAI analyzes headlines to detect potential fake news.",
    "How do I use the app?": "Enter a headline, select gender & platform, click Analyze News.",
    "Any tips for spotting fake news?": "Check multiple sources, verify images, and watch for sensational language.",
    "Can I see previous headlines?": "Yes! Navigate to the 'History & Insights' page to see past analyses.",
    "Why is gender and platform asked?": "These inputs help show patterns and insights in how news spreads across demographics."
}

# ---------- HOME PAGE ----------
if st.session_state.current_page == "Home":
    st.markdown("""
    <div class="title-row">
        <img src="logo.png.png" width="70">
        <h1>TruthLensAI</h1>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<h3>Detect fake news and explore insights!</h3>", unsafe_allow_html=True)

    if st.button("Go to Analyze Headline"):
        st.session_state.current_page = "Analyze Headline"

    st.markdown("---")
    st.markdown("""
    Welcome to **TruthLensAI**! This app allows you to:
    - Enter a news headline
    - Analyze it for possible fake news indicators
    - See platform and gender-specific patterns
    - Keep track of analyzed headlines
    """)
    st.markdown(f'<div class="tips-box">{current_tip}</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="white-box">
        <h3>How to Use</h3>
        <p>
        1. Navigate to <b>Analyze Headline</b> page or click the button above.<br>
        2. Enter the news headline.<br>
        3. Select your gender & platform.<br>
        4. Click <b>Analyze News</b>.<br>
        5. View past analyses in <b>History & Insights</b>.<br>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Frequently Asked Questions")
    question_list = ["Select a question"] + list(faq.keys())
    selected_question = st.selectbox("Click a question to get the answer:", question_list)
    if selected_question != "Select a question":
        st.markdown(f'<div class="faq-box">{faq[selected_question]}</div>', unsafe_allow_html=True)

# ---------- ANALYZE HEADLINE PAGE ----------
elif st.session_state.current_page == "Analyze Headline":
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        
        st.markdown("""
        <div class="title-row">
            <img src="logo.png.png" width="70">
            <h1>TruthLensAI</h1>
        </div>
        """, unsafe_allow_html=True)
        st.markdown("<h3>Detect fake news and explore insights</h3>", unsafe_allow_html=True)
        st.write("---")

        headline = st.text_input("Enter the news headline here:")

        # --- COMPLEXITY SCORE ---
        if headline:
            word_count = len(headline.split())
            if word_count <= 5:
                complexity = 25
                complexity_label = "Low"
            elif word_count <= 10:
                complexity = 50
                complexity_label = "Medium"
            else:
                complexity = 90
                complexity_label = "High"
            st.markdown(f"**Complexity Score:** {complexity_label} ({word_count} words)")
            st.progress(complexity / 100)

        gender = st.radio("Select your gender:", ["Male", "Female", "Other"])
        platform = st.selectbox("Select the platform where you found the news:", ["Instagram", "YouTube", "Facebook", "Twitter"])
        st.write("---")
        st.markdown(f"**Date:** {datetime.today().strftime('%d %B %Y')}")

        if st.button("Analyze News"):
            st.success(f"Analyzing headline: **{headline}**\n\nPlatform: **{platform}** | Gender: **{gender}** 🔍")
            st.session_state.history.append({
                "headline": headline,
                "gender": gender,
                "platform": platform,
                "date": datetime.today().strftime("%d %B %Y")
            })

            # --- FEEDBACK SECTION ---
            st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
            st.markdown("### Feedback")
            feedback = st.text_area("Your thoughts about this analysis:")
            if st.button("Submit Feedback"):
                st.success("Thanks for your feedback! ❤️")
            st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# ---------- HISTORY PAGE ----------
elif st.session_state.current_page == "History & Insights":
    st.header("Analysis History")
    if st.session_state.history:
        for i, record in enumerate(st.session_state.history, start=1):
            st.markdown(f"**{i}. {record['headline']}**")
            st.markdown(f"Platform: {record['platform']} | Gender: {record['gender']} | Date: {record['date']}")
            st.markdown("---")
    else:
        st.info("No headlines analyzed yet!")
