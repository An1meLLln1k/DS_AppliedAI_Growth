from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parent

predictions_path = BASE_DIR / "classification_predictions.csv"
metrics_path = BASE_DIR / "classification_metrics.csv"

# Training dataset.
# Target: high_value_order.
# Features: user_age, previous_orders, is_premium, product_category, city.
data = [
    {"user_age": 22, "previous_orders": 1, "is_premium": 0, "product_category": "book", "city": "Ekaterinburg", "amount": 1200},
    {"user_age": 25, "previous_orders": 2, "is_premium": 0, "product_category": "course", "city": "Ekaterinburg", "amount": 5000},
    {"user_age": 31, "previous_orders": 8, "is_premium": 1, "product_category": "laptop", "city": "Moscow", "amount": 90000},
    {"user_age": 28, "previous_orders": 5, "is_premium": 1, "product_category": "phone", "city": "Moscow", "amount": 70000},
    {"user_age": 35, "previous_orders": 7, "is_premium": 1, "product_category": "monitor", "city": "Moscow", "amount": 30000},
    {"user_age": 24, "previous_orders": 3, "is_premium": 0, "product_category": "keyboard", "city": "Ekaterinburg", "amount": 6000},
    {"user_age": 41, "previous_orders": 10, "is_premium": 1, "product_category": "laptop", "city": "Moscow", "amount": 95000},
    {"user_age": 29, "previous_orders": 4, "is_premium": 0, "product_category": "phone", "city": "Kazan", "amount": 55000},
    {"user_age": 33, "previous_orders": 6, "is_premium": 1, "product_category": "course", "city": "Moscow", "amount": 15000},
    {"user_age": 21, "previous_orders": 1, "is_premium": 0, "product_category": "mouse", "city": "Ekaterinburg", "amount": 2500},
    {"user_age": 45, "previous_orders": 12, "is_premium": 1, "product_category": "laptop", "city": "Kazan", "amount": 88000},
    {"user_age": 27, "previous_orders": 2, "is_premium": 0, "product_category": "monitor", "city": "Ekaterinburg", "amount": 22000},
    {"user_age": 39, "previous_orders": 9, "is_premium": 1, "product_category": "phone", "city": "Moscow", "amount": 76000},
    {"user_age": 23, "previous_orders": 1, "is_premium": 0, "product_category": "book", "city": "Kazan", "amount": 1500},
    {"user_age": 30, "previous_orders": 5, "is_premium": 0, "product_category": "course", "city": "Moscow", "amount": 9000},
    {"user_age": 34, "previous_orders": 6, "is_premium": 1, "product_category": "monitor", "city": "Kazan", "amount": 28000},
    {"user_age": 26, "previous_orders": 3, "is_premium": 0, "product_category": "keyboard", "city": "Moscow", "amount": 7000},
    {"user_age": 37, "previous_orders": 11, "is_premium": 1, "product_category": "laptop", "city": "Moscow", "amount": 98000},
    {"user_age": 32, "previous_orders": 4, "is_premium": 0, "product_category": "phone", "city": "Ekaterinburg", "amount": 52000},
    {"user_age": 44, "previous_orders": 13, "is_premium": 1, "product_category": "laptop", "city": "Moscow", "amount": 102000},
]

df = pd.DataFrame(data)

# Create classification target.
# 1 means high-value order, 0 means regular order.
df["high_value_order"] = (df["amount"] >= 50000).astype(int)

print("\n=== 1. Source data ===")
print(df.head())

print("\n=== 2. Target distribution ===")
print(df["high_value_order"].value_counts())

# Target: what the model predicts.
y = df["high_value_order"]

# Features: data used by the model.
# Important: amount is excluded to avoid target leakage.
X = df.drop(columns=["amount", "high_value_order"])

print("\n=== 3. Raw features ===")
print(X.head())

# Convert categorical features into numeric columns.
X_encoded = pd.get_dummies(X, columns=["product_category", "city"], drop_first=True)

print("\n=== 4. Encoded features ===")
print(X_encoded.head())

# Stratify keeps class proportions closer in train and test sets.
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

print("\n=== 5. Train/test sizes ===")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

print("\n=== 6. Train target distribution ===")
print(y_train.value_counts())

print("\n=== 7. Test target distribution ===")
print(y_test.value_counts())

# Baseline: always predict the most frequent class from the training set.
majority_class = y_train.mode()[0]
baseline_predictions = [majority_class] * len(y_test)

# Classification model.
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

model_predictions = model.predict(X_test)
model_probabilities = model.predict_proba(X_test)[:, 1]

comparison = X_test.copy()
comparison["actual_class"] = y_test.values
comparison["baseline_prediction"] = baseline_predictions
comparison["model_prediction"] = model_predictions
comparison["model_probability_high_value"] = model_probabilities.round(3)

print("\n=== 8. Prediction comparison ===")
print(
    comparison[
        [
            "actual_class",
            "baseline_prediction",
            "model_prediction",
            "model_probability_high_value",
        ]
    ]
)

baseline_metrics = {
    "approach": "baseline_majority_class",
    "accuracy": round(accuracy_score(y_test, baseline_predictions), 3),
    "precision": round(precision_score(y_test, baseline_predictions, zero_division=0), 3),
    "recall": round(recall_score(y_test, baseline_predictions, zero_division=0), 3),
    "f1": round(f1_score(y_test, baseline_predictions, zero_division=0), 3),
}

model_metrics = {
    "approach": "logistic_regression",
    "accuracy": round(accuracy_score(y_test, model_predictions), 3),
    "precision": round(precision_score(y_test, model_predictions, zero_division=0), 3),
    "recall": round(recall_score(y_test, model_predictions, zero_division=0), 3),
    "f1": round(f1_score(y_test, model_predictions, zero_division=0), 3),
}

metrics = pd.DataFrame([baseline_metrics, model_metrics])

print("\n=== 9. Metrics comparison ===")
print(metrics)

print("\n=== 10. Confusion matrix ===")
print(confusion_matrix(y_test, model_predictions))

if model_metrics["f1"] > baseline_metrics["f1"]:
    print("\nResult: model is better than baseline by F1.")
else:
    print("\nResult: model is not better than baseline by F1.")

comparison.to_csv(predictions_path, index=False)
metrics.to_csv(metrics_path, index=False)

print("\nSaved predictions to:", predictions_path)
print("Saved metrics to:", metrics_path)