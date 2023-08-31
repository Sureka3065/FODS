import pandas as pd

stock_data = pd.read_csv("finance_data.csv")
# Calculate the daily price changes
stock_data['PriceChange'] = stock_data['ClosingPrice'].diff()

mean_change = stock_data['PriceChange'].mean()
std = stock_data['PriceChange'].std()

print("Stock Price Variability Analysis")
print(f"Mean Daily Price Change: {mean_change:.2f}")
print(f"Standard Deviation of Daily Price Changes: {std:.2f}")
#Determine the direction of stock movement
positive_changes = stock_data[stock_data['PriceChange'] > 0]['PriceChange'].count()
negative_changes = stock_data[stock_data['PriceChange'] < 0]['PriceChange'].count()

print("\nStock Movement Direction")
print(f"Days with Positive Price Change: {positive_changes}")
print(f"Days with Negative Price Change: {negative_changes}")

'''
sample output 
Stock Price Variability Analysis
--------------------------------
Mean Daily Price Change: 0.78
Standard Deviation of Daily Price Changes: 3.68

Stock Movement Direction
-------------------------
Days with Positive Price Change: 5
Days with Negative Price Change: 4
'''
