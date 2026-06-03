import streamlit as st
import joblib
import numpy as np
import pandas as pd
import random

st.set_page_config(page_title="Spot the Fraud — ClearCheck", page_icon="🎯", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }
.score-card { background: #f9f9f9; border-radius: 16px; padding: 1.25rem 1.5rem; text-align: center; }
.score-big { font-family: 'Syne', sans-serif; font-size: 2.5rem; font-weight: 800; color: #1b5e20; }
.score-label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: #999; }
.txn-card { background: #fff; border: 1px solid #e8e8e8; border-radius: 16px; padding: 1.5rem; margin: 1rem 0; }
.hint-text { font-size: 0.85rem; color: #888; font-style: italic; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model = joblib.load('models/fraud_model.pkl')
    scaler = joblib.load('models/scaler2.pkl')
    df = pd.read_csv('data/creditcard.csv')
    return model, scaler, df

model, scaler, df = load_model()

if 'score' not in st.session_state:
    st.session_state.score = 0
if 'total' not in st.session_state:
    st.session_state.total = 0
if 'game_sample' not in st.session_state:
    st.session_state.game_sample = None
if 'game_guessed' not in st.session_state:
    st.session_state.game_guessed = False
if 'model_prediction' not in st.session_state:
    st.session_state.model_prediction = None
if 'model_probability' not in st.session_state:
    st.session_state.model_probability = None

def load_new_transaction():
    if random.random() < 0.5:
        sample = df[df['Class'] == 1].sample(1).iloc[0]
    else:
        sample = df[df['Class'] == 0].sample(1).iloc[0]
    st.session_state.game_sample = sample
    st.session_state.game_guessed = False
    st.session_state.model_prediction = None
    st.session_state.model_probability = None

if st.session_state.game_sample is None:
    load_new_transaction()

st.markdown("# 🎯 Spot the Fraud")
st.markdown("Look at the transaction details and guess whether it's fraud — then see what the model thinks. Who's smarter?")

st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="score-card">
        <div class="score-big">{st.session_state.score}/{st.session_state.total}</div>
        <div class="score-label">Your score</div>
    </div>""", unsafe_allow_html=True)
with col2:
    accuracy = (st.session_state.score / st.session_state.total * 100) if st.session_state.total > 0 else 0
    st.markdown(f"""
    <div class="score-card">
        <div class="score-big">{accuracy:.0f}%</div>
        <div class="score-label">Your accuracy</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""
    <div class="score-card">
        <div class="score-big">82%</div>
        <div class="score-label">Model accuracy</div>
    </div>""", unsafe_allow_html=True)

st.divider()

sample = st.session_state.game_sample

st.markdown("### Transaction to evaluate")
st.caption("Look at the details below. What's your gut feeling?")

col1, col2 = st.columns(2)
with col1:
    st.metric("💳 Amount", f"${sample['Amount']:.2f}")
with col2:
    st.metric("⏱️ Time elapsed", f"{int(sample['Time'])}s")

hours = int(sample['Time']) // 3600
st.markdown(f'<p class="hint-text">Transaction occurred ~{hours} hours into the monitoring period</p>', unsafe_allow_html=True)

high_v = [(f'V{i}', round(sample[f'V{i}'], 2)) for i in range(1, 29) if abs(sample[f'V{i}']) > 2]
if high_v:
    st.markdown(f'<p class="hint-text">⚠️ Unusual activity detected in {len(high_v)} encoded features</p>', unsafe_allow_html=True)
else:
    st.markdown('<p class="hint-text">✓ Encoded features appear within normal range</p>', unsafe_allow_html=True)

st.divider()

if not st.session_state.game_guessed:
    st.markdown("### Your guess")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Looks legitimate", use_container_width=True):
            user_guess = 0
            scaled = scaler.transform([[sample['Amount'], sample['Time']]])[0]
            v_features = [sample[f'V{i}'] for i in range(1, 29)]
            features = np.array(v_features + [scaled[0], scaled[1]]).reshape(1, -1)
            st.session_state.model_prediction = model.predict(features)[0]
            st.session_state.model_probability = model.predict_proba(features)[0][1]
            st.session_state.game_guessed = True
            st.session_state.total += 1
            if user_guess == int(sample['Class']):
                st.session_state.score += 1
            st.session_state.user_guess = user_guess
            st.rerun()
    with col2:
        if st.button("🚨 This is fraud!", use_container_width=True):
            user_guess = 1
            scaled = scaler.transform([[sample['Amount'], sample['Time']]])[0]
            v_features = [sample[f'V{i}'] for i in range(1, 29)]
            features = np.array(v_features + [scaled[0], scaled[1]]).reshape(1, -1)
            st.session_state.model_prediction = model.predict(features)[0]
            st.session_state.model_probability = model.predict_proba(features)[0][1]
            st.session_state.game_guessed = True
            st.session_state.total += 1
            if user_guess == int(sample['Class']):
                st.session_state.score += 1
            st.session_state.user_guess = user_guess
            st.rerun()

else:
    actual = int(sample['Class'])
    user_guess = st.session_state.user_guess
    model_pred = st.session_state.model_prediction
    probability = st.session_state.model_probability

    st.markdown("### Results")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Your guess**")
        if user_guess == 1:
            st.error("🚨 Fraud")
        else:
            st.success("✅ Legit")
    with col2:
        st.markdown("**Model's guess**")
        if model_pred == 1:
            st.error(f"🚨 Fraud ({probability:.0%})")
        else:
            st.success(f"✅ Legit ({1-probability:.0%})")
    with col3:
        st.markdown("**Actual answer**")
        if actual == 1:
            st.error("🚨 Was FRAUD")
        else:
            st.success("✅ Was LEGIT")

    st.write("")
    user_correct = user_guess == actual
    model_correct = model_pred == actual

    if user_correct and model_correct:
        st.success("🎉 You both got it right!")
    elif user_correct and not model_correct:
        st.success("🏆 You beat the model on this one!")
    elif not user_correct and model_correct:
        st.warning("🤖 Model got it, you didn't — better luck next time!")
    else:
        st.error("😅 You both got it wrong!")

    st.write("")
    if st.button("➡️ Next transaction", use_container_width=True, type="primary"):
        load_new_transaction()
        st.rerun()

st.divider()
if st.button("🔄 Reset score"):
    st.session_state.score = 0
    st.session_state.total = 0
    load_new_transaction()
    st.rerun()