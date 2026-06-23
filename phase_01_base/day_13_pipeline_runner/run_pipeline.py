from pathlib import Path
import subprocess
import sys


BASE_DIR = Path(__file__).resolve().parent
PHASE_DIR = BASE_DIR.parent

scripts = [
    PHASE_DIR / "day_10_ai_assisted_pandas_review" / "agent_solution.py",
    PHASE_DIR / "day_11_data_validation" / "validate_cleaned_orders.py",
    PHASE_DIR / "day_12_data_quality_report" / "quality_report.py",
]


def run_script(script_path: Path) -> None:
    print(f"\n=== Running: {script_path.name} ===")

    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        check=True,
        text=True,
        capture_output=True,
    )

    print(result.stdout)

    if result.stderr:
        print("\n--- STDERR ---")
        print(result.stderr)


def main() -> None:
    print("\n=== Day 13: Pipeline runner ===")

    for script in scripts:
        run_script(script)

    print("\n=== Pipeline finished successfully ===")


if __name__ == "__main__":
    main()