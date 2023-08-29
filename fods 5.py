import numpy as np
fuel_efficiency = np.array([30.5, 25.8, 28.9, 32.1, 20.3, 22.7, 26.4, 29.8, 33.2, 27.1])
average_efficiency = np.mean(fuel_efficiency)
print("Average Fuel Efficiency:", average_efficiency)
model1_index = 0
model2_index = 1
model1_efficiency = fuel_efficiency[model1_index]
model2_efficiency = fuel_efficiency[model2_index]
percentage_improvement = ((model2_efficiency - model1_efficiency) / model1_efficiency) * 100
print("Percentage Improvement:", percentage_improvement)
