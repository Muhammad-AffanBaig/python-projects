#Students marks manager
markslist = []
for i in range(5):
    marks = int(input("Student marks: "))
    markslist.append(marks)
sum = 0
Highest = markslist[0]
lowest = markslist[0]
countP = 0
countF = 0
for mark in markslist:
    sum += mark 
    if mark > Highest:
        Highest = mark
    if mark <lowest:
        lowest = mark
    if mark>=50:
        countP +=1
    else:
        countF +=1        
print("Highest:",Highest)
print("Lowest:",lowest)            
print("Sum:",sum)
print("Average:",sum/len(markslist))
# menu driven program
items = []
print("1.Add Items")
print("2.Remove Item")
print("3.Show List")
print("4.Exit")
while(True):
    digit = int(input("Enter the Choice: "))
    if digit == 1:
        addItem = input("Enter item to add: ")
        items.append(addItem)
    elif digit==2:
        removeItem = input("Enter item to remove: ")
        items.remove(removeItem)
    elif digit ==3:
        print(items)
    elif digit ==4:
        break
    else:
        print("invalid input")
