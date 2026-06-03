import streamlit as st

st.set_page_config(page_title="ClearCheck", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }
div[data-testid="stMarkdownContainer"] h1 { display: none; }
.hero-title { font-family: 'Syne', sans-serif; font-size: 3rem; font-weight: 800; letter-spacing: -2px; color: #e8f5e9; margin-bottom: 0.5rem; }
.hero-title span { color: #1b5e20; }
.about-hero { text-align: center; padding: 2rem 0; }
.about-hero p { color: #888; font-weight: 300; }
.pill { display: inline-block; background: #f0f0f0; color: #444; font-size: 0.8rem; padding: 5px 14px; border-radius: 20px; margin: 4px; font-weight: 500; }
.pill-green { background: #e8f5e9; color: #2e7d32; }
.tech-card { background: #f9f9f9; border-radius: 12px; padding: 1.25rem; margin-bottom: 0.75rem; }
.tech-card-title { font-weight: 500; font-size: 0.95rem; color: #0a0a0a; margin-bottom: 0.25rem; }
.tech-card-desc { font-size: 0.85rem; color: #888; font-weight: 300; }
.dev-card { background: #fff; border: 1px solid #e8e8e8; border-radius: 16px; padding: 2rem; text-align: center; margin: 1.5rem 0; }
.dev-avatar { width: 72px; height: 72px; background: #e8f5e9; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-family: 'Syne', sans-serif; font-size: 1.5rem; font-weight: 800; color: #1b5e20; margin: 0 auto 1rem; }
.dev-name { font-family: 'Syne', sans-serif; font-size: 1.2rem; font-weight: 700; }
.dev-title { font-size: 0.85rem; color: #888; font-weight: 300; }
#about { display: none; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="about-hero">
    <div class="hero-title">Clear<span>Check</span></div>
    <p>A machine learning fraud detection system built from scratch</p>
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("### What is ClearCheck?")
st.markdown("""
ClearCheck is a machine learning web application that detects fraudulent credit card transactions. It was built as a project to learn the full ML pipeline — from raw data to a deployed, interactive app.

The model was trained on a real-world dataset of 284,807 credit card transactions and achieves an AUC-ROC score of 0.97, meaning it's excellent at distinguishing fraud from legitimate activity.
""")

st.divider()
st.markdown("### Tech stack")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="tech-card">
        <div class="tech-card-title">🐍 Python</div>
        <div class="tech-card-desc">Core language for data processing, model training, and the app</div>
    </div>
    <div class="tech-card">
        <div class="tech-card-title">🌲 scikit-learn</div>
        <div class="tech-card-desc">Random Forest model, preprocessing, evaluation metrics</div>
    </div>
    <div class="tech-card">
        <div class="tech-card-title">⚖️ imbalanced-learn</div>
        <div class="tech-card-desc">SMOTE for handling the 0.17% fraud class imbalance</div>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="tech-card">
        <div class="tech-card-title">🎈 Streamlit</div>
        <div class="tech-card-desc">Multi-page web app framework for the interactive UI</div>
    </div>
    <div class="tech-card">
        <div class="tech-card-title">🐼 Pandas & NumPy</div>
        <div class="tech-card-desc">Data manipulation and numerical computing</div>
    </div>
    <div class="tech-card">
        <div class="tech-card-title">📊 Matplotlib & Seaborn</div>
        <div class="tech-card-desc">Confusion matrix, ROC curve, and data visualizations</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()
st.markdown("### Dataset")
st.markdown("""
**Credit Card Fraud Detection** — Kaggle

284,807 transactions made by European cardholders in September 2013 over 2 days. Features V1–V28 are PCA-transformed for privacy. Only the `Amount` and `Time` columns retain their original form.

- 492 fraud cases (0.17%)
- Zero missing values
- Source: Machine Learning Group at Université Libre de Bruxelles
""")

st.divider()
st.markdown("### Developer")

st.markdown("""
<div class="dev-card">
    <div class="dev-avatar">Tanvi P Yannawar</div>
    <div class="dev-name">TPY</div>
    <div class="dev-title">B.Tech CSE · First Year</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p style="text-align:center; font-size:0.8rem; color:#bbb;">
Built with Python, scikit-learn & Streamlit &nbsp;·&nbsp; ClearCheck v1.0
</p>
""", unsafe_allow_html=True)