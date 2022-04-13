"""
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

#ex1
friends = ["jay", "ali", "emily", "amy", "wyxi"]
for friend in friends:
    print(friend.title())

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#ex1
dinner_guest = ["Prince", "Lewis Hamilton", "Tom Hardy"]

def guest_list():
    for guest in dinner_guest:
        print(f"Hey, {guest} would you like to come to dinner?")


#ex2
print("Tom Hardy can't nmake it to dinner")
del dinner_guest[2]
dinner_guest.append("Unluckyluke")
print(guest_list())

#ex3
print("We have found a bigger dinner table so we can invite more guests")
dinner_guest.insert(0, "Leah")
dinner_guest.insert(2, "Ben")
dinner_guest.append("Wyxi")

print(guest_list())

#ex4
print("Sorry the table isnt coming we need to cut the guest list")
dinner_guest.pop()
dinner_guest.pop()
dinner_guest.pop()
dinner_guest.pop()
print(guest_list())

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print(len(cars))

#ex7

some_list = ["b", "q", "x", "t", "a"]
print(some_list)
print(sorted(some_list))
print(some_list)
print(sorted(some_list, reverse=True))
print(some_list)
some_list.reverse()
print(some_list)
some_list.reverse()
print(some_list)
some_list.sort()
print(some_list)

#ex8
print(len(dinner_guest))
"""
#avoiding index errors
motorcycles = ['honda', 'yamaha', 'suzuki']
#print(motorcycles[3])
print(motorcycles[-1])
#motorcycles = []
#print(motorcycles[3])
#print(motorcycles[-1])

