import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Sample dataset (features and labels)
x = np.array([[100, 24], [200, 12], [50, 6], [300, 36], [150, 18], [80, 9]])
y = np.array([0, 1, 0, 1, 0, 1])  # 0: Not Churned, 1: Churned

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Create a Logistic Regression classifier
logreg = LogisticRegression()

# Fit the classifier on the training data
logreg.fit(X_train, y_train)

# Input features for the new customer
min = int(input("Enter usage minutes: "))
duration = int(input("Enter contract duration: "))

features = np.array([[min, duration]])

# Predict whether the new customer will churn or not
predict = logreg.predict(features)

if predict[0] == 0:
    print("The new customer is not likely to churn.")
else:
    print("The new customer is likely to churn.")


'''
sample output 
Enter usage minutes: 180
Enter contract duration: 20
The new customer is likely to churn.
'''
