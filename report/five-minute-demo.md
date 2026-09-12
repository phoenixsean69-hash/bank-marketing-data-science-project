# Five-Minute Demonstration Script

## 1. Project Introduction

My project is called **Predicting Customer Response to Bank Marketing Campaigns**.

The main question was whether historical customer and campaign information could be used to predict whether a customer would subscribe to a term deposit.

The project used a public Bank Marketing dataset containing 45,211 observations.

## 2. Project Planning

Before modelling, I created a project charter, work breakdown structure, stakeholder matrix, risk register, change log and project schedule.

This was important because the assignment focused not only on building a model, but also on showing how the project was planned and controlled.

## 3. Data Audit

The dataset contained 17 variables.

The initial audit found:

- no standard missing values;
- no duplicate rows;
- several categorical variables containing unknown;
- and a strong class imbalance.

Only 11.7% of customers subscribed to the term deposit.

This meant that accuracy alone would be misleading.

I also identified duration as a potential leakage variable because call duration would only be known after the call had already taken place.

For this reason, I excluded it from the predictive models.

## 4. Exploratory Analysis

I produced several visualisations.

The analysis showed that subscription rates varied by:

- contact type;
- month;
- and previous campaign outcome.

For example, customers with a previous campaign outcome of success had a much higher observed subscription rate than customers with an unknown or failed previous outcome.

These findings influenced which variables were retained for modelling.

## 5. Baseline Model

The baseline model was a majority-class Dummy Classifier.

It achieved 88.3% accuracy.

However, it predicted every customer as a non-subscriber and identified none of the actual subscribers.

Its recall and F1-score for subscribers were both zero.

This showed why accuracy alone was not useful for this problem.

## 6. Improved Models

I then evaluated balanced Logistic Regression and Random Forest models.

Logistic Regression achieved:

- recall of 62.38%;
- F1-score of 37.32%;
- ROC-AUC of 0.7722.

Random Forest achieved:

- precision of 47.97%;
- recall of 40.26%;
- F1-score of 43.78%;
- ROC-AUC of 0.7936.

## 7. Final Decision

Random Forest was selected as the preferred model because it gave the strongest overall balance between precision, recall and discrimination.

Logistic Regression still performed better on recall, so it could be useful if the organisation's priority were to identify as many possible subscribers as possible.

## 8. Limitations

The model still has limitations.

It was trained on historical public data and may not represent current banking customers.

It also still misses some subscribers and produces some false positives.

Therefore, I would use it as a decision-support tool rather than an automatic customer-targeting system.

## 9. Handover and Monitoring

If the model were deployed, I would monitor:

- precision;
- recall;
- F1-score;
- ROC-AUC;
- data quality;
- and changes in customer behaviour.

The project also includes a handover plan, reproducible notebook, package versions and documented project-control evidence.

## 10. Closing Statement

The main lesson from the project is that a useful data science solution is more than a model.

It also needs good planning, data-quality checks, risk control, documentation, reproducibility and continuous monitoring.
