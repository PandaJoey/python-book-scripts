import datetime

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you, everyone. That was a great magic show!")

pizzas = ["pepperoni", "goats cheese", "american hot"]
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print(f"I really love {pizzas[1]} pizza")

#numerical lists
for value in range(1, 5):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehention
squares = [value**2 for value in range(1, 11)]
print(squares)

#ex1
for i in range(0, 21):
    print(i)

begin_time = datetime.datetime.now()
for i in range(0, 1_000_001):
    print(i)
print(datetime.datetime.now())
print(datetime.datetime.now() - begin_time)

million = list(range(1, 1_000_001))
print(min(million))
print(max(million))
print(sum(million))

for i in range(1, 21, 2):
    print(i)

for i in range(3, 31, 3):
    print(i)

for i in range(1, 11):
    print(i**3)

cubes = [value**3 for value in range(1, 11)]
print(cubes)

#list slicing

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

my_foods = ['pizza', 'falafel', 'carrot cake', 'chocolate']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

#ex 4.10
print(f"The first three items in this list are {my_foods[:3]}")
print(f"The three items in middle of the list are {my_foods[2:5]}")
print(f"The last 3 lines of the list are {my_foods[-3:]}")

#ex 4.11
pizzas = ["pepperoni", "goats cheese", "american hot"]
friend_pizza = pizzas[:]
pizzas.append("ham and pineapple")
friend_pizza.append("vegeterian")
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print(f"I really love {pizzas[1]} pizza")
for pizza in friend_pizza:
    print(f"I like {pizza} pizza")
print(f"I really love {friend_pizza[2]} pizza")

#tuples

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#causes error as you cant assign to tuples
#dimensions[0] = 250
#if you only want one item for some reason leave a comma after the first element
my_t = (3,)

for dimension in dimensions:
    print(dimension)

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)    
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

food = ("wings", "ribs", "steaks", "bacon", "cheese")
for item in food:
    print(f"We offer these things from the menu {item}")
    #food[0] = "salad"

food = ("wings", "vegan", "steaks", "bacon", "salad")
for item in food:
    print(f"We offer these things from the menu {item}")


