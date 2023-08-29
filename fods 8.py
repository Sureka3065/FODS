import pandas as pd
data = {
    'product_name': ['Product A', 'Product B','Product E', 'Product A', 'Product C', 'Product B','Product C','Product D'],
    'quantity_sold': [3, 2, 1,6,3, 4, 3, 2]
}
sales_data = pd.DataFrame(data)
product_sales_summary = sales_data.groupby('product_name')['quantity_sold'].sum()
sorted_product_sales = product_sales_summary.sort_values(ascending=False)
top_5_products = sorted_product_sales.head(5)
print("Top 5 products sold the most in the past month:")
print(top_5_products)
