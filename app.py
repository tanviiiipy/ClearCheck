import streamlit as st

st.set_page_config(
    page_title="ClearCheck",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.hero {
    text-align: center;
    padding: 3rem 1rem 2rem;
}

.hero-badge {
    display: inline-block;
    background: #e8f5e9;
    color: #2e7d32;
    font-size: 12px;
    font-weight: 500;
    letter-spacing: 2px;
    text-transform: uppercase;
    padding: 6px 16px;
    border-radius: 20px;
    margin-bottom: 1.5rem;
}

.hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: 4rem;
    font-weight: 800;
    letter-spacing: -2px;
    line-height: 1;
    margin: 0 0 0.5rem;
    color: #e8f5e9;
}

.hero h1 span {
    color: #1b5e20;
}

.hero p {
    font-size: 1.1rem;
    color: #555;
    font-weight: 300;
    max-width: 480px;
    margin: 0 auto 2rem;
    line-height: 1.7;
}

.nav-card {
    background: #fff;
    border: 1px solid #e8e8e8;
    border-radius: 16px;
    padding: 1.5rem;
    margin-bottom: 1rem;
    transition: all 0.2s;
    cursor: pointer;
}

.nav-card:hover {
    border-color: #1b5e20;
    box-shadow: 0 4px 24px rgba(27,94,32,0.08);
}

.nav-card-icon {
    font-size: 2rem;
    margin-bottom: 0.5rem;
}

.nav-card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    color: #e8f5e9;
    margin-bottom: 0.25rem;
}

.nav-card-desc {
    font-size: 0.85rem;
    color: #888;
    font-weight: 300;
}

.stat-row {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin: 2rem 0;
    flex-wrap: wrap;
}

.stat-item {
    text-align: center;
}

.stat-num {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #1b5e20;
}

.stat-label {
    font-size: 0.75rem;
    color: #888;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.divider {
    border: none;
    border-top: 1px solid #f0f0f0;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-badge">🛡️ ML-Powered Security</div>
    <h1>Clear<span>Check</span></h1>
    <p>A machine learning system that detects fraudulent credit card transactions in real time — trained on 284,807 real transactions.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="stat-row">
    <div class="stat-item">
        <div class="stat-num">284K</div>
        <div class="stat-label">Transactions trained on</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">99%</div>
        <div class="stat-label">Accuracy</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">0.98</div>
        <div class="stat-label">AUC-ROC Score</div>
    </div>
    <div class="stat-item">
        <div class="stat-num">492</div>
        <div class="stat-label">Fraud cases learned</div>
    </div>
</div>
<hr class="divider"/>
""", unsafe_allow_html=True)

st.markdown("### Explore ClearCheck")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="nav-card">
        <div class="nav-card-icon">🔍</div>
        <div class="nav-card-title">Analyse a Transaction</div>
        <div class="nav-card-desc">Load a real transaction and watch the model decide if it's fraud</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/1_Analyse.py", label="Go to Analyser →")

with col2:
    st.markdown("""
    <div class="nav-card">
        <div class="nav-card-icon">🎯</div>
        <div class="nav-card-title">Spot the Fraud</div>
        <div class="nav-card-desc">Can you out-guess the model? Test your instincts against AI</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/2_Spot_the_Fraud.py", label="Play the game →")

col3, col4 = st.columns(2)

with col3:
    st.markdown("""
    <div class="nav-card">
        <div class="nav-card-icon">⚙️</div>
        <div class="nav-card-title">How it Works</div>
        <div class="nav-card-desc">The full pipeline explained simply — from raw data to prediction</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/3_How_it_Works.py", label="Learn more →")

with col4:
    st.markdown("""
    <div class="nav-card">
        <div class="nav-card-icon">📊</div>
        <div class="nav-card-title">Model Stats</div>
        <div class="nav-card-desc">Precision, recall, confusion matrix — all the technical details</div>
    </div>
    """, unsafe_allow_html=True)
    st.page_link("pages/4_Model_Stats.py", label="See stats →")

st.markdown("""
<hr class="divider"/>
<p style="text-align:center; color:#bbb; font-size:0.8rem; font-weight:300;">
Built by Tanvi P Yannawar &nbsp;·&nbsp; Random Forest Model &nbsp;·&nbsp; Kaggle Credit Card Fraud Dataset
</p>
""", unsafe_allow_html=True)