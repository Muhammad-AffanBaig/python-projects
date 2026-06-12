#Practice Question1(Calculation of Electricity Bill per slab)
units = int(input("Enter Units: "))
if(units>=0 and units<=100):
    bill = units*5
    print("Electricity Bill: ",bill)
elif(units>100 and units<201):
    bill = 100*5 + (units-100)*10
    print("Electricity Bill: ",bill)
else:
    bill = 100*5 + 100*10 + (units-200)*15
    print("Electricity Bill: ",bill)


