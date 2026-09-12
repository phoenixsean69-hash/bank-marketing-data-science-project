import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
    classification_report
)

RANDOM_STATE = 42
DATA_PATH = "./data/bank-full.csv"

df = pd.read_csv(DATA_PATH, sep=";")

# Remove duration because it would not be known before the marketing call ends.
X = df.drop(columns=["y", "duration"])
y = df["y"].map({"no": 0, "yes": 1})

categorical_features = X.select_dtypes(include=["object", "str"]).columns.tolist()
numeric_features = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

print("CATEGORICAL FEATURES")
print(categorical_features)

print("\nNUMERIC FEATURES")
print(numeric_features)

print("\nFEATURE COUNT")
print(len(X.columns))

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=RANDOM_STATE,
    stratify=y
)

print("\nTRAINING SET SIZE")
print(X_train.shape)

print("\nTEST SET SIZE")
print(X_test.shape)

print("\nTRAIN TARGET DISTRIBUTION")
print(y_train.value_counts(normalize=True).round(4))

print("\nTEST TARGET DISTRIBUTION")
print(y_test.value_counts(normalize=True).round(4))

preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        ),
        (
            "numeric",
            "passthrough",
            numeric_features
        )
    ]
)

baseline_model = DummyClassifier(
    strategy="most_frequent",
    random_state=RANDOM_STATE
)

baseline_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", baseline_model)
    ]
)

baseline_pipeline.fit(X_train, y_train)

y_pred = baseline_pipeline.predict(X_test)

if hasattr(baseline_pipeline, "predict_proba"):
    y_prob = baseline_pipeline.predict_proba(X_test)[:, 1]
else:
    y_prob = None

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("\nBASELINE MODEL RESULTS")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")

if y_prob is not None:
    try:
        auc = roc_auc_score(y_test, y_prob)
        print(f"ROC-AUC:   {auc:.4f}")
    except ValueError:
        print("ROC-AUC: could not be calculated")

print("\nCONFUSION MATRIX")
print(confusion_matrix(y_test, y_pred))

print("\nCLASSIFICATION REPORT")
print(classification_report(y_test, y_pred, zero_division=0))
