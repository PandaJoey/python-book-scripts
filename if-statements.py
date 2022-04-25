"""
#different kinds of checks

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

#numerical comparisions 

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)

#multiple conditions

age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 22
print(age_0 >= 21 and age_1 >= 21)

age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21)

age_0 = 18
print(age_0 >= 21 or age_1 >= 21)

#list comparisions
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
'pepperoni' in requested_toppings

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

#booleans

game_active = True
can_edit = False

#ex 5.1
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

num_1 = 15
num_2 = 25
bool_1 = True
bool_2 = False
print(num_1 != num_2)
print(num_1 < num_2)
print(num_1 <= num_2)
print(num_1 <= 15 and num_2 >= num_1)
print(bool_1 != bool_2)

print(num_1 == num_2)
print(num_1 > num_2)
print(num_1 >= num_2)
print(num_1 >= 15 and num_2 <= num_1)
print(bool_1 == bool_2)

string_1 = "Hello"
string_2 = "world"
string_3 = "hello"
print(string_1 == string_2)
print(string_1.lower() == string_3)

#if statements
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

#if-else statements
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

#if-elif-else
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}")



requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

print("\nFinished making your pizza!")

#doesnt work as intended as it breaks out after the first true
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")


#ex 5.3 and 5.4 and 5.5
alien_colour = "red"
if alien_colour == "green":
    print(f"The alien is {alien_colour}, well done you get 5 points")
elif alien_colour == "yellow":
    print(f"you just earnth 10 points for killing the {alien_colour} alien")
else:
    print(f"then alient was {alien_colour}, you get 15 points!")

if alien_colour == "red":
    pass

age = 66

if age < 2:
    print("this person is a baby")
elif age >=2 and age < 4:
    print("this person is a toddler")
elif age >= 4 and age < 13:
    print("this person kid")
elif age >= 13 and age < 20:
    print("this person is a teenager")
elif age >= 20 and age < 65:
    print("this person is an adult")
else:
    print("this person is an elder")

fav_fruit = ["strawberry", "blueberrys", "raspberry", "blackberry", "gooseberrys"]
if 'strawberry' in fav_fruit:
    print("you really like Strawberries")
if 'blueberrys' in fav_fruit:
    print("you really like blueberrys")
if 'raspberry' in fav_fruit:
    print("you really like raspberry")
if 'blackberry' in fav_fruit:
    print("you really like blackberry")
if 'gooseberrys' in fav_fruit:
    print("you really like gooseberrys")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

#checking the list isnt empty
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
"""

#checking multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")

#ex 5.8

users = ["admin", "support", "accounts", "HR", "RnD", "marketing"]
if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello, {user} department")
else:
    print("Sorry the users list is empty")

"""
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
•Make a list of five or more usernames called current_users.
•Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
•Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
•Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted. (To do this, you’ll need to make a copy of
current_users containing the lowercase versions of all existing users.)
"""
current_users = ["admin", "support", "accounts", "HR", "RnD", "marketing"]
new_users = ["warehouse", "support", "dispatch", "delivery", "goods in", "marketing"]


for user in new_users:
    if user in current_users:
        print(f"sorry {user} is already in use")
    else:
        print(f"welcome {user}")