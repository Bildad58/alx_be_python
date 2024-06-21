Monthly_income = float(input ("Enter your monthly income: "))
Monthly_expenses= float(input ("Enter your total monthly expenses: "))

#monthlysavings
Monthly_savings = Monthly_income - Monthly_expenses

#Project Annual Savings
Projected_Savings = ('Monthly_Savings' * 12 + ('Monthly_Savings' * 12 * 0.05))

print(f"Your monthly savings are ${Monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${Monthly_savings:.2f}.")