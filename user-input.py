"""
#input examples
message = input("Tell me something, and I will repeat it back to you: ")
print(message)

#clear prompts
name = input("Please enter your name: ")
print(f"\nHello, {name}!")


#multiline prompts
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

#checking for int inputs
age = int(input("Please enter your age: "))
if age < 18:
    print("You are not old enough to vote")
else:
    print("You are old enough to vote")


height = int(input("How tall are you, in inches? "))
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    


#modulo operators
number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

#ex 7.1
car = input("What kind of car would you like to hire: ")
print(f"Let me check of we have a {car} in the lot for you!")


#ex 7.2
guests = int(input("How many guests are you looking to book for?: "))
if guests > 8:
    print("Sorry we dont have any tables avaliable for 8 right now please can you wait.")
else:
    print("Certainly please follow me!")



#ex 7.3

number = int(input("Please enter a number: "))
if number % 10 == 0:
    print(f"{number} is a multiple of 10")
else:
    print(f"{number} is not a multiple of 10")

"""

