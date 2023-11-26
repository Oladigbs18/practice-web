# list of 10  names of employees in an organization
employee_name = ["Aaliyah", "Mary", "Peter", "Jane", "James", "Elizabeth", "Paul", "Jennifer", "Aisha", "Julie"]
# to split the employee names into two groups
sublist1 = employee_name[0:5]
sublist2 = employee_name[5:10]
# to add a new employee to sublist2
sublist2.append("Kriti Brown")
# to remove the second employee from sublist1
sublist1.remove("Mary")
# to merge the two sublists into one list
employee_name = sublist1 + sublist2
# list of the 10 employees' salaries
salaryList = [50000, 70000, 60000, 80000, 90000, 100000, 110000, 120000, 130000, 140000]
# to give a rise of 4% to every employee and update salaryList
updatedsalaryList = [salary * 1.04 for salary in salaryList]
# to sort salaryList and show 3 top salaries
first_3 = sorted(salaryList,reverse=True)[:3]
# to print all of our results
print("The employee names are: ", employee_name)
print("The employee salaries are: ", salaryList)
print("The updated salaries are: ", updatedsalaryList)
print("The top 3 salaries are: ", first_3)