# analyzer.py
import pandas as pd
import json
import os

from helpers import calculate_total, format_currency

# Read data
df = pd.read_csv('data/sales.csv')

# Calculate total for each row
totals = []
for index, row in df.iterrows():
    total = calculate_total(row['quantity'], row['price'])
    totals.append(total)

# Add totals to our data
df['total'] = totals

# Display with formatted totals
print("Sales Data:")
for index, row in df.iterrows():
    formatted_total = format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# Show grand total
grand_total = df['total'].sum()
formatted_grand_total = format_currency(grand_total)
print(f"\n Grand Total: {formatted_grand_total}")

# Read the CSV file
df = pd.read_csv('data/sales.csv')
print("CSV Data:")
print(df)
print(f"\nShape: {df.shape[0]} rows, {df.shape[1]} columns")

# Quick operation: calculate total for each row
df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# Create output directory
os.makedirs('output', exist_ok=True)

# Save as different formats
# 1. JSON format (good for web APIs)
df.to_json('output/sales_data.json', orient='records', indent=2)

# 2. Excel format (good for sharing)
df.to_excel('output/sales_data.xlsx', index=False)

# 3. Updated CSV (with our new total column)
df.to_csv('output/sales_with_totals.csv', index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx") 
print("- output/sales_with_totals.csv")

# JSON - Great for APIs and web applications
# {
  # "date": "2024-01-01",
  # "product": "Laptop",
  # "quantity": 2,
  # "price": 999.99
# }

# CSV - Simple, universal, good for data analysis
# date,product,quantity,price
# 2024-01-01,Laptop,2,999.99

# Excel - Feature-rich, good for business users
# (Binary format with formatting, formulas, etc.)