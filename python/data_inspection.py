
import pandas as pd
from pathlib import Path

# 1. Locate project folder
PROJECT_DIR = Path(__file__).resolve().parents[1]

# 2. Locate raw dataset
DATA_PATH = PROJECT_DIR / "dataset" / "raw_data.csv"

# 3. Load dataset
print("=" * 60)
print("RETAIL SALES ANALYTICS - DATA INSPECTION")
print("=" * 60)

if not DATA_PATH.exists():
    raise FileNotFoundError(
        f"Dataset not found: {DATA_PATH}\n"
        "Place raw_data.csv inside the dataset folder."
    )

try:
    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")
except UnicodeDecodeError:
    df = pd.read_csv(DATA_PATH, encoding="cp1252")

# 4. Dataset dimensions
print("\n1. DATASET SIZE")
print("Total Rows:", df.shape[0])
print("Total Columns:", df.shape[1])

# 5. Column names
print("\n2. COLUMN NAMES")
print(df.columns.tolist())

# 6. First five records
print("\n3. FIRST FIVE RECORDS")
print(df.head().to_string())

# 7. Data types
print("\n4. DATA TYPES")
print(df.dtypes)

# 8. Missing values
print("\n5. MISSING VALUES")
missing = df.isnull().sum()
print(missing[missing > 0])

# 9. Duplicate records
print("\n6. DUPLICATE RECORDS")
print("Total Duplicates:", df.duplicated().sum())

# 10. Statistical summary
print("\n7. STATISTICAL SUMMARY")
print(df.describe(include="all").to_string())

# 11. Sales and profit summary
print("\n8. SALES AND PROFIT SUMMARY")

for column in ["Sales", "Profit", "Quantity", "Discount"]:
    if column in df.columns:
        print(f"{column}:")
        print("Total:", df[column].sum())
        print("Average:", df[column].mean())

# 12. Save inspection reports
REPORT_DIR = PROJECT_DIR / "reports"
REPORT_DIR.mkdir(exist_ok=True)

missing.to_csv(REPORT_DIR / "missing_values.csv")

df.dtypes.astype(str).rename("data_type").to_csv(
    REPORT_DIR / "column_data_types.csv"
)

print("\n" + "=" * 60)
print("DATA INSPECTION COMPLETED SUCCESSFULLY")
print("Reports saved in the reports folder.")
print("=" * 60)
