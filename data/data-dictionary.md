# Data Dictionary

## Dataset

Bank Marketing Dataset

## Target Variable

The target variable is `y`.

- `yes` = the customer subscribed to a term deposit
- `no` = the customer did not subscribe to a term deposit

## Variables

| Variable | Type | Meaning |
|---|---|---|
| age | Numeric | Customer age |
| job | Categorical | Customer occupation/job type |
| marital | Categorical | Marital status |
| education | Categorical | Education level |
| default | Categorical/Binary | Whether the customer has credit in default |
| balance | Numeric | Average yearly account balance |
| housing | Categorical/Binary | Whether the customer has a housing loan |
| loan | Categorical/Binary | Whether the customer has a personal loan |
| contact | Categorical | Contact communication type |
| day | Numeric | Day of month when the customer was contacted |
| month | Categorical | Month when the customer was contacted |
| duration | Numeric | Duration of the last contact in seconds |
| campaign | Numeric | Number of contacts made during the current campaign |
| pdays | Numeric | Number of days since the customer was previously contacted |
| previous | Numeric | Number of contacts made before the current campaign |
| poutcome | Categorical | Outcome of the previous marketing campaign |
| y | Target/Binary | Whether the customer subscribed to a term deposit |

## Initial Data Notes

The dataset uses semicolons as separators rather than commas.

Several categorical variables contain values such as `unknown`. These were examined during the data-quality audit rather than automatically treated as missing.

The variable `pdays` may contain `-1`, which represents a special condition and requires careful interpretation.

The variable `duration` requires special attention for possible data leakage because the call duration would only be known after the marketing contact had already taken place.

## Data Source

The dataset was obtained from the UCI Machine Learning Repository.

The full `bank-full.csv` dataset is used for this practical project.
