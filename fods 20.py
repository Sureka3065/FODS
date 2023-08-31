import scipy.stats as stats

conversion_rate_a = [0.12, 0.10, 0.14, 0.11, 0.09, 0.13, 0.08, 0.10, 0.12, 0.11]
conversion_rate_b = [0.15, 0.16, 0.14, 0.17, 0.13, 0.18, 0.14, 0.16, 0.15, 0.14]

t_statistic, p_value = stats.ttest_ind(conversion_rate_a, conversion_rate_b)

alpha = 0.05

if p_value < alpha:
    result = "statistically significant"
else:
    result = "not statistically significant"

print(f"The t-statistic is: {t_statistic:.4f}")
print(f"The p-value is: {p_value:.4f}")
print(f"Conclusion: There is a {result} difference in mean conversion rates between designs A and B.")



