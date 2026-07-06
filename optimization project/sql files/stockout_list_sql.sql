SELECT 
    p.Product_ID,
    p.Product_Name,
    s.Region,
    SUM(s.Quantity_Sold) AS Total_Sold,
    p.Stock_Quantity AS Current_Stock,
    p.Reorder_Level,
    CASE 
        WHEN p.Stock_Quantity <= p.Reorder_Level THEN 'URGENT: REORDER NOW'
        WHEN p.Stock_Quantity < (p.Reorder_Level * 1.5) THEN 'WARNING: LOW STOCK'
        ELSE 'Safe'
    END AS Restock_Status
FROM sales s
JOIN inventory p ON s.Product_ID = p.Product_ID
GROUP BY p.Product_ID, p.Product_Name, s.Region, p.Stock_Quantity, p.Reorder_Level
HAVING Restock_Status != 'Safe'
ORDER BY Total_Sold DESC;