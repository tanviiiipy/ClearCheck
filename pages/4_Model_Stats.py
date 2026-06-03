import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, roc_curve, auc
import matplotlib.patches as mpatches

st.set_page_config(page_title="Model Stats — ClearCheck", page_icon="📊", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;700;800&family=Inter:wght@300;400;500&display=swap');
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
h1, h2, h3 { font-family: 'Syne', sans-serif !important; }
.stat-card { background: #f9f9f9; border-radius: 12px; padding: 1.25rem; text-align: center; }
.stat-big { font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; }
.stat-label { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 1px; color: #999; margin-top: 4px; }
.green { color: #1b5e20; }
.blue { color: #1565c0; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_everything():
    model = joblib.load('models/fraud_model.pkl')
    scaler = joblib.load('models/scaler2.pkl')
    df = pd.read_csv('data/creditcard.csv')

    df['Amount_Scaled'] = scaler.transform(df[['Amount', 'Time']])[:, 0]
    df['Time_Scaled'] = scaler.transform(df[['Amount', 'Time']])[:, 1]
    df_model = df.drop(columns=['Amount', 'Time'])

    X = df_model.drop(columns=['Class'])
    y = df_model['Class']

    from sklearn.model_selection import train_test_split
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    cm = confusion_matrix(y_test, y_pred)
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)

    return cm, fpr, tpr, roc_auc, y_test, y_pred

st.markdown("# 📊 Model Stats")
st.markdown("All the technical performance metrics for ClearCheck's Random Forest model.")

with st.spinner("Computing stats..."):
    cm, fpr, tpr, roc_auc, y_test, y_pred = load_everything()

st.divider()
st.markdown("### Performance summary")

tn, fp, fn, tp = cm.ravel()
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * precision * recall / (precision + recall)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<div class="stat-card"><div class="stat-big green">{precision:.0%}</div><div class="stat-label">Precision</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="stat-card"><div class="stat-big green">{recall:.0%}</div><div class="stat-label">Recall</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="stat-card"><div class="stat-big green">{f1:.0%}</div><div class="stat-label">F1 Score</div></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="stat-card"><div class="stat-big blue">{roc_auc:.2f}</div><div class="stat-label">AUC-ROC</div></div>', unsafe_allow_html=True)

st.divider()
st.markdown("### Confusion matrix")
st.caption("Shows how many transactions the model classified correctly vs incorrectly.")

fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens',
            xticklabels=['Predicted Legit', 'Predicted Fraud'],
            yticklabels=['Actual Legit', 'Actual Fraud'],
            ax=ax, linewidths=0.5)
ax.set_title('Confusion Matrix', fontsize=13, fontweight='bold', pad=12)
plt.tight_layout()
st.pyplot(fig)

col1, col2 = st.columns(2)
with col1:
    st.metric("✅ Correctly caught frauds", tp)
    st.metric("✅ Correctly cleared legit", tn)
with col2:
    st.metric("❌ Missed frauds (false negatives)", fn)
    st.metric("❌ False alarms (false positives)", fp)

st.divider()
st.markdown("### ROC Curve")
st.caption("Shows the model's ability to distinguish fraud from legitimate transactions at all thresholds. Closer to the top-left corner = better.")

fig2, ax2 = plt.subplots(figsize=(6, 4))
ax2.plot(fpr, tpr, color='#1b5e20', linewidth=2, label=f'AUC = {roc_auc:.3f}')
ax2.plot([0, 1], [0, 1], color='#ccc', linestyle='--', linewidth=1, label='Random guessing')
ax2.fill_between(fpr, tpr, alpha=0.08, color='#1b5e20')
ax2.set_xlabel('False Positive Rate', fontsize=11)
ax2.set_ylabel('True Positive Rate', fontsize=11)
ax2.set_title('ROC Curve', fontsize=13, fontweight='bold')
ax2.legend(loc='lower right')
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
plt.tight_layout()
st.pyplot(fig2)

st.divider()
st.markdown("### Dataset breakdown")
col1, col2, col3 = st.columns(3)
col1.metric("Total transactions", "284,807")
col2.metric("Legitimate", "284,315 (99.83%)")
col3.metric("Fraud", "492 (0.17%)")

st.markdown("""
<br>
<p style="font-size:0.8rem; color:#bbb; text-align:center;">
Random Forest · 100 estimators · Trained with SMOTE balancing · Kaggle Credit Card Fraud Dataset
</p>
""", unsafe_allow_html=True)