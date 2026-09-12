# Project Charter

## Project Title

Predicting Customer Response to Bank Marketing Campaigns

## Problem Statement

Banks often contact large numbers of customers during marketing campaigns, but only a small proportion may respond positively. This can waste staff time, increase campaign costs and frustrate customers who are unlikely to be interested.

This project will use historical bank marketing data to investigate whether customer and campaign information can be used to predict whether a client is likely to subscribe to a term deposit.

## Analytical Question

Can historical customer and campaign information be used to predict whether a client is likely to subscribe to a term deposit?

## Main Stakeholders

- Marketing Manager
- Marketing Staff
- Data Analyst / Data Scientist
- IT / Data Support
- Bank Management
- Customers

## Project Objectives

1. Build and evaluate a reproducible classification model that predicts whether a customer will subscribe to a term deposit.
2. Compare a simple baseline approach with at least one improved model.

## Scope

The project will include:

- obtaining and documenting the dataset;
- creating a data dictionary;
- checking data quality;
- checking for possible data leakage and privacy concerns;
- exploratory data analysis;
- at least three useful visualisations;
- data preparation;
- baseline modelling;
- improved modelling;
- model evaluation;
- project risk and change tracking;
- and a final report.

## Exclusions

1. Contacting real bank customers.
2. Using private or confidential banking data.
3. Automatically making marketing decisions without human review.
4. Deploying the model into a live banking system.
5. Purchasing commercial software or paid datasets.

## Deliverables

- Project charter
- Work breakdown structure and schedule
- Progress-tracking evidence
- Stakeholder matrix
- Risk register
- Change log
- Status report
- Dataset or source link
- Data dictionary
- Reproducible Python notebook
- Charts and model outputs
- Final report
- Five-minute demonstration outline if required

## Assumptions

- The public dataset is suitable for academic use.
- It contains enough observations and useful variables.
- Google Colab and Python are sufficient for analysis.
- The project can be completed using free tools.

## Constraints

- No paid tools or services.
- Public historical data rather than live banking data.
- Limited assessment time.
- The model must remain manageable and reproducible.

## Acceptance Criteria

1. The notebook runs from start to finish using documented instructions and a recorded random seed.
2. The final model is evaluated on unseen data and performs better than a simple baseline on at least one agreed metric.
3. At least three useful visualisations are produced and explained.
4. Data preparation, modelling decisions and limitations are documented.
5. The portfolio includes genuine planning, progress tracking, risk management and change control.
6. Final conclusions are based on actual model outputs and not invented results.

## Tools

- GitHub
- Google Colab
- Python
- pandas
- NumPy
- matplotlib
- scikit-learn
