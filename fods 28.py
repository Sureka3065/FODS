import numpy as np
from sklearn.cluster import KMeans

# Sample customer data (features)
customer_data = np.array([[5.1, 3.5, 1.4, 0.2],   # Feature 1: Sepal length, Sepal width, Petal length, Petal width
                          [4.9, 3.0, 1.4, 0.2],
                          [5.8, 2.6, 4.0, 1.2],
                          [6.6, 3.0, 4.4, 1.4],
                          [7.3, 2.9, 6.3, 1.8]])

# Create a K-Means clustering model with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Fit the model on the customer data
kmeans.fit(customer_data)

new_customer_features = np.array([[6.2, 3.1, 5.2, 2.3]])
predicted_segment = kmeans.predict(new_customer_features)

print(f"The predicted segment for the new customer is: {predicted_segment[0]}")
