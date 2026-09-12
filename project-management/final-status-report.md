# Final Project Status Report

## Project

Predicting Customer Response to Bank Marketing Campaigns

## Status Date

12 September 2026

## Overall Status

GREEN

The main analytical work has been completed successfully.

The dataset was obtained, audited and explored. A baseline model and two improved models were evaluated using the same train/test split and random seed.

Random Forest was selected as the preferred model because it achieved the strongest overall balance of F1-score and ROC-AUC.

## Work Completed

- Project charter completed
- Stakeholder matrix completed
- Work breakdown structure and schedule completed
- Initial and updated risk registers completed
- Change log maintained
- Dataset downloaded and documented
- Data dictionary completed
- Data audit completed
- Exploratory data analysis completed
- Four EDA charts generated
- Data leakage risk identified and controlled
- Baseline model completed
- Logistic Regression model completed
- Random Forest model completed
- Model comparison completed
- Preferred model selected
- Model comparison chart generated

## Key Findings

The dataset contains 45,211 observations.

Only 11.7% of customers subscribed to a term deposit, creating a strong class imbalance.

The Dummy baseline achieved 88.3% accuracy but failed to identify any subscribers.

Balanced Logistic Regression improved subscriber recall to 62.38%.

Random Forest achieved:

- Accuracy: 87.90%
- Precision: 47.97%
- Recall: 40.26%
- F1-score: 43.78%
- ROC-AUC: 0.7936

Random Forest was selected as the preferred model because it produced the highest F1-score and ROC-AUC.

## Current Issues

The selected model still misses a significant number of subscribers.

The model also produces some false-positive marketing leads.

These limitations mean that the model should be used as a decision-support tool rather than an automatic campaign-selection system.

## Decisions Made

- Accuracy was rejected as the main performance metric.
- The duration variable was excluded to avoid data leakage.
- Class imbalance was addressed through balanced model training and suitable evaluation metrics.
- Random Forest was selected as the preferred final model.

## Schedule Status

The main analytical work is complete.

The remaining activities are:

- final report writing;
- portfolio review;
- presentation preparation;
- and final repository clean-up.

## Corrective Actions

No major corrective action is currently required.

Before final submission, all files will be checked for completeness and reproducibility.
