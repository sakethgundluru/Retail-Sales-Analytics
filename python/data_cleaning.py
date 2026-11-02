
import pandas as pd
from pathlib import Path

# ==========================================
# 1. PROJECT FILE PATHS
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parents[1]

INPUT_FILE = PROJECT_DIR / "dataset" / "raw_data.csv"
OUTPUT_FILE = PROJECT_DIR / "dataset" / "cleaned_data.csv"
REPORT_FILE = PROJECT_DIR / "reports" / "cleaning_report.txt"

print("=" * 60)
print("RETAIL SALES ANALYTICS - DATA CLEANING")
print("=" * 60)

# ==========================================
# 2. LOAD RAW DATA
# ==========================================

if not INPUT_FILE.exists():
    raise FileNotFoundError(f"File not found: {INPUT_FILE}")

try:
    df = pd.read_csv(INPUT_FILE, encoding="utf-8-sig")
except UnicodeDecodeError:
    df = pd.read_csv(INPUT_FILE, encoding="cp1252")

original_rows = len(df)

print("\nOriginal Rows:", original_rows)

# ==========================================
# 3. CLEAN COLUMN NAMES
# ==========================================

df.columns = df.columns.str.strip()

# ==========================================
# 4. CLEAN TEXT COLUMNS
# ==========================================

text_columns = df.select_dtypes(include=["object"]).columns

for column in text_columns:
    df[column] = df[column].apply(
        lambda value: value.strip()
        if isinstance(value, str)
        else value
    )

# ==========================================
# 5. CONVERT DATE COLUMNS
# ==========================================

date_columns = ["Order Date", "Ship Date"]

for column in date_columns:
    if column in df.columns:
        df[column] = pd.to_datetime(
            df[column],
            errors="coerce"
        )

# ==========================================
# 6. CONVERT NUMERICAL COLUMNS
# ==========================================

numeric_columns = [
    "Sales",
    "Quantity",
    "Discount",
    "Profit",
    "Postal Code"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce"
        )

# ==========================================
# 7. CHECK INVALID VALUES
# ==========================================

print("\nDATA QUALITY VALIDATION")

invalid_dates = {
    column: int(df[column].isna().sum())
    for column in date_columns
    if column in df.columns
}

invalid_numeric = {
    column: int(df[column].isna().sum())
    for column in numeric_columns
    if column in df.columns
}

duplicate_count = int(df.duplicated().sum())

negative_sales = int((df["Sales"] < 0).sum())
invalid_quantity = int((df["Quantity"] <= 0).sum())
invalid_discount = int(
    (~df["Discount"].between(0, 1)).sum()
)

invalid_ship_dates = 0

if "Order Date" in df.columns and "Ship Date" in df.columns:
    invalid_ship_dates = int(
        (df["Ship Date"] < df["Order Date"]).sum()
    )

print("Invalid dates:", invalid_dates)
print("Invalid numeric values:", invalid_numeric)
print("Duplicate records:", duplicate_count)
print("Negative sales:", negative_sales)
print("Invalid quantity:", invalid_quantity)
print("Discount outside 0-1:", invalid_discount)
print("Ship date before order date:", invalid_ship_dates)

# ==========================================
# 8. STOP IF IMPORTANT DATA ISSUES EXIST
# ==========================================

issues = []

if df.isna().any().any():
    issues.append("Missing or invalid values detected")

if duplicate_count > 0:
    issues.append("Duplicate records detected")

if negative_sales > 0:
    issues.append("Negative sales detected - review")

if invalid_quantity > 0:
    issues.append("Invalid quantities detected")

if invalid_discount > 0:
    issues.append("Invalid discount values detected")

if invalid_ship_dates > 0:
    issues.append("Shipping date precedes order date")

if issues:
    print("\nREVIEW REQUIRED:")
    for issue in issues:
        print("-", issue)

    raise ValueError(
        "Cleaning stopped. Investigate the issues above "
        "before exporting the cleaned dataset."
    )

# ==========================================
# 9. EXPORT CLEANED DATASET
# ==========================================

OUTPUT_FILE.parent.mkdir(exist_ok=True)

df.to_csv(OUTPUT_FILE, index=False)

# ==========================================
# 10. GENERATE CLEANING REPORT
# ==========================================

REPORT_FILE.parent.mkdir(exist_ok=True)

with open(REPORT_FILE, "w", encoding="utf-8") as file:
    file.write("RETAIL SALES DATA CLEANING REPORT\n")
    file.write("=" * 40 + "\n")
    file.write(f"Original rows: {original_rows}\n")
    file.write(f"Final rows: {len(df)}\n")
    file.write(f"Total columns: {len(df.columns)}\n")
    file.write(f"Duplicate records: {df.duplicated().sum()}\n")
    file.write(f"Missing values: {df.isna().sum().sum()}\n")
    file.write(f"Negative sales: {negative_sales}\n")
    file.write(f"Invalid quantities: {invalid_quantity}\n")
    file.write(f"Invalid discounts: {invalid_discount}\n")
    file.write(f"Invalid shipping dates: {invalid_ship_dates}\n")
    file.write("\nData cleaning completed successfully.\n")

# ==========================================
# 11. FINAL SUMMARY
# ==========================================

print("\nCLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)

print("Original Rows:", original_rows)
print("Cleaned Rows:", len(df))
print("Total Columns:", len(df.columns))
print("Missing Values:", df.isna().sum().sum())

print("\nCleaned Dataset Saved:", OUTPUT_FILE)
print("Cleaning Report Saved:", REPORT_FILE)

print("\nNEXT STEP: EXPLORATORY DATA ANALYSIS")
