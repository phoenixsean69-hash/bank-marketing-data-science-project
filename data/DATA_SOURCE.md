# Dataset Source and Provenance

## Dataset

Bank Marketing Dataset

## Source

UCI Machine Learning Repository

Dataset page:

https://archive.ics.uci.edu/dataset/222/bank+marketing

## File Used

`bank-full.csv`

## Dataset Size

- 45,211 observations
- 17 variables

## Purpose

The dataset contains information from direct marketing campaigns carried out by a Portuguese banking institution.

The target variable `y` indicates whether a customer subscribed to a term deposit.

## Usage in This Project

The dataset is used only for academic analysis.

No customer names, account numbers or direct personal identifiers are included in the working dataset.

The variable `duration` was excluded from predictive modelling because it would not be available before the marketing call was completed and could introduce data leakage.

## Reproducibility

The working dataset is stored in:

`data/bank-full.csv`

The data dictionary is stored in:

`data/data-dictionary.md`