#task no 1
'''ask user to enter his email that shoud have @gmail.com in the end if the user enter the email that dosenot contain @gmail.com
then disply a massage that you are not providing accurate email'''
usergmail=input("plese enter your gmail:")
print(usergmail.endswith("@gmail.com"))

#task no 3
'''ask user to enter url that shoud start with http://www.
(user url) and then convert into user url.com'''
userurl=input("enter user url:")
print(userurl.startswith("http://www."))
#task no 4
'''ask user to set your password that shoud
 contains numbers and alphabets'''
userp=input("enter your password:")
print(userp.isalnum())
#task no 5
'''ask user to enter his full name with cost or father name
after then make a first and last name fome this information'''
userfullname=str(input("enter your full name with cost or father name:"))
print("userfullname")
