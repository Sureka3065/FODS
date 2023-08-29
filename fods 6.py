item_prices = [2.5, 3.0, 1.75, 4.5]
item_quantities = [3, 2, 4, 1]
discount_rate = 10  
tax_rate = 8 
total_cost_before_discounts = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))
total_discount_amount = total_cost_before_discounts * (discount_rate / 100)
total_cost_after_discounts = total_cost_before_discounts - total_discount_amount
total_tax_amount = total_cost_after_discounts * (tax_rate / 100)
final_total_cost = total_cost_after_discounts + total_tax_amount
print("Total Cost before discounts and taxes: $", total_cost_before_discounts)
print("Total Discount Amount: $", total_discount_amount)
print("Total Cost after discounts: $", total_cost_after_discounts)
print("Total Tax Amount: $", total_tax_amount)
print("Final Total Cost including taxes: $", final_total_cost)
