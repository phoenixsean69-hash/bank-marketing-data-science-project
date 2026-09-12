# Model Comparison and Final Selection

## Models Evaluated

Three models were evaluated:

1. Dummy majority-class baseline
2. Balanced Logistic Regression
3. Balanced Random Forest

The same 80/20 stratified train/test split and random seed of 42 were used to support a fair comparison.

The variable duration was excluded from all realistic models because it would only become available after the marketing call and therefore presents a data-leakage risk.

## Results

| Model | Accuracy | Precision | Recall | F1-score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Dummy Baseline | 0.8830 | 0.0000 | 0.0000 | 0.0000 | 0.5000 |
| Logistic Regression | 0.7548 | 0.2662 | 0.6238 | 0.3732 | 0.7722 |
| Random Forest | 0.8790 | 0.4797 | 0.4026 | 0.4378 | 0.7936 |

## Baseline

The baseline model achieved 88.3% accuracy.

However, it predicted every customer as a non-subscriber and failed to identify any of the 1,058 subscribers in the test set.

Its high accuracy was therefore caused by class imbalance rather than useful predictive ability.

## Logistic Regression

Logistic Regression detected 660 of the 1,058 actual subscribers.

Its recall of 62.38% was the highest of the models tested.

However, precision was only 26.62%, meaning that many customers predicted as likely subscribers did not actually subscribe.

The model produced 1,819 false positives.

## Random Forest

Random Forest achieved:

- 87.90% accuracy;
- 47.97% precision;
- 40.26% recall;
- 43.78% F1-score;
- and 0.7936 ROC-AUC.

It identified 426 actual subscribers while producing 462 false positives.

Although its recall was lower than Logistic Regression, its precision was substantially higher and it achieved the strongest F1-score and ROC-AUC.

## Final Model Selection

Random Forest was selected as the preferred model for this project.

The reason for this decision is not that it has the highest accuracy.

Instead, it provides the best overall balance between identifying subscribers and limiting unnecessary marketing contacts.

Its F1-score of 0.4378 was higher than Logistic Regression's 0.3732, and its ROC-AUC of 0.7936 was also the highest among the models tested.

Logistic Regression remains a reasonable alternative if the business decides that identifying as many potential subscribers as possible is more important than reducing false-positive contacts.

## Acceptance Criteria

The final model satisfies the project's modelling acceptance criterion because it performs substantially better than the baseline on meaningful minority-class metrics.

The baseline achieved:

- F1-score: 0.0000
- ROC-AUC: 0.5000

Random Forest achieved:

- F1-score: 0.4378
- ROC-AUC: 0.7936

## Limitation

The Random Forest still misses 632 of the 1,058 subscribers in the test set.

Therefore, the model should not be described as perfectly accurate or suitable for fully automated marketing decisions.

It should be treated as a decision-support tool that could help prioritise potential customers while retaining human judgement.
