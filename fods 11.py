import matplotlib.pyplot as plt 
months=['jan','feb','mar','apr','may']
sales=[10000,12000,8000,15000,11000]

plt.plot(months,sales,marker='o')
plt.xlabel('months')
plt.ylabel('sales')
plt.title('monthly sales prediction')
plt.grid(True)
plt.show()
print()

plt.scatter(months,sales)
plt.xlabel('months')
plt.ylabel('sales')
plt.title('monthly sales prediction')
plt.grid(True)
-plt.show()

plt.bar(months,sales)
plt.xlabel('months')
plt.ylabel('sales')
plt.title('monthly sales prediction')
plt.grid(True)
plt.show()
