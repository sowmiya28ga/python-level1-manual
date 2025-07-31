print("Sowmi International [P]Ltd ")
print("No.22,Nagapura Dist,Bangalore")
print("-------------------------------")
print("Employee Pay Roll System")
print("-------------------------------")
id=int(input("Enter The Employee Id:"))
ename=input("Enter The Employee Name:")
sal=int(input("Enter The Salary:"))
print("Income")
bonas=sal*20/100
print("Bonas(20Percentage):",bonas)
overtime=sal*10/100
print("Overtime(10Percentage):",overtime)
travel=sal*5/100
print("Travel Allowance(5Percentage):",travel)
gross=sal+bonas+overtime+travel
print("GrossPay In Ruppess:",gross)
