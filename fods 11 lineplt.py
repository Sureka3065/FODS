import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales_values = [1000, 1500, 1200, 1800, 2000, 1600]

plt.figure(figsize=(10, 6))  
plt.plot(months, sales_values, marker='o', linestyle='-')

plt.title('Monthly Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Value')
plt.grid(True)

plt.show()
