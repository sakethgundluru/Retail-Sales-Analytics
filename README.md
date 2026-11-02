# Retail Sales Analytics | End-to-End Data Analytics Project

## Project Overview

An end-to-end Retail Sales Analytics project designed to analyze sales performance, profitability, customer purchasing behavior, product performance, and regional business trends.

This project uses Python, SQL, MySQL, and Power BI to transform raw retail data into meaningful business insights and support data-driven decision-making.

## Business Objectives

- Analyze overall sales and profitability.
- Identify top-performing product categories and products.
- Evaluate regional and customer performance.
- Understand the relationship between discounts and profitability.
- Analyze monthly sales trends.
- Identify loss-making products and improvement opportunities.

## Technology Stack

| Tool | Purpose |
|---|---|
| Python | Data cleaning, analysis and visualization |
| Pandas & NumPy | Data manipulation |
| Matplotlib & Seaborn | Exploratory data visualization |
| SQL | Business analysis and querying |
| MySQL | Database management |
| Power BI | Interactive business dashboards |
| Git & GitHub | Version control and project documentation |

## Dataset

**Dataset:** Sample Superstore

- Records: 9,994
- Columns: 21
- Data includes orders, customers, products, sales, discounts, quantities and profits.

## Project Structure

```text
Retail-Sales-Analytics/
│
├── dataset/
│   ├── raw_data.csv
│   └── cleaned_data.csv
│
├── python/
│   ├── data_inspection.py
│   ├── data_cleaning.py
│   ├── exploratory_analysis.py
│   └── import_to_mysql.py
│
├── sql/
│   ├── 01_database_setup.sql
│   └── 02_business_analysis.sql
│
├── powerbi/
│
├── reports/
├── screenshots/
├── requirements.txt
└── README.md
```

## Key Business Insights

| KPI | Result |
|---|---:|
| Total Sales | $2,297,200.86 |
| Total Profit | $286,397.02 |
| Total Orders | 5,009 |
| Total Customers | 793 |
| Total Quantity Sold | 37,873 |
| Average Order Value | $458.61 |
| Profit Margin | 12.47% |

### Important Findings

1. **Category Performance:** Technology generated the highest sales, approximately $836K.
2. **Regional Performance:** The West region generated the highest profit, approximately $108K.
3. **Monthly Performance:** November 2017 was the highest-sales month.
4. **Product Performance:** Canon imageCLASS 2200 Advanced Copier was the top product by sales.
5. **Profitability:** Several products generated significant losses, highlighting opportunities for pricing and product-level review.
6. **Discount Analysis:** Higher discount levels were associated with negative profitability in several discount groups. This is an observed relationship, not proof of causation.

## Python Analysis

- Data inspection and validation
- Missing-value and duplicate checks
- Data cleaning and transformation
- Exploratory Data Analysis (EDA)
- Business KPI calculations
- Visualization and report generation

## SQL Analysis

Business analysis includes:

- Total sales and profit
- Orders and customers
- Average Order Value
- Category and regional performance
- Monthly sales trends
- Top products and customers
- Loss-making products
- Discount and profitability analysis

## Power BI Dashboard

Interactive dashboard development is in progress.

Planned dashboard pages:

1. Executive Sales Overview
2. Product & Customer Analysis
3. Regional & Discount Analysis

## How to Run This Project

### 1. Clone the repository

```bash
git clone https://github.com/sakethgundluru/Retail-Sales-Analytics.git
```

### 2. Navigate to the project

```bash
cd Retail-Sales-Analytics
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Python scripts

```bash
python python/data_inspection.py
python python/data_cleaning.py
python python/exploratory_analysis.py
```

### 5. Database Setup

- Install MySQL Server.
- Create the `retail_sales_db` database.
- Configure your MySQL credentials using environment variables.
- Run the SQL scripts in the `sql/` folder.

## Skills Demonstrated

Python | SQL | MySQL | Power BI | Data Cleaning | Data Analysis | Exploratory Data Analysis | Data Visualization | Business Intelligence | KPI Reporting | GitHub

## Author

**Gundluru Saketh**

Data Analyst | SQL | Python | Power BI | Excel

[LinkedIn](https://www.linkedin.com/in/gundluru-saketh)

[GitHub](https://github.com/sakethgundluru)

---

*This project demonstrates an end-to-end approach to converting raw retail data into actionable business insights.*