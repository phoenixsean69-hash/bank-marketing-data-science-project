# Baseline Model Results

## Model Used

The baseline model used a DummyClassifier with the most_frequent strategy.

This means the model always predicts the majority class.

## Data Split

The data was split using an 80/20 stratified train/test split with:

Random seed: 42

Training observations: 36,168

Testing observations: 9,043

The class distribution was preserved:

- No subscription: 88.3%
- Subscription: 11.7%

## Features

The variable duration was excluded because it would only be known after a marketing call had taken place and could therefore introduce data leakage.

The modelling dataset contained 15 predictor variables.

## Baseline Results

- Accuracy: 0.8830
- Precision: 0.0000
- Recall: 0.0000
- F1-score: 0.0000
- ROC-AUC: 0.5000

## Confusion Matrix

- True negatives: 7,985
- False positives: 0
- False negatives: 1,058
- True positives: 0

## Interpretation

Although the model achieved 88.3% accuracy, it failed to identify a single customer who actually subscribed.

The high accuracy is caused by the class imbalance in the dataset.

Because 88.3% of customers did not subscribe, a model can achieve high accuracy simply by predicting 
o for every customer.

For this reason, accuracy will not be treated as the main measure of model usefulness.

The improved model will be evaluated using:

- precision;
- recall;
- F1-score;
- ROC-AUC;
- confusion matrix;
- and overall accuracy.

The improved model should identify at least some subscribers while maintaining acceptable overall performance.
