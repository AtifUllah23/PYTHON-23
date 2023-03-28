# task no 1
'''write python program for using nested loo access each individual element from list with in the list
 [['Mehak' 'Aysha' 'Sadia']['ali' 'ahmad' 'saif' ]]'''
my_list = [['Mehak', 'Aysha', 'Sadia'], ['ali', 'ahmad', 'saif']]

for inner_list in my_list:
    for element in inner_list:
        print(element)

# task no 2
'''print the following pattern

*
** 
*** 
**** 
***** 
**** 
*** 
** 
*
Here's the Python code to print the pattern above:'''
for i in range(1, 6):
    print("*" * i)
for i in range(4, 0, -1):
    print("*" * i)

# task no 3
'''design a program for ATM machine, machine has four different options 
1 check balance
2 withdraw 
3 deposit 
4 exit process your ATM instructions until your user press an exit button.'''
balance = 1000  # initial account balance

while True:
    # Display menu options
    print("ATM Machine Menu:")
    print("1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    # Get user input for menu option
    option = int(input("Enter your choice (1-4): "))

    # Execute user's chosen option
    if option == 1:
        print(f"Your account balance is: {balance}")
    elif option == 2:
        withdraw_amount = float(input("Enter amount to withdraw: "))
        if withdraw_amount > balance:
            print("Insufficient balance")
        else:
            balance -= withdraw_amount
            print(f"Withdrawal of {withdraw_amount} successful")
    elif option == 3:
        deposit_amount = float(input("Enter amount to deposit: "))
        balance += deposit_amount
        print(f"Deposit of {deposit_amount} successful")
    elif option == 4:
        print("Thank you for using our ATM")
        break
    else:
        print("Invalid option, please try again")

# task no 4
'''write python program to design a control application for your home appliances,
your task is to control your room appliances like TV, fans, bulb lights.. if you press the on button of the room's bulb
it will turn on, if you press the off button it will turn off, this system will continuously showing your options for on
and off your home appliances once user press the exit button then the program will be terminate.'''
# Initialize appliance status variables
tv_on = False
fan_on = False
bulb_on = False

while True:
    # Display menu options
    print("Home Appliance Control Menu:")
    print("1. Turn TV on/off")
    print("2. Turn fan on/off")
    print("3. Turn bulb on/off")
    print("4. Exit")

    # Get user input for menu option
    option = int(input("Enter your choice (1-4): "))

    # Execute user's chosen option
    if option == 1:
        if tv_on:
            tv_on = False
            print("TV turned off")
        else:
            tv_on = True
            print("TV turned on")
    elif option == 2:
        if fan_on:
            fan_on = False
            print("Fan turned off")
        else:
            fan_on = True
            print("Fan turned on")
    elif option == 3:
        if bulb_on:
            bulb_on = False
            print("Bulb turned off")
        else:
            bulb_on = True
            print("Bulb turned on")
    elif option == 4:
        print("Thank you for using our home appliance control system")
        break
    else:
        print("Invalid option, please try again")

# task no 5
'''write a program to design a control mechanism of ac/split for automatically adjust 
the AC setting once the room temperature is so cold. once the temperature of the room decreases to 15 degree 
then the compressor of AC switch off and when the temperature is about 20 degree then automatically 
switch on the compressor to obtain desert whole temperature. 
( remember we don't have sensor for getting the temperature of room just ask from the user user is a thermoset ). 
this process will be continue while the AC is on.'''
# Initialize AC status variables
ac_on = False
compressor_on = False

while True:
    # Get user input for desired room temperature
    temp = int(input("Enter the desired room temperature: "))

    # Check if temperature is within acceptable range
    if temp < 15 or temp > 30:
        print("Invalid temperature entered, please try again")
        continue

    # Check if AC is currently on
    if ac_on:
        # Check if temperature is too low
        if temp < 20:
            compressor_on = False
            print("Compressor turned off")
        # Check if temperature is too high
        elif temp > 25:
            compressor_on = True
            print("Compressor turned on")
        else:
            print("Temperature is within range")
    else:
        # Check if temperature is too high to turn on AC
        if temp > 25:
            print("Temperature too high, cannot turn on AC")
        else:
            ac_on = True
            compressor_on = True
            print("AC turned on, compressor turned on")

    # Check if user wants to turn off AC
    off = input("Enter 'off' to turn off the AC: ")
    if off.lower() == 'off':
        ac_on = False
        compressor_on = False
        print("AC turned off")
        break

# task no 6
# design a program for creating a clock.
import time

while True:
    # Get the current time
    current_time = time.strftime("%H:%M:%S")

    # Print the current time
    print(current_time, end="\r")

    # Wait for one second
    time.sleep(1)

# task no 7
'''write a program to design a Calendar system for 2023 in python , using string method for creating a 
beautiful console. align text in a center position and make some attractive borders using special characters.'''
# Import the calendar module
import calendar

# Define a function to print the calendar for each month
def print_month(month):
    # Get the calendar for the specified month and year
    cal = calendar.monthcalendar(2023, month)

    # Define the names of the months for formatting purposes
    month_names = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Print the month name in the center of the line
    print(f"{' ' * 11}{month_names[month]}{' ' * 11}")

    # Print the days of the week
    print("Su Mo Tu We Th Fr Sa")

    # Print a line separator
    print("-" * 21)

    # Print each week of the month
    for week in cal:
        # Format each day as a string with 2 spaces, or a blank space if the day is 0
        week_str = ' '.join(f"{day:2}" if day != 0 else '  ' for day in week)

        # Print the formatted week string in the center of the line
        print(f"{' ' * 3}{week_str.center(15)}{' ' * 3}")

    # Print a line separator
    print("-" * 21)

# Print the calendar for each month of the year
for month in range(1, 13):
    # Print a blank line before each month for spacing
    print()

    # Print the calendar for the current month
    print_month(month)

# task no 8
'''write a program to design a console based application for converting different currency. you are required to ask user 
to choose input which currency you want to convert and then ask the amount. after that ask in which currency you want to 
convert. then convert that currency into desired one... (currency should included euro dollar PKR INR and Yen).'''
# Define the conversion rates for each currency relative to USD
# note this rates is for today
rates = {'USD': 1.00, 'EUR': 0.93, 'PKR': 283.65, 'INR': 82.00, 'JPY': 131.63}

# Ask the user for the input currency and amount
input_currency = input("Enter input currency (USD, EUR, PKR, INR, JPY): ")
input_amount = float(input("Enter input amount: "))

# Ask the user for the output currency
output_currency = input("Enter output currency (USD, EUR, PKR, INR, JPY): ")

# Convert the input amount to USD using the conversion rate
usd_amount = input_amount / rates[input_currency]

# Convert the USD amount to the output currency using the conversion rate
output_amount = usd_amount * rates[output_currency]

# Print the output amount in the desired currency
print(f"{input_amount} {input_currency} = {output_amount} {output_currency}")

# task no 9
#write a program to create a function that helps to solve the  quadratic equation
import math

def solve_quadratic(a, b, c):
    """Solves a quadratic equation of the form ax^2 + bx + c = 0."""
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is positive, zero, or negative
    if discriminant > 0:
        # If the discriminant is positive, there are two real roots
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # If the discriminant is zero, there is one real root (the roots are equal)
        x = -b / (2*a)
        return x
    else:
        # If the discriminant is negative, there are no real roots (the roots are complex)
        return None

# task no 10
# write a program to create a function that helps to solve the quadratic equation
import math


def solve_quadratic(a, b, c):
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0.
    Returns a tuple of two roots, or None if there are no real roots.
    """
    # Calculate the discriminant (the part inside the square root)
    discriminant = b ** 2 - 4 * a * c

    # Check if there are any real roots
    if discriminant < 0:
        return None

    # Calculate the two roots using the quadratic formula
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    # Return the two roots as a tuple
    return (root1, root2)

# task no 11
# write a program to create a function that calculate the radius of diameter of circle
def circle_calculator(radius=None, diameter=None):
    """
    Given either the radius or diameter of a circle, calculates the other and returns a tuple (radius, diameter).
    """
    if radius is not None and diameter is not None:
        raise ValueError("Please provide only one argument: radius or diameter")

    if radius is None and diameter is None:
        raise ValueError("Please provide at least one argument: radius or diameter")

    if radius is not None:
        diameter = 2 * radius
    else:
        radius = diameter / 2

    return (radius, diameter)

# task no 12
'''write a program to create a mathematical functions 
prime function: for checking whether the number is prime or not 
even function: for checking whether the number is even or not 
odd function: for checking whether the number is odd or not 
mix number: to tell about the properties of number ( even or odd, positive or negative integer and prime number) 
if user give mix number ( 2 ) then the out put will be 2 is also prime number, 2 is also an odd, and 2 is prime also.'''
def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0

def is_odd(num):
    """Check if a number is odd."""
    return not is_even(num)

def analyze(num):
    """Analyze a number and return its properties."""
    properties = []
    if is_prime(num):
        properties.append("prime")
    if is_even(num):
        properties.append("even")
    else:
        properties.append("odd")
    if num > 0:
        properties.append("positive")
    elif num < 0:
        properties.append("negative")
    return ", ".join(properties)






