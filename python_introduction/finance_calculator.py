# Financial Calculator
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses

projected_annual_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 12)
print(f"Projected savings after one year, with interest is : {projected_annual_savings}")
#
