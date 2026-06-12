#Practice Question2(Triangle Type Checker)
a = int(input("Enter side one: "))
b = int(input("Enter side two: "))
c = int(input("Enter side three: "))
if(a == b and b == c):
    print("Equilateral Triangle")
elif( a == b or b==c or a ==c):
    print("Isosceles Triangle")
elif(a != b and b !=c and c!= a):
    print("Scalene Triangle")