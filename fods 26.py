import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1400, 3], [1600, 4], [1800, 3], [2000, 4], [2200, 5]])
y = np.array([200000, 250000, 280000, 300000, 330000])

lin_reg = LinearRegression()

lin_reg.fit(X, y)

area = float(input("Enter area: "))
bedrooms = int(input("Enter no of bedrooms: "))

features = np.array([[area, bedrooms]])

predict_price = lin_reg.predict(features)

print(f"The predicted price of the new house is: {predict_price[0]:,.2f}")
