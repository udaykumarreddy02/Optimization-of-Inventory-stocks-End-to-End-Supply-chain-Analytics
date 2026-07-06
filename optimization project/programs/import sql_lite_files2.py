import sqlite3
import pandas as pd
import os

# Get the paths
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
data_folder = os.path.join(project_dir, 'data')
sql_folder = os.path.join(project_dir, 'sql')

print(f" Using database: {os.path.join(data_folder, 'optistock.db')}")

# Connect to database
db_path = os.path.join(data_folder, 'optistock.db')
conn = sqlite3.connect(db_path)
print(" Connected to OptiStock Database!")

# Function to run SQL queries
def run_query(filename):
    print(f"\n{'='*60}")
    print(f" Running Query: {filename}")
    print(f"{'='*60}")
    
    sql_file_path = os.path.join(sql_folder, filename)
    
    if not os.path.exists(sql_file_path):
        print(f" ERROR: Could not find {filename}")
        return
        
    with open(sql_file_path, 'r') as file:
        query = file.read()
        
    df = pd.read_sql_query(query, conn)
    print(df.to_string(index=False))

# Run all 3 queries
run_query('1_revenue_overview.sql')
run_query('2_dead_stock.sql')
run_query('3_stockout_risk.sql')

conn.close()
print("\n All SQL queries executed successfully!")