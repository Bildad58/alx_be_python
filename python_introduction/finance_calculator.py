x = float(input ("Enter your monthly income: "))
y = float(input ("Enter your total monthly expenses: "))

#monthlysavings
Monthly_savings = " x - y "

#Project Annual Savings
Projected_Savings = ('Monthly_Savings' * 12 + ('Monthly_Savings' * 12 * 0.05))

print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")