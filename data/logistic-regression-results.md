# Logistic Regression Results

## Model

The first improved model was Logistic Regression with balanced class weights.

Class weighting was used because exploratory analysis showed that only 11.7% of customers subscribed to a term deposit.

The duration variable remained excluded to prevent data leakage.

## Results

- Accuracy: 0.7548
- Precision: 0.2662
- Recall: 0.6238
- F1-score: 0.3732
- ROC-AUC: 0.7722

## Confusion Matrix

- True negatives: 6,166
- False positives: 1,819
- False negatives: 398
- True positives: 660

## Comparison with Baseline

The baseline model achieved 88.3% accuracy but failed to identify any actual subscribers.

Logistic Regression had lower overall accuracy of 75.48%, but it successfully identified 660 of the 1,058 subscribers in the test set.

Its recall for the subscriber class increased from 0% to 62.38%.

ROC-AUC also improved from 0.5000 to 0.7722.

This shows why accuracy alone is not appropriate for this dataset.

## Interpretation

The Logistic Regression model provides substantially more useful predictions than the baseline.

Its main strength is recall. It identifies approximately 62% of actual subscribers.

Its main weakness is precision. Only about 27% of customers predicted as likely subscribers actually subscribed.

This means the model would generate a relatively large number of false-positive marketing leads.

For this reason, Logistic Regression will be treated as a useful improved model, but another model will be tested before selecting the final approach.

## Current Decision

The model meets the acceptance criterion of outperforming the baseline on meaningful classification metrics.

However, a second improved model will be evaluated to determine whether a better balance between recall and precision can be achieved.
