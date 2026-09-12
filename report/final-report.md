# Final Report: Predicting Customer Response to Bank Marketing Campaigns

## 1. Introduction

This project investigated whether historical customer and campaign information could be used to predict whether a bank customer would subscribe to a term deposit.

The purpose was not to create the most complex possible machine-learning system. Instead, the aim was to demonstrate a manageable and reproducible data science project that could be planned, executed, controlled, evaluated and handed over professionally.

The project used the UCI Bank Marketing dataset, containing 45,211 observations and 17 variables. The target variable, `y`, records whether a customer subscribed to a term deposit.

The main analytical question was:

**Can historical customer and campaign information be used to predict whether a client is likely to subscribe to a term deposit?**

The project was completed using free tools, including Python, pandas, matplotlib, scikit-learn, Google Colab-compatible code and GitHub-compatible project files.

## 2. Project Planning and Control

The work started with a project charter defining the problem, stakeholders, scope, exclusions, deliverables, assumptions, constraints and acceptance criteria.

A work breakdown structure and schedule were also prepared to organise the work into stages covering project setup, data acquisition, data auditing, exploratory analysis, preprocessing, modelling, evaluation and reporting.

The main stakeholders identified were the Marketing Manager, marketing staff, bank management, the data analyst, IT or data support staff and customers.

A risk register was maintained during the project. Early risks included possible poor data quality, class imbalance, data leakage, model underperformance and privacy concerns.

The project also maintained a change log. This was important because several decisions were made after inspecting the real data rather than being decided in advance.

For example, accuracy was removed as the main evaluation measure after the baseline model showed that high accuracy could be achieved without identifying any subscribers.

## 3. Data Audit and Preparation

The dataset contained 45,211 rows and 17 columns.

The initial data-quality audit found:

- no standard missing values;
- no duplicate rows;
- a mixture of numeric and categorical variables;
- several categorical variables containing the value `unknown`;
- and a strongly imbalanced target variable.

The target distribution was:

- 39,922 customers did not subscribe, representing 88.3%;
- 5,289 customers subscribed, representing 11.7%.

This imbalance became one of the most important modelling issues in the project.

A model predicting `no` for every customer could already achieve approximately 88.3% accuracy. For that reason, accuracy alone could not be used to judge whether a model was useful.

The audit also identified `duration` as a possible data-leakage variable. This field represents the duration of the marketing call. Because the value would only be known after the call took place, it would not be available when deciding who to contact in advance.

For that reason, `duration` was excluded from all realistic predictive models.

The variable `pdays` also required careful interpretation because negative values such as `-1` represent a special condition rather than a literal negative number of days.

## 4. Exploratory Data Analysis

Exploratory analysis was used to identify patterns and guide modelling decisions.

Four main visualisations were produced.

The first showed the strong class imbalance between subscribers and non-subscribers.

The second compared subscription rates by contact type. The observed rates were:

- cellular: 14.92%;
- telephone: 13.42%;
- unknown: 4.07%.

This suggested that contact type contained potentially useful predictive information.

The third chart examined subscription rate by month. Large differences were observed across the year. Examples included:

- March: 51.99%;
- December: 46.73%;
- September: 46.46%;
- October: 43.77%;
- May: 6.72%.

These differences suggested that the timing of campaigns may be associated with customer response. However, the results were treated as associations rather than proof that month directly causes subscription behaviour.

The fourth chart examined the outcome of previous campaigns. Customers whose previous campaign outcome was recorded as `success` had a subscription rate of 64.73%, compared with 12.61% for `failure` and 9.16% for `unknown`.

As a result of the exploratory analysis, `contact`, `month` and `poutcome` were retained as candidate predictors.

## 5. Modelling Approach

The data was divided using an 80/20 stratified train/test split with a recorded random seed of 42.

This produced:

- 36,168 training observations;
- 9,043 test observations.

Stratification ensured that the 88.3% to 11.7% class distribution was preserved in both datasets.

Three models were evaluated:

1. Dummy majority-class baseline;
2. balanced Logistic Regression;
3. balanced Random Forest.

The same test set was used for all models so that the comparison remained consistent.

The main evaluation metrics were accuracy, precision, recall, F1-score, ROC-AUC and the confusion matrix.

## 6. Baseline Results

The Dummy baseline predicted the majority class for every customer.

Its results were:

- Accuracy: 0.8830
- Precision: 0.0000
- Recall: 0.0000
- F1-score: 0.0000
- ROC-AUC: 0.5000

The confusion matrix showed:

- 7,985 true negatives;
- 0 false positives;
- 1,058 false negatives;
- 0 true positives.

Although the accuracy appeared high, the model failed to identify a single actual subscriber.

This result confirmed that accuracy was misleading for this project.

## 7. Improved Models

Balanced Logistic Regression was evaluated next.

Its results were:

- Accuracy: 0.7548
- Precision: 0.2662
- Recall: 0.6238
- F1-score: 0.3732
- ROC-AUC: 0.7722

The model identified 660 of the 1,058 actual subscribers in the test set.

Its main strength was recall. However, it also produced 1,819 false positives, showing that many customers predicted as likely subscribers did not actually subscribe.

The second improved model was a balanced Random Forest.

Its results were:

- Accuracy: 0.8790
- Precision: 0.4797
- Recall: 0.4026
- F1-score: 0.4378
- ROC-AUC: 0.7936

Its confusion matrix contained:

- 7,523 true negatives;
- 462 false positives;
- 632 false negatives;
- 426 true positives.

Random Forest had lower recall than Logistic Regression but substantially higher precision. It also achieved the strongest F1-score and ROC-AUC of the models tested.

## 8. Final Model Selection

Random Forest was selected as the preferred model.

The decision was not based on accuracy alone.

The baseline had slightly higher accuracy than Random Forest, but the baseline had no ability to identify subscribers.

Random Forest provided the strongest overall balance between identifying subscribers and reducing unnecessary marketing contacts.

Its F1-score improved from 0.0000 for the baseline to 0.4378, while ROC-AUC improved from 0.5000 to 0.7936.

Logistic Regression remains a useful alternative in a situation where the bank places greater importance on identifying as many potential subscribers as possible, because its recall was higher at 62.38%.

The final model choice would therefore still depend on business priorities.

## 9. Limitations

Several limitations remain.

First, the project uses historical public data and may not reflect current customer behaviour.

Second, results from this dataset may not generalise to another bank or another country.

Third, the target class remains imbalanced.

Fourth, Random Forest still missed 632 actual subscribers in the test data.

Fifth, variables such as age, job, marital status and education describe personal characteristics and should be used carefully in any real deployment.

Finally, the observed relationships are predictive associations and should not be treated as evidence of causation.

## 10. Recommendations and Handover

The model should be treated as a decision-support tool rather than an automatic marketing decision system.

Before any real deployment, the organisation should:

- validate the model using current internal data;
- confirm appropriate privacy and governance controls;
- monitor precision, recall, F1-score and ROC-AUC;
- monitor changes in customer and campaign data;
- review false positives and false negatives;
- retrain or review the model if performance declines;
- and retain human oversight over campaign decisions.

The technical handover should include the dataset source, data dictionary, preprocessing steps, reproducible notebook, random seed, package versions, model results, risk register, change log and monitoring plan.

## 11. Conclusion

The project demonstrated that useful prediction is possible using the Bank Marketing dataset even after removing the leakage-prone `duration` variable.

The majority-class baseline showed that high accuracy does not necessarily mean that a classification model is useful.

Both improved models produced more meaningful predictions.

Balanced Logistic Regression offered stronger recall, while Random Forest provided a better overall balance between precision and recall and achieved the highest F1-score and ROC-AUC.

Random Forest was therefore selected as the preferred model for this project.

The final outcome is not a production-ready banking system. It is a reproducible analytical prototype that demonstrates how a small data science project can be planned, controlled, evaluated and prepared for professional handover.