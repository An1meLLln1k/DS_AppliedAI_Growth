from pathlib import Path
import json

import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
PHASE_DIR = BASE_DIR.parent

input_path = PHASE_DIR / "day_10_ai_assisted_pandas_review" / "cleaned_paid_orders.csv"
output_path = BASE_DIR / "quality_report.json"

df = pd.read_csv(input_path)

expected_columns = [
    "order_id",
    "user_id",
    "name",
    "city",
    "product",
    "amount",
    "order_date",
    "status",
]

report = {
    "row_count": len(df),
    "column_count": len(df.columns),
    "columns_ok": list(df.columns) == expected_columns,
    "missing_values": df.isna().sum().to_dict(),
    "duplicate_order_id_count": int(df["order_id"].duplicated().sum()),
    "invalid_status_count": int((df["status"] != "paid").sum()),
    "non_positive_amount_count": int((df["amount"] <= 0).sum()),
    "all_checks_passed": True,
}

report["all_checks_passed"] = (
    report["row_count"] > 0
    and report["columns_ok"]
    and sum(report["missing_values"].values()) == 0
    and report["duplicate_order_id_count"] == 0
    and report["invalid_status_count"] == 0
    and report["non_positive_amount_count"] == 0
)

print("\n=== Data quality report ===")
print(json.dumps(report, indent=4, ensure_ascii=False))

with open(output_path, "w", encoding="utf-8") as file:
    json.dump(report, file, indent=4, ensure_ascii=False)

print("\nSaved to:", output_path)