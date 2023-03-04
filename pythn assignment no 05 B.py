#task no 1
'''ask user to enter his email that shoud have @gmail.com in the end if the user enter the email that dosenot contain @gmail.com
then disply a massage that you are not providing accurate email'''
usergmail=input("plese enter your gmail:")
print(usergmail.endswith("@gmail.com"))

#task no 2
username=input("user name")
print(username.title())
print("i hope you are fine,let me know how can i help you!")
print("press 1 for yes /npress 2 for no")
choice=input("enter your choice 1 or 2:")
if choice==1:
    print("share your problum with us")
    print("thanks for feedback,we will resolve your problum")
elif choice==2:
    print("okay!good to see you,stay conected")
#task no 3
'''ask user to enter url that shoud start with http://www.
(user url) and then convert into user url.com'''
userurl=input("enter user url:")
print(userurl.startswith("http://www."))
print(userurl.replace("url.com"))
#task no 4
'''ask user to set your password that shoud
 contains numbers and alphabets'''
userp=input("enter your password:")
print(userp.isalnum())
#task no 5
'''ask user to enter his full name with cost or father name
after then make a first and last name fome this information'''
userfullname=str(input("enter your full name with cost or father name:"))
print(userfullname.find("first name"))
print(userfullname.find("last name"))
