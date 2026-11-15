# Invoice Intelligence & Risk Prediction

A machine learning project for procurement analytics with two prediction workflows: freight-cost estimation and invoice manual-approval flagging. A Streamlit application provides an interface for both workflows.

## Project Modules

### 1. Freight Cost Prediction

- Accepts invoice quantity and invoice amount as input.
- Loads a trained regression model.
- Estimates freight costs for new inputs.

### 2. Invoice Manual-Approval Flag

- Uses invoice quantity, invoice amount, freight cost, total item quantity and total item amount.
- Loads a trained classification model and scaler.
- Predicts whether an invoice should be sent for manual approval.

## Reported Model Results

The following metrics are retained from the existing project documentation.

| Model | Metric | Result |
|---|---|---:|
| Freight-cost regression | R² | 96.99% |
| Freight-cost regression | MAE | 24.11 |
| Freight-cost regression | RMSE | 124.72 |
| Invoice classification | Accuracy | 89% |
| Invoice classification | Precision | 0.95 |
| Invoice classification | Recall | 0.71 |
| Invoice classification | F1-score | 0.82 |

These results have not been independently reproduced during this README update. Confirm the evaluation split and metric units before using them externally.

## Important Note About Invoice Classification

The existing implementation uses rule-based proxy labels, including an invoice amount discrepancy threshold of $5 and a goods-receiving delay threshold of 10 days.

The classifier therefore learns to reproduce those rules. Its reported performance should not be interpreted as proof of real-world fraud detection.

## Technology Stack

Python, Pandas, NumPy, Scikit-learn, Joblib, Plotly and Streamlit.

## Installation

```bash
git clone https://github.com/jayant13042004/invoice-intelligence-risk-prediction.git

cd invoice-intelligence-risk-prediction

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

## Required Model Artifacts

The inference modules expect these files inside the `models/` directory:

```text
models/
├── predict_freight_model.pkl
├── predict_flag_invoice.pkl
└── scaler.pkl
```

The application cannot generate predictions if the required model artifacts are missing.

Only load trusted pickle/joblib files. Deserializing untrusted model files can execute malicious code.

## Repository Structure

```text
invoice-intelligence-risk-prediction/
├── app.py
├── inference/
│   ├── predict_freight.py
│   └── predict_invoice.py
├── models/
├── requirements.txt
└── README.md
```

Additional notebooks, training scripts and data files may be present in the repository.

## Dataset

Add the verified dataset name, source URL and licence information before redistributing the dataset or claiming specific provenance.

## Author

**Jayant Jagtap**

[GitHub](https://github.com/jayant13042004)
