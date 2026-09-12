import pandas as pd

DATA_PATH = "../data/bank-full.csv"

df = pd.read_csv(DATA_PATH, sep=";")

print("DATASET SHAPE")
print(df.shape)

print("\nCOLUMNS")
print(df.columns.tolist())

print("\nFIRST FIVE ROWS")
print(df.head())

print("\nDATA TYPES")
print(df.dtypes)

print("\nMISSING VALUES")
print(df.isna().sum())

print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

print("\nTARGET DISTRIBUTION")
print(df["y"].value_counts())

print("\nTARGET DISTRIBUTION (%)")
print((df["y"].value_counts(normalize=True) * 100).round(2))

print("\nUNIQUE VALUES IN CATEGORICAL COLUMNS")
for col in df.select_dtypes(include="object").columns:
    print(f"\n{col}")
    print(df[col].value_counts(dropna=False))
