import streamlit as st

st.set_page_config(page_title="How it Works — ClearCheck", page_icon="⚙️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }
.step-card { display: flex; gap: 1.25rem; align-items: flex-start; background: #fff; border: 1px solid #e8e8e8; border-radius: 16px; padding: 1.5rem; margin-bottom: 1rem; }
.step-num { font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; color: #e0e0e0; min-width: 40px; }
.step-title { font-family: 'Syne', sans-serif; font-size: 1rem; font-weight: 700; color: #0a0a0a; margin-bottom: 0.3rem; }
.step-desc { font-size: 0.9rem; color: #666; font-weight: 300; line-height: 1.6; }
.highlight { background: #e8f5e9; color: #1b5e20; padding: 2px 8px; border-radius: 6px; font-weight: 500; font-size: 0.9rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("# ⚙️ How ClearCheck Works")
st.markdown("The full pipeline — from raw transaction data to a fraud prediction — explained simply.")

st.divider()

st.markdown("""
<div class="step-card">
    <div class="step-num">01</div>
    <div>
        <div class="step-title">Raw data comes in</div>
        <div class="step-desc">Every credit card transaction has details: the amount, the time, the merchant, the location, and dozens of other signals. This dataset contains <span class="highlight">284,807 real transactions</span> from European cardholders over 2 days.</div>
    </div>
</div>

<div class="step-card">
    <div class="step-num">02</div>
    <div>
        <div class="step-title">Privacy anonymization</div>
        <div class="step-desc">The bank can't share raw personal data publicly. So they ran a mathematical technique called <span class="highlight">PCA (Principal Component Analysis)</span> that transforms the original features into 28 anonymous values — V1 through V28. The patterns are preserved, but the raw details are hidden.</div>
    </div>
</div>

<div class="step-card">
    <div class="step-num">03</div>
    <div>
        <div class="step-title">Fixing the imbalance problem</div>
        <div class="step-desc">Only <span class="highlight">0.17% of transactions are fraud</span> — just 492 out of 284,807. If we train the model as-is, it learns to ignore fraud entirely since it barely sees any. We fix this with SMOTE, which generates synthetic fraud examples so the model trains on a balanced dataset.</div>
    </div>
</div>

<div class="step-card">
    <div class="step-num">04</div>
    <div>
        <div class="step-title">Training the model</div>
        <div class="step-desc">ClearCheck uses a <span class="highlight">Random Forest</span> — a collection of 100 decision trees that each vote on whether a transaction is fraud. The majority vote wins. Each tree learns slightly different patterns, which makes the overall model more robust than any single tree.</div>
    </div>
</div>

<div class="step-card">
    <div class="step-num">05</div>
    <div>
        <div class="step-title">Making a prediction</div>
        <div class="step-desc">When a new transaction comes in, all 100 trees vote. The model returns a <span class="highlight">probability score</span> — not just yes/no, but how confident it is. A score above ~50% means fraud. A score close to 0% or 100% means the model is very certain.</div>
    </div>
</div>

<div class="step-card">
    <div class="step-num">06</div>
    <div>
        <div class="step-title">Why not just use accuracy?</div>
        <div class="step-desc">A model that predicts "not fraud" for everything would be <span class="highlight">99.83% accurate</span> — but completely useless. ClearCheck uses Precision, Recall, F1 Score, and AUC-ROC instead, which actually measure how well it catches fraud without overwhelming banks with false alarms.</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()
st.markdown("### Key terms explained")

with st.expander("What is Precision?"):
    st.markdown("Out of every transaction the model flagged as fraud, **how many were actually fraud?** High precision = fewer false alarms. ClearCheck's precision: **82%**")

with st.expander("What is Recall?"):
    st.markdown("Out of all real fraud transactions, **how many did the model catch?** High recall = fewer frauds slipping through. ClearCheck's recall: **82%**")

with st.expander("What is AUC-ROC?"):
    st.markdown("A single number (0 to 1) measuring how well the model separates fraud from non-fraud across all possible thresholds. **1.0 = perfect, 0.5 = random guessing.** ClearCheck scores **0.97** — excellent.")

with st.expander("What is SMOTE?"):
    st.markdown("Synthetic Minority Oversampling Technique. It creates fake-but-realistic fraud examples by interpolating between existing fraud cases, so the model sees enough examples to actually learn what fraud looks like.")

with st.expander("What is a Random Forest?"):
    st.markdown("An ensemble of many decision trees. Each tree is trained on a slightly different random subset of the data, and they vote together on predictions. More trees = more stable, less prone to overfitting.")