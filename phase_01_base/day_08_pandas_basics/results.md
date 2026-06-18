# Day 08: pandas basics

## What I did

* Created two CSV files: `users.csv` and `orders.csv`.
* Loaded CSV files into pandas DataFrames using `pd.read_csv()`.
* Inspected the data using `head()`, `info()` and `describe()`.
* Filtered users by city and age.
* Calculated basic order metrics:

  * total order amount;
  * average order amount.
* Merged `users` and `orders` by `user_id`.
* Calculated total order amount by user.
* Added customer levels based on total order amount.
* Calculated total order amount by city.
* Saved processed user summary to `user_summary.csv`.

## Artifacts

* `users.csv`
* `orders.csv`
* `pandas_basics.py`
* `user_summary.csv`
* `results.md`

## Key takeaways

* `pd.read_csv()` loads CSV files into DataFrames.
* `head()` helps quickly inspect the first rows of a table.
* `info()` shows column names, data types and missing values.
* `describe()` gives basic statistics for numeric columns.
* Boolean filtering in pandas works similarly to SQL `WHERE`.
* `groupby()` works similarly to SQL `GROUP BY`.
* `merge()` works similarly to SQL `JOIN`.
* `apply()` can be used to create new values based on custom logic.
* `to_csv()` saves processed data to a CSV file.

## SQL to pandas mapping

| SQL concept           | pandas equivalent           |
| --------------------- | --------------------------- |
| `SELECT * FROM table` | `pd.read_csv()` / DataFrame |
| `WHERE`               | Boolean filtering           |
| `GROUP BY`            | `groupby()`                 |
| `JOIN`                | `merge()`                   |
| `CASE WHEN`           | custom function + `apply()` |
| export result         | `to_csv()`                  |

## Result

Completed the first pandas practice task. The script loads user and order data, performs basic filtering, grouping and merging, creates a user-level summary and saves the result as a CSV file.

## Next step

Practice pandas filtering, sorting, missing values and simple feature creation.
