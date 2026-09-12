# Reproducibility Notes

## Main Notebook


otebook/bank_marketing_final.ipynb

## Dataset

data/bank-full.csv

## Random Seed

42

## Execution

The notebook was executed from start to finish successfully.

## Environment

Required Python packages are listed in:

equirements.txt

## Main Outputs

The notebook reproduces:

- data audit results;
- target distribution;
- exploratory data analysis;
- generated charts;
- baseline model results;
- Logistic Regression results;
- Random Forest results;
- and final model comparison.

## Important Modelling Decision

The variable duration is excluded from the predictive models because it would not be known before the marketing call ends and therefore presents a data-leakage risk.
