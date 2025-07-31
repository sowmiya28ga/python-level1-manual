print("sowmi supermarket")
print("No.33,Nerhu Street,Puducherry")
print("-------------------------------")
print("Bill Reciept")
print("-------------------------------")
sno=int(input("Enter The Serial No:"))
par=input("Enter The Particulars:")
rate=int(input("Enter The Rate:"))
qua=int(input("Enter The Quantity:"))
total=rate*qua
print("Total Amount Rs:",total)
gst=total*10/100
print("gst(10%):",gst)
paid=total+gst
print("Amount To Be Paid Rs :",paid)
