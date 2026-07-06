SELECT 
    s.Region,
    p.Category,
    COUNT(DISTINCT s.Order_ID) AS Total_Orders,
    SUM(s.Quantity_Sold) AS Total_Units_Sold,
    ROUND(SUM(s.Total_Revenue), 2) AS Gross_Revenue,
    ROUND(SUM(s.Total_Revenue - (s.Quantity_Sold * p.Unit_Cost)), 2) AS Net_Profit
FROM sales s
JOIN inventory p ON s.Product_ID = p.Product_ID
GROUP BY s.Region, p.Category
ORDER BY Net_Profit DESC;