# Bank Marketing Data Science Project

Practical Data Science Project and Management Portfolio.

## Project Question

Can historical customer and campaign information be used to predict whether a client is likely to subscribe to a term deposit?
## Dataset

This project uses the UCI Bank Marketing dataset.

- 45,211 observations
- 17 variables
- Target variable: `y`
- Positive class: customer subscribed to a term deposit
- Negative class: customer did not subscribe

The variable `duration` was excluded from predictive modelling because it would only be known after the marketing call and could introduce data leakage.

## Models

The following models were evaluated:

- Dummy baseline classifier
- Balanced Logistic Regression
- Balanced Random Forest

## Final Model

Random Forest was selected as the preferred model.

Results:

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Dummy Baseline | 0.8830 | 0.0000 | 0.0000 | 0.0000 | 0.5000 |
| Logistic Regression | 0.7548 | 0.2662 | 0.6238 | 0.3732 | 0.7722 |
| Random Forest | 0.8790 | 0.4797 | 0.4026 | 0.4378 | 0.7936 |

## Main Files

- `notebook/bank_marketing_final.ipynb`
- `report/final-report.md`
- `report/reflection.md`
- `project-management/project-charter.md`
- `project-management/wbs-and-schedule.md`
- `project-management/risk-register.md`
- `project-management/change-log.md`
- `project-management/task-board.md`
- `REPRODUCIBILITY.md`

## Reproducibility

Random seed: `42`

Install dependencies using:

```powershell
pip install -r requirements.txt
