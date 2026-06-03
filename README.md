# ClearCheck 🛡️

ClearCheck is a machine learning web app that detects fraudulent credit card transactions. You load a real transaction, the model analyses it, and tells you whether it's fraud — along with a confidence score. There's also a game where you guess before the model does.

It was trained on 284,807 real transactions from a Kaggle dataset and uses a Random Forest model that scores 0.97 on AUC-ROC.

---

## What's inside

The app has 6 pages. The home page links to everything else. The Analyse page lets you load random transactions and see the model's verdict in real time. Spot the Fraud is a game where you guess first and then compare with the model. How it Works explains the full ML pipeline in plain English. Model Stats shows the confusion matrix, ROC curve, and all the performance numbers. The About page covers the tech stack and dataset credits.

---

## Running it locally

Clone the repo and install dependencies:

```bash
git clone https://github.com/tanviiiipy/ClearCheck.git
cd ClearCheck
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn xgboost streamlit joblib
```

Download `creditcard.csv` from [Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) and put it in the `data/` folder. Then open `notebook.ipynb` and run all cells — this trains the model and saves the files to `models/`. After that, launch the app:

```bash
python -m streamlit run app.py
```

The model files aren't included in the repo because they're too large for GitHub, so you do need to run the notebook first.

---

## Tech

Python, scikit-learn, Streamlit, Pandas, Matplotlib, Seaborn, imbalanced-learn, XGBoost. The class imbalance problem (only 0.17% of transactions are fraud) was handled using SMOTE.

---

## Dataset

[Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) — Machine Learning Group, Université Libre de Bruxelles.

---

Built by Tanvi P Yannawar — B.Tech CSE, First Year