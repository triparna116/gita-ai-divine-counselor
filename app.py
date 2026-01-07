import streamlit as st
import random
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Gita AI | The Divine Counselor",
    page_icon="🪈",
    layout="wide"
)

# ---------------- SESSION STATE ----------------
if "example" not in st.session_state:
    st.session_state.example = ""

# ---------------- CSS ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(0, 8, 20, 0.93), rgba(0, 8, 20, 0.98)),
                url("https://www.transparenttextures.com/patterns/dark-matter.png");
    color: white;
}

.divine-card {
    background: rgba(255, 255, 255, 0.06);
    border: 2px solid #FFD700;
    border-radius: 16px;
    padding: 22px;
    margin-bottom: 20px;
    box-shadow: 0 0 18px rgba(255, 215, 0, 0.25);
}

h1, h2, h3 {
    color: #FFD700 !important;
}

p {
    font-size: 1.02rem;
}

.stTextInput input {
    height: 42px !important;
    padding: 0.45rem !important;
    background-color: rgba(255,255,255,0.12) !important;
    border: 1px solid #FFD700 !important;
    color: white !important;
}

.stButton>button {
    background-color: #FFD700 !important;
    color: #001021 !important;
    font-weight: bold;
    border-radius: 20px;
    padding: 0.35rem 0.8rem;
    margin-bottom: 6px;
}

.stButton>button:hover {
    box-shadow: 0 0 15px #FFD700;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<h1 style='text-align:center;'>🪈 Gita AI: The Divine Counselor</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#FFD700;'>AI-Powered Guidance Inspired by the Bhagavad Gita</p>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center; max-width:850px; margin:auto;'>"
    "Ask your life questions and receive calm, meaningful guidance inspired by the timeless wisdom of the Bhagavad Gita."
    "</p>",
    unsafe_allow_html=True
)

st.write("---")

# ---------------- LAYOUT ----------------
left, right = st.columns([1, 1.6])

# ---------------- LEFT ----------------
with left:
    st.markdown('<div class="divine-card">', unsafe_allow_html=True)
    st.subheader("📖 Verse of the Moment")

    shlokas = [
        ("कर्मण्येवाधिकारस्ते मा फलेषु कदाचन", "Focus on actions, not outcomes."),
        ("योगः कर्मसु कौशलम्", "Excellence in action is yoga."),
        ("उद्धरेदात्मनाऽत्मानं", "Elevate yourself by your own effort.")
    ]

    v, m = random.choice(shlokas)
    st.markdown(f"*{v}*")
    st.caption(m)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="divine-card">', unsafe_allow_html=True)
    st.subheader("✨ Example Questions")

    if st.button("💼 Career anxiety"):
        st.session_state.example = "How should I deal with career anxiety?"

    if st.button("📉 Fear of failure"):
        st.session_state.example = "What does the Gita say about failure?"

    if st.button("🎓 Exam stress"):
        st.session_state.example = "How can I stay calm during exams?"

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- RIGHT ----------------
with right:
    st.markdown('<div class="divine-card">', unsafe_allow_html=True)
    st.subheader("🙏 Ask Lord Krishna")

    user_input = st.text_input(
        "Share your concern",
        value=st.session_state.example,
        placeholder="I feel confused about my future and career..."
    )

    if st.button("Seek Divine Guidance"):
        if user_input.strip():
            with st.spinner("Reflecting on the Gita..."):
                time.sleep(2)

            response = (
                f"My dear seeker, regarding *'{user_input}'*, remember this: "
                "You have the right to act with sincerity, but not to be attached to results. "
                "When effort is pure and intention steady, peace naturally follows."
            )

            st.markdown(
                f"""
                <div class="divine-card">
                    <h3>🪷 Krishna Says</h3>
                    <p>{response}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.warning("Please write something to receive guidance.")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.write("---")
st.caption("Built with ❤️ using Python & Streamlit | Inspired by the Bhagavad Gita")