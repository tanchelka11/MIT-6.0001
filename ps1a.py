# how many months it will take to save for a down payment 
annual_salary = float(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = float(input("Enter the cost of your dream home:"))

portion_down_payment = 0.25*total_cost
r = 0.04
monthly_salary = annual_salary/12 
current_savings = 0
numMonths = 0

while portion_down_payment > current_savings:
    current_savings += monthly_salary*portion_saved + current_savings*r/12
    numMonths = numMonths + 1 
print ("Number of months:", numMonths)
