Monthly_income = input ("Enter your monthly income: ")
Monthly_expenses= input ("Enter your total monthly expenses: ")

#monthlysavings
Monthly_savings = Monthly_income + Monthly_expenses

#Project Annual Savings
Projected_Savings = float('Monthly_Savings' * 12 + ('Monthly_Savings' * 12 * 4))

print(f"Your monthly savings are ${Monthly_savings: }.")
print(f"Projected savings after one year, with interest, is: ${Monthly_savings: }.")