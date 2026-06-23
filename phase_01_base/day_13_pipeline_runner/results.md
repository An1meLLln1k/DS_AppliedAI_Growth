# Day 13: Pipeline runner

## Goal

Build a single runner script that executes the full data workflow from cleaning to validation and quality reporting.

## What I did

* Created `run_pipeline.py`.
* Added sequential execution of three scripts:

  * `agent_solution.py`
  * `validate_cleaned_orders.py`
  * `quality_report.py`
* Used `subprocess.run()` to launch each step.
* Used `check=True` so the pipeline stops if any step fails.
* Verified that the full pipeline finishes successfully.

## Pipeline steps

1. `agent_solution.py`

   Loads users and dirty orders data, filters valid paid orders, joins user information, fills missing order dates and saves `cleaned_paid_orders.csv`.

2. `validate_cleaned_orders.py`

   Runs automated validation checks with `assert`:

   * final report is not empty;
   * all statuses are `paid`;
   * all amounts are positive;
   * no missing values;
   * unique `order_id`;
   * expected column structure.

3. `quality_report.py`

   Generates a structured JSON data quality report with row counts, missing values, duplicate checks, invalid status checks, amount checks and overall pass/fail status.

## Result

The pipeline finished successfully.

Final validation result:

```text
All validation checks passed.
```

Final quality report result:

```json
{
    "row_count": 6,
    "column_count": 8,
    "columns_ok": true,
    "duplicate_order_id_count": 0,
    "invalid_status_count": 0,
    "non_positive_amount_count": 0,
    "all_checks_passed": true
}
```

## Key takeaway

A data workflow should be executable as one controlled pipeline, not as disconnected manual scripts.

This is especially useful in AI-assisted workflows because generated code must be integrated, validated and monitored before its output can be trusted.
