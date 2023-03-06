# task no 1
"""create a password baed system for mobile. set the password as "pf-23"
 if user enter the correct password then display this massage: you are successful login.
 otherwise display this massage you entered the wrong password."""
from random import choice

password = str(input("enter your password:"))
if password == "PF-23":
    print('your successfully login')
else:
    print('you are entered a wrong password')
    # task no 2
'''create a login form.ask user to enter his/her mobile number and password.set the mobile# as "03073514050" and
 password as "pf-23" if user enter the correct password then display this massage: yor are succesfully login.
 otherwise display this massage: you are entered a wrong email or password.'''
a = input("enter your mobile number:")
b = input("enter your password:")
if a == "03073514050":
    var = b == "pf-23"
    print("you are successfully login")
else:
    print("you are entered wrong email or password")
    # task no 3
    '''write a program to take input marks of five subjects from user python,java,c++,maths and DSA.
    calculate the percentage and grade according to the following:
    percentage>=90%:grade A
    percentage>=80%:grade B
    percentage>=70%:grade C
    percentage>=60%:grade D
    percentage>=50%:grade E
    percentage>=40%:grade F.'''

    python = int(input("python marks:"))
    java = int(input("java marks:"))
    cplusplus = int(input("c++ marks:"))
    maths = int(input("maths marks:"))
    DSA = int(input("DSA marks:"))
    print()
    total = python + java + cplusplus + maths + DSA
    print("total marks:", total)
    percentage = (total / 500) * 100
    print("percentage=", percentage, "%")
    percentage = float(input("enter your marks percentage %:"))
    if percentage >= 90:
        print("grade A")
    elif percentage >= 80:
        print("grade B")
    elif percentage >= 70:
        print("grade C")
    elif percentage >= 60:
        print("grade D")
    elif percentage >= 50:
        print("grade E")
    elif percentage >= 40:
        print("grade F")
    # task no 4
    '''write a program to take input any alphabet and check whether it is
    vowel or consonant.'''
    alphabet = input("enter any alphabet:")
    if alphabet in 'a,e,i,o,u,A,E,I,O,U':
        print(alphabet, "is a vowel")
    elif alphabet in 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z,B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,W,X,Y,Z':
        print(alphabet, "is consonant")
    else:
        print("sorry,this is not an alphabet")

        # task no 5
        '''write a program to check whether the triangle is equilateral,isosceles or scalene triangle.
        (study about how to check whether the triangle is equilteral etc
         and apply conditional statements by taking the side/angles from user.'''
        print("enter the lenghts of sides of triangle")
        a = int(input('value of a:'))
        b = int(input('value of b:'))
        c = int(input('value of c:'))
        if a == b == c:
            print('it is equilateral triangle')
        elif a == b or b == c or c == a:
            print('it is the isosceles triangle')
        else:
            print('it is scalene trianlr')

# task no 6
'''if the user age is greater then 13 years create its account else just say that you are 
not eligible to create an id on this platform.try after he turn out to be 13 years.'''
name = input("enter your name:")
email = input("enter your email:")
password = input("enter your password:")
age = float(input("enter your age:"))
gender = input("enter your gender:")
var = id == 13 - age
if age > 13:
    print('you are eligible')
else:
    print('you are not eligible try after')
    print(var)

# task no 7
'''design a console bsed application for converting different currency.
(currency shouud includ euro,dollar,pkr,inr and yen.)'''
print('welcome to currency converter')
pkr = float(input("enter pkr currency to convert:"))
print('press 1 for change your into euro /npress 2 for doller/nprees 3 for inr/npress 4 for yen')
if choice == 1:
    print(pkr * .0034)
elif choice == 2:
    print(pkr * .0036)
elif choice == 3:
    print(pkr * .29)
elif choice == 4:
    print(pkr * 0.49)
# task no 8
'''design an atm machine that his 3 main features
1) deposit
2) withdraw
3) check balance.'''
cb = 5000
db = int(input("enter deposit amount:"))
wb = int(input("enter withdrawa amount:"))
print("press 1 for deposit/npress 2 for withdraw(if it exceed from current balance then deliver a assage that you"
      " have enough balance)/npress 3 for cheak balance")
if choice == 1:
    print(cb + db)
elif choice == 2:
    print(cb < wb)
    print("you don't have enough balance")
elif choice == 2:
    print(cb)
# task no 9
'''gamexone offering a new position in their software house,you selected for an interview.
the criteria for selecting your position either as a programmer or management person is that if you have 4.5 years
of experience in game development then you will be hired as a game developer otherwise they will shortlisted you for
management.'''
youex = float(input("enter your experience:"))
if youex >= 4.5:
    print("congratulation you are hired is a game developer")
elif youex < 4.5:
    print("you are shortlisted for management.")
# task no 10
'''design a career counseling system for students to select their field.
you are requested to think like a counsellor
 who guide students to choose career according interest and passion.'''
interest = input("enter you interest or hobbies:")
var1 = "darwing,management,"
var2 = "logical,interest in programming,problum solving,technologies"
var3 = "interested n bio sciences and development of humanity "
if interest == var1:
    print("arts is best for you")
elif interest == var2:
    print("engineering is for you")
elif interest == var3:
    print("medical is your future")
