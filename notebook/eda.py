import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "./data/bank-full.csv"
CHART_DIR = "./charts"

os.makedirs(CHART_DIR, exist_ok=True)

df = pd.read_csv(DATA_PATH, sep=";")

print("Dataset shape:", df.shape)
print("\nTarget distribution:")
print(df["y"].value_counts())
print("\nTarget percentage:")
print((df["y"].value_counts(normalize=True) * 100).round(2))

# Chart 1: Target class distribution
target_counts = df["y"].value_counts()

plt.figure(figsize=(7, 5))
target_counts.plot(kind="bar")
plt.title("Customer Subscription Outcome")
plt.xlabel("Subscribed to Term Deposit")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "01_target_distribution.png"), dpi=200)
plt.close()

# Chart 2: Subscription rate by contact type
contact_rate = (
    df.assign(subscribed=(df["y"] == "yes").astype(int))
      .groupby("contact")["subscribed"]
      .mean()
      .sort_values(ascending=False) * 100
)

plt.figure(figsize=(8, 5))
contact_rate.plot(kind="bar")
plt.title("Subscription Rate by Contact Type")
plt.xlabel("Contact Type")
plt.ylabel("Subscription Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "02_subscription_by_contact.png"), dpi=200)
plt.close()

# Chart 3: Subscription rate by month
month_order = [
    "jan", "feb", "mar", "apr", "may", "jun",
    "jul", "aug", "sep", "oct", "nov", "dec"
]

month_rate = (
    df.assign(subscribed=(df["y"] == "yes").astype(int))
      .groupby("month")["subscribed"]
      .mean()
      .reindex(month_order) * 100
)

plt.figure(figsize=(10, 5))
month_rate.plot(kind="bar")
plt.title("Subscription Rate by Contact Month")
plt.xlabel("Month")
plt.ylabel("Subscription Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "03_subscription_by_month.png"), dpi=200)
plt.close()

# Extra chart: Subscription rate by previous campaign outcome
poutcome_rate = (
    df.assign(subscribed=(df["y"] == "yes").astype(int))
      .groupby("poutcome")["subscribed"]
      .mean()
      .sort_values(ascending=False) * 100
)

plt.figure(figsize=(8, 5))
poutcome_rate.plot(kind="bar")
plt.title("Subscription Rate by Previous Campaign Outcome")
plt.xlabel("Previous Campaign Outcome")
plt.ylabel("Subscription Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(os.path.join(CHART_DIR, "04_subscription_by_poutcome.png"), dpi=200)
plt.close()

print("\nSUBSCRIPTION RATE BY CONTACT TYPE (%)")
print(contact_rate.round(2))

print("\nSUBSCRIPTION RATE BY MONTH (%)")
print(month_rate.round(2))

print("\nSUBSCRIPTION RATE BY PREVIOUS CAMPAIGN OUTCOME (%)")
print(poutcome_rate.round(2))

print("\nCharts saved to:", CHART_DIR)
