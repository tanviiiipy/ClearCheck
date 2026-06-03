import streamlit as st
import joblib
import numpy as np
import pandas as pd

st.set_page_config(page_title="Analyse — ClearCheck", page_icon="🔍", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }
.tag { display: inline-block; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 500; }
.tag-fraud { background: #fdecea; color: #c62828; }
.tag-legit { background: #e8f5e9; color: #2e7d32; }
.metric-card { background: #f9f9f9; border-radius: 12px; padding: 1rem 1.25rem; margin-bottom: 0.5rem; }
.metric-label { font-size: 11px; text-transform: uppercase; letter-spacing: 1px; color: #999; margin-bottom: 4px; }
.metric-value { font-family: 'Syne', sans-serif; font-size: 1.4rem; font-weight: 700; color: #0a0a0a; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model = joblib.load('models/fraud_model.pkl')
    scaler = joblib.load('models/scaler2.pkl')
    df = pd.read_csv('data/creditcard.csv')
    return model, scaler, df

model, scaler, df = load_model()

st.markdown("# 🔍 Transaction Analyser")
st.markdown("Load a real transaction from the dataset. The model has never been told the answer — watch it decide.")

st.divider()

col1, col2 = st.columns(2)
with col1:
    if st.button("🎲 Random transaction", use_container_width=True):
        st.session_state.analyse_sample = df.sample(1).iloc[0]
        st.session_state.analyse_revealed = False
with col2:
    if st.button("🚨 Random fraud", use_container_width=True):
        st.session_state.analyse_sample = df[df['Class'] == 1].sample(1).iloc[0]
        st.session_state.analyse_revealed = False

if 'analyse_sample' not in st.session_state:
    st.session_state.analyse_sample = df.sample(1).iloc[0]
    st.session_state.analyse_revealed = False

sample = st.session_state.analyse_sample

st.divider()
st.markdown("### Transaction details")
st.caption("The bank anonymized the raw data (merchant, location, card number etc.) into 28 encoded values for privacy. The model reads those hidden patterns.")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Amount</div>
        <div class="metric-value">${sample['Amount']:.2f}</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Time (seconds elapsed)</div>
        <div class="metric-value">{int(sample['Time'])}s</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-label">Transaction ID</div>
        <div class="metric-value">#{int(sample.name)}</div>
    </div>""", unsafe_allow_html=True)

st.divider()

if st.button("🔍 Analyse this transaction", use_container_width=True, type="primary"):
    scaled = scaler.transform([[sample['Amount'], sample['Time']]])[0]
    v_features = [sample[f'V{i}'] for i in range(1, 29)]
    features = np.array(v_features + [scaled[0], scaled[1]]).reshape(1, -1)

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]
    actual = int(sample['Class'])

    st.divider()
    st.markdown("### Model verdict")

    if prediction == 1:
        st.error("🚨 FRAUDULENT transaction detected")
        st.progress(float(probability), text=f"Fraud confidence: {probability:.1%}")
    else:
        st.success("✅ Transaction appears legitimate")
        st.progress(float(1 - probability), text=f"Legitimate confidence: {(1-probability):.1%}")

    st.divider()
    st.markdown("### Actual answer")

    if actual == 1:
        st.markdown('<span class="tag tag-fraud">🚨 This was FRAUD</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="tag tag-legit">✅ This was LEGITIMATE</span>', unsafe_allow_html=True)

    st.write("")
    if prediction == actual:
        st.balloons()
        st.success("✅ Model got it right!")
    else:
        st.warning("⚠️ Model got this one wrong — no model is 100% perfect. This is why banks have human reviewers too.")

    st.divider()
    st.markdown("### What does the confidence score mean?")
    st.markdown(f"""
The model doesn't just say yes/no — it gives a **probability score** between 0% and 100%.

- This transaction scored **{probability:.1%}** fraud probability
- Anything above ~50% gets flagged as fraud
- A score close to 0% or 100% means the model is very confident
- A score near 50% means the model is uncertain

In a real bank, transactions with high fraud probability get **automatically blocked**, and borderline ones go to a **human reviewer**.
    """)