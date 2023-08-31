import numpy as np
import pandas as pd
import scipy.stats as stats


data = {'concentration': [4.6, 3.8, 4.2, 4.0, 4.3, 3.9, 4.1, 4.4, 3.7, 4.5]}

df = pd.DataFrame(data)

size = 5
c_lvl = 0.95
desired_precision = 0.1

mean = df['concentration'][:size].mean()
std = df['concentration'][:size].std(ddof=1)

error = std / np.sqrt(size)

t_score = stats.t.ppf(1 - (1 - c_lvl) / 2, df=size - 1)

mof = t_score * error

lower_bound = mean - mof
upper_bound = mean + mof

requiredsize = ((t_score * std) / desired_precision) ** 2

print("\nPoint Estimation:")
print(f"Sample Mean: {mean:.4f}")
print(f"Sample Standard Deviation: {std:.4f}")

print("\nConfidence Interval:")
print(f"Lower Bound: {lower_bound:.4f}")
print(f"Upper Bound: {upper_bound:.4f}")
print(f"Confidence Level: {c_lvl * 100:.2f}%")

print("\nRequired Sample Size for Desired Precision:")
print(f"Required Sample Size: {int(np.ceil(requiredsize))}")


