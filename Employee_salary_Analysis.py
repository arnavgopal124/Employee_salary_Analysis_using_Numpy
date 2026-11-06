import numpy as np

m = int(input("Enter No. of employee In Company:-"))

names = []

for i in range(m):
    name = input(f"Enter name of Employee {i+1}: ")
    names.append(name)

ID = []
for i in range(m):
    id = input(f"Enter ID of employee {i+1}: ")
    ID.append(id)

Department = []
for i in range(m):
    department = input(f"Enter Department Of Employee {i+1}: ")
    Department.append(department)

Salary = []
for i in range(m):
    salary = float(input(f"Enter Salary of Employee {i+1}: "))
    Salary.append(salary)


names = np.array(names)
ID = np.array(ID)
Department = np.array(Department)
Salary = np.array(Salary)

print("\nEmployee Names : " , names)
print("Employee ID : " , ID)
print("Departments : " , Department)
print("Saleries : ", Salary)

Total_salary_expenditure = np.sum(Salary , axis=0)
print("Total_salary_expenditure :- " , Total_salary_expenditure)

average_salary = np.mean(Salary , axis= 0)
print("Average Salary :- " , average_salary)

Highest_salary = np.argmax(Salary)
print("Highest Salary :- " , Salary[Highest_salary])
print("Name of employee who got highest salary :- " ,names[Highest_salary])

Lowest_salary = np.argmin(Salary)
print("Lowest Salary :- " , Salary[Lowest_salary])
print("Name of employee who got lowest salary :- " , names[Lowest_salary])

Condition = Salary > average_salary
Condition_name = names[Condition]
Condition_salary = Salary[Condition]
print("Employee who got Salary above average salary :- " , Condition_name)
print("Their Salaries :- " , Condition_salary)
print("Number of employees: " , np.sum(Condition))



rank_index = np.argsort(Salary)[::-1]
ranked_salary = Salary[rank_index]
ranked_names = np.array(names)[rank_index]
print("Name of Employee Salary wise rank :- " , ranked_names)
print("Salary according to rank :- " , ranked_salary)

condition_1 = Department == "IT"
condition_2 = Department == "HR"
condition_3 = Department == "Finance"
condition_4 = Department == "Marketing"
average_salary_IT = np.mean(Salary[condition_1])
average_salary_HR = np.mean(Salary[condition_2])
average_salary_Finance = np.mean(Salary[condition_3])
average_salary_Marketing = np.mean(Salary[condition_4])
print("Average Salary of IT :- " , average_salary_IT)
print("Average Salary of HR :- " , average_salary_HR)
print("Average Salary of Finance :- " , average_salary_Finance)
print("Average Salary of Marketing :- " , average_salary_Marketing)


condition = Salary > 40000
count = np.sum(condition)
print("Number of employees earning above ₹40,000:", count)
print("Employee names:", names[condition])
print("Employee salaries:", Salary[condition])

annual_salary = Salary * 12
print("Employee Names :- " , names)
print("Annual Salary :- " , annual_salary)


condition = Salary < 30000
count = np.sum(condition)
print("Number of employees earning below 30000:", count)
print("Employee names:", names[condition])
print("Employee salaries:", Salary[condition])

median_salary = np.median(Salary)
print("Median Salary of all employee :- " , median_salary)

standard_deviation = np.std(Salary)
print("Standard Deviation :- " , standard_deviation)

variance = np.var(Salary)
print("Variance :- " , variance)

print("\n" + "="*45)
print("       EMPLOYEE SALARY ANALYSIS")
print("="*45)

print("\nTotal Employees:", m)
print("Total Salary Expenditure:", Total_salary_expenditure)
print("Average Salary:", average_salary)
print("Median Salary:", median_salary)

print("\nHighest Paid Employee:", names[Highest_salary])
print("Highest Salary:", Salary[Highest_salary])

print("\nLowest Paid Employee:", names[Lowest_salary])
print("Lowest Salary:", Salary[Lowest_salary])


print("\nStandard Deviation:", standard_deviation)
print("Variance:", variance)

print("\nAnnual Salary:")

for i in range(m):
    print(f"{names[i]}: ₹{annual_salary[i]}")

print("\n" + "="*45)
print("             REPORT COMPLETE")
print("="*45)