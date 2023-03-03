
#task no 1 how to make simople calculator
'''list of operation
1. addition
2. subtraction
3. multiplicaton
4. devesion
5. floor devesion'''
num1=float(input("enter first number:"))
num2=float(input("enter second number:"))
print("press 1 for addition /npress 2 for subtraction /npress 3 for muliplication /npress 4 for devesion /npress 5 for floor division")
choice=int(input("enter your choice from 1 to 5:"))
if choice==1:
    print(num1+num2)
elif choice==2:
    print(num1-num2)
elif choice ==3:
    print(num1*num2)
elif choice==4:
    print(num1/num2)
elif choice==5:
    print(num1//num2)
else:
    print("invalid input")

    '''task no 2 how to cheak two number
     whether thay are equal or no'''
    num1 = float(input("enter first number:"))
    num2 = float(input("enter second number:"))
    print(num1==num2) #if equal
    print(num1!=num2)#if not equal

    #task no 3 design a system that culculatess the area of a plot
    l=float(int('enter the length of plot:'))
    w=float(int('enter the width of plot:'))
    #as we know that area==l*w so
    a=l*w
    print(a)

    #task no 4 design a BMI system
    x=float (input("enter your hight in m:"))
    y=float(input("enter your weight:"))
    z=y/x**2
    print("your body mass index is:",z)

    #task no 5
    '''create a program to convert
    user weight in kg into pounds
    hight into inches
    radian to degree'''
    kg=float(input("enter kg:"))
    pounds=kg*2.2046
    print(pounds)

    heightinfeet =float(input("enter your height in feet:"))
    inches=12*heightinfeet
    print(inches)

    radian=float(input("enter radian:"))
    deg=57.296*radian
    print(radian)

    '''task no 5 write a perogram to calculate the 
    area of a trapezoid
    area of a parallelogram
    calculate the volume and area of a cylinder'''
    base1 = float(input("pleas enter the first base of a trapezoid:"))
    base2 = float(input("pleas enter the secnd base of a trapezoid:"))
    height = float(input("pleas enter the height of a trapezoid:"))
    # calculate the area
    areaoftrapezoid=0.5*(base1+base2)
    print(areaoftrapezoid)
    b = float(input("pleas enter the base of a parallelogran:"))
    h = float(input("pleas enter the hieght of a parallelogram:"))

    areaofparallelogram=b*h
    print(areaofparallelogram)
    # calculate the volume and area of a cylinder
    r=float(input("pleas enter the radius of cylinder:"))
    h=float(input("pleas enter the height of cylinder:"))
    volumeofcylinder=3.14156*r*r*h
    print(volumeofcylinder)







