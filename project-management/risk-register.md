# Risk Register

## Scoring Method

Probability and impact are rated from 1 to 5.

Risk Score = Probability x Impact

| Risk | Category | Probability | Impact | Score | Owner | Mitigation | Contingency | Trigger |
|---|---|---:|---:|---:|---|---|---|---|
| Target class imbalance causes misleading model performance | Model/Data | 5 | 4 | 20 | Data Analyst | Use stratified splitting and evaluate precision, recall, F1-score and ROC-AUC | Apply class weighting or alternative modelling approach | Model predicts mainly the majority class |
| duration creates data leakage | Model | 4 | 5 | 20 | Data Analyst | Exclude duration from the realistic predictive model | Compare with and without it and document the difference | Unrealistically high model performance |
| unknown categories reduce data quality or usefulness | Data | 4 | 3 | 12 | Data Analyst | Retain initially and assess impact rather than treating automatically as missing | Group or exclude if justified | unknown dominates important variables |
| pdays = -1 is misinterpreted as a real number | Data | 4 | 3 | 12 | Data Analyst | Treat it as a special indicator meaning no previous contact where confirmed | Engineer a separate previous-contact indicator | Model treats -1 as a normal numeric value |
| Model performs poorly on unseen data | Model | 3 | 4 | 12 | Data Analyst | Compare baseline and improved models | Adjust preprocessing or model choice | Evaluation fails acceptance criteria |
| Analysis takes longer than planned | Schedule | 3 | 3 | 9 | Project Manager | Track progress and prioritise required outputs | Reduce optional analysis | Tasks slip by more than one day |
| Customer-related variables create fairness or privacy concerns | Ethics/Privacy | 2 | 5 | 10 | Project Manager | Use public anonymised data and avoid unnecessary identifiers | Exclude questionable variables | Sensitive information is identified |
| Project decisions are not documented | Project Control | 2 | 3 | 6 | Project Manager | Maintain change log and status report continuously | Reconstruct from Git history if needed | Analysis changes without recorded reason |

## Current Highest Risks

The highest current risks are class imbalance and possible leakage from duration.

These risks will be actively addressed before model training.
