from dotenv import load_dotenv
load_dotenv()
import os
import pandas as pd
import mysql.connector

# Read cleaned dataset
df = pd.read_csv("dataset/cleaned_data.csv")

# Connect to MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("MYSQL_PASSWORD"),
    database="retail_sales_db"
)

cursor = connection.cursor()

# Insert data
columns = [
    "Row ID", "Order ID", "Order Date", "Ship Date",
    "Ship Mode", "Customer ID", "Customer Name", "Segment",
    "Country", "City", "State", "Postal Code", "Region",
    "Product ID", "Category", "Sub-Category", "Product Name",
    "Sales", "Quantity", "Discount", "Profit"
]

column_names = ", ".join(f"`{col}`" for col in columns)
placeholders = ", ".join(["%s"] * len(columns))

sql = f"INSERT INTO orders ({column_names}) VALUES ({placeholders})"

# Convert dates and missing values
df["Order Date"] = pd.to_datetime(df["Order Date"]).dt.date
df["Ship Date"] = pd.to_datetime(df["Ship Date"]).dt.date
df = df.where(pd.notna(df), None)

records = [
    tuple(row)
    for row in df[columns].itertuples(index=False, name=None)
]

cursor.executemany(sql, records)
connection.commit()

print("Records inserted:", cursor.rowcount)

cursor.close()
connection.close()
