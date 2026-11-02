
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# ==========================================
# 1. PROJECT PATHS
# ==========================================

PROJECT_DIR = Path(__file__).resolve().parents[1]

DATA_FILE = PROJECT_DIR / "dataset" / "cleaned_data.csv"
OUTPUT_DIR = PROJECT_DIR / "reports"
CHART_DIR = PROJECT_DIR / "screenshots"

OUTPUT_DIR.mkdir(exist_ok=True)
CHART_DIR.mkdir(exist_ok=True)

# ==========================================
# 2. LOAD CLEANED DATA
# ==========================================

df = pd.read_csv(DATA_FILE)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("=" * 60)
print("RETAIL SALES ANALYTICS - EXPLORATORY DATA ANALYSIS")
print("=" * 60)

# ==========================================
# 3. KEY BUSINESS METRICS
# ==========================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
total_quantity = df["Quantity"].sum()

average_order_value = total_sales / total_orders
profit_margin = (total_profit / total_sales) * 100

print("\n1. BUSINESS PERFORMANCE")

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Total Quantity: {total_quantity:,}")
print(f"Average Order Value: ${average_order_value:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")

# ==========================================
# 4. SALES BY CATEGORY
# ==========================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n2. SALES BY CATEGORY")
print(category_sales)

category_sales.to_csv(
    OUTPUT_DIR / "sales_by_category.csv"
)

# ==========================================
# 5. PROFIT BY REGION
# ==========================================

region_profit = (
    df.groupby("Region")["Profit"]
    .sum()
    .sort_values(ascending=False)
)

print("\n3. PROFIT BY REGION")
print(region_profit)

region_profit.to_csv(
    OUTPUT_DIR / "profit_by_region.csv"
)

# ==========================================
# 6. MONTHLY SALES TREND
# ==========================================

df["Year_Month"] = df["Order Date"].dt.to_period("M").astype(str)

monthly_sales = (
    df.groupby("Year_Month")["Sales"]
    .sum()
    .sort_index()
)

print("\n4. MONTHLY SALES TREND")
print(monthly_sales)

monthly_sales.to_csv(
    OUTPUT_DIR / "monthly_sales.csv"
)

# ==========================================
# 7. TOP 10 CUSTOMERS
# ==========================================

top_customers = (
    df.groupby("Customer Name")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Total_Orders=("Order ID", "nunique")
    )
    .sort_values("Total_Sales", ascending=False)
    .head(10)
)

print("\n5. TOP 10 CUSTOMERS")
print(top_customers)

top_customers.to_csv(
    OUTPUT_DIR / "top_10_customers.csv"
)

# ==========================================
# 8. TOP 10 PRODUCTS
# ==========================================

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n6. TOP 10 PRODUCTS")
print(top_products)

top_products.to_csv(
    OUTPUT_DIR / "top_10_products.csv"
)

# ==========================================
# 9. LOSS-MAKING PRODUCTS
# ==========================================

loss_products = (
    df.groupby("Product Name")["Profit"]
    .sum()
    .sort_values()
    .head(10)
)

print("\n7. TOP 10 LOSS-MAKING PRODUCTS")
print(loss_products)

loss_products.to_csv(
    OUTPUT_DIR / "loss_making_products.csv"
)

# ==========================================
# 10. DISCOUNT AND PROFIT ANALYSIS
# ==========================================

discount_analysis = (
    df.groupby("Discount")
    .agg(
        Total_Sales=("Sales", "sum"),
        Total_Profit=("Profit", "sum"),
        Average_Profit=("Profit", "mean"),
        Order_Lines=("Order ID", "count")
    )
    .sort_index()
)

print("\n8. DISCOUNT AND PROFIT ANALYSIS")
print(discount_analysis)

discount_analysis.to_csv(
    OUTPUT_DIR / "discount_analysis.csv"
)

# ==========================================
# 11. CHART 1 - SALES BY CATEGORY
# ==========================================

plt.figure(figsize=(9, 5))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values
)

plt.title("Total Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Sales ($)")
plt.tight_layout()

plt.savefig(CHART_DIR / "sales_by_category.png")
plt.close()

# ==========================================
# 12. CHART 2 - PROFIT BY REGION
# ==========================================

plt.figure(figsize=(9, 5))

sns.barplot(
    x=region_profit.index,
    y=region_profit.values
)

plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit ($)")
plt.tight_layout()

plt.savefig(CHART_DIR / "profit_by_region.png")
plt.close()

# ==========================================
# 13. CHART 3 - MONTHLY SALES
# ==========================================

plt.figure(figsize=(13, 5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.xticks(rotation=60)
plt.tight_layout()

plt.savefig(CHART_DIR / "monthly_sales_trend.png")
plt.close()

# ==========================================
# 14. CHART 4 - TOP 10 CUSTOMERS
# ==========================================

plt.figure(figsize=(11, 6))

sns.barplot(
    x=top_customers["Total_Sales"].values,
    y=top_customers.index
)

plt.title("Top 10 Customers by Sales")
plt.xlabel("Sales ($)")
plt.ylabel("Customer")
plt.tight_layout()

plt.savefig(CHART_DIR / "top_10_customers.png")
plt.close()

# ==========================================
# 15. CHART 5 - DISCOUNT VS PROFIT
# ==========================================

plt.figure(figsize=(9, 5))

sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit",
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit ($)")
plt.tight_layout()

plt.savefig(CHART_DIR / "discount_vs_profit.png")
plt.close()

# ==========================================
# 16. BUSINESS SUMMARY
# ==========================================

summary = f"""
RETAIL SALES ANALYTICS - BUSINESS SUMMARY

Total Sales: ${total_sales:,.2f}
Total Profit: ${total_profit:,.2f}
Total Orders: {total_orders:,}
Total Customers: {total_customers:,}
Total Quantity: {total_quantity:,}
Average Order Value: ${average_order_value:,.2f}
Profit Margin: {profit_margin:.2f}%

Highest Sales Category: {category_sales.idxmax()}
Highest Profit Region: {region_profit.idxmax()}
Best Sales Month: {monthly_sales.idxmax()}
"""

with open(
    OUTPUT_DIR / "business_summary.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(summary)

print("\n" + summary)

print("=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("Analysis reports saved in reports/")
print("Charts saved in screenshots/")
print("=" * 60)
