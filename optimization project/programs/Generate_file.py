import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# SMART PATH DETECTION - Automatically finds the correct folder
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
data_folder = os.path.join(project_dir, 'data')

# Create the data folder if it doesn't exist
os.makedirs(data_folder, exist_ok=True)

print(f" Saving files to: {data_folder}")

# ==========================================
# 1. GENERATE INVENTORY DATA
# ==========================================
print("Generating Inventory Data...")
products = {
    'Product_ID': [f'P{str(i).zfill(3)}' for i in range(1, 51)],
    'Product_Name': [f'Product_{i}' for i in range(1, 51)],
    'Category': np.random.choice(['Electronics', 'Home Appliances', 'Audio', 'Wearables'], 50),
    'Unit_Cost': np.random.uniform(20.0, 500.0, 50).round(2)
}
df_inventory = pd.DataFrame(products)
df_inventory['Stock_Quantity'] = np.random.randint(0, 500, 50)
df_inventory['Reorder_Level'] = np.random.randint(50, 150, 50)
df_inventory['Warehouse_Region'] = np.random.choice(['North', 'South', 'East', 'West'], 50)

# Save
csv_path = os.path.join(data_folder, 'raw_inventory.csv')
df_inventory.to_csv(csv_path, index=False)
print(f"Saved: {csv_path}")

# ==========================================
# 2. GENERATE SALES DATA
# ==========================================
print("Generating Sales Data...")
num_sales = 10000
start_date = datetime(2025, 1, 1)
end_date = datetime(2026, 6, 24)

sales_data = {
    'Order_ID': [f'ORD{str(i).zfill(6)}' for i in range(1, num_sales + 1)],
    'Order_Date': [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(num_sales)],
    'Customer_ID': [f'CUST{str(random.randint(1000, 9999))}' for _ in range(num_sales)],
    'Product_ID': np.random.choice(df_inventory['Product_ID'], num_sales),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], num_sales),
    'Quantity_Sold': np.random.randint(1, 10, num_sales)
}

df_sales = pd.DataFrame(sales_data)
df_sales = df_sales.merge(df_inventory[['Product_ID', 'Unit_Cost']], on='Product_ID', how='left')
df_sales['Unit_Price'] = (df_sales['Unit_Cost'] * np.random.uniform(1.3, 2.0, num_sales)).round(2)
df_sales['Total_Revenue'] = (df_sales['Quantity_Sold'] * df_sales['Unit_Price']).round(2)
df_sales = df_sales.sort_values('Order_Date')

# Save
csv_path = os.path.join(data_folder, 'raw_sales.csv')
df_sales.to_csv(csv_path, index=False)
print(f"Saved: {csv_path}")
print(" Phase 1 Complete!")