# Data Audit Report

## Dataset Overview

The Bank Marketing dataset contains 45,211 observations and 17 variables.

The target variable is y, which indicates whether a customer subscribed to a term deposit.

## Structure

The dataset includes both numeric and categorical variables.

Examples of numeric variables include:

- age
- balance
- day
- duration
- campaign
- pdays
- previous

Categorical variables include:

- job
- marital
- education
- default
- housing
- loan
- contact
- month
- poutcome
- y

## Completeness

No standard missing values were detected in the dataset.

All 17 variables contained values for all 45,211 observations.

However, several categorical fields contain the value unknown. These values are not technically missing but represent unavailable or unrecorded information and therefore still require consideration.

Examples include:

- job
- education
- contact
- poutcome

## Duplicate Records

No duplicate rows were detected.

This means no duplicate removal is required at this stage.

## Target Distribution

The target variable is imbalanced.

- 
o: 39,922 records (88.3%)
- yes: 5,289 records (11.7%)

Because of this imbalance, overall accuracy could be misleading.

For example, a model that predicts 
o for every customer would already achieve approximately 88.3% accuracy while providing no useful prediction of successful subscriptions.

Therefore, additional metrics such as precision, recall, F1-score and ROC-AUC will be used.

## Consistency and Special Values

Several fields contain values that require careful interpretation.

### unknown

The value unknown appears in multiple categorical variables.

These values will initially be retained as valid categories instead of being removed or automatically replaced.

Their influence will be reviewed during analysis.

### pdays

The variable pdays contains negative values such as -1.

This appears to represent customers who were not previously contacted rather than a literal negative number of days.

The variable will therefore require special treatment during preprocessing.

## Possible Data Leakage

The variable duration represents the duration of the customer contact.

This information would only be known after the call has occurred.

If the project objective is to predict customer response before contacting them, using duration would give the model information that would not be available at prediction time.

For this reason, duration is considered a leakage risk.

The realistic predictive model will exclude this variable.

## Privacy and Ethics

The dataset is public and does not contain direct identifiers such as customer names or account numbers.

However, variables such as age, job, marital status and education still describe personal characteristics.

These variables will therefore be discussed carefully when interpreting model results.

The model will be treated as a decision-support tool rather than an automated system for targeting customers without human oversight.

## Initial Data Quality Conclusion

The dataset is structurally clean because it contains no standard missing values or duplicate rows.

The main analytical concerns are:

1. class imbalance;
2. possible leakage from duration;
3. interpretation of pdays = -1;
4. high frequency of unknown categories in some variables;
5. and responsible use of personal characteristics.

These findings affect both the modelling strategy and the project risk register.
