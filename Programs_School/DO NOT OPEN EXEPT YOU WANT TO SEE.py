from typing import List
import random

askhowname = int(input("how do you want to get your name? 1:generated 2:self written.: "))
askhowage = int(input("how do you want to get your age? 1:generated 2:self written.: "))
askhowclass = int(input("how do you want to get your class? 1:generated 2:self written.: "))
#askwhatpers = int(input("how do you want to get your personality? 1:generated 2:self written.: "))
#ABOVE NOT YET IMPLEMENTED!!!!
forename = list()
forename.append("Markus")
forename.append("John")
forename.append("James")
forename.append("Bob")

surname = list()
surname.append("Smith")
surname.append("Lorencius")
surname.append("Malinodas")
surname.append("Schmidt")


if askhowname == 1:
    fname = random.choice(forename)
    sname = random.choice(surname)
    print("name:", fname, sname)
elif askhowname == 2:
    print("Please write your name you made!")
    fname = input("Your forename: ")
    sname = input("Your surname: ")
else:
    print("Wrong input, Fallback to name 'Some Guy'.")
    fname = "Some"
    sname = "Guy"

if askhowage == 1:
    age = random.randint(14, 200)
    print("age:", age)
elif askhowage == 2:
    age = int(input("please write your age: "))
    print("age: ", age)
else:
    print("wrong input! fallback to a random age!")
    age = random.randint()

if askhowclass == 1:
    print("Classgenerator not yet implemented!")
    classi = input("please write your class by yourself!: ")
elif askhowclass == 2:
    classi = input("please write your class: ")
else:
    print("invalid input! Fallback to 'i-can-nothing'")
    classi = "i-can-nothing"

print("here is your character text")
print("My name is", fname, sname, ". I am", age, "years old and my class is:", classi)