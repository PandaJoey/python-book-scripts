#ex1
name = input("Hi What is your name?: ")
message = f"Hey {name}, would you like to learn some python?"
print(message)

#ex2
first_name = "joe"
second_name = "crickmore"
full_name = f"{first_name} {second_name }"

print(full_name.lower())
print(full_name.upper())
print(full_name.title())

#ex3+4
famous_person = "Albert Einstein"
qoute = "A person who never made a mitsake never tried anything new."
message = f"{famous_person} ones said, {qoute}"
print(message)

#ex5
person = " \t Joe \nCrickmore "
print(person.lstrip())
print(person.rstrip())
print(person.strip())