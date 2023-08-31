import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import export_text
X = np.array([
    [50000, 3, 0],  # Mileage: 50000, Age: 3, Brand: 0 (Toyota)
    [80000, 5, 1],  # Mileage: 80000, Age: 5, Brand: 1 (Honda)
    [30000, 2, 0],  # Mileage: 30000, Age: 2, Brand: 0 (Toyota)
    [60000, 4, 2]   # Mileage: 60000, Age: 4, Brand: 2 (Ford)
])
# target prices
y = np.array([15000, 12000, 18000, 10000])

model = DecisionTreeRegressor()
model.fit(X, y)
# Input feature values for the new car
features = np.array([33000, 2, 0])  # Mileage: 33000, Age: 2, Brand: 0 (Honda)
predicted_price = model.predict([features])[0]
print(f"Predicted price for the new car: ${predicted_price:.2f}")

decision_path = model.decision_path([features])
print("\nDecision path:")
print(export_text(model, feature_names=['Mileage', 'Age', 'Brand']))


'''
sample output 
Predicted price for the new car: $18000.00

Decision path:
|--- Brand <= 0.50
|   |--- Age <= 2.50
|   |   |--- value: [18000.00]
|   |--- Age >  2.50
|   |   |--- value: [15000.00]
|--- Brand >  0.50
|   |--- Mileage <= 70000.00
|   |   |--- value: [10000.00]
|   |--- Mileage >  70000.00
|   |   |--- value: [12000.00]
'''
