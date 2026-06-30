from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


BASE_DIR = Path(__file__).resolve().parent

predictions_path = BASE_DIR / "baseline_vs_model_predictions.csv"
metrics_path = BASE_DIR / "metrics_summary.csv"

# Training dataset.
# Target: amount.
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

print("\n=== 1. Source data shape ===")
print(df.shape)

# Split target and features.
y = df["amount"]
X = df.drop(columns=["amount"])

# Encode categorical features.
X_encoded = pd.get_dummies(X, columns=["product_category", "city"], drop_first=True)

# Split into train and test sets.
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded,
    y,
    test_size=0.25,
    random_state=42,
)

print("\n=== 2. Train/test sizes ===")
print("X_train:", X_train.shape)
print("X_test:", X_test.shape)
print("y_train:", y_train.shape)
print("y_test:", y_test.shape)

# Baseline model: always predict the mean target value from the training set.
baseline_prediction_value = y_train.mean()
baseline_predictions = [baseline_prediction_value] * len(y_test)

baseline_mae = mean_absolute_error(y_test, baseline_predictions)
baseline_r2 = r2_score(y_test, baseline_predictions)

# ML model.
model = LinearRegression()
model.fit(X_train, y_train)

model_predictions = model.predict(X_test)

model_mae = mean_absolute_error(y_test, model_predictions)
model_r2 = r2_score(y_test, model_predictions)

# Build comparison table.
comparison = X_test.copy()
comparison["actual_amount"] = y_test.values
comparison["baseline_prediction"] = pd.Series(baseline_predictions).round(2).values
comparison["model_prediction"] = model_predictions.round(2)
comparison["baseline_error"] = (
    comparison["actual_amount"] - comparison["baseline_prediction"]
).abs()
comparison["model_error"] = (
    comparison["actual_amount"] - comparison["model_prediction"]
).abs()

print("\n=== 3. Prediction comparison ===")
print(
    comparison[
        [
            "actual_amount",
            "baseline_prediction",
            "model_prediction",
            "baseline_error",
            "model_error",
        ]
    ]
)

metrics = pd.DataFrame(
    [
        {
            "approach": "baseline_mean",
            "mae": round(baseline_mae, 2),
            "r2": round(baseline_r2, 3),
        },
        {
            "approach": "linear_regression",
            "mae": round(model_mae, 2),
            "r2": round(model_r2, 3),
        },
    ]
)

print("\n=== 4. Metrics comparison ===")
print(metrics)

mae_improvement = baseline_mae - model_mae

print("\n=== 5. Interpretation ===")
print("Baseline MAE:", round(baseline_mae, 2))
print("Model MAE:", round(model_mae, 2))
print("MAE improvement:", round(mae_improvement, 2))

if model_mae < baseline_mae:
    print("Result: model is better than baseline.")
else:
    print("Result: model is not better than baseline.")

comparison.to_csv(predictions_path, index=False)
metrics.to_csv(metrics_path, index=False)

print("\nSaved predictions to:", predictions_path)
print("Saved metrics to:", metrics_path)