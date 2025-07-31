print("Government of Tamilnadu")
print("Electricity Board")
print("-----------------------")
no=input("Enter The EB.No:")
str=input("Enter The Customer Name:")
no1=int(input("Reading For Previous Month:"))
no2=int(input("Reading For Current Month:"))
total=no2-no1
print("Total Unit Consumed:",total)
paid=total*5
print("Amount To Be Paid:",paid)
