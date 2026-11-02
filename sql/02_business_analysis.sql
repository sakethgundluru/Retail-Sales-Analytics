
USE retail_sales_db;

-- 1. Total Sales
SELECT ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders;

-- 2. Total Profit
SELECT ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders;

-- 3. Total Orders
SELECT COUNT(DISTINCT `Order ID`) AS Total_Orders
FROM orders;

-- 4. Total Customers
SELECT COUNT(DISTINCT `Customer ID`) AS Total_Customers
FROM orders;

-- 5. Average Order Value
SELECT ROUND(
    SUM(Sales) / COUNT(DISTINCT `Order ID`), 2
) AS Average_Order_Value
FROM orders;

-- 6. Sales by Category
SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC;

-- 7. Profit by Region
SELECT
    Region,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Region
ORDER BY Total_Profit DESC;

-- 8. Sales by Segment
SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Segment
ORDER BY Total_Sales DESC;

-- 9. Monthly Sales
SELECT
    DATE_FORMAT(`Order Date`, '%Y-%m') AS Sales_Month,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Sales_Month
ORDER BY Sales_Month;

-- 10. Top 10 Products by Sales
SELECT
    `Product Name`,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY `Product Name`
ORDER BY Total_Sales DESC
LIMIT 10;

-- 11. Top 10 Customers by Sales
SELECT
    `Customer Name`,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;


-- 12. Customers Generating the Highest Profit
SELECT
    `Customer Name`,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY `Customer Name`
ORDER BY Total_Profit DESC
LIMIT 10;


-- 13. Loss-Making Products
SELECT
    `Product Name`,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY `Product Name`
HAVING SUM(Profit) < 0
ORDER BY Total_Profit ASC
LIMIT 10;


-- 14. Profit Margin by Category
SELECT
    Category,
    ROUND(SUM(Profit), 2) AS Total_Profit,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit) / SUM(Sales) * 100, 2) AS Profit_Margin
FROM orders
GROUP BY Category
ORDER BY Profit_Margin DESC;


-- 15. Sales by State
SELECT
    State,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY State
ORDER BY Total_Sales DESC
LIMIT 10;


-- 16. Discount Impact on Profit
SELECT
    Discount,
    COUNT(*) AS Total_Records,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Discount
ORDER BY Discount;


-- 17. Sales by Shipping Mode
SELECT
    `Ship Mode`,
    COUNT(DISTINCT `Order ID`) AS Total_Orders,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY `Ship Mode`
ORDER BY Total_Sales DESC;


-- 18. Yearly Sales Performance
SELECT
    YEAR(`Order Date`) AS Sales_Year,
    ROUND(SUM(Sales), 2) AS Total_Sales,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Sales_Year
ORDER BY Sales_Year;


-- 19. Monthly Profit Trend
SELECT
    DATE_FORMAT(`Order Date`, '%Y-%m') AS Sales_Month,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Sales_Month
ORDER BY Sales_Month;


-- 20. Orders with Negative Profit
SELECT
    `Order ID`,
    `Customer Name`,
    `Product Name`,
    ROUND(Sales, 2) AS Sales,
    ROUND(Profit, 2) AS Profit,
    Discount
FROM orders
WHERE Profit < 0
ORDER BY Profit ASC
LIMIT 20;
