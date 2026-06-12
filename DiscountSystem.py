#Practice Question4(Discount System)
amount = int(input("Enter shopping amount : "))
if(amount<1000):
    discount = 0
    bill = amount - discount
    print("Total Bill :",bill) 
elif(amount >=1000 and amount <3000):
    discount = 0.05*amount
    bill = amount - discount
    print("Total Bill :",bill) 
elif(amount >=3000 and amount <5000):
    discount = 0.10*amount
    bill = amount - discount
    print("Total Bill :",bill)     
else:
    discount = 0.15*amount
    bill = amount - discount
    print("Total Bill :",bill) 