import datetime
"""
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

4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.


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
"""

#list slicing

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
print(players[:4])