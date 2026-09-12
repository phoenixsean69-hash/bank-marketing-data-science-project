import matplotlib.pyplot as plt

models = [
    "Baseline",
    "Logistic Regression",
    "Random Forest"
]

f1_scores = [0.0000, 0.3732, 0.4378]
roc_auc = [0.5000, 0.7722, 0.7936]

x = range(len(models))
width = 0.35

plt.figure(figsize=(9, 5))

plt.bar(
    [i - width/2 for i in x],
    f1_scores,
    width,
    label="F1-score"
)

plt.bar(
    [i + width/2 for i in x],
    roc_auc,
    width,
    label="ROC-AUC"
)

plt.xticks(list(x), models)
plt.ylabel("Score")
plt.title("Model Performance Comparison")
plt.ylim(0, 1)
plt.legend()
plt.tight_layout()

plt.savefig(
    "./charts/05_model_comparison.png",
    dpi=200
)

plt.close()

print("Saved: charts/05_model_comparison.png")
