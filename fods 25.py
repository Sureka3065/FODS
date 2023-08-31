import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
x = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

dt= DecisionTreeClassifier()

dt.fit(X_train, y_train)

sepal_length = float(input("Enter sepal length: "))
sepal_width = float(input("Enter sepal width: "))
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))

features = np.array([[sepal_length, sepal_width,
                                 petal_length, petal_width]])

predicted_species = dt.predict(features)

species_names = ['Setosa', 'Versicolor', 'Virginica']
predicted_species_name = species_names[predicted_species[0]]

print(f"The predicted species of the new flower is: {predicted_species_name}")


