SELECT 
    p.Product_ID,
    p.Product_Name,
    p.Category,
    p.Warehouse_Region,
    p.Stock_Quantity AS Current_Stock,
    COALESCE(SUM(s.Quantity_Sold), 0) AS Total_Sold,
    CASE 
        WHEN COALESCE(SUM(s.Quantity_Sold), 0) = 0 THEN 'CRITICAL: ZERO SALES'
        WHEN p.Stock_Quantity > (COALESCE(SUM(s.Quantity_Sold), 0) * 5) THEN 'WARNING: OVERSTOCKED'
        ELSE 'Healthy'
    END AS Stock_Health_Status
FROM inventory p
LEFT JOIN sales s ON p.Product_ID = s.Product_ID
GROUP BY p.Product_ID, p.Product_Name, p.Category, p.Warehouse_Region, p.Stock_Quantity
HAVING Stock_Health_Status != 'Healthy'
ORDER BY Current_Stock DESC;