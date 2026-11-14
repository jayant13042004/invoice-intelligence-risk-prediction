# Invoice Intelligence & Risk Prediction

Data processing and machine learning pipeline on **1M+ procurement records**: freight-cost prediction and invoice-risk classification, with a Streamlit app to explore results.

## What it does
- Data cleaning, preprocessing, exploratory analysis, and feature engineering
- **Freight-cost regression:** compared multiple regression models
- **Invoice-risk classifier:** Random Forest tuned with GridSearchCV and 5-fold cross-validation, using features built from invoice amount discrepancies and goods-receiving delays
- Interactive Streamlit application for exploring the results

## Results
| Task | Metric | Value |
|---|---|---|
| Freight-cost regression | R² / MAE / RMSE | 96.99% / 24.11 / 124.72 |
| Invoice-risk classification | Accuracy / Precision / Recall / F1 | 89% / 0.95 / 0.71 / 0.82 |

**Label definition:** risk labels are rule-based (invoice amount difference above $5, or receiving delay above 10 days). The classifier learns this rule from the engineered features, so these scores describe how well it reproduces the rule, not confirmed real-world risk or fraud.

## Tech stack
Python, Pandas, NumPy, Scikit-learn, Streamlit

## Run locally
```bash
git clone https://github.com/jayant13042004/invoice-intelligence-risk-prediction.git
cd invoice-intelligence-risk-prediction
pip install -r requirements.txt
streamlit run [app_file].py
```
(Screenshot: `![app](images/app.png)`)

## Dataset
[Name and link of the procurement dataset you used]

## Author
Jayant Jagtap · [LinkedIn](https://www.linkedin.com/in/jayantjagtap/)
