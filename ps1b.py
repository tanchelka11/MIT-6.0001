annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))

portion_down_payment = 0.25*total_cost
r = 0.04
current_savings = 0
numMonths = 0

while current_savings<portion_down_payment:
    print(annual_salary)
    monthly_salary = annual_salary/12 
    current_savings += monthly_salary*portion_saved + current_savings*r/12
    numMonths +=1 
    #factoring in the raise every 6 months 
    if numMonths%6==0: 
        annual_salary += annual_salary*semi_annual_raise

print ("Number of months:", numMonths)
