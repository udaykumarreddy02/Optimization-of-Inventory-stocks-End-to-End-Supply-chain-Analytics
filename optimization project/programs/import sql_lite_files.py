import sqlite3
import pandas as pd
import os

# Get the path to the data folder
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
data_folder = os.path.join(project_dir, 'data')

print(f"Loading data from: {data_folder}")

# 1. Connect to the database (creates it if it doesn't exist)
db_path = os.path.join(data_folder, 'optistock.db')
conn = sqlite3.connect(db_path)
print("Connected to SQLite Database!")

# 2. Load the CSVs into Pandas
df_inventory = pd.read_csv(os.path.join(data_folder, 'raw_inventory.csv'))
df_sales = pd.read_csv(os.path.join(data_folder, 'raw_sales.csv'))

# 3. Push the data into SQL tables
df_inventory.to_sql('inventory', conn, if_exists='replace', index=False)
df_sales.to_sql('sales', conn, if_exists='replace', index=False)

print("Data successfully loaded into 'inventory' and 'sales' tables!")

# 4. Verify the data
cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM inventory;")
inv_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM sales;")
sales_count = cursor.fetchone()[0]

print(f"Verification: {inv_count} rows in Inventory, {sales_count} rows in Sales.")
conn.close()
print("Database is ready!")